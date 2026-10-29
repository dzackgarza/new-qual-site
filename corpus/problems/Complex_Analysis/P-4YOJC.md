---
schema: qual/card@1
id: P-4YOJC
kind: problem
title: An entire function with a vanishing Taylor coefficient at every point is a
  polynomial
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Entire Functions
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Suppose $f$ is analytic, defined on all of $\CC$, and for each $z_0 \in \CC$ there is at least one coefficient in the expansion $f(z) = \sum_{n=0}^\infty c_n(z-z_0)^n$ is zero.
Prove that $f$ is a polynomial.
:::

::: {.hint}
Use the fact that $c_n n! = f^{(n)}(z_0)$ and use a countability argument.
:::

::: {.solution}

For $n\geq0$, let $Z_n\coloneqq\theset{z\in\CC\st f^{(n)}(z)=0}$.

::: pf

::: {.pf-step #cover}
$\CC=\Union_{n\geq0}Z_n$.

::: pf-proof
For each $z_0$, some coefficient $c_n=f^{(n)}(z_0)/n!$ of the expansion at $z_0$ vanishes, so $z_0\in Z_n$.
:::

:::

::: {.pf-step #some-derivative}
Some $f^{(N)}$ vanishes identically.

::: pf-proof
If no $f^{(n)}$ vanishes identically, then each $Z_n$ is a discrete closed subset of $\CC$ by the identity theorem, so it meets each compact disc $\abs{z}\leq k$ in finitely many points and is countable.
Then $\Union_nZ_n$ is countable, contradicting step [](#cover){.pf-ref}, since $\CC$ is uncountable.
:::

:::

::: pf-step
$f$ is a polynomial.

::: pf-proof
By step [](#some-derivative){.pf-ref}, $f^{(n)}(0)=0$ for all $n\geq N$, so the Taylor series of $f$ at $0$, which equals $f$ on $\CC$, is a polynomial of degree less than $N$.
:::

:::

:::

:::
