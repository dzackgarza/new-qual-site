---
schema: qual/card@1
id: P-HGQ8T
kind: problem
title: For symmetric $A,B$, the product $AB$ is symmetric iff $AB=BA$; $BB^t$ and
  $B+B^t$ are symmetric
classification:
  areas:
  - algebra
  topics:
  - Matrices
  - Bilinear Forms
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

Let $A, B \in M_n(R)$ be $n \times n$ matrices over a commutative ring $R$.

(a) Prove that if $A$ and $B$ are symmetric matrices ($A^t = A, B^t = B$), then the product $AB$ is symmetric if and only if $A$ and $B$ commute ($AB = BA$).

(b) For an arbitrary matrix $B \in M_n(R)$, prove that $B B^t$ and $B + B^t$ are symmetric, and $B - B^t$ is skew-symmetric.

:::

::: {.solution}

::: pf

::: pf-step

(a) If $A^t=A$ and $B^t=B$, then $AB$ is symmetric if and only if $AB=BA$.

::: pf-proof

Since $R$ is commutative, $(AB)^t=B^tA^t=BA$. Hence $(AB)^t=AB$ if and only if $BA=AB$.

:::

:::

::: pf-step

(b) $BB^t$ and $B+B^t$ are symmetric, and $B-B^t$ is skew-symmetric.

::: pf-proof

We have
$$
(BB^t)^t=(B^t)^tB^t=BB^t,
\qquad
(B+B^t)^t=B^t+B=B+B^t,
\qquad
(B-B^t)^t=B^t-B=-(B-B^t).
$$

:::

:::

:::

:::
