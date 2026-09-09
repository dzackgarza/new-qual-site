---
schema: qual/card@1
id: E-HAT-3.3-24
kind: problem
title: "Homology of closed 3-manifolds"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 24; the stored statement matches the current online text and diagram where applicable.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Let $M$ be a closed connected 3-manifold, and write $H_1(M; \mathbb{Z})$ as $\mathbb{Z}^r \oplus F$, the direct sum of a free abelian group of rank $r$ and a finite group $F$.
Show that $H_2(M; \mathbb{Z})$ is $\mathbb{Z}^r$ if $M$ is orientable and $\mathbb{Z}^{r-1} \oplus \mathbb{Z}_2$ if $M$ is nonorientable.
In particular, $r \geq 1$ when $M$ is nonorientable.
Using Exercise 6, construct examples showing there are no other restrictions on the homology groups of closed 3-manifolds.

::: {.solution}
Write
\[
H_1(M;\mathbb Z)\cong\mathbb Z^r\oplus F
\]
with $F$ finite.

If $M$ is orientable, Poincaré duality and the universal coefficient theorem give
\[
H_2(M;\mathbb Z)\cong H^1(M;\mathbb Z)
\cong\operatorname{Hom}(H_1(M),\mathbb Z)
\cong\mathbb Z^r.
\]

Suppose $M$ is nonorientable. Corollary 3.28 says that the torsion subgroup of $H_2(M;\mathbb Z)$ is exactly $\mathbb Z_2$. Also every closed odd-dimensional manifold has Euler characteristic zero. Since $M$ is connected and nonorientable,
\[
H_0(M)\cong\mathbb Z,
\qquad H_3(M)=0.
\]
Hence
\[
0=\chi(M)=1-r+\operatorname{rank}H_2(M),
\]
so
\[
\operatorname{rank}H_2(M)=r-1.
\]
Therefore
\[
\boxed{H_2(M;\mathbb Z)\cong\mathbb Z^{r-1}\oplus\mathbb Z_2.}
\]
In particular $r\ge1$.

It remains to see that there are no further restrictions. Write
\[
F\cong\mathbb Z_{m_1}\oplus\cdots\oplus\mathbb Z_{m_s}.
\]
For orientable examples, take the connected sum of $r$ copies of $S^1\times S^2$ and lens spaces $L(m_j,1)$. Exercise 6 gives
\[
H_1\cong\mathbb Z^r\oplus F,
\qquad
H_2\cong\mathbb Z^r.
\]

For nonorientable examples, let $N$ be the twisted $S^2$-bundle over $S^1$, obtained as the mapping torus of a reflection of $S^2$. Its mapping-torus sequence gives
\[
H_1(N)\cong\mathbb Z,
\qquad
H_2(N)\cong\mathbb Z_2.
\]
Taking the connected sum of $N$, $r-1$ copies of $S^1\times S^2$, and the same lens spaces yields
\[
H_1\cong\mathbb Z^r\oplus F,
\qquad
H_2\cong\mathbb Z^{r-1}\oplus\mathbb Z_2.
\]
Thus every group pattern allowed by the formulas occurs.
:::
