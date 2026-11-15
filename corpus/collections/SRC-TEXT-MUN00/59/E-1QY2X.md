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
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The construction of the surjective loop rested on the sentence "$B^2/\partial B^2$ obtained by
    collapsing the boundary circle to a point is two closed discs glued along their boundary
    circles, which is a sphere", which is not a proof and describes the wrong space: the quotient is
    a single disc with its boundary collapsed, and gluing two discs along their boundary circles
    gives a sphere but is not that quotient. The step now proves $B^2/\partial B^2\cong S^2$ by an
    explicit map $g:B^2\to S^2$ with third coordinate $-\cos\pi\abs x$ and horizontal part
    $(\sin\pi\abs x/\abs x)\,x$, which is continuous, constant exactly on $\partial B^2$ with value
    $(0,0,1)$, and injective off $\partial B^2$, so that it induces a continuous bijection from the
    compact quotient onto the Hausdorff sphere, hence a homeomorphism by Theorem 26.6; the book
    pictures the same quotient in Figure 22.2 (printed p. 136). The rest of the step is unchanged.
    Checked against the book: the exercise on printed p. 370, Theorem 44.1 on printed p. 272,
    Theorem 26.6 on printed p. 167 and Figure 22.2 on printed p. 136.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Two repairs, from a second reader's report on this card. (1) The step called the
    map e : I^2 -> B^2 a linear homeomorphism; a linear map carries the square onto a
    parallelogram, not onto the disc, and no such map exists. What the step needs is
    a continuous surjection, and it now uses p(s,t) = (s cos 2 pi t, s sin 2 pi t),
    onto because r(cos theta, sin theta) is p(r, theta/2 pi); h = gbar o q o p is
    then continuous and surjective as a composite of surjections, which is all that
    the construction of the surjective loop uses. (2) The argument that g induces a
    homeomorphism B^2/partial B^2 -> S^2 said that g is constant on the boundary
    circle, that its fibre over (0,0,1) is the boundary circle and that it is
    injective off the boundary circle; that gives injectivity of the induced map and
    the bijection also needs surjectivity, which was used but not stated. The step
    now proves that g is onto: for (u,z) in S^2 with z not 1, r = arccos(-z)/pi
    lies in [0,1) and gives cos pi r = -z and sin pi r = |u|, so x = u r/|u| (and
    x = 0 when u = 0, where z = -1) maps to (u,z), while z = 1 is the value on the
    boundary circle. It then states that the fibres of g are the fibres of q, which
    is what makes the induced map a bijection. Checked against the book: the
    exercise on printed p. 370, Theorem 44.1 on printed p. 272, Theorem 26.6 on
    printed p. 167 and Figure 22.2 on printed p. 136; the arithmetic of the
    inversion formula was worked through in both directions, and the surjectivity
    computation checked at u = 0 and at z = 1. Not claimed: that the earlier note of
    2026-11-14 on this card is wrong about anything except the surjectivity it left
    implicit.
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
the Peano curve. Let $q:B^2\to B^2/\partial B^2$ be the map collapsing the
boundary circle to a point, and let $g:B^2\to S^2$ be
$$
g(x)=\Bigl(\frac{\sin\pi\abs x}{\abs x}\,x_1,\
\frac{\sin\pi\abs x}{\abs x}\,x_2,\ -\cos\pi\abs x\Bigr)\quad (x\ne\mathbf 0),
\qquad g(\mathbf 0)=(0,0,-1),
$$
where $S^2$ is the unit sphere of $\RR^3$. The map $g$ is continuous: the factor
$\sin\pi\abs x/\abs x$ tends to $\pi$ as $x\to\mathbf 0$, and the third coordinate
is continuous. It is constant on $\partial B^2$, where $\abs x=1$, with value
$(0,0,1)$, and its fibre over $(0,0,1)$ is $\partial B^2$.

It is also onto. Let $(u,z)\in S^2$. If $z=1$ then $u=\mathbf 0$ and $(u,z)$ is the
value of $g$ at every point of $\partial B^2$. If $z\ne1$, the number
$r=(\arccos(-z))/\pi$ lies in $[0,1)$ and satisfies $\cos\pi r=-z$ and
$\sin\pi r=\sqrt{1-z^2}=\abs u$. If $u\ne\mathbf 0$ then $r>0$, and the point
$x=u\,r/\abs u$ has $\abs x=r$, so
$$
\frac{\sin\pi\abs x}{\abs x}\,x=\frac{\sin\pi r}{r}\cdot\frac{ur}{\abs u}
=u\,\frac{\sin\pi r}{\abs u}=u,
\qquad -\cos\pi\abs x=-\cos\pi r=z,
$$
that is, $g(x)=(u,z)$; and if $u=\mathbf 0$ then $\sin\pi r=0$, so $r=0$ and
$z=-1$, which is $g(\mathbf 0)$. Hence every point of $S^2$ is a value of $g$.

It is injective off $\partial B^2$: a point $(u,z)$ of $S^2$ with $z\ne1$
determines $\abs x$ by the third coordinate, $z=-\cos\pi\abs x$, which is $0$ only
for $z=-1$, then $\sin\pi\abs x$ as the positive square root of $1-z^2$, and hence
$x=u\,\abs x/\sin\pi\abs x$ when $z\ne-1$, while $z=-1$ forces $x=\mathbf 0$. So
the fibres of $g$ are the fibres of $q$, and $g$ induces a continuous bijection
$\bar g:B^2/\partial B^2\to S^2$, which is a homeomorphism because
$B^2/\partial B^2$ is compact and $S^2$ is Hausdorff (Theorem 26.6, printed
p. 167); the construction is the one pictured in Figure 22.2 of the book (printed
p. 136).

The step needs a continuous surjection $I^2\to B^2$, and not a homeomorphism:
take $p(s,t)=(s\cos2\pi t,\,s\sin2\pi t)$, which is continuous and onto, the point
$r(\cos\theta,\sin\theta)$ of $B^2$ being $p(r,\theta/2\pi)$. A linear map of
$I^2$ would not do, since it carries the square onto a parallelogram. Put
$h=\bar g\circ q\circ p:I^2\to S^2$. Then $h$ is continuous and surjective, being
a composite of surjections, and
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
