---
schema: qual/card@1
id: P-AGH461RATIONALQUARTICONUNIQUEQUADRIC
kind: problem
title: A rational quartic in $\PP^3$ lies on a unique, nonsingular, quadric surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Embeddings
  - Genus
  - Linear Systems
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.6.1 and the retained companion solution. The source
    statement needs no correction. The companion's cohomological
    existence/uniqueness argument is retained, while its final appeal to a
    "rational normal quartic" is replaced by Hartshorne's quadric-cone genus
    calculation, recorded on FE-CRVQUAD.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Printed exercise read: Hartshorne IV.6.1, printed p. 355 -- "A rational curve of degree 4 in
    P^3 is contained in a unique quadric surface Q, and Q is necessarily nonsingular." The card
    states it verbatim, adding and dropping no hypothesis.

    The proof read step by step; every step is correct as written. s1: a plane quartic is a
    nonsingular plane curve of genus 3 by the plane-curve formula, and X is rational, so X is not
    planar. s2: deg 2H = 8 with X isomorphic to P^1, so h^0(X, O_X(2)) = 9, while
    h^0(P^3, O(2)) = 10, so the restriction map has a kernel and X lies on a quadric. s3: if two
    independent containing quadrics share a plane, irreducibility puts X in a plane; otherwise
    their intersection Y is a complete intersection of degree 4 = deg X, and the kernel of
    O_Y -> O_X has zero-dimensional support while O_Y, Y being a complete intersection, is
    Cohen--Macaulay of pure dimension 1, so Y = X and p_a(Y) = 1 contradicts p_a(X) = 0. s4: a
    singular quadric is a pair of planes, a double plane, or a cone; the first two put X in a
    plane, and a curve of degree 4 = 2*2 on a cone has genus (2-1)^2 = 1, against 0.

    Compared with the published solution. Lomont's 6.1, retained at
    tmp/sources/hartshorne-solutions-lomont.md and beginning at line 250 of that file, gives the
    same existence count and the same uniqueness argument by the complete-intersection genus, and
    then ends "Then by (Ex. 3.6) X is the rational quartic curve in P^3, so Q is nonsingular.
    (TODO - not clear?)". That last step is the one this card proves in s4, so the card is stronger
    exactly where the published solution is unfinished.

    Changed in this pass: s4 now cites the printed statement of the cone genus, Hartshorne's
    Remark 6.4.1(d) at printed pp. 352--353, beside FE-CRVQUAD; it had cited the fact card alone.
    (The first version of this event gave those pages as 367--368, which are PDF pages; corrected here.)
    No claim changed.

    Not checked: the proof on FE-CRVQUAD (read, not re-derived), and Hartshorne V. Ex. 2.9, to
    which Remark 6.4.1(d) is deferred and which is not read here.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Three repairs in s3 and s1, all prompted by a review that read the two steps' reasons rather
    than their conclusions; no statement of the card changes.

    s3's uniqueness argument ended "the complete-intersection curve Y is Cohen-Macaulay of pure
    dimension 1, so O_Y has no nonzero zero-dimensional subsheaf". That inference is not available:
    Cohen--Macaulay gives unmixedness of the associated primes, but a nonzero zero-dimensional
    subsheaf is killed by a power of the maximal ideal of a point, so what rules it out is O_Y being
    a domain at each point, that is S1 and reducedness, which a (2,2) complete intersection need not
    have -- V(xy, z^2) in P^3 has no common factor between its two quadrics and is non-reduced along
    both of its lines. The step now compares Hilbert polynomials instead, which needs neither
    property: X lies in Y and is reduced, so the two sheaves agree at the generic point and the
    kernel K of O_Y -> O_X is zero-dimensional; a zero-dimensional sheaf of length l has Euler
    characteristic l for every twist, so P_Y = P_X + l, while P_X = 4t + 1 - g(X) = 4t + 1 and
    P_Y = 4t + 1 - p_a(Y) = 4t. Hence 4t = 4t + 1 + l, so l = -1, impossible, the kernel is zero and
    Y = X, which contradicts g(X) = 0 with p_a(Y) = 1. The same conclusion, now with a proof that
    covers the non-reduced and embedded-point cases the earlier sentence did not.

    s1 and s3 now cite the printed formulas they use: the plane-curve genus to II.8.20.3 at printed
    p. 183 and II. Ex. 8.4(f), and the complete-intersection genus to II. Ex. 8.4(g) at printed
    p. 188. Those references were used and not named.

    Not checked: the same two items as above, FE-CRVQUAD's proof and Hartshorne V. Ex. 2.9.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Citation form (#184). Every reference in this card's text is now carried by its numbered
    statement: Exercise IV.6.1; Exercise IV.3.4(a), (b); Exercise IV.3.6(b); Example II.8.20.3 and
    Exercise II.8.4(f) for the plane-curve genus; Exercise II.8.4(g) for the (2,2)
    complete-intersection genus; Remark IV.6.4.1(d) with Exercise V.2.9 for the quadric-cone genus.
    No page, PDF page or page offset appears in the card's text; the locators inside the events of
    2026-09-18 and 2026-11-19 are records of those passes and are left as written (QUAL-11). The
    mathematics is unchanged in this pass.
