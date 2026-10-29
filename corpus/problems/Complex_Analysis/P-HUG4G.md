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

::: {.problem}
Let $\Omega \subseteq \CC$ be an open domain, and let $T \subset \Omega$ be a closed triangle whose interior $T^\circ \subset \Omega$.

(1) Assuming $f \in C^1(\Omega)$ (meaning $f(z) = u(x, y) + i v(x, y)$ has continuous real partial derivatives), apply **Green's Theorem** and the Cauchy-Riemann equations to prove Cauchy's Theorem on triangles:
$$\oint_{\partial T} f(z) \, dz = 0.$$

(2) State **Goursat's Theorem** (which removes the assumption that $f'$ is continuous) and outline Goursat's proof via triangular subdivision.
:::

::: {.solution}
In both parts $f$ is holomorphic on $\Omega$; in (1) it is also $C^1$, so $u,v$ satisfy $u_x=v_y$ and $u_y=-v_x$.

::: pf

::: pf-step
(1) If $f$ is $C^1$ on $\Omega$, then $\oint_{\partial T}f(z)\,dz=0$.

::: pf-proof
With $dz=dx+i\,dy$,
$$
\oint_{\partial T}f(z)\,dz=\oint_{\partial T}(u\,dx-v\,dy)+i\oint_{\partial T}(v\,dx+u\,dy).
$$
Green's theorem, valid since $u,v$ are $C^1$ on a neighborhood of $T$, turns these into $-\iint_T(v_x+u_y)\,dA$ and $\iint_T(u_x-v_y)\,dA$, and the Cauchy–Riemann equations make both integrands zero.
:::

:::

::: pf-step
(2) Goursat's theorem: if $f$ is complex differentiable at every point of an open set $\Omega$, then $\oint_{\partial T}f(z)\,dz=0$ for every closed triangle $T\subset\Omega$.

::: pf-proof

::: {.pf-step #nested}
There are nested closed triangles $T=T_0\supset T_1\supset\cdots$ with $\operatorname{diam}T_n=2^{-n}d$, $\operatorname{length}\partial T_n=2^{-n}p$, and $\abs{\oint_{\partial T}f\,dz}\le 4^n\abs{\oint_{\partial T_n}f\,dz}$, where $d$ and $p$ are the diameter and perimeter of $T$.

::: pf-proof
Joining the midpoints of the sides divides $T_n$ into four similar triangles with half the diameter and perimeter. The interior edges cancel, so $\oint_{\partial T_n}$ is the sum of the four boundary integrals, and one of them, chosen as $T_{n+1}$, has modulus at least a quarter of the total.
:::

:::

::: pf-step
$\oint_{\partial T}f\,dz=0$.

::: pf-proof
The $T_n$ are nested nonempty compact sets with diameters tending to $0$, so they meet in one point $z_0\in T$. Write $f(z)=f(z_0)+f'(z_0)(z-z_0)+\eta(z)(z-z_0)$ with $\eta(z)\to0$ as $z\to z_0$. The polynomial part has a primitive, so its integral over $\partial T_n$ vanishes, and
$$
\abs{\oint_{\partial T_n}f\,dz}=\abs{\oint_{\partial T_n}\eta(z)(z-z_0)\,dz}\le\sup_{T_n}\abs\eta\cdot 2^{-n}d\cdot 2^{-n}p.
$$
By step [](#nested){.pf-ref}, $\abs{\oint_{\partial T}f\,dz}\le dp\sup_{T_n}\abs\eta$, which tends to $0$ as $n\to\infty$.
:::

:::

:::

:::

:::

:::
