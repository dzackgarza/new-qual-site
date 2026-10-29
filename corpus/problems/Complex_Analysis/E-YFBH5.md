---
schema: qual/card@1
id: E-YFBH5
kind: problem
title: Analytic self-maps of the disc with a zero of order $k$ at $0$ and $\abs{f}\to
  1$ at the boundary
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Schwarz Lemma
  - Zeros
  - Maximum Modulus Principle
relations: []
review: draft
---

::: {.problem}
Suppose $f:\DD\to\DD$ is analytic, has a single zero of order $k$ at $z=0$, and satisfies $\lim_{\abs z \to 1} \abs{f(z)} = 1$.
Give with proof a formula for $f(z)$.
:::

::: {.solution}
Let $g$ be the holomorphic extension of $f(z)/z^k$ across $0$.

::: pf

::: {.pf-step #nonvanishing}
$g$ has no zeros on $\DD$, and $\abs{g(z)}\to1$ as $\abs z\to1$.

::: pf-proof
$g(0)\neq0$ because the zero of $f$ at $0$ has order exactly $k$, and $g$ has no other zeros because $0$ is the only zero of $f$.
Also $\abs{g(z)} = \abs{f(z)}/\abs z^k\to1$.
:::

:::

::: {.pf-step #bound}
If $h$ is holomorphic on $\DD$ and $\abs{h(z)}\to1$ as $\abs z\to1$, then $\abs h\le1$ on $\DD$.

::: pf-proof
Fix $z_0\in\DD$ and $\varepsilon>0$.
There is $r_0<1$ with $\abs{h(z)}<1+\varepsilon$ for $r_0<\abs z<1$.
For $\max\{r_0,\abs{z_0}\}<r<1$, the maximum modulus principle on $\abs z\le r$ gives $\abs{h(z_0)}\le\max_{\abs z=r}\abs h<1+\varepsilon$.
Since $\varepsilon$ is arbitrary, $\abs{h(z_0)}\le1$.
:::

:::

::: {.pf-step #unimodular}
$\abs g\equiv1$ on $\DD$.

::: pf-proof
By step [](#nonvanishing){.pf-ref}, both $g$ and $1/g$ are holomorphic on $\DD$ with modulus tending to $1$ at the boundary.
Step [](#bound){.pf-ref} applied to each gives $\abs g\le1$ and $\abs{1/g}\le1$.
:::

:::

::: pf-step
$\boxed{f(z) = \lambda z^k}$ for some constant $\lambda$ with $\abs\lambda=1$, and every such map satisfies the hypotheses.

::: pf-proof
By step [](#unimodular){.pf-ref}, $g(\DD)$ lies in the unit circle, which contains no nonempty open set, so $g$ is a constant $\lambda$ with $\abs\lambda=1$ by the open mapping theorem.
Conversely, $\lambda z^k$ maps $\DD$ into $\DD$, vanishes only at $0$ to order $k$, and has modulus $\abs z^k\to1$.
:::

:::

:::

:::
