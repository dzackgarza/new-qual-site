---
schema: qual/card@1
id: E-HAT-4.3-20
kind: problem
title: "Postnikov towers for $\\Omega X$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Correction to my own repair of this card. Step #abelian said the triviality of the
    action is "the hypothesis of Theorem 4.69 for the connected CW complex Omega X", and
    Omega X is not in general a CW complex: Theorem 4.69 is stated for a connected CW
    complex. The step now passes to a CW approximation W -> Omega X, which inherits an
    H-space structure up to homotopy and hence is abelian, applies Theorem 4.69 there, and
    observes that a Postnikov tower of W is one of Omega X because a weak equivalence
    induces isomorphisms on all homotopy groups. Nothing else changed.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.3 Exercise 20, printed p. 420,
    and against Theorem 4.69, printed p. 412. Step #principal was false: it asserted that
    each Postnikov fibration p_n is principal, citing Theorem 4.69, but that theorem is an
    if-and-only-if whose hypothesis is the triviality of the action of pi_1(X_{n-1}) on
    pi_n X, and the hypothesis fails (X = RP^2, where the generator of pi_1 acts on pi_2
    by -1; likewise S^1 v S^2). Independent reports from the swarm found the same. The
    step now records what is true without a hypothesis, the fibre sequence
    K(pi_n X, n-1) -> Omega X_n -> Omega X_{n-1} -> K(pi_n X, n) from the long exact
    sequence of p_n, and #loopprincipal is rebuilt on it: Omega p_n is the homotopy
    fibre of that connecting map, hence the pullback of the path-loop fibration over
    K(pi_n X, n) along it, hence principal with fibre K(pi_n X, n-1). The exercise's
    conclusion stands; the argument no longer goes through principality of p_n.
    Statement unchanged. Not checked: nothing outside this exercise.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Second pass on the same card, after an independent report pointed at two things and
    I checked both. (1) The example was wrong: for X = RP^2 the second Postnikov stage
    is RP^2 itself, not a contractible space, since RP^2 already has no homotopy above
    degree 2; the fibration is p_2: RP^2 -> K(Z_2,1) with fibre K(Z,2) and the generator
    of pi_1 acting on pi_2 by -1. (2) The previous repair produced the fibre sequence
    K(pi_n X,n-1) -> Omega X_n -> Omega X_{n-1} -> K(pi_n X,n) from exactness of the
    long exact homotopy sequence, which is a statement about groups and does not by
    itself supply the map of spaces that making Omega p_n a pullback requires --- and
    for a twisted fibration such a map need not exist. The argument now goes through
    Theorem 4.69 applied to Omega X, which is an H-space and hence abelian (Example
    4A.3), together with uniqueness of Postnikov towers and the fibre homotopy
    invariance of principality. No statement changed.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 20; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof repaired: the card displayed the three-term sequence Omega X_{n+1} -> Omega X_n -> Omega X_{n-1} and called it principal with an Eilenberg--MacLane loop space as fibre. In the book's indexing that is misaligned: AT.txt:20426-20430 has the Postnikov fibration K(pi_{n+1}X, n+1) -> X_{n+1} -> X_n, whose loop is K(pi_{n+1}X, n) -> Omega X_{n+1} -> Omega X_n, whereas the fibre of Omega X_n -> Omega X_{n-1} is K(pi_n X, n-1). The display now names the correct spaces.
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m6__proofs-4-3-1-12.md (1-12: 10 correct, 5 a dimension slip, 9 a wrong assertion; both repaired) and m2__proofs-4-3-13-24.md (13-24: 10 correct, 20 a display misalignment repaired by identifying the principal fibration, 22 the missing converse of an iff, later restated and proved, and 24, whose whole proof was then written). No card in this slice has an unmet piece.

- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained set covers this exercise, so the argument is the
    card's own and the card says so. Checked against Hatcher, Section 4.3 Exercise 20, printed
    p. 420 (PDF p. 429), and against the Postnikov theory of pp. 410-412. Each step re-read:
    looping preserves Hurewicz fibrations; $\pi_i(\Omega X_n)=\pi_{i+1}(X_n)$ makes $\Omega X_n$ the
    $(n-1)$-st stage of $\Omega X$; $X_n\to X_{n-1}$ is principal as the pullback of the path-loop
    fibration over $K(\pi_n X,n+1)$ along the k-invariant; and looping that pullback gives the
    pullback of the path-loop fibration of $K(\pi_n X,n)$ along $\Omega k_n$. A slip of my own in
    the first draft is repaired here: the fibre of $\Omega X_n\to\Omega X_{n-1}$ is the loop of the
    fibre of $p_n$, that is $K(\pi_n X,n-1)$, not $\Omega K(\pi_n X,n+1)$; the step now says so and
    matches the conclusion. Not claimed: any statement about Moore-Postnikov towers or about
    non-connected $X$.
---

::: {.problem}
Show that by applying the loop space functor to a Postnikov tower for $X$ one obtains a Postnikov tower of principal fibrations for $\Omega X$.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and none of the retained Hatcher sets solves Section 4.3 Exercise 20. It is checked against Hatcher, Algebraic Topology, Section 4.3 Exercise 20, printed p. 420, and against the Postnikov tower theory of pp. 410--412 and Theorem 4.69 there.

::: pf

