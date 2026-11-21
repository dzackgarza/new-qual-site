---
schema: qual/card@1
id: P-CAF24E
kind: problem
title: '$L^1$-bounded holomorphic functions on the disc have a locally uniform subsequence'
classification:
  areas:
  - complex-analysis
  topics:
  - Normal Families
  - Uniform Convergence
relations: []
review: draft
---

::: {.problem}
Let $f_n : \DD \to \CC$ be holomorphic functions such that
$$
\int_{\DD} \abs{f_n}\, dx\, dy \le 1, \qquad \forall n \ge 1.
$$
Show that there exists a subsequence of $\{f_n\}$ that converges locally uniformly on $\DD$.
:::

::: {.solution}

The argument is the card's own, from the submean inequality for subharmonic functions and Montel's theorem; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $f_{n}$ be holomorphic on $\DD$ with $\int_{\DD}\abs{f_{n}}\,dA\le1$ for every $n$, where $dA$ is area measure.

::: pf

::: {.pf-step #bound}
For every compact $K\Subset\DD$ there is $M$ with $\sup_{K}\abs{f_{n}}\le M$ for all $n$.

::: pf-proof
Since $K$ is compact and $\DD$ open, $r=\operatorname{dist}(K,\partial\DD)>0$, so $B(z,r)\subset\DD$ for every $z\in K$. For holomorphic $f$ the function $\abs{f}$ is subharmonic, so the submean inequality gives, for $z\in K$,
$$
\abs{f_{n}(z)}\le\frac{1}{\pi r^{2}}\int_{B(z,r)}\abs{f_{n}(w)}\,dA(w)\le\frac{1}{\pi r^{2}}\int_{\DD}\abs{f_{n}}\,dA\le\frac{1}{\pi r^{2}},
$$
the middle inequality because $B(z,r)\subset\DD$ and the integrand is nonnegative. So $M=1/(\pi r^{2})$ works, independently of $n$.
:::

:::

::: {.pf-step #normal}
The family $\{f_{n}\}$ is normal in $H(\DD)$.

::: pf-proof
It is locally uniformly bounded by step [](#bound){.pf-ref}, and a locally uniformly bounded family of holomorphic functions on a plane domain is normal (Montel's theorem).
:::

:::

::: {.pf-step #subsequence}
There is a subsequence of $(f_{n})$ converging locally uniformly on $\DD$ to a holomorphic function.

::: pf-proof
By step [](#normal){.pf-ref} the sequence $(f_{n})$ has a subsequence converging uniformly on every compact subset of $\DD$. In the spherical formulation of normality the limit could be the constant $\infty$, but the local bounds of step [](#bound){.pf-ref} exclude that: on each compact $K$ the limit of a locally uniformly convergent subsequence is again bounded by $M$, hence finite. A locally uniform limit of holomorphic functions on $\DD$ is holomorphic (Weierstrass' theorem on locally uniform limits).
:::

:::

:::
:::
