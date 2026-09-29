---
schema: qual/card@1
id: P-BERK80S-15
kind: problem
title: Left and right radicals of a bilinear form have equal dimension
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 15 of the vendored Berkeley Preliminary Exam, Summer 1980; restored the lost arrow in $B:E\times E\to F$ and the garbled “for all” conditions.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified that the two radicals are kernels of maps represented by a matrix and its transpose, hence have equal nullity.
---

::: {.problem}
Let $E$ be a finite-dimensional vector space over a field $F$.
Suppose $B:E\times E\to F$ is a bilinear map, not necessarily symmetric.
Define
\[
E_1=\{x\in E:B(x,y)=0\text{ for all }y\in E\},
\]
\[
E_2=\{y\in E:B(x,y)=0\text{ for all }x\in E\}.
\]
Prove that $\dim E_1=\dim E_2$.
:::

::: {.solution}
Let $n=\dim E$ and choose a basis $e_1,\ldots,e_n$ of $E$. Let
$$
M=(B(e_i,e_j))_{i,j}
$$
be the matrix of the bilinear form in this basis, and for $x\in E$ let
$[x]$ be its coordinate column vector.

::: pf

::: {.pf-step #s1}

$\dim E_1=\nullity(M^T)$.

::: pf-proof

Write $x=\sum_i x_i e_i$. For each basis vector $e_j$,
$$
B(x,e_j)=\sum_i x_i B(e_i,e_j).
$$
Thus the column whose $j$th entry is $B(x,e_j)$ is $M^T[x]$. By linearity
of $B$ in the second variable,
$$
x\in E_1
\iff B(x,e_j)=0\text{ for every }j
\iff M^T[x]=0.
$$

:::

:::

::: {.pf-step #s2}

$\dim E_2=\nullity(M)$.

::: pf-proof

For $y=\sum_j y_j e_j$, the column whose $i$th entry is $B(e_i,y)$ is
$M[y]$. By linearity of $B$ in the first variable,
$$
y\in E_2
\iff B(e_i,y)=0\text{ for every }i
\iff M[y]=0.
$$

:::

:::

::: {.pf-step #s3}

One has
$$
\boxed{\dim E_1=\dim E_2}.
$$

::: pf-proof

A matrix and its transpose have the same rank, so rank-nullity gives
$$
\nullity(M)=n-\operatorname{rank}(M)
=n-\operatorname{rank}(M^T)
=\nullity(M^T).
$$
Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give the claim.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required equality.

:::

:::

:::
