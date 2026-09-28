---
schema: qual/card@1
id: E-HAT-4.2-38
kind: problem
title: "$\\pi_3(S^1 \\vee S^2)$ is not finitely generated"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 38; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show $\pi_3(S^1 \vee S^2)$ is not finitely generated as a module over $\mathbb{Z}[\pi_1(S^1 \vee S^2)]$ by considering Whitehead products in the universal cover, using the results in Example 4.52. Generalize this to $\pi_{i+j-1}(S^1 \vee S^i \vee S^j)$ for $i, j > 1$.
:::

::: {.solution}
Let
\[
X=S^1\vee S^2.
\]
Its universal cover is an infinite line with a copy \(S_k^2\) of \(S^2\) attached at each integer \(k\in\mathbb Z\). Let
\[
\iota_k\in\pi_2(\widetilde X)
\]
be the inclusion of the \(k\)-th sphere. The deck generator \(t\) acts by
\[
t\iota_k=\iota_{k+1}.
\]

Example 4.52 and the Hilton--Milnor calculation show that in
\[
\pi_3(\widetilde X)
\]
the Whitehead products
\[
[\iota_a,\iota_b],\qquad a<b,
\]
form independent infinite-order summands, in addition to the individual \(\pi_3(S_k^2)\)-summands. Translation acts by
\[
t[\iota_a,\iota_b]=[\iota_{a+1},\iota_{b+1}].
\]
Thus the difference
\[
d=b-a>0
\]
is invariant under the \(\mathbb Z[t,t^{-1}]\)-action. For every \(d\ge1\), the class
\[
[\iota_0,\iota_d]
\]
lies in a different module orbit, and these classes are independent. Hence no finite set can generate all of them:
\[
\boxed{\pi_3(S^1\vee S^2)\text{ is not finitely generated over }\mathbb Z[\pi_1].}
\]

More generally, let
\[
Y=S^1\vee S^i\vee S^j,
\qquad i,j>1.
\]
In the universal cover there are copies \(S^i_a\) and \(S^j_b\) at every integer. If \(\alpha_a\) and \(\beta_b\) denote their fundamental homotopy classes, then
\[
[\alpha_a,\beta_b]
\in\pi_{i+j-1}(\widetilde Y)
\]
are independent Hilton--Milnor summands. Deck translation sends
\[
[\alpha_a,\beta_b]\mapsto[\alpha_{a+1},\beta_{b+1}],
\]
so again the difference \(b-a\) labels infinitely many distinct module orbits. Therefore
\[
\boxed{\pi_{i+j-1}(S^1\vee S^i\vee S^j)
\text{ is not finitely generated over }\mathbb Z[\pi_1].}
\]
:::
