---
schema: qual/card@1
id: E-HAT-4.3-1
kind: problem
title: "Map $\\mathbb{RP}^\\infty \\to K(\\mathbb{Z},2)$ trivial on homology"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show there is a map $\mathbb{RP}^\infty \to \mathbb{CP}^\infty = K(\mathbb{Z}, 2)$ which induces the trivial map on $\tilde{H}_*(-; \mathbb{Z})$ but a nontrivial map on $\tilde{H}^*(-; \mathbb{Z})$.
How is this consistent with the universal coefficient theorem?
:::

::: {.solution}
Let
\[
u\in H^2(\mathbb{RP}^\infty;\mathbb Z)\cong\mathbb Z/2
\]
be the nonzero class. Since
\[
\mathbb{CP}^\infty=K(\mathbb Z,2),
\]
representability gives a map
\[
f:\mathbb{RP}^\infty\to\mathbb{CP}^\infty
\]
such that, for the canonical generator \(c\in H^2(\mathbb{CP}^\infty;\mathbb Z)\),
\[
f^*(c)=u\ne0.
\]
Thus \(f^*\) is nontrivial on reduced integral cohomology.

On the other hand
\[
\widetilde H_i(\mathbb{RP}^\infty;\mathbb Z)
\cong
\begin{cases}
\mathbb Z/2,&i\text{ odd},\\
0,&i\text{ even},
\end{cases}
\]
while \(H_*(\mathbb{CP}^\infty;\mathbb Z)\) is free abelian and concentrated in even degrees. Hence every reduced homology homomorphism induced by \(f\) is zero.

There is no contradiction with the universal coefficient theorem. In degree \(2\),
\[
H^2(\mathbb{RP}^\infty;\mathbb Z)
\cong
\operatorname{Ext}(H_1(\mathbb{RP}^\infty),\mathbb Z)
\cong\mathbb Z/2,
\]
whereas the generator of \(H^2(\mathbb{CP}^\infty)\) comes from
\[
\operatorname{Hom}(H_2(\mathbb{CP}^\infty),\mathbb Z).
\]
Naturality of the UCT exact sequence allows its pullback to land in the Ext term; the UCT splitting is not natural. Thus
\[
\boxed{f_*|_{\widetilde H_*}=0\text{ while }f^*|_{\widetilde H^*}\ne0.}
\]
:::
