#  Biomimetic Nose Cone Design for Aerodynamic Optimization

**Author:** Bonny Chen  
**Project Type:** Ongoing Research  
**Software:** OpenFOAM, Autodesk Fusion 360, Python (Open3D, Trimesh), Excel  
**Keywords:** Biomimicry, Rocket Design, Aerodynamics, Curvature Blending, CFD Simulation  

This project was conducted independently during high school as an exploratory engineering study.

---

<details>
<summary> Table of Contents</summary>

- [1. Abstract](#1-abstract)
- [2. Introduction](#2-introduction)
- [3. Literature Review](#3-literature-review)
- [4. Research Methodology](#4-research-methodology)
  - [4.1 Design and Modeling](#41-design-and-modeling)
  - [4.2 Simulation and Fabrication](#42-simulation-and-fabrication)
  - [4.3 Physical Testing](#43-physical-testing)
- [5. Key Limitation and Redefinition](#5-key-limitation-and-redefinition)
- [6. Revised Research Direction](#6-revised-research-direction)
- [7. Validation and Calculation Check](#7-validation-and-calculation-check)
- [8. Reflection](#8-reflection)
- [9. Future Work](#9-future-work)
- [10. Repository Structure](#10-repository-structure)

</details>

---

## 1. Abstract
This ongoing study integrates **biomimetics**, **curve fitting**, and **fluid dynamics** to explore naturally occurring shapes that exhibit low drag and high stability, applying these findings to rocket nose cone design. Inspired by high-speed biological forms such as sharks, swallows, sailfish, and eagles, I developed a computational and experimental workflow combining **Open3D** modeling, **Python scripting**, **CFD simulation (OpenFOAM)**, and **wind tunnel testing**. 

Initial simulations and physical tests suggested that while biomimetic shapes can offer smoother flow attachment, full replication of biological asymmetry introduces aerodynamic imbalance in rockets. This led to a refined approach—**partial curvature blending**—where local geometric segments inspired by nature are smoothly integrated while preserving axial symmetry.

---

## 2. Introduction
### 2.1 Research Motivation
As the structural design lead in my high school’s **Taiwan Rocket Cup** team, I became fascinated by how different nose cone profiles—conical, ogive, ellipsoidal, parabolic—affect performance. Beyond these traditional geometries, I began questioning whether nature’s own streamlined designs could inspire more efficient solutions.

### 2.2 Research Objectives
The primary objective is to determine whether integrating biological curvature patterns can:
1. Reduce drag coefficient (Cd) by improving flow attachment.
2. Minimize flow separation and pressure gradients.
3. Enhance stability by smoothening the pitching moment variation during flight.

---

## 3. Literature Review
Traditional rocket nose cones are defined by analytical or parametric curves—ogive, conical, and Haack series—optimized for drag under ideal flow conditions. However, they often fail to balance **stability** and **wake control** at transonic speeds.

Recent advances in **biomimetic engineering** highlight how natural organisms achieve aerodynamic efficiency through subtle curvature transitions and distributed surface textures. Shark heads, for example, minimize turbulence via micro-riblet patterns (Bechert et al., 2000), while birds’ beaks and head contours control lift and flow reattachment during dives (NASA Research Center, 2023).

Techniques such as **shape blending** and **morphing surfaces** enable controlled interpolation between geometries (Wang et al., 2016), providing a framework to integrate biological curvature into aerodynamic models.

Despite wide use in vehicle and aircraft design, **biomimetic blending for rockets** remains underexplored. This research aims to bridge that gap.

---

## 4. Research Methodology
### 4.1 Design and Modeling
**(1) Selection of Biological Models**  
Four species were selected for their high-speed, low-drag morphologies: shark, sailfish, swallow, and eagle. 3D models were obtained from open databases (Sketchfab), oriented using **Open3D**, and cropped to isolate the head sections.

**(2) Model Preprocessing**  
- Automatic orientation alignment via principal axes computation.
- Laplacian smoothing to remove noise and preserve curvature continuity.
- Head extraction defined within adjustable AABB boundaries.

**(3) Shape Blending**  
The standard ogive model and biological head models were converted into point clouds. Weighted interpolation generated blended geometries:
\[ \vec{p}_{blend} = (1 - \alpha)\vec{p}_{eng} + \alpha\vec{p}_{bio} \]
with blending ratios \( \alpha = 0.2, 0.4, 0.6, 0.8 \). The resulting shapes were reconstructed via convex hull algorithms and exported as STL meshes.

### 4.2 Simulation and Fabrication
- **Software:** OpenFOAM v12 (simulation) and ParaView v5.13 (visualization).  
- **Conditions:** Mach 0.8–1.2, steady-state incompressible flow, no-slip wall boundary.  
- **Process:** Mesh generation (snappyHexMesh), steady-state pressure and velocity field computation, and drag coefficient estimation.

3D models were printed in **PLA**, mounted on PP tubes, and post-processed for surface smoothness. Pressure ports were drilled according to CFD pressure gradient results.

### 4.3 Physical Testing
A custom low-speed wind tunnel was constructed for flow visualization using smoke filaments. Pressure sensors (BMP388) measured surface pressure variations, validating CFD accuracy. Launch tests using commercial fireworks rockets were conducted to evaluate stability and altitude.

---

## 5. Key Limitation and Redefinition
CFD results revealed that **fully biomimetic geometries introduced lateral asymmetry**, creating side forces and unstable pitching moments. Rockets, unlike birds or fish, lack adaptive control surfaces to counteract such effects.

This realization redefined the research question:
> *How can biological curvature principles be integrated while maintaining aerodynamic symmetry?*

---

## 6. Revised Research Direction
### Functional Biomimicry through Local Curvature Blending
The improved model extracts only the **front curvature segment** (roughly 20–30% of the total nose length) and blends it into the engineering base using a smooth transition function.

\[ r(x) = (1 - \alpha(x))r_{eng}(x) + \alpha(x)r_{bio}(x) \]
with \( \alpha(x) = \alpha_{max} \cdot smoothstep(0.2L, 0.8L; x) \).

This ensures:
- Axisymmetric flow and stable pressure field.  
- Continuous geometric curvature (C¹ smoothness).  
- Retained **functional essence of biomimicry**—flow redirection and gradual deceleration.

### Quantitative Verification
Validation using Excel computation (`bionosecone_blend_caculate.xlsx`) confirmed:
- \( RMSE_{\alpha} = 1.7×10^{-11} \): nearly perfect adherence to smoothstep curve.  
- \( RMSE_{r} = 0.0044~m \): minimal deviation from theoretical radius blending.

---
## 7. Future Work
Future work will continue with a staged validation approach that balances numerical
analysis and physical testing. After finalizing the blended nose cone geometry using
the Excel-based parametric model, the design will be imported into Autodesk Inventor
for preliminary CFD analysis.

Inventor-based CFD will be used as a qualitative sanity check to evaluate overall
flow trends and identify obvious geometric issues before physical fabrication,
rather than as a source of final aerodynamic performance metrics.

Following numerical inspection, physical prototypes will be fabricated for
experimental validation. Low-speed wind tunnel testing with smoke-flow visualization
will be conducted to observe flow attachment, separation, and symmetry. Image-based
analysis of the flow patterns will then guide further geometric refinement before
subsequent real-world testing.


---
## Excel Nose Cone Blending

This project includes an Excel-based workflow for blending a **tangent ogive nose cone**
with a **bionic-inspired profile** to generate a smooth axial radius distribution.

The Excel workbook is used as a **geometry pre-processing step** before CAD modeling
in Autodesk Inventor and CFD simulation.

- Workbook file: `/excel/bionosecone_blend_caculate.xlsx`
- Quick overview (conceptual): `/excel/README_quickstart.md`
- Technical documentation (math & parameters): `/excel/README_technical.md`

### Early CFD Issues (OpenFOAM)

<p align="center">
  <img src="assets/cfd_iteration/threshold_error.png" width="500">
</p>

<p align="center">
  <em>Incorrect threshold causing rectangular geometry</em>
</p>


<p align="center">
  <img src="assets/cfd_iteration/rough_surface_streamtracer.png" width="500">
</p>

<p align="center">
  <em>Surface irregularities causing non-physical flow artifacts</em>
</p>


## 10. Repository Structure
```
├── assets/                         # Figures and visualization assets
│   └── cfd_iteration/              # Early OpenFOAM failure / iteration screenshots
│       ├── threshold_error.png
│       ├── misalignment.png
│       ├── rough_surface_p.png
│       ├── rough_surface_streamtracer.png
│       ├── rough_surface_streamtracer2.png
│       └── README.md
├── 0/                              # OpenFOAM initial & boundary conditions
├── constant/                       # OpenFOAM physical properties and mesh
├── system/                         # OpenFOAM solver and numerical settings
├── excel/                          # Excel-based nose cone blending workflow
│   ├── bionosecone_blend_caculate.xlsx
│   ├── README_quickstart.md
│   └── README_technical.md
├── MakerPortfolio.pdf
├── allmodel.zip
└── nosecone_case.foam

```

---


[↑ Back to top](#1-abstract)
