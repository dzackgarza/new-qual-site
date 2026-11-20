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

- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose; no statement changed and no citation
    changed. Re-checked in the proof: sigma-compactness of R and the choice of a point outside each
    pi_n(K_n); that the cubes K_m exhaust R^infty; that the affine map sends 0 to (-m,...,-m) and 1
    to (m,...,m), so onto [-m,m]^m; that [m-1,m] for m >= 1 is a locally finite closed cover of
    [0,infinity), so the pasted map is continuous by Exercise 18.9(c) and onto the union of the
    K_m; that distinct points of {0,1}^omega have uniform distance exactly 1, so the radius-1/3
    balls are pairwise disjoint and box-open, and that a separable space has no uncountable family
    of pairwise disjoint nonempty open sets. Added where the card asserted it in a clause: the
    continuity of each piece q_m into R^infty carrying the box topology follows because q_m has
    only finitely many nonzero coordinates, so the preimage of a box-open set is a finite
    intersection of open sets together with all of I or the empty set. What was not re-read: the
    search record for published solutions, which the audit events above carry.
---

::: {.exercise}

(a) If $\RR^\omega$ is given the product topology, show there is no continuous surjective map $f: \RR \to \RR^\omega$.
[Hint: Show that $\RR^\omega$ is not a countable union of compact subspaces.]

(b) If $\RR^\omega$ is given the product topology, determine whether or not there is a continuous surjective map of $\RR$ onto the subspace $\RR^\infty$.

(c) What happens to the statements in (a) and (b) if $\RR^\omega$ is given the uniform topology or the box topology?
:::

::: {.solution}
Part (a) is the argument of Math StackExchange 74766's answer 74779 (2011), recorded in the audit above, and it is the exercise's own hint; parts (b) and (c) have no published treatment that was located and are the card's own, as the audit records. The book's numbering is §44 Exercise 3.

::: pf

