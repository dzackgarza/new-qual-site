---
schema: qual/card@1
id: E-R3LKO
kind: problem
title: When the inclusion induces an isomorphism on fundamental groups
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 58 Exercise 7, printed p. 366,
    with Theorem 58.7, Theorem 58.3 and Corollary 58.5. Parts (a) and (b) are the two sufficient conditions, and the card's counterexample for the converse is $D^2$ with $A=S^1$ and a constant map, where $j_*:\ZZ\to0$ is not an isomorphism. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    Part (b) now has a published source: UC Riverside Math 205A, Fall 2014, Solutions Part 7, the
    sheet's solution of Hatcher's Exercise 0.4, its p. 5, read in the MinerU extraction
    tmp/sources/ucr-math205A-2014-solutions07.md, together with Hatcher's Proposition 1.18 on
    printed p. 37 of *Algebraic Topology* (2002), the homotopy invariance of $\pi_1$ that the sheet
    applies. The solution transcribes the sheet's argument: the hypothesis that $H$ maps $A\times
    I$ into $A$ lets $H$ be read as a homotopy inside $A$ from $f\circ j$ to the identity, so $f$
    and $j$ are homotopy inverse and $j_*$ is an isomorphism. The sheet is correct and needed no
    repair. Parts (a) and (c) have no located published source, and the card says so: (a) uses
    Lemma 58.4 with $h=\operatorname{id}_X$ and $k=j\circ f$ for surjectivity and $f\circ j=
    \operatorname{id}_A$ for injectivity, and (c) uses $X=B^2$, $A=S^1$ and a constant $f$, where
    $\pi_1(A)=\ZZ$ and $\pi_1(X)$ is trivial. Checked against the book: the exercise on printed
    p. 367, the definition of homotopy inverse on printed p. 363, Lemma 58.4 on printed p. 363,
    Theorem 58.7 on printed p. 364, Theorem 54.5 on printed p. 345, and the triviality of
    $\pi_1(B^2)$ used in Theorem 55.2 on printed p. 348. Not claimed: that the sheet treats parts
    (a) or (c) -- it solves Hatcher's Exercise 0.4, which is part (b).
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the transcription above, in Lamport form, with the sourced part
    and the unsourced parts labelled in its own text.
---

::: {.exercise}

Let $A$ be a subspace of $X$; let $j: A \to X$ be the inclusion map, and let $f: X \to A$ be a continuous map.
Suppose there is a homotopy $H: X \times I \to X$ between the map $j \circ f$ and the identity map of $X$.

(a) Show that if $f$ is a retraction, then $j_*$ is an isomorphism.

(b) Show that if $H$ maps $A \times I$ into $A$, then $j_*$ is an isomorphism.

(c) Give an example in which $j_*$ is not an isomorphism.
:::

::: {.solution}
The exercise is §58 Exercise 7, printed p. 367; the base point is a point
$x_0\in A$, and $j_*$ is the homomorphism $\pi_1(A,x_0)\to\pi_1(X,x_0)$ induced
by the inclusion.

Part (b) is transcribed from UC Riverside Math 205A, Fall 2014, Solutions Part 7,
the sheet's solution of Hatcher's Exercise 0.4, its p. 5, read in
`tmp/sources/ucr-math205A-2014-solutions07.md`. Its point is that the hypothesis
that $H$ maps $A\times I$ into $A$ lets $H$ be read as a homotopy inside $A$, so
that $f$ and $j$ become homotopy inverse, and the conclusion follows from the
homotopy invariance of $\pi_1$: Hatcher, *Algebraic Topology* (2002),
Proposition 1.18, printed p. 37, which in this book is Theorem 58.7, printed
p. 364. Parts (a) and (c) have no located published source; their proofs are
checked against the book, (a) using Lemma 58.4 and (c) using Theorem 55.2's
observation that $B^2$ has trivial fundamental group.

::: pf

::: {.pf-step #a}
(a) If $f$ is a retraction, then $j_*$ is an isomorphism.

::: pf-proof
That $f$ is a retraction means $f\circ j=\operatorname{id}_A$, so by functoriality
$f_*\circ j_*=\operatorname{id}_{\pi_1(A,x_0)}$, and $j_*$ is injective.

For surjectivity, apply Lemma 58.4 (printed p. 363) to the homotopic maps
$h=\operatorname{id}_X$ and $k=j\circ f$, both defined on $X$, with the base point
$x_0$: there is a path $\alpha$ in $X$ from $x_0=h(x_0)$ to $j(f(x_0))$ such that
$k_*=\hat\alpha\circ h_*$, that is
$$
j_*\circ f_*=\hat\alpha .
$$
Since $\hat\alpha$ is an isomorphism, it is surjective, so every element of
$\pi_1(X,x_0)$ is $j_*(f_*(c))$ for some $c\in\pi_1(A,x_0)$; hence $j_*$ is
surjective. Being injective and surjective, $j_*$ is an isomorphism.
:::

:::

::: {.pf-step #b}
(b) If $H$ maps $A\times I$ into $A$, then $j_*$ is an isomorphism.

::: pf-proof
Let $H:X\times I\to X$ be the homotopy from $j\circ f$ to $\operatorname{id}_X$,
and put $K=\restrictionof{H}{A\times I}$, read as a map $K:A\times I\to A$; this
is legitimate because $H(A\times I)\subseteq A$. For $a\in A$,
$$
K(a,0)=H(a,0)=j(f(a))=f(a),\qquad K(a,1)=H(a,1)=a,
$$
so $K$ is a homotopy from $f\circ j$ to $\operatorname{id}_A$, while $H$ itself is
a homotopy from $j\circ f$ to $\operatorname{id}_X$. By the definition on printed
p. 363, $f$ and $j$ are homotopy inverse; so $j$ is a homotopy equivalence and
$j_*$ is an isomorphism by Theorem 58.7 (printed p. 364), that is, by Hatcher's
Proposition 1.18 (printed p. 37).
:::

:::

::: {.pf-step #c}
(c) An example in which $j_*$ is not an isomorphism: $X=B^2$, $A=S^1$, $f$ the
constant map at $(1,0)$.

::: pf-proof
The ball is convex, so the straight-line homotopy $(x,t)\mapsto(1-t)f(x)+tx$
carries $j\circ f$, which is $f$ regarded as a map into $B^2$, to
$\operatorname{id}_{B^2}$; thus the hypothesis of the exercise holds for these
$X,A,f$. Now $\pi_1(S^1,(1,0))\cong\ZZ$ by Theorem 54.5 (printed p. 345), while
$\pi_1(B^2,(1,0))$ is trivial: $B^2$ is convex, hence contractible, hence has the
fundamental group of a point by Theorem 58.3 or 58.7, and this is the fact used
in the proof of Theorem 55.2 (printed p. 348). So
$j_*:\ZZ\to 1$ cannot be injective, and it is not an isomorphism. This also shows
that the hypothesis of part (b) cannot be dropped: here $H(x,t)=(1-t)f(x)+tx$
sends a point of $S^1$ with $0<t<1$ to a point of norm less than one, so $H$ does
not map $A\times I$ into $A$.
:::

:::

:::
:::
