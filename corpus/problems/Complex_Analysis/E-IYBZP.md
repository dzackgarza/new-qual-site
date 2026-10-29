---
schema: qual/card@1
id: E-IYBZP
kind: problem
title: A holomorphic function with a vanishing Taylor coefficient at every point is
  a polynomial
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Cauchy Integral Formula
relations: []
review: draft
---

::: {.exercise}
If $f$ is holomorphic on a region $\Omega$ and for each $z_0\in\Omega$ at least one coefficient in the power series $f(z)=\sum_{n=0}^\infty c_n(z-z_0)^n$ is zero, show that $f$ is a polynomial.
:::

::: {.solution}
For $n\ge0$, let $Z_n\coloneqq\theset{z\in\Omega \st f^{(n)}(z)=0}$, which is closed in $\Omega$.
Since $c_n=f^{(n)}(z_0)/n!$, the hypothesis says $\Omega=\bigcup_{n\ge0}Z_n$.

::: pf

::: {.pf-step #baire}
Some $f^{(N)}$ vanishes on a nonempty open subset of $\Omega$.

::: pf-proof
Choose a closed disk $\overline D\subseteq\Omega$ with interior $D$.
Since $\overline D$ is a complete metric space and $\overline D=\bigcup_n\qty{Z_n\intersect\overline D}$, Baire's theorem gives some $Z_N\intersect\overline D$ with nonempty interior in $\overline D$.
A nonempty relatively open subset of $\overline D$ meets the dense subset $D$ in a nonempty open subset of $\Omega$, on which $f^{(N)}=0$.
:::

:::

::: {.pf-step #vanish}
$f^{(N)}\equiv0$ on $\Omega$.

::: pf-proof
This follows from step [](#baire){.pf-ref} by the identity theorem, since $\Omega$ is connected.
:::

:::

::: pf-step
$f$ is a polynomial of degree at most $N-1$, and $f\equiv0$ if $N=0$.

::: pf-proof
If $N=0$, step [](#vanish){.pf-ref} says $f\equiv0$.
If $N\ge1$, fix $z_0\in\Omega$; the polynomial $P(z)\coloneqq\sum_{n<N}f^{(n)}(z_0)(z-z_0)^n/n!$ has the same derivatives of order less than $N$ at $z_0$ as $f$, and all its derivatives of order at least $N$ vanish, as do those of $f$ by step [](#vanish){.pf-ref}.
So every derivative of $f-P$ vanishes at $z_0$, and the identity theorem gives $f=P$ on $\Omega$.
:::

:::

:::

:::
