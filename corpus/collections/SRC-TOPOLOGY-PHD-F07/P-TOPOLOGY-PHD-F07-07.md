---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F07-07
kind: problem
title: The real line is not compact
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
  note: Checked against Part One, question 7 of the Topology Ph.D. Qualifying Exam dated January 12, 2008 in assets/attachments/F07phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Exhibited the cover {(-n,n): n>=1}; every finite subfamily is contained in
    its largest member and misses points outside that bounded interval.
---

::: {.problem}
Prove that $\mathbb R$ is not compact.
:::

::: {.solution}
<1>1. The family
\[
\mathcal U=\{(-n,n):n\in\mathbb N,\ n\ge1\}
\]
is an open cover of $\mathbb R$.
::: {.proof}
Each interval $(-n,n)$ is Euclidean open.
Given $x\in\mathbb R$, choose an integer $n>|x|$.
Then
\[
-n<x<n,
\]
so $x\in(-n,n)$.
Thus the union of the members of $\mathcal U$ is all of $\mathbb R$.
:::

<1>2. No finite subfamily of $\mathcal U$ covers $\mathbb R$.
::: {.proof}
Take finitely many members
\[
(-n_1,n_1),\ldots,(-n_k,n_k).
\]
Let
\[
N=\max\{n_1,\ldots,n_k\}.
\]
Since these intervals are nested as their radii increase,
\[
(-n_1,n_1)\cup\cdots\cup(-n_k,n_k)=(-N,N).
\]
The point $N+1$ does not belong to this union.
Hence the chosen finite subfamily does not cover $\mathbb R$.
:::

<1>3. Therefore $\mathbb R$ is not compact.
::: {.proof}
Compactness requires every open cover to have a finite subcover.
The open cover in <1>1 has no finite subcover by <1>2, so $\mathbb R$ fails the definition of compactness.
:::
:::
