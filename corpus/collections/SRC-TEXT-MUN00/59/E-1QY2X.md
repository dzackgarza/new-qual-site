---
schema: qual/card@1
id: E-1QY2X
kind: problem
title: A flawed proof that the sphere is simply connected
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 59 Exercise 2, printed p. 370,
    with Theorem 57.3 and Theorem 59.3. The card names the flaw, that the flawed proof chooses a point of $S^2$ off the image of a loop, which a continuous loop need not miss; it justifies that with a space-filling curve and repairs the argument in the two ways available after this chapter. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    A published criticism has now been located: Pearse, *Topology (2nd ed.) — James R. Munkres*,
    solutions, Cornell 2005, §59 Exercise 2, his p. 24, read in the MinerU extraction
    tmp/sources/cornell-erin-munkres.md. The solution is that criticism transcribed: the proposed
    proof chooses $p$ outside the image of the loop, and no such point need exist, a continuous map
    of $I$ into $S^2$ being able to fill the sphere; the source points to Theorem 44.1 (printed
    p. 272), which the card uses to construct a surjective loop. The source is correct and needed
    no repair; the card supplies what it leaves implicit, that the surjective map of $I$ can be
    turned into a loop by appending a path, and that $S^2$ is a continuous image of $I^2$, the
    quotient of $B^2$ by its boundary circle. Checked against the book: the exercise on printed
    p. 370, Theorem 44.1 on printed p. 272, and Theorem 59.3 on printed p. 369 for the conclusion
    the proposed proof was aiming at. Not claimed: that the exercise wants a proof of simple
    connectedness -- it asks for a criticism, and the true statement is quoted only to say that the
    failure is in the argument, not in the conclusion.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the criticism above, in Lamport form, with the source and the
    book's pages named in its own text.
---

::: {.exercise}

Criticize the following "proof" that $S^2$ is simply connected.
Let $f$ be a loop in $S^2$ based at $x_0$.
Choose a point $p$ of $S^2$ not lying in the image of $f$.
Since $S^2 - \theset{p}$ is homeomorphic with $\RR^2$, and $\RR^2$ is simply connected, the loop $f$ is path homotopic to the constant loop.
:::

::: {.solution}
The exercise is §59 Exercise 2, printed p. 370, and it asks for a criticism of a
proposed proof, not for a proof. The criticism is transcribed from Pearse,
*Topology (2nd ed.) — James R. Munkres*, solutions, Cornell 2005, §59 Exercise 2,
his p. 24, read in `tmp/sources/cornell-erin-munkres.md`: the step that chooses
$p\notin f(I)$ has no justification, because a loop can be surjective, and the
source points to Munkres's Theorem 44.1 (printed p. 272) for a continuous map of
$I$ onto $I^2$ to compose with.

The load-bearing step of the proposed proof is "choose a point $p$ of $S^2$ not
lying in the image of $f$". Everything after it is correct: if $p\notin f(I)$,
then $f$ is a loop in $S^2-\theset p$, which is homeomorphic to $\RR^2$, and
$\RR^2$ is simply connected, so $f$ is path homotopic to a constant loop. What
fails is that the point need not exist: a loop is a continuous map of an
interval, and a continuous map of an interval can fill the whole sphere. The rest
of the exercise's conclusion happens to be true -- $S^2$ is simply connected by
Theorem 59.3 (printed p. 369) -- but the proposed proof does not establish it,
because its hypothesis can fail.

::: pf

::: {.pf-step #surjective-loop}
There is a loop in $S^2$ whose image is all of $S^2$.

::: pf-proof
Let $\pi:I\to I^2$ be the continuous surjection of Theorem 44.1 (printed p. 272),
the Peano curve. The boundary circle of $B^2$ is a circle, so the quotient
$B^2/\partial B^2$ obtained by collapsing it to a point is two closed discs glued
along their boundary circles, which is a sphere; let $q:B^2\to S^2$ be that
quotient map, and let $h:I^2\to S^2$ be $q$ composed with a homeomorphism
$I^2\to B^2$. Then $h$ is continuous and surjective, and
$f=h\circ\pi:I\to S^2$ is a continuous map of $I$ into $S^2$ whose image is
$h(I^2)=S^2$. To make it a loop, take a path $\gamma:I\to S^2$ from $f(1)$ to
$f(0)$, which exists because $S^2$ is path connected, and put $F(s)=f(2s)$ for
$s\le\tfrac12$ and $F(s)=\gamma(2s-1)$ for $s\ge\tfrac12$; the two formulas agree
at $s=\tfrac12$ where both are $f(1)$, so $F$ is continuous by the pasting lemma,
$F(0)=f(0)=\gamma(1)=F(1)$, and the image of $F$ contains the image of $f$, which
is $S^2$. So $F$ is a loop in $S^2$ with image $S^2$.
:::

:::

::: {.pf-step}
$\boxed{\text{The proof is invalid}}$: its choice of $p\notin f(I)$ can fail, by
step [](#surjective-loop){.pf-ref}, so it proves nothing about a general loop.

::: pf-proof
Let $f$ be a surjective loop, which exists by step [](#surjective-loop){.pf-ref}.
There is no point $p$ of $S^2$ outside $f(I)$, so the proposed proof cannot be
started for this $f$. Since the conclusion must hold for every loop, an argument
that requires a point off the image establishes the theorem only for the loops
that miss a point. The remedy is a proof that does not choose such a $p$: Theorem
59.3, whose proof splits $S^2$ into two open discs and uses Corollary 59.2.
:::

:::

:::
:::