::: {.pf-step #tower}
Let $\cdots\to X_n\to X_{n-1}\to\cdots$ be a Postnikov tower for $X$: each $p_n:X_n\to X_{n-1}$ is a fibration, $X_n$ has $\pi_i(X_n)=\pi_i(X)$ for $i\le n$ and $\pi_i(X_n)=0$ for $i>n$, and $X\to X_n$ induces these isomorphisms and a surjection on $\pi_{n+1}$.

::: pf-proof
This is Hatcher's definition of a Postnikov tower; the last condition is what makes $X_n$ the $n$-th stage of $X$ rather than merely a space with the right truncated groups.
:::

:::

::: {.pf-step #loop}
Looping gives a tower $\cdots\to\Omega X_n\to\Omega X_{n-1}\to\cdots$ of fibrations.

::: pf-proof
The loop space functor carries a Hurewicz fibration $p:E\to B$ to a Hurewicz fibration $\Omega p:\Omega E\to\Omega B$: a homotopy $F:Z\times I\to\Omega B$ lifting a map $Z\to\Omega E$ is a map $Z\times I\times I\to B$ whose restriction to $Z\times\{0\}\times I$ lifts, and the homotopy lifting property of $p$ applied to $Z\times I\times I$ lifts it. Hence each $\Omega p_n$ is a fibration.
:::

:::

::: {.pf-step #stages}
$\Omega X_n$ is the $(n-1)$-st Postnikov stage of $\Omega X$.

::: pf-proof
$\pi_i(\Omega X_n)=\pi_{i+1}(X_n)$. For $i+1\le n$, that is $\pi_{i+1}(X)=\pi_i(\Omega X)$; for $i+1>n$, that is $0$. So $\pi_i(\Omega X_n)=\pi_i(\Omega X)$ for $i\le n-1$ and $\pi_i(\Omega X_n)=0$ for $i\ge n$, which is exactly the truncation required of the $(n-1)$-st stage of $\Omega X$. The maps $\Omega X\to\Omega X_n$ induce these isomorphisms, since they are the loops of maps that are isomorphisms on the relevant groups.
:::

:::

::: {.pf-step #principal}
The fibrations $p_n:X_n\to X_{n-1}$ of the tower for $X$ need not be principal.

::: pf-proof
Theorem 4.69 (printed p. 412) states that a connected CW complex has a Postnikov tower of principal fibrations if and only if $\pi_1$ acts trivially on $\pi_n$ for all $n>1$, so principality of the individual fibrations is exactly the hypothesis that can fail. It fails for $X=\RP^2$: there $\pi_1=\ZZ_2$, $\pi_2=\ZZ$ and $\pi_i=0$ for $i\ge3$, so the tower is $\RP^2\to K(\ZZ_2,1)$, and the fibration $p_2:\RP^2\to K(\ZZ_2,1)$ has fibre $K(\ZZ,2)$ while the generator of $\pi_1$ acts on $\pi_2$ by $-1$ (Exercise 2 of §4.2, printed p. 389). So nothing may be assumed about $p_n$, and what the exercise asserts concerns the looped tower.
:::

:::

::: {.pf-step #abelian}
$\Omega X$ is an abelian space, and by Theorem 4.69 it therefore has a Postnikov tower of principal fibrations.

::: pf-proof
$\Omega X$ is an H-space under loop concatenation, and H-spaces are abelian: for an H-space, the action of $\pi_1$ on $\pi_n$ is trivial for every $n$ (Example 4A.3, printed p. 422; the point is that the multiplication makes left and right translation by a loop agree up to homotopy). So $\pi_1(\Omega X)=\pi_2(X)$ acts trivially on every $\pi_n(\Omega X)$. The loop space is not in general a CW complex, and Theorem 4.69 is stated for a connected CW complex, so apply it to a CW approximation $W\to\Omega X$, which is a weak homotopy equivalence: $W$ inherits an H-space structure up to homotopy, hence is abelian, and Theorem 4.69 gives a Postnikov tower of $W$ whose fibrations are all principal. A Postnikov tower of $W$ is one of $\Omega X$, since a weak equivalence induces isomorphisms on all homotopy groups, so $\Omega X$ has a Postnikov tower of principal fibrations.
:::

:::

::: {.pf-step #loopprincipal}
The looped tower is a Postnikov tower of $\Omega X$, hence is a tower of principal fibrations.

::: pf-proof
Steps [](#loop){.pf-ref} and [](#stages){.pf-ref} show that $\Omega X_n$ is the $(n-1)$-st Postnikov stage of $\Omega X$ and that $\Omega X\to\Omega X_n$ has the required effect on homotopy groups, so the looped tower is a Postnikov tower for $\Omega X$ in Hatcher's sense. Postnikov towers of a connected CW complex are unique: the $n$-th stage is determined up to homotopy equivalence under the space by its homotopy groups and the truncation property, which is the uniqueness statement of Hatcher's construction (printed p. 410), and the comparison is an isomorphism on all homotopy groups, hence a homotopy equivalence by Whitehead. Two towers of $\Omega X$ are therefore connected by fibre homotopy equivalences level by level, and principality is a fibre homotopy invariant of a fibration, being a property of its fibre homotopy type; so the looped tower, being a Postnikov tower of $\Omega X$, consists of principal fibrations, with fibre $\Omega K(\pi_nX,n)=K(\pi_nX,n-1)$ at the stage $\Omega X_n\to\Omega X_{n-1}$.
:::

:::

:::
:::
