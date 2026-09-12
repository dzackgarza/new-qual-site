---
schema: qual/card@1
id: E-SS2.EX-5
kind: problem
title: "Cauchy's theorem via Green's theorem for C1 functions"
classification:
  areas:
  - complex-analysis
  topics: ["Cauchy's Theorem", 'Contour Integration', 'Residues']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: exercise
5. Suppose $f$ is continuously complex diferentiable on $\Omega ,$ and $T \subset \Omega$ is a triangle whose interior is also contained in Ω. Apply Green’s theorem to show that

$$
\int_ {T} f (z) d z = 0.
$$

This provides a proof of Goursat’s theorem under the additional assumption that $f ^ { \prime }$ is continuous.

[Hint: Green’s theorem says that if $( F , G )$ is a continuously diferentiable vector field, then

$$
\int_ {T} F d x + G d y = \int_ {\mathrm{Interiorof} T} \left(\frac {\partial G}{\partial x} - \frac {\partial F}{\partial y}\right) d x d y.
$$

For appropriate $F$ and G, one can then use the Cauchy-Riemann equations.]
:::

::: solution
Write
\[
f=u+iv,
\qquad dz=dx+i\,dy.
\]
Then
\[
f(z)\,dz=(u\,dx-v\,dy)+i(v\,dx+u\,dy).
\]
Because $f$ is continuously complex differentiable, $u$ and $v$ are $C^1$ and satisfy the Cauchy--Riemann equations
\[
u_x=v_y,
\qquad
u_y=-v_x.
\]

Apply Green's theorem to the real part:
\[
\int_T u\,dx-v\,dy
=\iint_{\operatorname{int}T}(-v_x-u_y)\,dx\,dy=0.
\]
Apply it again to the imaginary part:
\[
\int_T v\,dx+u\,dy
=\iint_{\operatorname{int}T}(u_x-v_y)\,dx\,dy=0.
\]
Hence both real and imaginary parts vanish, and therefore
\[
\boxed{\displaystyle \int_T f(z)\,dz=0}.
\]
:::