::: {.pf-step #sigmacompact}
$\RR$ is $\sigma$-compact, so every continuous image of $\RR$ is a countable union of compact subspaces.

::: pf-proof
$\RR=\bigcup_{n\geq1}[-n,n]$, a countable union of compact subspaces. If $g\colon\RR\to Y$ is continuous then $Y=\bigcup_{n\geq1}g([-n,n])$, and each $g([-n,n])$ is compact as the continuous image of a compact space (Theorem 26.5).
:::
:::

::: {.pf-step #notsigmacompact}
$\RR^{\omega}$ with the product topology is not a countable union of compact subspaces.

::: pf-proof
Suppose $\RR^{\omega}=\bigcup_{n\geq1}K_{n}$ with each $K_{n}$ compact. The coordinate projection $\pi_{n}(K_{n})$ is compact as the continuous image of a compact space, hence closed and bounded in $\RR$ (Theorem 27.3), so there is $x_{n}\in\RR-\pi_{n}(K_{n})$. For the point $x=(x_{1},x_{2},\ldots)$ one has $\pi_{n}(x)=x_{n}\notin\pi_{n}(K_{n})$, so $x\notin K_{n}$ for every $n$, contradicting $\RR^{\omega}=\bigcup_{n}K_{n}$.
:::
:::

::: {.pf-step #parta}
There is no continuous surjection $f\colon\RR\to\RR^{\omega}$ in the product topology.

::: pf-proof
Such a surjection would make $\RR^{\omega}=f(\RR)$ a countable union of compact subspaces by step [](#sigmacompact){.pf-ref}, contradicting step [](#notsigmacompact){.pf-ref}.
:::
:::

::: {.pf-step #cube}
For each $m\geq1$ there is a continuous surjection $q_{m}\colon I\to K_{m}=[-m,m]^{m}\times\{(0,0,\ldots)\}$ with $q_{m}(0)=q_{m}(1)=\mathbf{0}$.

::: pf-proof
By [[E-SADP0]] there is a continuous surjection $h_{m}\colon I\to I^{m}$. The map $x\mapsto(2mx_{i}-m)_{i}$ carries $I^{m}$ homeomorphically onto $[-m,m]^{m}$, sending $(0,\ldots,0)$ to $(-m,\ldots,-m)$ and $(1,\ldots,1)$ to $(m,\ldots,m)$; the inclusion $y\mapsto(y,0,0,\ldots)$ of $[-m,m]^{m}$ into $\RR^{\omega}$ is continuous, each of its coordinate functions being a coordinate of $y$ or the constant $0$. So the composite $q_{m}\colon I\to K_{m}$ is a continuous surjection. Reparametrize it: use the first third of $I$ for a straight path from $\mathbf{0}$ to $q_{m}(0)$, the middle third for $q_{m}$ composed with the affine map of $[1/3,2/3]$ onto $I$, and the last third for a straight path from $q_{m}(1)$ to $\mathbf{0}$; the three pieces agree at the two junction points, and the pasting lemma (Theorem 18.3) makes the result continuous. The added paths end at $\mathbf{0}$, so the reparametrized map is still onto $K_{m}$ and it begins and ends at $\mathbf{0}$.
:::
:::

::: {.pf-step #paste}
There is a continuous surjection $F\colon[0,\infty)\to\RR^{\infty}$.

::: pf-proof
The cubes $K_{m}$ exhaust $\RR^{\infty}$: a point of $\RR^{\infty}$ has all but finitely many coordinates $0$, and if $m\geq1$ bounds their absolute values and exceeds its last nonzero index, the point lies in $K_{m}$. Let $F$ restrict to $q_{m}$ on $[m-1,m]$, with $q_{m}$ as in step [](#cube){.pf-ref}. Adjacent pieces agree at $\mathbf{0}$, and $\theset{[m-1,m]\mid m\geq1}$ is a locally finite closed cover of $[0,\infty)$, so $F$ is continuous by Exercise 18.9(c), and it is onto $\bigcup_{m}K_{m}=\RR^{\infty}$.
:::
:::

::: {.pf-step #partb}
There is a continuous surjection $\RR\to\RR^{\infty}$ in the product topology.

::: pf-proof
Compose the surjection $F$ of step [](#paste){.pf-ref} with $t\mapsto\abs{t}$, which is continuous and onto $[0,\infty)$.
:::
:::

::: {.pf-step #nonseparable}
$\RR^{\omega}$ with the uniform topology, and hence also with the box topology, is not separable.

::: pf-proof
The set $D=\theset{0,1}^{\omega}$ is uncountable, and distinct points of $D$ differ in some coordinate, so their uniform distance is $1$. Hence the balls $B_{\bar\rho}(d,1/3)$ for $d\in D$ are pairwise disjoint and nonempty, and they are open in the uniform topology. That topology is coarser than the box topology, so these sets are box-open as well. A separable space has a countable dense subset and hence, being metrizable here, a countable basis; in a space with a countable basis every family of pairwise disjoint nonempty open sets is countable, since each member contains a basis element and distinct members contain distinct ones. So neither the uniform nor the box topology on $\RR^{\omega}$ is separable.
:::
:::

::: {.pf-step #partc1}
There is no continuous surjection $\RR\to\RR^{\omega}$ in the uniform topology or in the box topology.

::: pf-proof
$\RR$ is separable, since $\QQ$ is countable and dense, and a continuous image of a separable space is separable: the images of a countable dense set are dense in the image. A continuous surjection onto $\RR^{\omega}$ would therefore make it separable, contradicting step [](#nonseparable){.pf-ref}.
:::
:::

::: {.pf-step #partc2}
There is a continuous surjection $\RR\to\RR^{\infty}$ in the uniform topology and in the box topology.

::: pf-proof
The construction of steps [](#cube){.pf-ref} and [](#paste){.pf-ref} is available in both finer topologies on the subspace $\RR^{\infty}$. Each $q_{m}$ takes values in $K_{m}$, whose points have coordinate $0$ beyond the $m$-th, so for a box-open $U=\RR^{\infty}\cap\prod_{i}U_{i}$ the preimage $q_{m}^{-1}(U)$ is the intersection of the open sets $\theset{x\in I\mid(q_{m}(x))_{i}\in U_{i}}$ over the finitely many $i\leq m$, together with all of $I$ if $0\in U_{i}$ for every $i>m$ and with the empty set otherwise; so it is open, and $q_{m}$ is continuous into $\RR^{\infty}$ with the box topology, hence also with the uniform topology, which the box topology refines. The cover $\theset{[m-1,m]}$ is locally finite, closed, and its pieces agree at $\mathbf{0}$, so the pasted map is continuous and onto. Composing with $t\mapsto\abs{t}$ gives the surjection from $\RR$.
:::
:::
:::

:::
