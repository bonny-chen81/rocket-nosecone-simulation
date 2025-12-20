# Bionic Nose Cone Blending — Technical Documentation

This workbook implements a **parametric blending method** to generate a smooth nose cone radius profile by combining a classical tangent ogive geometry with a bionic-inspired contour.

The output is designed for **Autodesk Inventor**, where the blended profile is revolved into a 3D solid.

---

## 1. Engineering Baseline: Tangent Ogive

The engineering reference profile is a **tangent ogive nose cone**, defined by:

- nose length: \( L \)
- base radius: \( R \)
- generating circle radius:
\[
\rho = \frac{R^2 + L^2}{2R}
\]

The tangent ogive radius as a function of axial position \(x\) is:

\[
r_{\text{eng}}(x)
=
\sqrt{\rho^2 - (L - x)^2}
-
(\rho - R)
\]

These values are precomputed and placed in the `blend` sheet as `r_eng_m`.

---

## 2. Bionic Profile

The bionic profile \( r_{\text{bio}}(x) \) is obtained by:
- digitizing a biological contour,
- scaling it to match the same total length and base radius,
- interpolating it onto the same axial grid as the ogive.

This ensures pointwise compatibility during blending.

---

## 3. Blending Formulation

The final blended radius is defined as:

\[
r_{\text{blend}}(x)
=
(1-\alpha(x))\, r_{\text{eng}}(x)
+
\alpha(x)\, r_{\text{bio}}(x)
\]

---

## 4. Blending Weight Function

A normalized transition coordinate is defined as:

\[
t(x) = \mathrm{clamp}
\left(
\frac{x - x_0}{\Delta x},\; 0,\; 1
\right)
\]

where:
- \(x_0 = \text{blend\_start\_fracL} \cdot L\)
- \(\Delta x = \text{blend\_span\_fracL} \cdot L\)

A **smoothstep function** is used:

\[
\alpha(x) = \alpha_{\max} \left( 3t^2 - 2t^3 \right)
\]

This ensures a C¹-continuous transition in the blending region.

---

## 5. Workbook Structure

### `extras`
- Stores all global parameters:
  - geometry
  - blending location
  - blending strength
- Acts as a single source of truth for the workbook.

### `blend`
- Computes:
  - normalized blending coordinate
  - blending weight
  - final blended radius

---

## 6. CAD Workflow (Autodesk Inventor)

1. Export the blended `(x, r)` data from Excel.
2. Import points into Inventor as a sketch.
3. Fit a spline through the points.
4. Revolve the spline about the centerline to generate the nose cone solid.

This approach separates **geometric reasoning** (Excel) from **solid modeling** (Inventor), improving controllability and iteration speed.

---

## 7. Notes on Smoothness

- The blending weight is C¹-continuous.
- The final radius curve is continuous, but curvature continuity depends on the input profiles.
- For higher-order smoothness, spline-based blending can be applied in future iterations.
