"""Experiment (f), part 2: the beta-dial and intense-set sparseness.

Implements the two survey-to-builder handoffs of the Architecture 2 dossier
(docs/research_atlas/conditional_criteria_dossier.md, sections 11.3.1 and
11.3.2), extending the vortex-stretching anatomy run (alignment_depletion.py,
LEARNINGS #10) without modifying it.

1. THE BETA-DIAL (handoff 11.3.1, the lead). The Constantin-Fefferman family
   hypothesizes a Holder-beta modulus on the vorticity direction
   xi = omega/|omega| over the intense set, and the modulus carries scaling
   tax a = +beta (LEARNINGS #12): beta = 1 is CF 1993, beta = 1/2 is Beirao
   da Veiga-Berselli 2002 (enstrophy height), and the unconditional beta = 0
   endpoint is open (Direction 02). The companion experiment measures
   |grad xi|, the beta = 1 modulus at the grid scale. Here we measure the
   Holder-beta seminorm for beta in {1, 1/2, 1/4} from pairwise samples at
   dyadic separations h = dx * 2^m along the three axes, with both endpoints
   in the intense set (top decile of |omega|, matching the companion). The
   pairwise increment is the CF modulus |xi(x) x xi(x + h e)| = sin(theta),
   the exact quantity in the CF hypothesis. It is orientation-insensitive
   (the stretching geometry cares about the line of xi, not its sign), which
   is also what makes the 2D control exact rather than approximate. The
   per-time seminorm estimate is the 99th percentile of the pairwise quotient
   sin(theta)/h^beta (robust to isolated pairs), then the sup over trusted
   separations. Readout: which beta the flow sustains with a non-growing
   seminorm as the cascade develops.

   The single most informative number for Direction 02: the log-log slope of
   the misalignment angle theta(h) at the time of peak enstrophy production,
   the empirical local Holder exponent of the direction field.

2. SPARSENESS OF THE INTENSE SET (handoff 11.3.2). Grujic's framework derives
   regularity from 1D-sparseness (filamentariness) of the vorticity
   super-level sets, the one conditional route claiming an algebraic bite on
   the scaling gap. At each diagnostic time, for dyadic thresholds
   M = max|omega| * 2^-k (k = 0..4, with >= so k = 0 is the peak point):
   the volume fraction of {|omega| >= M}; the largest periodic run length
   above threshold along each grid line (the linear-slice statistic of the
   sparseness framework), as a fraction of the box, median and 95th
   percentile over lines that meet the set; and the depletion factor
   restricted to the sub-set. Together: the empirical sparseness-to-depletion
   table.

CONTROLS. 2D control: in 2D the vorticity direction is +-e_z, every cross
product xi(x) x xi(y) vanishes identically, so all Holder-beta seminorms are
exactly zero; the companion 2D run computes them through the same code path
and prints the exact zeros. The geometric family passes the 2D control
non-vacuously: its hypothesis is automatic precisely where regularity is
free. Resolution honesty: the smallest separation is one grid cell, which
reads grid-scale (aliasing-contaminated) structure on a 32^3 spectral grid;
m = 0 is reported but excluded from seminorms and fits. The local-exponent
fit uses h = 2dx..8dx (the half-box separation enters the seminorm sup but
not the fit, since it is not local). The enstrophy budget residual is the
resolution alarm (LEARNINGS #10): the peak-production readout is taken
inside the resolved window.

Run:  python -m experiments.vortex_stretching.beta_dial
Env:  NS_BD_N=32  NS_BD_NU=0.01  NS_BD_TEND=4.0
"""

from __future__ import annotations

import contextlib
import io
import os

import numpy as np

try:
    with contextlib.redirect_stderr(io.StringIO()):
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
except Exception:
    plt = None

from experiments._shared import Flow2D, Flow3D, taylor_green_initial
from experiments.vortex_stretching.alignment_depletion import (
    palinstrophy_dissipation,
    strain_and_gradients,
)

