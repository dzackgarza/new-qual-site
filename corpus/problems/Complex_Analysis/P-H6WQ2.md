---
schema: qual/card@1
id: P-H6WQ2
kind: problem
title: $\int_{\partial T}f(z)\,dz=0$ for a $C^1$ function on a triangle, by Green's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Theorem
  - Cauchy-Riemann
relations: []
review: draft
---

::: {.problem}
Suppose $f$ is continuously complex differentiable on $\Omega$, and $T$ is
a triangle whose interior is contained in $\Omega$. Use Green's theorem to
prove $\int_{\partial T}f(z)\,dz=0$.
:::

::: {.solution}
Write $f=u+iv$. Then
\[
\int_{\partial T}f(z)\,dz
=\int_{\partial T}(u\,dx-v\,dy)
+i\int_{\partial T}(v\,dx+u\,dy).
\]
Green's theorem turns the real and imaginary parts into
\[
\iint_T(-v_x-u_y)\,dxdy,
\qquad
\iint_T(u_x-v_y)\,dxdy,
\]
respectively. Both vanish by the Cauchy--Riemann equations, proving the
contour integral is zero.
:::