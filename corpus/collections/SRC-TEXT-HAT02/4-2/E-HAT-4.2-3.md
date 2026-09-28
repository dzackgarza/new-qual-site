---
schema: qual/card@1
id: E-HAT-4.2-3
kind: problem
title: "Homotopy groups of punctured lens spaces"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

::: {.problem}
Let $X$ be obtained from a lens space of dimension $2n+1$ by deleting a point.
Compute $\pi_{2n}(X)$ as a module over $\mathbb{Z}[\pi_1(X)]$.
:::

::: {.solution}
Let the lens space be
\[
L^{2n+1}=S^{2n+1}/G,
\qquad G\cong\mathbb Z_m,
\]
and let \(X=L-\{x\}\). The inverse image of \(x\) in the universal cover consists of one free \(G\)-orbit of \(m\) points, so the universal cover of \(X\) is
\[
\widetilde X=S^{2n+1}-G\widetilde x.
\]
A sphere with \(m\) points deleted is homotopy equivalent to a wedge of \(m-1\) copies of \(S^{2n}\). Therefore \(\widetilde X\) is \((2n-1)\)-connected and
\[
\pi_{2n}(X)
\cong\pi_{2n}(\widetilde X)
\cong H_{2n}(\widetilde X)
\cong\mathbb Z^{m-1}
\]
by Hurewicz.

We now keep track of the \(G\)-action. Equivariant Alexander duality identifies
\[
H_{2n}(S^{2n+1}-G\widetilde x)
\cong \widetilde H^0(G\widetilde x).
\]
The latter is the reduced permutation module on the regular \(G\)-set. If
\[
\mathbb Z[G]\cong\mathbb Z[t]/(t^m-1),
\qquad N=1+t+\cdots+t^{m-1},
\]
then
\[
\widetilde H^0(G\widetilde x)
\cong \mathbb Z[G]/\mathbb Z N.
\]
Multiplication by \(t-1\) gives an exact sequence
\[
0\longrightarrow\mathbb ZN
\longrightarrow\mathbb Z[G]
\xrightarrow{\ t-1\ }
I_G\longrightarrow0,
\]
where
\[
I_G=\ker(\varepsilon:\mathbb Z[G]\to\mathbb Z)
\]
is the augmentation ideal. Hence
\[
\mathbb Z[G]/\mathbb ZN\cong I_G
\]
as \(\mathbb Z[G]\)-modules.

Consequently
\[
\boxed{\pi_{2n}(X)\cong I_G=(t-1)\mathbb Z[G]}
\]
as a module over \(\mathbb Z[\pi_1(X)]\cong\mathbb Z[G]\).
:::
