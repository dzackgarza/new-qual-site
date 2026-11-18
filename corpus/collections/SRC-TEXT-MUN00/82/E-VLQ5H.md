---
schema: qual/card@1
id: E-VLQ5H
kind: problem
title: The uncountable fundamental group of the infinite earring
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §82 Supplementary Exercise 5, printed p. 500. Searched outside the checkout for issue #146; the
    record is tmp/sources/mse-searches-146.md and the saved threads are tmp/sources/mse-3925195-E-VLQ5H.md and
    tmp/sources/mse-4917558-E-VLQ5H.md, both read whole. The uncountability is proved by Paul Frost: answer
    3928674 (2020-11-30) constructs the loop with a prescribed sequence of winding numbers, shows it is
    continuous because every neighbourhood of the base point contains almost all the circles, and recovers
    the n-th winding number from the retraction r_n, so that Z^N embeds in pi_1; answer 4917615 (2024-05-16)
    supplies the continuity at the base point and the homotopy (r_n o gamma) = gamma_n that the first leaves
    implicit. That argument is now stated on the card with both URLs; the card's own proof is the same
    injection with the printed hint's zeros and ones in place of the winding numbers. What neither answer
    addresses is the exercise's other assertion, that the earring is compact, Hausdorff and second countable,
    which the card proves. Rejected in the search: mse 667035, on the structure of the group.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 82 Supplementary Exercise 5, printed p. 500. The infinite earring is compact Hausdorff and second countable, and its fundamental group is uncountable, by the retractions onto the circles and an uncountable family of loops. Checked against Example 1 of Section 80 and Corollary 58.6. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. The previous note cited "Corollary 58.6", a statement about the fundamental group of a wedge used nowhere here; the citation is withdrawn and replaced by the ones used. Citations added: Example 1 of §80 (printed p. 487) for the earring and the retractions onto its circles, Theorem 27.3 (printed p. 173) for closed and bounded implying compact in the plane, Theorem 31.2 (printed p. 196) for a subspace of a Hausdorff space being Hausdorff, Theorem 30.2 (printed p. 191) for a subspace of a second-countable space being second countable, Theorem 54.5 (printed p. 345) for the fundamental group of a circle, and Theorem 18.3 (printed p. 108) for continuity of a map glued from two closed pieces. Corrected: continuity of the loop $f_a$ was attributed to the diameters of the circles tending to 0 alone, which is a statement about the values near $t=1$ only; the proof now also covers the junction points $t=1-2^{-k}$, where the two adjacent arcs meet at $p$, by the pasting lemma. Corrected: closedness of the earring in the plane was argued as "the only possible accumulation point of the family is $p$", which does not exhibit a neighbourhood of an arbitrary point outside $X$; the proof now does, separating $y\notin X$, $y\ne p$, from all but finitely many circles by radius and from the rest by closedness. What the certificate does not cover: the uncountability of $\{0,1\}^{\NN}$ is taken as known.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. Pages verified: Example 1 of §80 on printed p. 487,
    which defines the circles and also the retraction r_n, so the card's attribution of the
    retraction to that example is right; Theorem 27.3 on printed p. 173; Theorem 31.2(a) on
    printed p. 196; Theorem 30.2 on printed p. 191; Theorem 54.5 on printed p. 345; Theorem
    18.3 on printed p. 108; and Theorem 7.8 on printed p. 50, which now replaces the earlier
    note's "the uncountability of {0,1}^N is taken as known". Written out that the prose left
    implicit: the continuity of r_n at each of the three kinds of point, in particular on C_n
    where it is the identity, and r_n(U) contained in U at p; the well-definedness of f_a at
    the junction points, both prescriptions giving p; and the closedness argument's
    separation of a point y outside X from all but finitely many circles by radius and from
    the rest by closedness. The union of the intervals I_n is [0,1] and consecutive ones meet
    only at the junctions, which is what lets the pasting lemma apply. No repair to the
    statement.
---

::: {.exercise}

Let $X$ be the infinite earring (see Example 1 of §80). Show that $X$ is a compact Hausdorff space with a countable basis whose fundamental group is uncountable.
[Hint: Let $r_n: X \to C_n$ be a retraction. Given a sequence $a_1, a_2, \ldots$ of zeros and ones, show there exists a loop $f$ in $X$ such that, for each $n$, the element $(r_n)_*[f]$ is trivial if and only if $a_n = 0$.]

:::

::: {.solution}
The injection argument is Paul Frost's, in his answer 3928674 (https://math.stackexchange.com/a/3928674, 2020-11-30) to question 3925195, "Fundamental group of Hawaiian earring is uncountable" (https://math.stackexchange.com/questions/3925195), and in his answer 4917615 (https://math.stackexchange.com/a/4917615, 2024-05-16) to question 4917558, which supplies the continuity check the first leaves to the reader; he writes the loop with prescribed winding numbers, and recovers the $n$-th one from the retraction $r_n$, so that $\ZZ^{\NN}$ embeds in $\pi_1$. The card's proof is that injection with the zeros and ones of the printed hint in place of the winding numbers, and it also proves the first half of the exercise, that $X$ is compact Hausdorff with a countable basis, which neither answer addresses.

Throughout, $X=\bigcup_{n\ge1}C_n$ is the infinite earring of Example 1 of §80 (printed p. 487): $C_n$ is the circle of radius $1/n$ with centre $(1/n,0)$, so that every $C_n$ passes through the origin $p$ --- the book's $b_0$ --- and $C_n$ has diameter $2/n$. The exercise is §82 Supplementary Exercise 5 (printed p. 500).

