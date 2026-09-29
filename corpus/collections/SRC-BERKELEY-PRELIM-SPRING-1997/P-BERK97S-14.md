---
schema: qual/card@1
id: P-BERK97S-14
kind: problem
title: Determinant of the matrix exponential
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Show that
\[
\det(\exp M)=e^{\operatorname{tr}M}
\]
for every complex $n\times n$ matrix $M$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

There is an invertible matrix $S$ such that
$$
T\coloneqq S^{-1}MS
$$
is upper triangular.

::: pf-proof

Over $\CC$, the characteristic polynomial of $M$ splits completely.
Hence the standard triangularization theorem gives a basis in which $M$ is upper triangular.

:::

:::

::: pf-step

If the diagonal entries of $T$ are $\lambda_1,\ldots,\lambda_n$, then $\exp T$ is upper triangular with diagonal entries
$$
e^{\lambda_1},\ldots,e^{\lambda_n}.
$$

::: pf-proof

Every power $T^k$ is upper triangular, and its $i$th diagonal entry is $\lambda_i^k$.
Therefore the power series
$$
\exp T
=
\sum_{k=0}^{\infty}\frac{T^k}{k!}
$$
is upper triangular, and its $i$th diagonal entry is
$$
\sum_{k=0}^{\infty}\frac{\lambda_i^k}{k!}
=
e^{\lambda_i}.
$$

:::

:::

::: {.pf-step #s3}

One has
$$
\boxed{\det(\exp M)=e^{\operatorname{tr}M}}.
$$

::: pf-proof

The exponential power series commutes with similarity, so step [](#s1){.pf-ref} gives
$$
\exp T=S^{-1}(\exp M)S.
$$
Hence
$$
\det(\exp M)
=
\det(\exp T)
=
\prod_{i=1}^n e^{\lambda_i}
=
e^{\lambda_1+\cdots+\lambda_n}.
$$
Since $T$ is upper triangular,
$$
\lambda_1+\cdots+\lambda_n
=
\operatorname{tr}T
=
\operatorname{tr}M,
$$
where the last equality uses invariance of trace under similarity.
This gives the displayed identity.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required formula.

:::

:::

:::
