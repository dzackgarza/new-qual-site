---
schema: qual/card@1
id: E-TUKVC
kind: problem
title: Entire functions with a vanishing Taylor coefficient at every point are polynomials
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Entire Functions
  - Polynomials
  - Identity Theorem
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
For $n\geq 0$ put $Z_n \coloneqq \theset{z\in \CC \st f^{(n)}(z) = 0 }$.

::: pf

::: {.pf-step #cover}
Each $Z_n$ is closed and $\bigcup_{n\geq 0} Z_n = \CC$.

::: pf-proof
$Z_n$ is the zero set of the continuous function $f^{(n)}$. At $z_0\in\CC$ the hypothesis gives $n$ with $c_n = f^{(n)}(z_0)/n! = 0$, so $z_0\in Z_n$.
:::

:::

::: {.pf-step #interior}
Some $Z_n$ contains a disc $D_\varepsilon(z_0)$.

::: pf-proof
By the Baire category theorem, the complete metric space $\CC$ is not a countable union of closed sets with empty interior, so by step [](#cover){.pf-ref} some $Z_n$ has nonempty interior.
:::

:::

::: pf-step
$f$ is a polynomial of degree less than $n$.

::: pf-proof
By step [](#interior){.pf-ref}, the entire function $f^{(n)}$ vanishes on a disc, so $f^{(n)}\equiv 0$ on $\CC$ by the identity theorem. Then $f^{(k)}(0) = 0$ for all $k\geq n$, and the Taylor series of $f$ at $0$, which converges to $f$ on $\CC$, is $\sum_{k<n}\frac{f^{(k)}(0)}{k!}z^k$.
:::

:::

:::

:::
