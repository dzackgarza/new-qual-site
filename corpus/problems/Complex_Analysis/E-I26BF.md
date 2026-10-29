---
schema: qual/card@1
id: E-I26BF
kind: problem
title: An injective holomorphic function has nonvanishing derivative
classification:
  areas:
  - complex-analysis
  topics:
  - Biholomorphisms
  - Zeros
  - Open Mapping Theorem
relations: []
review: draft
---

::: {.exercise}
Show that if $f$ is holomorphic on $\Omega$ and injective, then $f'(z)$ is nonvanishing on $\Omega$.
:::

::: {.solution}
Suppose, for contradiction, that $f'(z_0)=0$ for some $z_0\in\Omega$; after translating, $z_0=0$ and $f(0)=0$.

::: pf

::: {.pf-step #root}
Near $0$, $f=\varphi^m$ for some $m\ge2$ and some holomorphic $\varphi$ with $\varphi(0)=0$ and $\varphi'(0)\neq0$.

::: pf-proof
An injective $f$ is nonconstant, so $0$ is a zero of $f$ of some finite order $m$, and $m\geq2$ since $f(0)=f'(0)=0$.
Write $f(z)=z^mg(z)$ with $g$ holomorphic near $0$ and $g(0)\neq0$.
On a small disk $D$ about $0$, $g$ has no zeros and so has a holomorphic $m$-th root $h$; let $\varphi(z)\coloneqq zh(z)$, so $\varphi'(0)=h(0)\neq0$.
:::

:::

::: pf-step
$f$ is not injective near $0$, a contradiction.

::: pf-proof
By step [](#root){.pf-ref} and the inverse function theorem, $\varphi$ maps a neighborhood $U\subseteq D$ of $0$ biholomorphically onto a disk $\abs w<\delta$.
For $0<\varepsilon<\delta$ and $\zeta=e^{2\pi i/m}\neq1$, the distinct points $w_1=\varepsilon$ and $w_2=\zeta\varepsilon$ satisfy $w_1^m=w_2^m$, so their preimages under $\varphi$ are distinct points of $U$ with the same image under $f$.
:::

:::

:::

:::
