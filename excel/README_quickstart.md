# Nose Cone Blending Workbook (Quick Start)

This folder contains an Excel workbook used to generate a **blended rocket nose cone profile**.

The profile is created by smoothly combining:
- a standard **tangent ogive nose cone** (engineering baseline), and
- a **bionic-inspired contour** (digitized and fitted from biological shapes).

The final blended geometry is intended for **Autodesk Inventor**, where it is revolved into a 3D nose cone for further structural design and simulation.

---

## What this workbook does (in plain language)

Instead of abruptly switching from an engineering nose cone to a bionic shape, this workbook:
- gradually transitions between the two shapes along the nose length
- ensures the radius changes smoothly
- avoids sharp geometric discontinuities that can cause modeling or simulation issues

---

## How to use (basic)

1. Open the Excel file in this folder.
2. In the `extras` sheet:
   - Set the nose length and diameter.
   - Adjust how strongly the bionic shape influences the final geometry.
3. In the `blend` sheet:
   - Column A: axial position along the nose cone
   - Column B: tangent ogive radius
   - Column C: bionic radius
4. Copy the final blended `(x, r)` values.
5. Import them into **Autodesk Inventor** and revolve the curve into a 3D nose cone.

No programming is required.

---

## When this approach is useful

- Exploring how biological shapes influence aerodynamic geometry
- Creating smooth experimental nose cone profiles
- Preparing clean input geometry before CAD or CFD work
