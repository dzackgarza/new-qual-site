---
schema: qual/card@1
id: E-ER6ZN
kind: problem
title: Surjections onto R^omega under the product, uniform, and box topologies
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

(a) If $\mathbb{R}^\omega$ is given the product topology, show there is no continuous surjective map $f: \mathbb{R} \to \mathbb{R}^\omega$.
[Hint: Show that $\mathbb{R}^\omega$ is not a countable union of compact subspaces.]

(b) If $\mathbb{R}^\omega$ is given the product topology, determine whether or not there is a continuous surjective map of $\mathbb{R}$ onto the subspace $\mathbb{R}^\infty$.

(c) What happens to the statements in (a) and (b) if $\mathbb{R}^\omega$ is given the uniform topology or the box topology?
:::

::: {.solution}
(a) The real line is \(\sigma\)-compact:
\[
\mathbb R=\bigcup_{n\ge1}[-n,n].
\]
Hence every continuous image of \(\mathbb R\) is a countable union of compact subspaces.

But \(\mathbb R^\omega\) in the product topology is not \(\sigma\)-compact. Indeed, suppose
\[
\mathbb R^\omega=\bigcup_{n\ge1}K_n
\]
with each \(K_n\) compact. The coordinate projection \(\pi_n(K_n)\subset\mathbb R\) is compact, hence bounded. Choose \(x_n\in\mathbb R-\pi_n(K_n)\), and let \(x=(x_1,x_2,\ldots)\). Then \(x\notin K_n\) for every \(n\), contradiction. Therefore no continuous surjection \(\mathbb R\to\mathbb R^\omega\) exists in the product topology.

(b) There is a continuous surjection onto \(\mathbb R^\infty\). Let
\[
K_m=[-m,m]^m\times\{0\}\times\{0\}\times\cdots.
\]
The \(K_m\)'s exhaust \(\mathbb R^\infty\). For each \(m\), choose a continuous surjection \(q_m:I\to K_m\) with \(q_m(0)=q_m(1)=0\), as in Exercise `E-WVVWW`. Map the interval \([m-1,m]\) onto \(K_m\) via \(q_m\). Since adjacent pieces agree at the origin, the pasted map \([0,\infty)\to\mathbb R^\infty\) is continuous and surjective; compose with \(t\mapsto|t|\) to obtain a continuous surjection from \(\mathbb R\).

(c) In both the uniform and box topologies, \(\mathbb R^\omega\) is nonseparable. The subset
\[
D=\{0,1\}^\omega
\]
is uncountable, and distinct points of \(D\) have uniform distance \(1\). Thus the uniform balls of radius \(1/3\) about points of \(D\) are pairwise disjoint. The box topology is finer than the uniform topology, so these balls are also box-open. A separable space cannot contain an uncountable family of pairwise disjoint nonempty open sets. Hence neither version of \(\mathbb R^\omega\) is separable. Since a continuous image of the separable space \(\mathbb R\) is separable, there is no continuous surjection from \(\mathbb R\) onto \(\mathbb R^\omega\) in either topology.

For \(\mathbb R^\infty\), however, the construction in (b) works in both the uniform and box subspace topologies. Each finite-stage inclusion
\[
\mathbb R^m\times\{0\}^{\{i>m\}}\hookrightarrow\mathbb R^\infty
\]
is continuous for both topologies, and the piecewise construction is locally finite on the domain \([0,\infty)\). Thus continuous surjections
\[
\mathbb R\twoheadrightarrow\mathbb R^\infty
\]
exist for the product, uniform, and box topologies.
:::
