---
schema: qual/card@1
id: P-G2RYI
kind: problem
title: Weierstrass theorem on locally uniform limits of holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
  - Holomorphic Functions
  - Morera
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
Let $\Omega \subseteq \CC$ be an open domain, and let $\{f_n\}$ be a sequence of holomorphic functions on $\Omega$ that converges uniformly to a function $f$ on every compact subset $K \subset \Omega$.
Prove that:

(1) The limit function $f$ is holomorphic on $\Omega$.

(2) The sequence of derivatives $\{f_n'\}$ converges uniformly to $f'$ on every compact subset $K \subset \Omega$ (Weierstrass Convergence Theorem).
:::

::: {.solution}
::: pf

::: pf-step
(1) $f$ is holomorphic on $\Omega$.

::: pf-proof
Every point of $\Omega$ has a compact disk neighborhood in $\Omega$ on which $f_n\to f$ uniformly, so $f$ is continuous.
Let $T$ be a closed triangle contained in an open disk $D\subseteq\Omega$. Each $f_n$ is holomorphic on $D$, so $\int_{\partial T}f_n\,dz=0$ by Goursat's theorem, and uniform convergence on $\partial T$ gives
$$
\int_{\partial T}f(z)\,dz=\lim_{n\to\infty}\int_{\partial T}f_n(z)\,dz=0.
$$
By Morera's theorem $f$ is holomorphic on each such disk, hence on $\Omega$.
:::

:::

::: pf-step
(2) For every compact $K\subset\Omega$, $f_n'\to f'$ uniformly on $K$.

::: pf-proof

::: {.pf-step #neighborhood}
There is $r>0$ such that $K_r \coloneqq \theset{z \suchthat \operatorname{dist}(z,K)\le r}$ is a compact subset of $\Omega$.

::: pf-proof
The continuous function $z\mapsto\operatorname{dist}(z,\CC\setminus\Omega)$ is positive on $K$, so it has a positive minimum $2r$ on $K$ (take $r=1$ if $\Omega=\CC$). Then $K_r\subseteq\Omega$, and $K_r$ is closed and bounded.
:::

:::

::: pf-step
$\sup_K\abs{f_n'-f'}\le\frac1r\sup_{K_r}\abs{f_n-f}$, and the right side tends to $0$.

::: pf-proof
For $z\in K$ the closed disk $\abs{\zeta-z}\le r$ lies in $K_r$, and $f_n-f$ is holomorphic on $\Omega$ by (1). Cauchy's formula for the derivative gives
$$
f_n'(z)-f'(z)=\frac1{2\pi i}\int_{\abs{\zeta-z}=r}\frac{f_n(\zeta)-f(\zeta)}{(\zeta-z)^2}\,d\zeta,
$$
so $\abs{f_n'(z)-f'(z)}\le\frac1r\sup_{K_r}\abs{f_n-f}$. The right side tends to $0$ because $K_r$ is compact by step [](#neighborhood){.pf-ref}.
:::

:::

:::

:::

:::

:::
