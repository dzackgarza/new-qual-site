---
schema: qual/card@1
id: P-LD3TY
kind: problem
title: Geometric diagonalisation of a quadratic form
classification:
  areas:
  - algebra
  topics:
  - Quadratic Forms
  - Diagonalization
  - Geometry
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Explain geometrically how you diagonalize a real quadratic form $q(x) = x^t A x$ on $\mathbb{R}^n$ (Principal Axis Theorem and Gram-Schmidt orthogonalization).
:::

::: solution
**Goal:** Provide the geometric explanation of diagonalizing a quadratic form via the Principal Axis Theorem (rotating to the axes of ellipsoid level surfaces) and Gram–Schmidt / Lagrange orthogonalization.

<1>1. Quadratic Forms as Quadric Level Surfaces:
    *Proof:*
    <2>1. A real quadratic form on $\mathbb{R}^n$ is defined by $q(x) = x^t A x = \sum_{i, j=1}^n A_{ij} x_i x_j$, where $A = A^t \in M_n(\mathbb{R})$ is a symmetric matrix.
    <2>2. **Geometric View:** The level set $\{x \in \mathbb{R}^n \mid q(x) = 1\}$ defines a quadric hypersurface in $\mathbb{R}^n$ (e.g. an ellipsoid, hyperboloid, or cylinder).
    <2>3. In the standard coordinate basis, the presence of cross terms $x_i x_j$ ($i \ne j$) means the principal symmetry axes of the ellipsoid/hyperboloid are tilted relative to the standard coordinate axes.

<1>2. Diagonalization via Principal Axis Theorem (Orthogonal Rotation):
    *Proof:*
    <2>1. **Finding the Extrema on the Unit Sphere (Rayleigh Quotient):**
        - Consider the optimization problem of maximizing $q(x)$ on the unit sphere $S^{n-1} = \{x \in \mathbb{R}^n \mid \|x\| = 1\}$.
        - By compactness of $S^{n-1}$, the continuous function $q(x)$ attains its global maximum at some unit vector $v_1$.
        - Using Lagrange multipliers $\nabla (x^t A x - \lambda (x^t x - 1)) = 0 \implies 2 A x - 2\lambda x = 0 \implies A v_1 = \lambda_1 v_1$.
        - Geometrically, $v_1$ points along the longest principal semi-axis of the quadric, and $\lambda_1 = q(v_1)$ is the reciprocal square of its length ($1/a_1^2$).
    <2>2. **Successive Orthogonal Complements:**
        - Next, maximize $q(x)$ subject to $\|x\| = 1$ and $x \perp v_1$ (on the equator).
        - This yields a second orthogonal axis $v_2 \perp v_1$ with eigenvalue $\lambda_2$.
        - Repeating this process $n$ times yields an **orthonormal basis of eigenvectors** $\{v_1, v_2, \dots, v_n\}$.
    <2>3. **Change of Coordinates (Rotation Matrix $P \in \operatorname{SO}(n)$):**
        - Let $P = [v_1 \mid v_2 \mid \cdots \mid v_n]$ be the orthogonal matrix ($P^t P = I_n$).
        - Setting $x = P y$, the new coordinates $y = (y_1, \dots, y_n)$ align precisely with the principal axes of the quadric:
            $$q(x) = (P y)^t A (P y) = y^t (P^t A P) y = y^t \operatorname{diag}(\lambda_1, \dots, \lambda_n) y = \sum_{i=1}^n \lambda_i y_i^2.$$
        - In the $y$-coordinates, all cross terms vanish, and the quadric equation becomes $\lambda_1 y_1^2 + \cdots + \lambda_n y_n^2 = 1$.

<1>3. Geometric Non-Orthogonal Diagonalization (Completing the Square / Sylvester's Law):
    *Proof:*
    <2>1. **Conjugate Directions (Gram–Schmidt with respect to $A$):**
        - Geometrically, choosing vectors $w_1, \dots, w_n$ that are $q$-orthogonal (conjugate with respect to the bilinear form, $w_i^t A w_j = 0$ for $i \ne j$) corresponds to finding conjugate diameters of the quadric.
        - Scaling the axes $z_i = \sqrt{|\lambda_i|} y_i$ transforms the ellipsoid into a standard unit sphere $\sum z_i^2 = 1$, exhibiting the signature $(p, q, r)$ (Sylvester's Law of Inertia).

<1>4. Conclusion:
    Diagonalization geometrically corresponds to rotating the coordinate system to align with the mutually perpendicular symmetry axes (principal axes) of the quadric level surface $q(x) = 1$. Q.E.D.
:::