::: pf

::: {.pf-step #compact}
$X$ is a compact Hausdorff space with a countable basis.

::: pf-proof

::: {.pf-step #closed}
$X$ is closed and bounded in $\RR^2$.

::: pf-proof
$X$ lies in the disk of radius $2$ about $p$, so it is bounded. For closedness let $y\in\RR^2-X$; if $y=p$ there is nothing to prove, so let $d=\abs{y-p}>0$. Every circle with $2/n<d/2$ lies in the disk of radius $d/2$ about $p$, which is disjoint from the ball of radius $d/2$ about $y$; the finitely many remaining circles are closed and do not contain $y$, so their union is closed and misses $y$, and a ball about $y$ small enough to avoid that union and the disk of radius $d/2$ about $p$ meets no $C_n$. Hence $\RR^2-X$ is open and $X$ is closed.
:::

:::

::: {.pf-step #compact-hausdorff}
$X$ is compact, Hausdorff and second countable.

::: pf-proof
A closed and bounded subspace of $\RR^2$ is compact (Theorem 27.3, printed p. 173). As a subspace of the Hausdorff space $\RR^2$ it is Hausdorff (Theorem 31.2(a), printed p. 196), and as a subspace of the second-countable space $\RR^2$ it is second countable (Theorem 30.2, printed p. 191).
:::

:::

:::

:::

::: {.pf-step #retraction}
For each $n$ the map $r_n:X\to C_n$ that is the identity on $C_n$ and sends every other circle to $p$ is a continuous retraction.

::: pf-proof
It is a retraction by construction, and Example 1 of §80 (printed p. 487) introduces it. For continuity: at a point of $C_n$ other than $p$ it agrees with the identity on $C_n$, which is continuous; at a point $x\in C_i$ with $i\ne n$ and $x\ne p$, a neighbourhood of $x$ in $X$ can be taken inside $C_i$ and away from $C_n$, and there $r_n$ is constant with value $p$; at $p$, a neighbourhood $U$ of $p$ in $X$ satisfies $r_n(U)\subset U\cup\{p\}=U$, because points of $U\cap C_n$ map to themselves and all other points of $U$ map to $p$. So $r_n$ is continuous.
:::

:::

::: {.pf-step #loop}
For each $a=(a_1,a_2,\ldots)\in\{0,1\}^{\NN}$ the map $f_a$ defined below is a continuous loop in $X$ based at $p$.

::: pf-proof
Let $I_n=[1-2^{-(n-1)},1-2^{-n}]$ for $n\ge1$, closed intervals whose union is $[0,1]$ and which meet only in the points $1-2^{-k}$, and on $I_n$ let $f_a$ traverse $C_n$ once from $p$ back to $p$ if $a_n=1$ and let $f_a$ be constant at $p$ if $a_n=0$; set $f_a(1)=p$. This is well defined, since on $I_n\cap I_{n+1}=\{1-2^{-n}\}$ both prescriptions give $p$. It is continuous: on the interior of each $I_n$ it is a path in the closed set $C_n$, hence continuous; at a junction point $1-2^{-k}$ the restrictions to the two closed intervals $I_k$ and $I_{k+1}$ are continuous and agree there, so the pasting lemma (Theorem 18.3, printed p. 108) applies to their union; and at $t=1$, where $f_a(1)=p$, every value of $f_a$ on $I_n$ lies in $C_n$, of diameter $2/n$, so $f_a(t)\to p$ as $t\to1$. Hence $f_a$ is continuous with $f_a(0)=f_a(1)=p$, a loop based at $p$.
:::

:::

::: {.pf-step #winding}
For every $n$, $(r_n)_*[f_a]$ is trivial if $a_n=0$ and is the generator of $\pi_1(C_n,p)\cong\ZZ$ if $a_n=1$.

::: pf-proof
The composite $r_n\circ f_a$ is constant at $p$ on each $I_i$ with $i\ne n$, because $f_a$ takes values in $C_i$ there and $r_n$ collapses $C_i$ to $p$, and on $I_n$ it is the loop that traverses $C_n$ once, or is constant when $a_n=0$. So $[r_n\circ f_a]$ is respectively the class of a generator or the trivial class in $\pi_1(C_n,p)$, which is isomorphic to $\ZZ$ (Theorem 54.5, printed p. 345). Since $(r_n)_*[f_a]=[r_n\circ f_a]$, the claim follows.
:::

:::

::: {.pf-step}
$\pi_1(X,p)$ is uncountable.

::: pf-proof
Let $a\ne b$ in $\{0,1\}^{\NN}$ and choose $n$ with $a_n\ne b_n$. By step [](#winding){.pf-ref} the classes $(r_n)_*[f_a]$ and $(r_n)_*[f_b]$ differ, one being trivial and the other the generator; if $[f_a]=[f_b]$ in $\pi_1(X,p)$, applying the homomorphism $(r_n)_*$ would give equal images. Hence $[f_a]\ne[f_b]$, and $a\mapsto[f_a]$ is an injection of $\{0,1\}^{\NN}$ into $\pi_1(X,p)$. The set of binary sequences is in bijection with the power set of $\NN$, which is uncountable (Theorem 7.8, printed p. 50), so $\pi_1(X,p)$ is uncountable. Together with step [](#compact){.pf-ref} this proves the exercise.
:::

:::

:::
:::
