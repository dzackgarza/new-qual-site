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
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The computation of $U\cap X$ was wrong and is repaired. The disc of radius $1/2$ about $(0,1)$
    meets the tooth $\{1/n\}\times I$ in $\{1/n\}\times(a_n,1]$ with
    $a_n=1-\sqrt{1/4-1/n^2}$, which for every $n\ge3$ is strictly above $1/2$ and tends to $1/2$
    from above; the card wrote $(1/2,1]$ and called every piece of $U\cap X$ clopen, but the piece
    $\{0\}\times(1/2,1]$ is closed and not open in $U\cap X$, the teeth accumulating on it. The
    step now computes $U\cap X$, proves each tooth $T_n$ clopen -- closed as
    $U\cap X\cap(\{1/n\}\times I)$, open because a small disc about a point of $T_n$ meets $X$ only
    in that vertical line -- records that the axis piece is not open, and justifies the last step
    by the clopenness of $T_n$ alone: a path in $U$ from $(1/n,1)$ to $x_0$ has connected image, so
    its inverse image of the clopen set $T_n$ is a nonempty open-and-closed subset of $I$, hence all
    of $I$, while $x_0\notin T_n$. The source states this last step in one sentence, "there clearly
    isn't such a path since these two points are in different path components", and does not
    compute the intersection, so the repair is the card's own and the source's claim stands.
    Checked against the book: the exercise and its hint on printed p. 367, the definition of
    deformation retract on printed p. 360, and the tube lemma, Lemma 26.8, on printed p. 168.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    The last step of the first part is now supplied, from a second reader's report on
    this card. That step said that the constant map at the point x_0 and the identity
    are homotopic "because X is contractible", but the contraction written out just
    before it is a homotopy from the identity to the constant map at (0,0), the
    origin of the comb, and it never reaches x_0 = (0,1). The step now goes through
    the path t :-> (0,t), which lies in X because 0 x I is one of the comb's
    segments, and the homotopy G(x,t) = (0,t) that it gives from the constant map at
    (0,0) to the constant map at x_0; transitivity of homotopy (Lemma 51.1) then puts
    the identity homotopic to i o r. The alternative route through the book is
    recorded: a contractible space is path connected (§51 Exercise 3(b)), so the set
    [X,X] has a single element (§51 Exercise 3(d)). The second part, that the point
    is not a deformation retract, and with it the tube-lemma argument and the
    computation of U cap X, is unchanged. Checked against the book: the exercise and
    its hint on printed p. 366 -- the card and the note of 2026-11-14 gave p. 367,
    and §58 exercises 1 to 8 are on p. 366, read on the page image of the PDF, where
    the exercise is printed with its star -- Lemma 51.1 on printed p. 324, §51
    Exercise 3 on printed p. 330, the definition of a deformation retract on printed
    p. 360 and the definition of homotopy inverse on printed p. 363. Not claimed:
    that the book's own hint is used; the card reaches the other half of the exercise
    by the tube lemma, as its earlier note records.
---

::: {.exercise}

Find a space $X$ and a point $x_0$ of $X$ such that the inclusion $\theset{x_0} \to X$ is a homotopy equivalence, but $\theset{x_0}$ is not a deformation retract of $X$.
[Hint: Let $X$ be the subspace of $\RR^2$ that is the union of the line segments $(1/n) \times I$, for $n \in \ZZ_+$, the line segment $0 \times I$, and the line segment $I \times 0$; let $x_0$ be the point $(0, 1)$. If $\theset{x_0}$ is a deformation retract of $X$, show that for any neighborhood $U$ of $x_0$, the path component of $U$ containing $x_0$ contains a neighborhood of $x_0$.]
:::

::: {.solution}
The exercise is §58 Exercise 8, with the space and the point of
its hint: $X$ is the union of the segments $\theset{1/n}\times I$ for
$n\in\ZZ_+$, of $0\times I$ and of $I\times 0$ in $\RR^2$, and $x_0=(0,1)$.

