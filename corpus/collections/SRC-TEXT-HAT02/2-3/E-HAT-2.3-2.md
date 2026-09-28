---
schema: qual/card@1
id: E-HAT-2.3-2
kind: problem
title: Candidate homology theory $\Pi_i \tilde{H}_i(X)/\oplus_i \tilde{H}_i(X)$ satisfies all axioms except wedge axiom
classification:
  areas:
  - topology
  topics:
  - Homology
  - Axiomatic Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.3, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Define a candidate for a reduced homology theory on CW complexes by $\tilde{h}_n(X) = \Pi_i \tilde{H}_i(X) / \oplus_i \tilde{H}_i(X)$.
Thus $\tilde{h}_n(X)$ is independent of $n$ and is zero if $X$ is finite-dimensional, but is not identically zero, for example for $X = \vee_i S^i$.
Show that the axioms for a homology theory are satisfied except that the wedge axiom fails.
:::

::: {.solution}
Put
\[
Q(X)=\prod_{i\in\mathbb Z}\widetilde H_i(X)\big/\bigoplus_{i\in\mathbb Z}\widetilde H_i(X),
\qquad \widetilde h_n(X)=Q(X).
\]

<1>1. Homotopy invariance holds.
::: {.proof}
A homotopy equivalence induces isomorphisms on every reduced homology group, hence on their product, their direct sum, and therefore on the quotient $Q(X)$.
:::

<1>2. Exactness holds, with all connecting maps induced coordinatewise from ordinary homology.
::: {.proof}
For a cofibration sequence $A\to X\to X/A$, ordinary reduced homology gives a long exact sequence. Reindexing turns the connecting map into a degree-preserving map between the products defining $Q$. Products of exact sequences of abelian groups are exact. Direct sums are exact as well. Applying the snake lemma to
\[
0\to\bigoplus_i\widetilde H_i(-)\to\prod_i\widetilde H_i(-)\to Q(-)\to0
\]
for the three terms of the cofibration sequence gives exactness for $Q$.
:::

<1>3. The dimension axiom holds.
::: {.proof}
For $S^0$ only one reduced homology group is nonzero. Hence product and direct sum coincide, so $Q(S^0)=0$ in every degree.
:::

<1>4. The wedge axiom fails.
::: {.proof}
Let
\[
X=\bigvee_{j\ge1}S^j.
\]
Then $\widetilde H_i(X)\cong\mathbb Z$ for every $i\ge1$, so
\[
Q(X)\cong\prod_{i\ge1}\mathbb Z\big/\bigoplus_{i\ge1}\mathbb Z\ne0.
\]
But each individual sphere $S^j$ is finite-dimensional, hence $Q(S^j)=0$. Therefore
\[
\bigoplus_j\widetilde h_n(S^j)=0
\]
while $\widetilde h_n(\bigvee_jS^j)\ne0$.
:::

Thus the candidate satisfies the reduced homology axioms except the infinite wedge axiom.
:::
