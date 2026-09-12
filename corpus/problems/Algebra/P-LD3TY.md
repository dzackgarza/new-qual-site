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
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Explain geometrically how you diagonalize a real quadratic form $q(x) = x^t A x$ on $\mathbb{R}^n$ (Principal Axis Theorem and Gram-Schmidt orthogonalization).
:::

::: solution
Write the real quadratic form as
\[
q(x)=x^TAx
\]
with $A=A^T$. By the real spectral theorem, there is an orthogonal matrix
\[
Q=[v_1\ \cdots\ v_n]
\]
whose columns are orthonormal eigenvectors of $A$, with
\[
Q^TAQ=\operatorname{diag}(\lambda_1,\dots,\lambda_n).
\]
With the orthogonal change of coordinates $x=Qy$,
\[
q(x)=\lambda_1y_1^2+\cdots+\lambda_ny_n^2.
\]
Thus diagonalization is geometrically a rotation/reflection of coordinates to the mutually orthogonal principal directions of the form; the cross terms disappear in those coordinates.

One way to find the principal directions is variational. On the Euclidean unit sphere, the extrema of the Rayleigh quotient
\[
x\mapsto x^TAx
\]
occur at eigenvectors: the Lagrange-multiplier equation is
\[
Ax=\lambda x.
\]
After choosing one unit eigenvector, its Euclidean orthogonal complement is $A$-invariant, so the procedure can be repeated there. This is the geometric content behind the principal-axis theorem.

For a positive-definite form, the level set $q=1$ is an ellipsoid; if $\lambda_i>0$, the principal semiaxis in the $v_i$ direction has length $1/\sqrt{\lambda_i}$. For an indefinite form, positive and negative eigenvalues give the different families of hyperbolic directions, while zero eigenvalues give flat/cylindrical directions. Thus the signs and nullity, not a universal “longest axis,” encode the geometry.

A nonorthogonal diagonalization can also be obtained by completing squares, equivalently by Gram--Schmidt orthogonalization for the symmetric bilinear form associated to $q$ (when the required pivots are nonzero). Sylvester's law of inertia states that after an invertible linear change of coordinates the form has the normal form
\[
y_1^2+\cdots+y_p^2-y_{p+1}^2-\cdots-y_{p+q}^2,
\]
with the numbers of positive, negative, and zero directions invariant.
:::
