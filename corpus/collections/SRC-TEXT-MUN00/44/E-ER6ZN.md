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
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Math StackExchange 74766, "Is [0,1]^\omega a
    continuous image of [0,1]?" (2011-10-22), carries the proof of part (a) that the card states:
    answer 74779 by user17182 writes R as the union of the intervals [-n,n], so that a continuous
    surjection would write R^\omega as a union of compact subspaces f([-n,n]), and that is
    impossible because the projection pi_n of the n-th compact piece is a bounded subset of R and
    a point can be chosen outside each of them. The card's part (a) is this argument, and it is
    now recorded as its source; parts (b) and (c) have no published treatment on that page or in
    the other searches listed in the COMPLAINTS.md entry for §43--§50, and remain the card's own.
    The exercise number is corrected here: this is §44 Exercise 3 in the book's numbering, not
    Exercise 2 as the note above has it, Exercise 2 being the map R -> R^n. The printed page,
    275, is right. Nothing else on the card was changed, and its parts (b) and (c) were not
    re-read in this pass.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Part (b) took the map onto the cube [-m,m]^m from the card of §44 Exercise 1, which gives a
    continuous surjection of I onto I^m only; the step now writes the affine homeomorphism of I^m
    onto [-m,m]^m, the coordinate x going to 2mx - m, the inclusion of [-m,m]^m in R^omega, whose
    coordinate functions are coordinates of the point or the constant 0, and the composite of the
    three. The 2026-11-15 note above also says it corrects the exercise number from 2 to 3; it
    corrects nothing, since the note of 2026-11-11 already numbers this as Exercise 3, printed
    p. 275, and its "§44 Exercise 2" is the card of the map from R onto R^n, cited there as the
    earlier source of the reparametrization.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    The affine map named in the 2026-11-15 note above was written x |-> 2mx - 1, which is not the map
    the card uses and not a homeomorphism onto [-m,m]^m: it sends 0 to -1 and 1 to 2m - 1, so its
    image is [-1, 2m-1]. A reader of this card reported it. The body of the solution has
    x |-> (2m x_i - m)_i, which sends 0 to (-m,...,-m) and 1 to (m,...,m), and therefore maps I^m
    onto [-m,m]^m; the note now gives 2mx - m. Nothing in the proof changed, and the rest of the card
    was not re-read in this pass.

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
The $K_m$'s exhaust $\RR^\infty$. By [[E-SADP0]] there is, for each $m$, a continuous surjection $h_m:I\to I^m$. The affine map $x\mapsto(2mx_i-m)_i$ carries $I^m$ homeomorphically onto $[-m,m]^m$, and the inclusion $y\mapsto(y,0,0,\dots)$ of $[-m,m]^m$ into $\RR^\omega$ is continuous, each of its coordinate functions being a coordinate of $y$ or the constant $0$; so $q_m:I\to K_m$, the composite of $h_m$ with these two maps, is a continuous surjection onto $K_m$. Reparametrize $q_m$ so that it starts and ends at the origin, using the first third of $I$ for a straight path from $0$ to $q_m(0)$, the middle third for $q_m$, and the last third for a straight path from $q_m(1)$ back to $0$. The result, still written $q_m:I\to K_m$, is a continuous surjection with $q_m(0)=q_m(1)=0$. Map the interval $[m-1,m]$ onto $K_m$ via $q_m$. Adjacent pieces agree at the origin, and the cover of $[0,\infty)$ by the intervals $[m-1,m]$ is a locally finite closed cover, so the pasted map $F:[0,\infty)\to\RR^\infty$ is continuous (Exercise 18.9(c)) and surjective; compose with $t\mapsto\abs{t}$ to obtain a continuous surjection from $\RR$.

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
