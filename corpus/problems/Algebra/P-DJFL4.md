---
schema: qual/card@1
id: P-DJFL4
kind: problem
title: An endomorphism of $\RR^5$ with eigenvalue $0$ is neither injective nor surjective
classification:
  areas:
  - algebra
  topics:
  - Rank and Nullity
  - Eigenvalues and Eigenvectors
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $L:\RR^5\to\RR^5$ be linear. Show that if $0$ is an eigenvalue of $L$, then $L$ is neither injective nor surjective.
:::

::: {.solution}

::: pf

::: pf-step

The map $L$ is not injective.

::: pf-proof

Since $0$ is an eigenvalue, there is a nonzero vector $v$ such that $L(v)=0$. Thus $0\ne v\in\ker L$.

:::

:::

::: pf-step

The map $L$ is not surjective.

::: pf-proof

By rank-nullity,
\[
5=\dim\ker L+\dim\operatorname{im}L.
\]
Since $\dim\ker L\ge1$,
\[
\dim\operatorname{im}L\le4<5=\dim\RR^5.
\]
Hence $\operatorname{im}L\ne\RR^5$.

:::

:::

:::

:::