BETAS = (1.0, 0.5, 0.25)
N_LEVELS = 5            # dyadic thresholds M = wmax * 2^-k, k = 0..N_LEVELS-1
INTENSE_QUANTILE = 0.9  # same intense set as alignment_depletion.py
RESID_ALARM = 0.05      # budget residual above this marks the unresolved regime
GROWTH_BOUND = 2.0      # tolerance for the "non-growing seminorm" verdict


def separations(n: int):
    """Dyadic separations in cells, up to half the box."""
    return [2**m for m in range(8) if 2**m <= n // 2]


def pairwise_deltas(xi, mask, sep_cells: int):
    """CF modulus |xi(x) x xi(x + h e)| over pairs with both endpoints in the
    intense set, pooled over the axis directions. Works for the 2D control too
    (xi embedded as a 3-vector field over a 2D grid)."""
    out = []
    for ax in range(mask.ndim):
        pm = mask & np.roll(mask, -sep_cells, axis=ax)
        if not pm.any():
            continue
        xs = np.roll(xi, -sep_cells, axis=ax + 1)
        cx = xi[1] * xs[2] - xi[2] * xs[1]
        cy = xi[2] * xs[0] - xi[0] * xs[2]
        cz = xi[0] * xs[1] - xi[1] * xs[0]
        out.append(np.sqrt(cx * cx + cy * cy + cz * cz)[pm])
    return np.concatenate(out) if out else np.array([])


def line_max_runs(mask):
    """Largest periodic run above threshold along each grid line, all axes,
    restricted to lines that meet the set. Doubling the line handles the
    periodic wrap; the cap at n handles the all-True line."""
    runs = []
    for ax in range(mask.ndim):
        n_ax = mask.shape[ax]
        b = np.moveaxis(mask, ax, -1).reshape(-1, n_ax)
        b = b[b.any(axis=1)]
        if b.size == 0:
            continue
        b2 = np.concatenate([b, b], axis=1)
        idx = np.arange(2 * n_ax)
        last_false = np.maximum.accumulate(
            np.where(~b2, idx[None, :], -1), axis=1
        )
        r = np.where(b2, idx[None, :] - last_false, 0).max(axis=1)
        runs.append(np.minimum(r, n_ax))
    return np.concatenate(runs) if runs else np.array([], dtype=int)


def snapshot(f: Flow3D, seps):
    """Production/dissipation/depletion plus the beta-dial pair statistics and
    the sparseness table at one time."""
    n = f.n
    dx3 = (2.0 * np.pi / n) ** 3

    w = f.vorticity()
    wmag = np.sqrt(w[0] ** 2 + w[1] ** 2 + w[2] ** 2)
    xi = w / np.maximum(wmag, 1e-12)
    S = strain_and_gradients(f)

    Sw = np.einsum("ij...,j...->i...", S, w)
    prod_field = np.einsum("i...,i...->...", w, Sw)
    P = float(np.sum(prod_field) * dx3)
    D = float(palinstrophy_dissipation(f))

    lam3 = np.linalg.eigvalsh(np.moveaxis(S.reshape(3, 3, -1), 2, 0))[:, 2]
    stretch_cap = lam3 * wmag.reshape(-1) ** 2
    cap_total = float(np.sum(stretch_cap))
    depletion = P / (cap_total * dx3) if cap_total > 0 else float("nan")

    mask = wmag >= np.quantile(wmag, INTENSE_QUANTILE)
    q99_delta, sup_delta, med_theta, q99_theta, pairs = [], [], [], [], []
    for sep in seps:
        d = pairwise_deltas(xi, mask, sep)
        pairs.append(int(d.size))
        if d.size == 0:
            for lst in (q99_delta, sup_delta, med_theta, q99_theta):
                lst.append(float("nan"))
            continue
        th = np.degrees(np.arcsin(np.clip(d, 0.0, 1.0)))
        q99_delta.append(float(np.quantile(d, 0.99)))
        sup_delta.append(float(d.max()))
        med_theta.append(float(np.median(th)))
        q99_theta.append(float(np.quantile(th, 0.99)))

    wmax = float(wmag.max())
    pf = prod_field.reshape(-1)
    volfrac, run_med, run_p95, depl_k = [], [], [], []
    for k in range(N_LEVELS):
        mk = wmag >= wmax * 2.0 ** (-k)
        volfrac.append(float(np.mean(mk)))
        runs = line_max_runs(mk) / float(n)
        run_med.append(float(np.median(runs)) if runs.size else float("nan"))
        run_p95.append(
            float(np.quantile(runs, 0.95)) if runs.size else float("nan")
        )
        mflat = mk.reshape(-1)
        cap = float(np.sum(stretch_cap[mflat]))
        depl_k.append(
            float(np.sum(pf[mflat]) / cap) if cap > 0 else float("nan")
        )

    return {
        "P": P, "D": D, "depletion": depletion, "wmax": wmax,
        "q99_delta": q99_delta, "sup_delta": sup_delta,
        "med_theta": med_theta, "q99_theta": q99_theta, "pairs": pairs,
        "volfrac": volfrac, "run_med": run_med, "run_p95": run_p95,
        "depl_k": depl_k,
    }


def seminorm_sup(q99_delta, hs, beta, idxs):
    vals = [
        q99_delta[i] / hs[i] ** beta
        for i in idxs
        if np.isfinite(q99_delta[i])
    ]
    return max(vals) if vals else float("nan")


def fit_slope(hs, vals, idxs):
    pts = [(hs[i], vals[i]) for i in idxs if np.isfinite(vals[i]) and vals[i] > 0]
    if len(pts) < 2:
        return float("nan")
    lh = np.log([p[0] for p in pts])
    lv = np.log([p[1] for p in pts])
    return float(np.polyfit(lh, lv, 1)[0])


def main():
    n = int(os.environ.get("NS_BD_N", "32"))
    nu = float(os.environ.get("NS_BD_NU", "0.01"))
    t_end = float(os.environ.get("NS_BD_TEND", "4.0"))
    dt = 0.01
    snap_every = int(round(0.25 / dt))

    dx = 2.0 * np.pi / n
    seps = separations(n)
    hs = [s * dx for s in seps]
    trusted = list(range(1, len(seps)))
    fit_idx = trusted[:-1] if len(trusted) > 2 else list(trusted)

    print("Beta-dial and intense-set sparseness (Taylor-Green, 3D incompressible NS)")
    print(f"grid {n}^3, nu = {nu}, t_end = {t_end}, dx = {dx:.4f}")
    print(f"separations h/dx = {seps}; m = 0 (one cell) untrusted; "
          f"fit window h/dx = {[seps[i] for i in fit_idx]}")
    print()

    f = Flow3D(n=n, nu=nu)
    f.set_velocity(taylor_green_initial(n))
    vol = (2.0 * np.pi) ** 3

    Z = [f.enstrophy() * vol]
    snaps = [(0, snapshot(f, seps))]
    nsteps = int(round(t_end / dt))
    for step in range(1, nsteps + 1):
        f.step(dt)
        Z.append(f.enstrophy() * vol)
        if step % snap_every == 0:
            snaps.append((step, snapshot(f, seps)))

    resids = []
    for step, s in snaps:
        if 0 < step < nsteps:
            dZdt = (Z[step + 1] - Z[step - 1]) / (2.0 * dt)
            resids.append(abs(s["P"] - s["D"] - dZdt) / max(abs(dZdt), 1e-12))
        else:
            resids.append(float("nan"))

    print("Holder-beta seminorms of xi on the intense set "
          "(q99 of sin(theta)/h^beta over pairs, sup over h in "
          f"[{seps[trusted[0]]}dx, {seps[trusted[-1]]}dx]):")
    print(f"{'t':>5} {'P':>9} {'D':>9} {'resid%':>7} {'deplete':>8} "
          f"{'b=1':>8} {'b=1/2':>8} {'b=1/4':>8} {'pairs_min':>10}")
    print("-" * 80)
    semis = np.full((len(BETAS), len(snaps)), np.nan)
    for i, (step, s) in enumerate(snaps):
        t = step * dt
        for bi, beta in enumerate(BETAS):
            semis[bi, i] = seminorm_sup(s["q99_delta"], hs, beta, trusted)
        pmin = min(s["pairs"][j] for j in trusted)
        rs = f"{100 * resids[i]:7.2f}" if np.isfinite(resids[i]) else "      -"
        print(f"{t:5.2f} {s['P']:9.3f} {s['D']:9.3f} {rs} {s['depletion']:8.3f} "
              f"{semis[0, i]:8.3f} {semis[1, i]:8.3f} {semis[2, i]:8.3f} "
              f"{pmin:10d}")

    alarm = next(
        (i for i in range(1, len(snaps))
         if np.isfinite(resids[i]) and resids[i] > RESID_ALARM),
        len(snaps),
    )
    resolved = list(range(alarm))
    i_star = max(resolved[1:] or resolved, key=lambda i: snaps[i][1]["P"])
    t_star = snaps[i_star][0] * dt
    t_resolved = snaps[resolved[-1]][0] * dt
    s_star = snaps[i_star][1]

    print()
    print(f"theta(h) on the intense set at peak resolved production, "
          f"t* = {t_star:.2f}:")
    print(f"{'h/dx':>5} {'h':>7} {'pairs':>7} {'med_deg':>8} {'p99_deg':>8}  note")
    for j, sep in enumerate(seps):
        if j == 0:
            note = "one cell, untrusted"
        elif j in fit_idx:
            note = "fit window"
        else:
            note = "sup only (not local)"
        print(f"{sep:5d} {hs[j]:7.3f} {s_star['pairs'][j]:7d} "
              f"{s_star['med_theta'][j]:8.2f} {s_star['q99_theta'][j]:8.2f}  {note}")

    alpha_med = fit_slope(hs, s_star["med_theta"], fit_idx)
    alpha_p99 = fit_slope(hs, s_star["q99_theta"], fit_idx)
    alpha_m0 = fit_slope(hs, s_star["med_theta"], [0] + fit_idx)
    print(f"  empirical local Holder exponent (median theta, trusted window): "
          f"alpha = {alpha_med:.2f}")
    print(f"  same fit on the 99th percentile: alpha = {alpha_p99:.2f}; "
          f"including the untrusted one-cell point: {alpha_m0:.2f}")
    for a, b in zip(fit_idx[:-1], fit_idx[1:]):
        va, vb = s_star["med_theta"][a], s_star["med_theta"][b]
        if va > 0 and vb > 0:
            sl = float(np.log(vb / va) / np.log(hs[b] / hs[a]))
            print(f"  adjacent dyadic slope {seps[a]}dx -> {seps[b]}dx: {sl:.2f}")
    print("  reference: fully decorrelated direction lines give median 60 deg,")
    print("  so angles approaching that mark the end of the coherent range.")

    print()
    print(f"Sparseness-to-depletion at t* = {t_star:.2f} "
          f"(wmax = {s_star['wmax']:.3f}); run lengths as fraction of the box:")
    print(f"{'k':>3} {'M/wmax':>8} {'vol_frac':>10} {'run_med':>8} "
          f"{'run_p95':>8} {'depl_set':>9}")
    for k in range(N_LEVELS):
        print(f"{k:3d} {2.0**-k:8.4f} {s_star['volfrac'][k]:10.5f} "
              f"{s_star['run_med'][k]:8.3f} {s_star['run_p95'][k]:8.3f} "
              f"{s_star['depl_k'][k]:9.3f}")
    print()
    print("Evolution at the mid threshold M = wmax/4 (k = 2):")
    print(f"{'t':>5} {'vol_frac':>10} {'run_p95':>8} {'depl_set':>9}")
    for i, (step, s) in enumerate(snaps):
        if step % (2 * snap_every) == 0:
            print(f"{step * dt:5.2f} {s['volfrac'][2]:10.5f} "
                  f"{s['run_p95'][2]:8.3f} {s['depl_k'][2]:9.3f}")

    print()
    print("2D CONTROL (same code path; xi embedded as +-e_z):")
    rng = np.random.default_rng(0)
    n2 = 64
    spec = np.zeros((n2, n2), dtype=np.complex128)
    k1 = np.fft.fftfreq(n2, d=1.0 / n2)
    kx2, ky2 = np.meshgrid(k1, k1, indexing="ij")
    low = (kx2**2 + ky2**2 <= 16) & (kx2**2 + ky2**2 > 0)
    spec[low] = rng.normal(size=low.sum()) + 1j * rng.normal(size=low.sum())
    w0 = np.fft.ifftn(spec).real
    w0 *= 3.0 / np.abs(w0).max()
    g = Flow2D(n=n2, nu=nu)
    g.set_vorticity(w0)
    for _ in range(nsteps):
        g.step(dt)
    w2 = np.fft.ifftn(g.wh).real
    mask2 = np.abs(w2) >= np.quantile(np.abs(w2), INTENSE_QUANTILE)
    xi2 = np.zeros((3, n2, n2))
    xi2[2] = np.sign(w2)
    sup2 = 0.0
    for sep in separations(n2):
        d = pairwise_deltas(xi2, mask2, sep)
        if d.size:
            sup2 = max(sup2, float(d.max()))
    print(f"  sup over all pairs and separations of |xi(x) x xi(y)| = {sup2}")
    print("  -> every Holder-beta seminorm is exactly zero: in 2D the direction")
    print("     field has no degrees of freedom, the CF hypothesis is automatic,")
    print("     and 2D is indeed smooth. The control passes non-vacuously.")

    i_base = min(
        range(1, len(snaps)), key=lambda i: abs(snaps[i][0] * dt - 0.5)
    )
    window = [i for i in resolved if i >= i_base]
    growth, t_flat = {}, {}
    for bi, beta in enumerate(BETAS):
        base = semis[bi, i_base]
        wmaxv = float(np.nanmax(semis[bi, window]))
        growth[beta] = wmaxv / base if base > 0 else float("nan")
        j_flat = next(i for i in window if semis[bi, i] >= 0.98 * wmaxv)
        t_flat[beta] = snaps[j_flat][0] * dt
    sustained = [beta for beta in BETAS if growth[beta] <= GROWTH_BOUND]
    plateaued = all(t_flat[b] <= t_resolved - 0.49 for b in BETAS)
    sat_h = next(
        (hs[j] for j in trusted
         if np.isfinite(s_star["q99_delta"][j]) and s_star["q99_delta"][j] >= 0.999),
        None,
    )

    print()
    print("FINDINGS:")
    print(f"  resolved window (budget residual <= {100 * RESID_ALARM:.0f}%): "
          f"t <= {t_resolved:.2f}; peak resolved production at t* = {t_star:.2f} "
          f"(P = {s_star['P']:.2f}, global depletion {s_star['depletion']:.2f}).")
    print(f"  seminorm growth over t in [0.5, {t_resolved:.2f}] "
          f"(max/baseline at t = 0.5):")
    for beta in BETAS:
        print(f"    beta = {beta:<4}: x{growth[beta]:.2f}, flat from "
              f"t = {t_flat[beta]:.2f}")
    if plateaued:
        print(f"  -> all three seminorms grow by a factor ~"
              f"{np.nanmean(list(growth.values())):.1f} while the cascade "
              f"develops, then hold flat to the")
        print(f"     edge of the resolved window (from t = "
              f"{max(t_flat.values()):.2f}): bounded, but not beta-separating.")
        if sat_h is not None:
            print(f"     The plateau is saturation: the q99 misalignment reaches "
                  f"90 deg at h = {sat_h:.3f},")
            print("     so the seminorm reads h^-beta mechanically there; the "
                  "beta-discriminating")
            print("     information lives in theta(h) at the still-coherent "
                  "separations (alpha below).")
    elif sustained:
        print(f"  -> the flow sustains beta up to {max(sustained)} with a "
              f"non-growing seminorm (bound x{GROWTH_BOUND:.1f}).")
    else:
        print(f"  -> no beta in the tested set stays within x{GROWTH_BOUND:.1f} "
              "or plateaus; the coherence is degrading at these scales.")
    print(f"  empirical local Holder exponent of xi at t*: alpha = "
          f"{alpha_med:.2f} (median theta(h) slope, h in "
          f"[{seps[fit_idx[0]]}dx, {seps[fit_idx[-1]]}dx]).")
    print("  ladder for comparison: alpha >= 1 is CF-1993 coherence, 1/2 is the")
    print("  Beirao da Veiga-Berselli rung, 0 is the open critical endpoint.")
    v_half = s_star["volfrac"][1]
    if v_half > 0.2:
        print(f"  sparseness: NOT sparse at these laminar parameters: vol "
              f"fraction {v_half:.2f} at")
        print(f"    M = wmax/2 and run lengths up to the whole box (p95 = "
              f"{s_star['run_p95'][1]:.2f}). The TG field")
        print("    is a global smooth pattern, so the Grujic hypothesis has no "
              "purchase here;")
        print("    this run is the non-filamentary baseline the framework's "
              "near-singular")
        print("    hypothesis must be contrasted against, not a test of it.")
    else:
        print(f"  sparseness: vol fraction {v_half:.4f} at M = wmax/2, run "
              f"lengths med {s_star['run_med'][1]:.3f} /")
        print(f"    p95 {s_star['run_p95'][1]:.3f} of the box: filamentary "
              "structure is present; see the")
        print("    full sparseness-to-depletion table above.")
    print("  CAVEATS: 32^3 at Re ~ 100 is a mild, laminar-symmetric flow; the")
    print("  one-cell separation is excluded as under-resolved, so no claim is")
    print(f"  made below h = {2 * dx:.3f}. Observation, not proof: the open")
    print("  problem is whether this coherence is FORCED near a singularity.")

    cache_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_cache")
    os.makedirs(cache_dir, exist_ok=True)
    ts = np.array([step * dt for step, _ in snaps])
    grab = lambda key: np.array([s[key] for _, s in snaps])
    np.savez_compressed(
        os.path.join(cache_dir, "beta_dial.npz"),
        ts=ts, resids=np.array(resids), betas=np.array(BETAS),
        seps=np.array(seps), hs=np.array(hs), semis=semis,
        P=grab("P"), D=grab("D"), depletion=grab("depletion"),
        wmax=grab("wmax"), q99_delta=grab("q99_delta"),
        sup_delta=grab("sup_delta"), med_theta=grab("med_theta"),
        q99_theta=grab("q99_theta"), pairs=grab("pairs"),
        volfrac=grab("volfrac"), run_med=grab("run_med"),
        run_p95=grab("run_p95"), depl_k=grab("depl_k"),
        t_star=t_star, alpha_med=alpha_med, alpha_p99=alpha_p99,
    )

    if plt is None:
        print("  (matplotlib unavailable in this environment; theta(h) plot "
              "skipped, data in _cache/beta_dial.npz)")
    else:
        fig, ax = plt.subplots(figsize=(6.0, 4.5))
        ax.loglog(hs, s_star["med_theta"], "o-", label="median theta")
        ax.loglog(hs, s_star["q99_theta"], "s--", label="99th pct theta")
        if np.isfinite(alpha_med):
            xf = np.array([hs[fit_idx[0]], hs[fit_idx[-1]]])
            lh = np.log([hs[i] for i in fit_idx])
            lv = np.log([s_star["med_theta"][i] for i in fit_idx])
            yf = np.exp(np.polyval(np.polyfit(lh, lv, 1), np.log(xf)))
            ax.loglog(xf, yf, "k-", lw=2, label=f"fit slope {alpha_med:.2f}")
        ax.axvline(hs[0], color="red", alpha=0.4, ls=":",
                   label="one cell (untrusted)")
        ax.set_xlabel("separation h")
        ax.set_ylabel("misalignment angle (deg)")
        ax.set_title(f"theta(h) on the intense set, t* = {t_star:.2f}")
        ax.legend()
        fig.tight_layout()
        png = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "beta_dial_theta_h.png"
        )
        fig.savefig(png, dpi=130)
        print(f"  theta(h) plot saved to {png}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
