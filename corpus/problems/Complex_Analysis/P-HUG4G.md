---
schema: qual/card@1
id: P-HUG4G
kind: problem
title: Cauchy's theorem via Green's theorem, and Goursat's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Green's Theorem
  - Cauchy Integral Theorem
  - Contour Integration
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
Let $\Omega \subseteq \mathbb{C}$ be an open domain, and let $T \subset \Omega$ be a closed triangle whose interior $T^\circ \subset \Omega$.
1. Assuming $f \in C^1(\Omega)$ (meaning $f(z) = u(x, y) + i v(x, y)$ has continuous real partial derivatives), apply **Green's Theorem** and the Cauchy-Riemann equations to prove Cauchy's Theorem on triangles:
$$\oint_{\partial T} f(z) \, dz = 0.$$

2. State **Goursat's Theorem** (which removes the assumption that $f'$ is continuous) and outline Goursat's proof via triangular subdivision.
:::

::: solution
Let $f=u+iv$ and $dz=dx+i\,dy$. Then
\[
\oint_{\partial T}f(z)\,dz
=
\oint_{\partial T}(u\,dx-v\,dy)
+i\oint_{\partial T}(v\,dx+u\,dy).
\]
Green's theorem gives
\[
\oint_{\partial T}(u\,dx-v\,dy)
=-\iint_T(v_x+u_y)\,dA,
\]
and
\[
\oint_{\partial T}(v\,dx+u\,dy)
=\iint_T(u_x-v_y)\,dA.
\]
The Cauchy--Riemann equations make both integrands zero, so
\[
\oint_{\partial T}f(z)\,dz=0.
\]

Goursat's theorem removes the $C^1$ assumption: if $f$ is complex differentiable at every point of an open set, then the integral around every triangle contained in the open set is zero.

For the standard proof, repeatedly subdivide a triangle into four congruent triangles and choose at each stage one whose boundary integral has modulus at least one quarter of its parent's. This produces nested triangles $T_n$ with diameter and perimeter scaled by $2^{-n}$ and a unique common point $z_0$. Differentiability at $z_0$ gives
\[
f(z)=f(z_0)+f'(z_0)(z-z_0)+\eta(z)(z-z_0),
\qquad \eta(z)\to0.
\]
The constant and linear terms integrate to zero, while
\[
\left|\oint_{\partial T_n}\eta(z)(z-z_0)\,dz\right|
\le
\sup_{T_n}|\eta|\,\operatorname{diam}(T_n)\,\operatorname{length}(\partial T_n).
\]
Multiplying by the factor $4^n$ accumulated from the subdivisions cancels the $4^{-n}$ geometric factor. Since $\sup_{T_n}|\eta|\to0$, the original triangle integral is zero.
:::
