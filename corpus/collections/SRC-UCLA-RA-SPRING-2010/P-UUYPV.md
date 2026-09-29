---
schema: qual/card@1
id: P-UUYPV
kind: problem
title: An elliptic function has equally many zeros and poles in a period square
classification:
  areas:
  - real-analysis
  topics:
  - Meromorphic Functions
  - Argument Principle
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $F(z)$ be a non-constant meromorphic function on the complex plane $\mathbb{C}$ such that $F(z+1)=F(z)=F(z+i)$ for all $z$.
Let $Q$ be a square with vertices $z, z+1, z+i,$ and $z+1+i$ such that $F$ has no zeros and no poles on $\partial Q$.
Prove that inside $Q$ the function $F$ has the same number of zeros as poles (counting multiplicities).
:::

::: {.solution}
**Goal:** Let $F$ be a non-constant meromorphic function on $\CC$ with periods $1$ and $i$, and let $Q$ be a period square with no zeros or poles of $F$ on $\bd Q$.
Prove $F$ has the same number of zeros as poles inside $Q$ (counting multiplicities).

::: pf

::: {.pf-step #s1}

Setup: let $G = F'/F$; $G$ is meromorphic with periods $1$ and $i$ wherever $F \ne 0, \infty$.

::: pf-proof

$F(z+1) = F(z)$ and $F(z+i) = F(z)$; differentiating, $F'(z+1) = F'(z)$, $F'(z+i) = F'(z)$, so $G$ is doubly periodic on its domain.

:::

:::

::: {.pf-step #s2}

By the argument principle, $N - P = \frac{1}{2\pi i}\oint_{\bd Q} G(z)\, dz$ where $N, P$ are the numbers of zeros and poles of $F$ inside $Q$.

::: pf-proof

the argument principle for meromorphic functions.

:::

:::

::: {.pf-step #s3}

$\oint_{\bd Q} G\, dz = 0$.

::: pf-proof

::: pf-step

Write $Q = \{z_0 + s + it : 0 \le s, t \le 1\}$ and $\bd Q$ as the four sides $\gamma_1, \gamma_2, \gamma_3, \gamma_4$ (bottom, right, top, left, counterclockwise).

::: pf-proof

parametrization.

:::

:::

::: {.pf-step #s3-2}

The integrals over opposite sides cancel: $\int_{\gamma_1} G + \int_{\gamma_3} G = 0$ and $\int_{\gamma_2} G + \int_{\gamma_4} G = 0$.

::: pf-proof

$\int_{\gamma_3} G = \int_1^0 G(z_0 + s + i)\, ds = -\int_0^1 G(z_0 + s)\, ds = -\int_{\gamma_1} G$ by the period $i$ (and similarly the vertical sides cancel by the period $1$); no zeros or poles on $\bd Q$ makes $G$ continuous there, so the integrals are well defined.

:::

:::

::: pf-step

Total integral is 0.

::: pf-proof

sum over the four sides: step [](#s3-2){.pf-ref} gives pairwise cancellation.

:::

:::

:::

:::

::: {.pf-step #s4}

$N = P$.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} give $N - P = 0$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove the claim.

:::

:::

:::
