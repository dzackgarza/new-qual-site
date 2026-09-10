---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS4A-HW4
kind: problem
title: Mayer–Vietoris homology sequence for an open cover
classification:
  areas:
  - topology
  topics:
  - Mayer-Vietoris
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $X$ be a topological space and $A,B\subset X$ open subspaces with $X=A\cup B$.
What does the Mayer--Vietoris theorem say about the homology groups of $X$ and its subspaces?
:::

::: {.solution}
For an open cover \(X=A\cup B\), Mayer--Vietoris gives a natural long exact sequence
\[
\cdots\to H_n(A\cap B)
\xrightarrow{(i_*,-j_*)}
H_n(A)\oplus H_n(B)
\xrightarrow{k_*+\ell_*}
H_n(X)
\xrightarrow{\partial}
H_{n-1}(A\cap B)\to\cdots,
\]
where \(i,j\) are the inclusions of \(A\cap B\) into \(A,B\), and \(k,\ell\) are the inclusions of \(A,B\) into \(X\). The sequence continues through degree \(0\):
\[
H_1(X)\to H_0(A\cap B)\to H_0(A)\oplus H_0(B)\to H_0(X)\to0.
\]
Equivalently, using reduced homology gives the corresponding reduced long exact sequence without the terminal augmentation issue. Exactness means at every term the image of one map equals the kernel of the next, so knowing the homology of \(A\), \(B\), and \(A\cap B\) constrains and often determines the homology of \(X\).
:::