---

::: {.problem}
A rational curve of degree 4 in $\PP^3$ is contained in a unique quadric surface $Q$, and $Q$ is necessarily nonsingular.
:::

::: {.solution}
Let $X\subseteq\PP^3$ be the given rational quartic, and put
$H=\OO_X(1)$.

::: pf

::: {.pf-step #s1}

The curve $X$ is not contained in a plane.

::: pf-proof

If $X$ lay in a plane, then, being a nonsingular plane curve of degree $4$,
it would have genus
$$
\frac{(4-1)(4-2)}2=3
$$
by the plane-curve genus formula, Hartshorne Example II.8.20.3 and Exercise II.8.4(f).
But $X$ is rational, so its genus is $0$.  Hence $X$ is nondegenerate in
$\PP^3$.

:::

:::

::: {.pf-step #s2}

At least one quadric surface contains $X$.

::: pf-proof

Since $X\cong\PP^1$ and $\deg H=4$,
$$
\deg(2H)=8,
\qquad
h^0(X,\OO_X(2))=8+1=9.
$$
Twisting the ideal sequence of $X$ by $\OO_{\PP^3}(2)$ gives
$$
0\longrightarrow\mathcal I_X(2)
\longrightarrow\OO_{\PP^3}(2)
\longrightarrow\OO_X(2)
\longrightarrow0.
$$
On global sections,
$$
h^0(\PP^3,\OO_{\PP^3}(2))=\binom{5}{3}=10>9,
$$
so the restriction map cannot be injective.  Thus
$$
H^0(\PP^3,\mathcal I_X(2))\neq0,
$$
and a nonzero element is the equation of a quadric containing $X$.

:::

:::

::: {.pf-step #s3}

That containing quadric is unique.

::: pf-proof

Suppose two linearly independent quadrics $Q_1,Q_2$ contain $X$.
They cannot have a common plane component: otherwise, because $X$ is
irreducible and lies in each quadric, the common-factor alternatives force
$X$ into a plane, contrary to step [](#s1){.pf-ref}.  Hence
$$
Y=Q_1\cap Q_2
$$
is a complete-intersection curve of type $(2,2)$.

By Bezout,
$$
\deg Y=2\cdot2=4=\deg X.
$$
The surjection $\OO_Y\twoheadrightarrow\OO_X$ has kernel supported in
dimension $0$: the two sheaves agree at the generic point of $X$, since $X$
is a reduced curve and lies in $Y$.  Comparing Hilbert polynomials, a
zero-dimensional sheaf of length $\ell$ has $\chi=\ell$ constant in $t$, so
$$
P_Y(t)=P_X(t)+\ell
\qquad\text{for all }t,
$$
while
$$
P_X(t)=4t+1-g(X)=4t+1,
\qquad
P_Y(t)=4t+1-p_a(Y)=4t,
$$
the second by the complete-intersection genus formula, Hartshorne Exercise II.8.4(g), which gives
$$
p_a(Y)
=1+\frac{(2)(2)(2+2-4)}2
=1.
$$
The two displays give $4t=4t+1+\ell$, so $\ell=-1$, which is impossible;
hence the kernel is zero and
$Y=X$ scheme-theoretically.
This contradicts the genus: the nonsingular rational curve $X$ has
$p_a(X)=0$, while $p_a(Y)=1$.

:::

:::

::: {.pf-step #s4}

The unique quadric $Q$ is nonsingular.

::: pf-proof

Over the algebraically closed ground field, a singular quadric surface in
$\PP^3$ is either a union (possibly doubled) of planes or an irreducible
quadric cone.  The first possibility would put the irreducible curve $X$ in
a plane, contradicting step [](#s1){.pf-ref}.

Suppose therefore that $Q$ is a quadric cone.  For a curve of even degree
$2a$ on a quadric cone the genus is $a^2-2a+1=(a-1)^2$: Hartshorne's
Remark 6.4.1(d), deferred there to V. Ex. 2.9 and
proved on [[FE-CRVQUAD]].  Here $\deg X=4=2\cdot2$, so this gives
$$
p_a(X)=(2-1)^2=1,
$$
again contradicting the fact that the nonsingular rational curve $X$ has
genus $0$.  Thus $Q$ cannot be singular.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} gives existence, step [](#s3){.pf-ref} gives uniqueness, and step [](#s4){.pf-ref} proves
that the unique quadric is nonsingular.

:::

:::

:::
