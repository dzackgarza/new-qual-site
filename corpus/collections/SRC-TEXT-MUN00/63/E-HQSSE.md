---
schema: qual/card@1
id: E-HQSSE
kind: problem
title: Two disjoint curves on the sphere make three regions
classification:
  areas:
  - topology
  topics:
  - Jordan Curve Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Let $C_1$ and $C_2$ be disjoint simple closed curves in $S^2$.

(a) Show that $S^2 - C_1 - C_2$ has precisely three components.
[Hint: If $W_1$ is the component of $S^2 - C_1$ disjoint from $C_2$, and if $W_2$ is the component of $S^2 - C_2$ disjoint from $C_1$, show that $\overline{W}_1 \cup \overline{W}_2$ does not separate $S^2$.]

(b) Show that these three components have boundaries $C_1$ and $C_2$ and $C_1 \cup C_2$, respectively.
:::

::: {.solution}
By the Jordan curve theorem, each \(C_i\) separates \(S^2\) into exactly two components, each having boundary \(C_i\).

Since \(C_2\) is connected and disjoint from \(C_1\), it lies wholly in one component of \(S^2-C_1\). Let \(W_1\) be the other component. Similarly, let \(W_2\) be the component of \(S^2-C_2\) disjoint from \(C_1\). Then \(W_1\) and \(W_2\) are disjoint: if a point lay in both, the connected sets \(C_1\) and \(C_2\) would lie on opposite sides of each other in both Jordan decompositions, which is impossible; equivalently, by the Jordan-Schoenflies theorem the closures \(\overline W_1\) and \(\overline W_2\) are disjoint closed disks.

The set
\[
K=\overline W_1\cup\overline W_2
\]
is the union of two disjoint closed disks. Its complement is an open annulus and is therefore connected. Hence
\[
R=S^2-K
\]
is connected. Moreover
\[
S^2-(C_1\cup C_2)=W_1\ \sqcup\ R\ \sqcup\ W_2.
\]
All three sets are nonempty, open, and connected, so these are precisely the three components. This proves (a).

For (b), the Jordan curve theorem gives
\[
\partial W_1=C_1,\qquad \partial W_2=C_2.
\]
The remaining component \(R\) lies between the two curves. Every point of \(C_1\) is approached from \(W_1\) on one side and from \(R\) on the other, so \(C_1\subset\partial R\); similarly \(C_2\subset\partial R\). Conversely, a boundary point of \(R\) cannot lie in the open set \(S^2-(C_1\cup C_2)\), since there it would belong to one of the three open components. Thus
\[
\partial R\subset C_1\cup C_2.
\]
Therefore
\[
\partial R=C_1\cup C_2.
\]
So the three component boundaries are \(C_1\), \(C_2\), and \(C_1\cup C_2\), respectively.
:::
