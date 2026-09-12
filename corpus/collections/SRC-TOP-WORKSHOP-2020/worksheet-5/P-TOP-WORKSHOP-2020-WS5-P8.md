---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS5-P8
kind: problem
title: Cell structure on $S^2$ and long exact sequence computation of $H_i(S^n)$
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
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
(May 2013)

(a) Describe how to construct a cell structure on the $2$-sphere $S^2$ consisting of one $0$-cell, one $1$-cell, and two $2$-cells, and explain how to use this cell structure to calculate the simplicial homology groups of $S^2$.

(b) Explain how a long exact sequence may be used to calculate all of the (singular) homology groups $H_i(S^n)$ of the $n$-sphere $S^n$ (and calculate these groups for all $i$ and $n$).
:::

::: {.solution}
(a) Use the equator as the \(1\)-skeleton. Give that circle one \(0\)-cell \(v\) and one \(1\)-cell \(e\). The northern and southern open hemispheres are two \(2\)-cells \(N,S\), each attached along the equator. Orient them so their attaching maps have degrees \(+1\) and \(-1\). The cellular chain complex is
\[
0\to\mathbb Z^2\langle N,S\rangle
\xrightarrow{\partial_2}
\mathbb Z\langle e\rangle
\xrightarrow{0}
\mathbb Z\langle v\rangle\to0,
\]
with
\[
\partial_2(m,n)=m-n.
\]
Therefore
\[
H_2(S^2)=\ker\partial_2\cong\mathbb Z,
\qquad
H_1(S^2)=\mathbb Z/\operatorname{im}\partial_2=0,
\qquad
H_0(S^2)=\mathbb Z.
\]

(b) Decompose \(S^n\) into open neighborhoods of its upper and lower hemispheres. Each is contractible and their intersection deformation retracts onto \(S^{n-1}\). The reduced Mayer--Vietoris long exact sequence therefore yields isomorphisms
\[
\widetilde H_i(S^n)\cong\widetilde H_{i-1}(S^{n-1})
\]
for \(n\ge1\). Starting from
\[
\widetilde H_0(S^0)\cong\mathbb Z,
\]
induction gives
\[
\widetilde H_i(S^n)\cong
\begin{cases}
\mathbb Z,&i=n,\\
0,&i\ne n.
\end{cases}
\]
Hence for \(n\ge1\),
\[
H_i(S^n)\cong
\begin{cases}
\mathbb Z,&i=0,n,\\
0,&\text{otherwise}.
\end{cases}
\]
For \(n=0\), \(S^0\) has two points, so \(H_0(S^0)\cong\mathbb Z^2\) and all higher groups vanish.
:::
