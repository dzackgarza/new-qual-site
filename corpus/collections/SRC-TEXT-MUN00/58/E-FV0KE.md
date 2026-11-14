---
schema: qual/card@1
id: E-FV0KE
kind: problem
title: A homotopy equivalence to a point that is not a deformation retract
classification:
  areas:
  - topology
  topics:
  - Homotopy Equivalence
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
    Checked line by line against Munkres, Topology (2000), Section 58 Exercise 8, printed p. 366-367,
    with Theorem 58.3 and the compactness of $\{x_0\}\times I$. The comb space is contracted to $(0,1)$ in two stages, and the argument that no deformation retraction onto $(0,1)$ exists uses the uniform tube $H(V\times I)\subset U$ around the compact set $\{x_0\}\times I$ and the fact that the path component of $\{x_0\}$ in $X\cap\{y>\frac12\}$ is a single tooth, which is not a neighbourhood. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    A published proof has now been located: Cameron Gordon, *Algebraic Topology*, Fall 2019, notes
    by Jackson Van Dyke, Example 1.11 with Claim 1.1 and its proof, printed pp. 12-13, read in the
    MinerU extraction tmp/sources/utexas-gordon-algtop-notes.md. The solution transcribes the
    claim and its tube-lemma argument (the disc of radius $1/2$ about $x_0$, the tube $W\times I$
    inside the preimage, a point $(1/n,1)\in W$, and a path in $U$ between two different path
    components), and writes out the contractibility of the comb, which the source states. The
    source's claim is phrased for a *strong* deformation retraction, which is exactly this book's
    deformation retract (printed p. 360), so no translation of the statement is needed. The source
    is correct and needed no repair. Checked against the book: the exercise and its hint on printed
    p. 367, the definition of deformation retract on printed p. 360, the definition of homotopy
    inverse on printed p. 363, and the tube lemma (Lemma 26.8) on printed p. 168. Not claimed: that
    the source uses Munkres's hint -- it does not, and its argument is independent of the hint's
    suggested route through path components of a neighbourhood of $x_0$, which the card reaches by
    the same disc.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the transcription above, in Lamport form, with the source and
    the book's numbers named in its own text.
---

::: {.exercise}

Find a space $X$ and a point $x_0$ of $X$ such that the inclusion $\theset{x_0} \to X$ is a homotopy equivalence, but $\theset{x_0}$ is not a deformation retract of $X$.
[Hint: Let $X$ be the subspace of $\RR^2$ that is the union of the line segments $(1/n) \times I$, for $n \in \ZZ_+$, the line segment $0 \times I$, and the line segment $I \times 0$; let $x_0$ be the point $(0, 1)$. If $\theset{x_0}$ is a deformation retract of $X$, show that for any neighborhood $U$ of $x_0$, the path component of $U$ containing $x_0$ contains a neighborhood of $x_0$.]
:::

::: {.solution}
The exercise is §58 Exercise 8, printed p. 367, with the space and the point of
its hint: $X$ is the union of the segments $\theset{1/n}\times I$ for
$n\in\ZZ_+$, of $0\times I$ and of $I\times 0$ in $\RR^2$, and $x_0=(0,1)$.

The proof is transcribed from Cameron Gordon, *Algebraic Topology*, Fall 2019,
notes by Jackson Van Dyke, Example 1.11 with Claim 1.1 and its proof, printed
pp. 12--13, read in `tmp/sources/utexas-gordon-algtop-notes.md`. The claim there
is that the comb space does not strong deformation retract to $(0,1)$, which in
this book's terminology (printed p. 360) is the assertion that $\theset{x_0}$ is
not a deformation retract of $X$; the contractibility of the comb is part of the
same example. The source's argument is the tube lemma (Lemma 26.8, printed
p. 168) applied to an open disc about $x_0$, and it is the only part of the proof
that needs an idea; the contractibility is a two-stage deformation retraction
written out in step [](#contractible){.pf-ref}.

::: pf

::: {.pf-step #contractible}
$X$ is contractible, and the inclusion $i:\theset{x_0}\to X$ is a homotopy
equivalence.

::: pf-proof
First $H((x,y),t)=(x,(1-t)y)$ is continuous and maps $X\times I$ into $X$: a point
of $X$ has $y=0$, or $x=0$, or $x=1/n$ for some $n$, and $(x,(1-t)y)$ is then of
the same kind. It fixes $X\cap(I\times 0)=I\times 0$ pointwise and carries $X$
onto $I\times 0$ at $t=1$. Second, $K((x,0),t)=((1-t)x,0)$ is a deformation
retraction of the interval $I\times 0$ onto $(0,0)$. So $\operatorname{id}_X$ is
homotopic to the constant map at $(0,0)$, and $X$ is contractible.

Let $r:X\to\theset{x_0}$ be the only map. Then $r\circ i=
\operatorname{id}_{\theset{x_0}}$, and $i\circ r$ is the constant map at $x_0$,
which is homotopic to $\operatorname{id}_X$ because $X$ is contractible. So $i$
and $r$ are homotopy inverse by the definition on printed p. 363, and $i$ is a
homotopy equivalence.
:::

:::

::: {.pf-step #not-a-retract}
$\theset{x_0}$ is not a deformation retract of $X$.

::: pf-proof
Suppose it is, and let $F:X\times I\to X$ satisfy $F(x,0)=x$, $F(x,1)=x_0$ for all
$x\in X$, and $F(x_0,t)=x_0$ for all $t\in I$. Let $U$ be the open disc of radius
$\tfrac12$ about $x_0$ in $\RR^2$, so that
$$
U\cap X=\bigl(\theset 0\times(\tfrac12,1]\bigr)\cup\bigcup_{n\ge3}
\bigl(\theset{1/n}\times(\tfrac12,1]\bigr),
$$
a disjoint union of closed vertical segments, each of them both open and closed
in $U\cap X$; so two points of $U\cap X$ lie in the same path component of
$U\cap X$ only if they lie in the same segment.

The set $F^{-1}(U)$ is open in $X\times I$ and contains $x_0\times I$, because
$F(x_0,t)=x_0\in U$. Since $I$ is compact, Lemma 26.8, the tube lemma (printed
p. 168), applied with the compact factor $I$ gives a neighbourhood $W$ of $x_0$
in $X$ with $W\times I\subseteq F^{-1}(U)$.

Since $1/n\to0$, the set $W$ contains a point $(1/n,1)$ for some $n\ge3$. Then
$t\mapsto F((1/n,1),t)$ is a path in $X$ whose image lies in $U$, because
$W\times I\subseteq F^{-1}(U)$, and it runs from $F((1/n,1),0)=(1/n,1)$ to
$F((1/n,1),1)=x_0$. Those two points lie in different path components of
$U\cap X$, namely in the segments $\theset{1/n}\times(\tfrac12,1]$ and
$\theset 0\times(\tfrac12,1]$, and a path in $U\cap X$ cannot join them.
Contradiction.
:::

:::

::: {.pf-step}
$\boxed{X\ \text{and}\ x_0\ \text{answer the exercise}}$: the inclusion
$\theset{x_0}\to X$ is a homotopy equivalence and $\theset{x_0}$ is not a
deformation retract of $X$.

::: pf-proof
The first assertion is step [](#contractible){.pf-ref} and the second is step
[](#not-a-retract){.pf-ref}. The space and the point are those of the exercise's
hint, so they are a space and a point with the required property.
:::

:::

:::
:::
