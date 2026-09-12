---
schema: qual/card@1
id: E-HAT-3.3-5
kind: problem
title: "Orientability of products"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that $M \times N$ is orientable iff $M$ and $N$ are both orientable.

::: {.solution}
Suppose first that $M^m$ and $N^n$ are oriented. Around $(x,y)\in M\times N$, choose oriented coordinate balls $U\ni x$ and $V\ni y$. Give $U\times V$ the product orientation. If one changes either oriented chart by an orientation-preserving transition map, the product transition map has positive determinant. Hence these product orientations are compatible and $M\times N$ is orientable.

Conversely suppose $M\times N$ is orientable. The local orientation system of a product is the tensor product of the two local orientation systems:
\[
H_{m+n}(M\times N,(M\times N)-\{(x,y)\};\mathbb Z)
\cong
H_m(M,M-\{x\};\mathbb Z)\otimes
H_n(N,N-\{y\};\mathbb Z).
\]
Fix $y_0\in N$. Restricting the orientation system of $M\times N$ to $M\times\{y_0\}$ gives the orientation system of $M$ tensored with the fixed rank-one group
\[
H_n(N,N-\{y_0\};\mathbb Z).
\]
Since the restricted product orientation system is trivial, the orientation system of $M$ is trivial. Thus $M$ is orientable. The same argument with a fixed $x_0\in M$ shows that $N$ is orientable.

Therefore
\[
\boxed{M\times N\text{ is orientable iff both }M\text{ and }N\text{ are orientable}.}
\]
:::
