---
schema: qual/card@1
id: E-ER6ZN
kind: problem
title: Surjections from $\RR$ onto $\RR^\omega$ and $\RR^\infty$ under the product, uniform, and box topologies
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
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §44 Exercise 3 (printed p. 275) was located; the sets searched are listed in
    the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against the book, with
    Theorem 26.5 (the continuous image of a compact space is compact) and Theorem 21.3 / the definition of
    separability for the countability argument. Part (a) is the exercise's hint: R is sigma-compact as the
    union of the intervals [-n,n], so every continuous image of R is a countable union of compact
    subspaces, while R^omega in the product topology is not, because the n-th coordinate projection of
    the n-th compact set is compact and bounded and one chooses a point outside all of them. Part (b) is
    yes: the cubes [-m,m]^m x {0} x ... exhaust R^infty and each is a continuous image of I, so the
    piecewise pasted map is a continuous surjection. Part (c): R^omega in the uniform and the box
    topologies contains the uncountable subset {0,1}^omega whose points are pairwise at distance 1, so it
    is not separable and admits no continuous surjection from the separable space R; for R^infty the
    construction of (b) is continuous in both finer topologies, because the trace of a basic open set on
    a finite-stage cube restricts only its finitely many nonzero coordinates. What was corrected: part
    (b) cited the card of §44 Exercise 2 for the reparametrization that makes each piece start and end at
    the origin, which this batch's transcription of that card no longer carries; the reparametrization is
    now written out, and the pasting cites Exercise 18.9(c), the locally finite closed cover form of the
    pasting lemma, which the card had invoked without a reference.
---

::: {.exercise}

(a) If $\RR^\omega$ is given the product topology, show there is no continuous surjective map $f: \RR \to \RR^\omega$.
[Hint: Show that $\RR^\omega$ is not a countable union of compact subspaces.]

(b) If $\RR^\omega$ is given the product topology, determine whether or not there is a continuous surjective map of $\RR$ onto the subspace $\RR^\infty$.

(c) What happens to the statements in (a) and (b) if $\RR^\omega$ is given the uniform topology or the box topology?
:::

::: {.solution}
(a) The real line is $\sigma$-compact:
$$
\RR=\bigcup_{n\ge1}[-n,n].
$$
Hence every continuous image of $\RR$ is a countable union of compact subspaces.

But $\RR^\omega$ in the product topology is not $\sigma$-compact. Indeed, suppose
$$
\RR^\omega=\bigcup_{n\ge1}K_n
$$
with each $K_n$ compact. The coordinate projection $\pi_n(K_n)\subset\RR$ is compact, hence bounded. Choose $x_n\in\RR-\pi_n(K_n)$, and let $x=(x_1,x_2,\ldots)$. Then $x\notin K_n$ for every $n$, contradiction. Therefore no continuous surjection $\RR\to\RR^\omega$ exists in the product topology.

(b) There is a continuous surjection onto $\RR^\infty$. Let
$$
K_m=[-m,m]^m\times\{0\}\times\{0\}\times\cdots.
$$
The $K_m$'s exhaust $\RR^\infty$. By [[E-SADP0]] there is, for each $m$, a continuous surjection $q:I\to K_m$; reparametrize it so that it starts and ends at the origin, using the first third of $I$ for a straight path from $0$ to $q(0)$, the middle third for $q$, and the last third for a straight path from $q(1)$ back to $0$. The result, still written $q_m:I\to K_m$, is a continuous surjection with $q_m(0)=q_m(1)=0$. Map the interval $[m-1,m]$ onto $K_m$ via $q_m$. Adjacent pieces agree at the origin, and the cover of $[0,\infty)$ by the intervals $[m-1,m]$ is a locally finite closed cover, so the pasted map $F:[0,\infty)\to\RR^\infty$ is continuous (Exercise 18.9(c)) and surjective; compose with $t\mapsto\abs{t}$ to obtain a continuous surjection from $\RR$.

(c) In both the uniform and box topologies, $\RR^\omega$ is nonseparable. The subset
$$
D=\{0,1\}^\omega
$$
is uncountable, and distinct points of $D$ have uniform distance $1$. Thus the uniform balls of radius $1/3$ about points of $D$ are pairwise disjoint. The box topology is finer than the uniform topology, so these balls are also box-open. A separable space cannot contain an uncountable family of pairwise disjoint nonempty open sets. Hence neither version of $\RR^\omega$ is separable. Since a continuous image of the separable space $\RR$ is separable, there is no continuous surjection from $\RR$ onto $\RR^\omega$ in either topology.

For $\RR^\infty$, however, the construction in (b) works in both the uniform and box subspace topologies. Each finite-stage inclusion
$$
\RR^m\times\{0\}^{\{i>m\}}\hookrightarrow\RR^\infty
$$
is continuous for both topologies, and the piecewise construction is locally finite on the domain $[0,\infty)$. Thus continuous surjections
$$
\RR\twoheadrightarrow\RR^\infty
$$
exist for the product, uniform, and box topologies.
:::
