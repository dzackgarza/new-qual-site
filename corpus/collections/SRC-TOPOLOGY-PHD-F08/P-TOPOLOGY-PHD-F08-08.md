---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-08
kind: problem
title: The open unit interval is not compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part One, question 8 of the Topology Ph.D. Qualifying Exam dated January 17, 2009 in assets/attachments/F08phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Used the increasing open cover U_n=(1/n,1), n>=2. It covers (0,1), while
    every finite subfamily is contained in one U_N and misses positive points
    at most 1/N.
---

::: {.problem}
Prove that the open interval $(0,1)$ considered as a subset of $\mathbb R$ in the usual topology is not compact.
:::

::: {.solution}
For each integer $n\ge2$, set
\[
U_n=\left(\frac1n,1\right)\subseteq(0,1).
\]

<1>1. The family
\[
\{U_n:n\ge2\}
\]
is an open cover of $(0,1)$.
::: {.proof}
Each $U_n$ is open in the subspace topology on $(0,1)$.
Let $x\in(0,1)$.
By the Archimedean property, choose an integer $n$ with
\[
n>\frac1x.
\]
Then
\[
\frac1n<x<1,
\]
so $x\in U_n$.
Thus the family covers $(0,1)$.
:::

<1>2. No finite subfamily of this cover covers $(0,1)$.
::: {.proof}
Take finitely many sets
\[
U_{n_1},\ldots,U_{n_k}
\]
and let
\[
N=\max\{n_1,\ldots,n_k\}.
\]
Since $1/n$ decreases as $n$ increases,
\[
U_{n_i}\subseteq U_N
\]
for every $i$.
Hence
\[
U_{n_1}\cup\cdots\cup U_{n_k}=U_N.
\]
But
\[
\frac1{2N}\in(0,1)
\]
and
\[
\frac1{2N}\notin U_N
\]
because $1/(2N)<1/N$.
Therefore the finite subfamily does not cover $(0,1)$.
:::

<1>3. Hence $(0,1)$ is not compact.
::: {.proof}
By <1>1 there is an open cover of $(0,1)$, and by <1>2 it has no finite subcover.
This is exactly the negation of compactness.
:::
:::
