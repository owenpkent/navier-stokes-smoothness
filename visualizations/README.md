# Visualizations: manim scenes

Built with [manim Community Edition](https://docs.manim.community/) (v0.18+).

## Setup

| Dependency | Purpose | Install |
|---|---|---|
| Python 3.10+ | Runtime | python.org or system package manager |
| manim | Animation engine | `pip install manim` |
| FFmpeg | Video encoding | `winget install Gyan.FFmpeg` / `brew install ffmpeg` |
| LaTeX (MiKTeX or TeX Live) | Math typesetting | miktex.org / tug.org/texlive |

```bash
pip install manim
```

## Rendering

```bash
# Low quality, fast preview (480p, 15fps)
manim -ql visualizations/<folder>/<script>.py <SceneName>

# Medium / high / 4K
manim -qm visualizations/<folder>/<script>.py <SceneName>
manim -qh visualizations/<folder>/<script>.py <SceneName>
manim -qk visualizations/<folder>/<script>.py <SceneName>
```

Output lands in `media/videos/<script_name>/<quality>/`. Rendered video is gitignored (`media/`).

## Scene index

| # | Folder | Scene Class | What it shows | Status |
|---|---|---|---|---|
| 1 | `01_scaling_zoom/` | `ScalingZoom` | The scaling symmetry $u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2 t)$ and why the energy is supercritical: zooming into small scales, the energy bar shrinks while the critical norm stays fixed. | Present |
| 2 | `02_vortex_stretching/` | `VortexStretching` | The 3D vs 2D structural difference: a vortex tube stretching and intensifying (3D), versus a flat vortex that cannot stretch (2D). | TODO |
| 3 | `03_burgers_shock/` | `BurgersShock` | A smooth profile steepening into a shock (inviscid) and viscosity holding it smooth. | TODO |
| 4 | `04_singular_set_ckn/` | `SingularSetCKN` | The Caffarelli-Kohn-Nirenberg picture: the singular set is at most one-dimensional in spacetime. | TODO |

## Notes

- All scenes use manim Community Edition (v0.18+).
- Scenes are self-contained: each file imports only `manim` and `numpy`.
- Math is rendered via LaTeX; requires a working LaTeX installation.
- Scene 1 (`ScalingZoom`) is the present, renderable scene; the others are stubs on the TODO list.
