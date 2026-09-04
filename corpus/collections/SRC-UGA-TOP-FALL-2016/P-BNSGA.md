---
schema: qual/card@1
id: P-BNSGA
kind: problem
title: $\pi_1$ and the universal cover of the unit sphere union a diameter
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked against problem 5 of the official UGA Fall 2016 topology exam; corrected the card's introduced final-letter typo from "the universal cover of X" to "the universal cover of A".
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the quotient homotopy type, the infinite-chain covering locally at both attachment points, and simple connectivity of the total space.
---

::: problem
Let $A$ be the union of the unit sphere in $\RR^3$ and the interval $\theset {(t, 0, 0) : -1 \leq t \leq 1} \subset \RR^3$.

Compute $\pi_1 (A)$ and give an explicit description of the universal cover of $A$.
:::

::: {.solution}
Let
\[
p=(-1,0,0),
\qquad
q=(1,0,0),
\]
and let $I$ be the diameter joining $p$ to $q$.
Thus
\[
A=S^2\cup I,
\qquad
S^2\cap I=\{p,q\}.
\]

<1>1. The space $A$ is homotopy equivalent to $S^2\vee S^1$.
::: {.proof}
Give $A$ a CW structure in which the diameter $I$ is a contractible subcomplex.
Collapsing a contractible CW subcomplex to a point is a homotopy equivalence, so
\[
A\simeq A/I.
\]
The quotient $A/I$ is the sphere with the two points $p$ and $q$ identified.
This space is homotopy equivalent to
\[
S^2\vee S^1.
\]
Equivalently, choose an arc in the sphere from $p$ to $q$; together with the identified point it supplies the circle factor, while the remaining sphere supplies the $S^2$ factor.
:::

<1>2. Therefore
\[
\boxed{\pi_1(A)\cong\ZZ.}
\]
::: {.proof}
By <1>1 and homotopy invariance of the fundamental group,
\[
\pi_1(A)
\cong
\pi_1(S^2\vee S^1).
\]
Van Kampen's theorem gives
\[
\pi_1(S^2\vee S^1)
\cong
\pi_1(S^2)*\pi_1(S^1)
\cong
0*\ZZ
\cong
\ZZ.
\]
A generator may be represented by traversing the diameter from $p$ to $q$ and then returning from $q$ to $p$ along any path on the sphere.
:::

<1>3. Construct a space $\widetilde A$ from copies
\[
S_m^2\cong S^2,
\qquad m\in\ZZ,
\]
and intervals
\[
I_m\cong[0,1],
\qquad m\in\ZZ,
\]
as follows.
Choose points $p_m,q_m\in S_m^2$ corresponding to $p,q$ and attach
\[
I_m(0)=p_m,
\qquad
I_m(1)=q_{m+1}.
\]
Thus $\widetilde A$ is a bi-infinite chain of spheres joined by intervals.
::: {.proof}
Schematically the space is
\[
\cdots
S_{-1}^2
\mathbin{-}I_{-1}\mathbin{-}
S_0^2
\mathbin{-}I_0\mathbin{-}
S_1^2
\mathbin{-}I_1\mathbin{-}
S_2^2
\cdots,
\]
where the right end of $I_m$ is attached to $q_{m+1}$ and its left end to $p_m$.
This is a connected CW complex.
:::

<1>4. There is a covering map
\[
\pi:\widetilde A\longrightarrow A
\]
that maps every $S_m^2$ homeomorphically onto $S^2$ and every $I_m$ homeomorphically onto the diameter $I$, taking its initial endpoint to $p$ and terminal endpoint to $q$.
::: {.proof}
On the interiors of the spheres and intervals this is plainly a local homeomorphism with one copy for each $m\in\ZZ$.

Near $p$, choose a small neighborhood in $A$ consisting of a disk neighborhood of $p$ in $S^2$ together with a short initial segment of $I$.
Its inverse image is the disjoint union of the corresponding neighborhoods of the points $p_m$, each using the initial segment of $I_m$.
Each maps homeomorphically onto the chosen neighborhood of $p$.

Near $q$, the analogous lifted neighborhood at $q_m$ uses the terminal segment of $I_{m-1}$.
Again the inverse image is a disjoint union of copies mapped homeomorphically onto the base neighborhood.
Thus every point of $A$ has an evenly covered neighborhood, so $\pi$ is a covering map.
:::

<1>5. The space $\widetilde A$ is simply connected.
::: {.proof}
The incidence graph whose vertices are the spheres $S_m^2$ and whose edges are the intervals $I_m$ is the bi-infinite line, hence a tree.
Each sphere and each interval is simply connected, and the attachments occur at single points.
Van Kampen's theorem therefore shows that every finite subchain is simply connected.

The CW complex $\widetilde A$ is locally finite, so the compact image of any loop meets only finitely many cells and is contained in a finite subchain.
That finite subchain is simply connected, hence the loop is nullhomotopic.
Therefore
\[
\pi_1(\widetilde A)=0.
\]
:::

<1>6. Hence the covering in <1>4 is the universal cover of $A$.
::: {.proof}
By <1>3 the total space is connected, and by <1>5 it is simply connected.
Thus
\[
\boxed{\widetilde A\to A}
\]
is the universal covering space.
The deck transformation corresponding to the generator of $\pi_1(A)\cong\ZZ$ shifts every index by one:
\[
S_m^2\longmapsto S_{m+1}^2,
\qquad
I_m\longmapsto I_{m+1}.
\]
:::
:::