The proof is transcribed from Cameron Gordon, *Algebraic Topology*, Fall 2019,
notes by Jackson Van Dyke, Example 1.11 with Claim 1.1 and its proof, printed
pp. 12--13, read in `tmp/sources/utexas-gordon-algtop-notes.md`. The claim there
is that the comb space does not strong deformation retract to $(0,1)$, which in
this book's terminology (printed p. 360) is the assertion that $\theset{x_0}$ is
not a deformation retract of $X$; the contractibility of the comb is part of the
same example. The source's argument is the tube lemma (Lemma 26.8) applied to an open disc about $x_0$, and it is the only part of the proof
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
\operatorname{id}_{\theset{x_0}}$, and $i\circ r$ is the constant map at $x_0$.
The contraction above ends at $(0,0)$ and not at $x_0$, and the step from one to the
other is the path $t\mapsto(0,t)$: it is a path in $X$, since $0\times I\subseteq
X$, running from $(0,0)$ to $x_0=(0,1)$, and
$$
G(x,t)=(0,t)
$$
is a homotopy, independent of $x$, from the constant map at $(0,0)$ to the constant
map at $x_0$. So $\operatorname{id}_X$ is homotopic to the constant map at $x_0$ by
transitivity of homotopy (Lemma 51.1), that is, $i\circ r\simeq\operatorname{id}_X$;
equivalently, $X$ being contractible it is path connected by §51 Exercise 3(b)
, and then any two of its self-maps are homotopic by §51 Exercise
3(d). With
$r\circ i=\operatorname{id}_{\theset{x_0}}$, the maps $i$ and $r$ are homotopy
inverse by the definition on printed p. 363, and $i$ is a homotopy equivalence.
:::

:::

::: {.pf-step #not-a-retract}
$\theset{x_0}$ is not a deformation retract of $X$.

::: pf-proof
Suppose it is, and let $F:X\times I\to X$ satisfy $F(x,0)=x$, $F(x,1)=x_0$ for all
$x\in X$, and $F(x_0,t)=x_0$ for all $t\in I$. Let $U$ be the open disc of radius
$\tfrac12$ about $x_0=(0,1)$ in $\RR^2$. A point of $X$ is $(0,y)$ or $(1/n,y)$
with $0\le y\le1$, and its distance to $x_0$ is the square root of
$t^2+(y-1)^2$, where $t$ is its first coordinate; so
$$
U\cap X=\bigl(\theset 0\times(\tfrac12,1]\bigr)\ \cup\!\!\bigcup_{n\ge3}
\bigl(\theset{1/n}\times(a_n,1]\bigr),\qquad
a_n=1-\sqrt{\tfrac14-\tfrac1{n^2}},
$$
the terms $n=1,2$ being empty because $1/n\ge\tfrac12$ there.

For $n\ge3$ the tooth $T_n=\theset{1/n}\times(a_n,1]$ is both closed and open in
$U\cap X$. It is closed, being $U\cap X\cap\bigl(\theset{1/n}\times I\bigr)$; and
it is open, because a disc about a point of $T_n$ of radius smaller than the
distance from $\theset{1/n}$ to the other vertical lines of $X$ meets $X$ only in
$\theset{1/n}\times I$, whose points in $U$ are exactly those of $T_n$. The
remaining piece $\theset 0\times(\tfrac12,1]$ is closed in $U\cap X$, being
$U\cap X\cap\bigl(\theset 0\times I\bigr)$, but it is not open: $a_n\to\tfrac12$
from above, so for $y\in(\tfrac12,1]$ the points $(1/n,y)$ lie in $U\cap X$ for
every large $n$ and tend to $(0,y)$.

The set $F^{-1}(U)$ is open in $X\times I$ and contains $x_0\times I$, because
$F(x_0,t)=x_0\in U$. Since $I$ is compact, Lemma 26.8, the tube lemma (printed
p. 168), applied with the compact factor $I$ gives a neighbourhood $W$ of $x_0$
in $X$ with $W\times I\subseteq F^{-1}(U)$.

Since $1/n\to0$, the set $W$ contains a point $(1/n,1)$ for some $n\ge3$. Then
$t\mapsto F((1/n,1),t)$ is a path in $X$ whose image lies in $U$, because
$W\times I\subseteq F^{-1}(U)$, and it runs from $F((1/n,1),0)=(1/n,1)$ to
$F((1/n,1),1)=x_0$. Its image is connected, so it stays in the tooth that
contains its first point: the inverse image of the clopen set $T_n$ is a
nonempty subset of $I$ that is open and closed, hence all of $I$, and
$(1/n,1)\in T_n$. But $x_0=(0,1)\notin T_n$, and the path ends at $x_0$.
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
