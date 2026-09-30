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
By contradiction: after translating, suppose $0\in\Omega$, $f(0) = 0$ and $f'(0)=0$. An injective $f$ is nonconstant, so $0$ is a zero of $f$ of some finite order $m$, and $m\geq2$ since $f(0)=f'(0)=0$.
Write $f(z)=z^mg(z)$ with $g$ holomorphic near $0$ and $g(0)\neq0$. On a small disk $D$ about $0$, $g$ is nonvanishing and has a holomorphic $m$-th root $h$, so $f=\varphi^m$ with $\varphi(z)\definedas zh(z)$.
Since $\varphi'(0)=h(0)\neq0$, $\varphi$ maps a neighborhood $U\subseteq D$ of $0$ biholomorphically onto a disk $\abs w<\delta$.
For $0<\eps<\delta$ and $\zeta=e^{2\pi i/m}\neq1$, the distinct points $w_1=\eps$ and $w_2=\zeta\eps$ satisfy $w_1^m=w_2^m$, so their preimages under $\varphi$ are distinct points of $U$ with the same image under $f$, contradicting injectivity.
:::
