---
schema: qual/card@1
id: P-AGH546QUARTICBASE
kind: problem
title: Three determined base points for quartics through thirteen points
classification:
  areas:
  - algebraic-geometry
  topics:
  - Birational Geometry
  - Cubic Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.6 and the retained Egbert dimension/Bézout argument,
    and compared the phrase "general position" with the later V.4.15 card.
    The dimension count h^0(O_P2(4))=15 shows that 13 independent point
    conditions leave a two-dimensional vector space, hence a pencil. That
    condition alone is not enough for three distinct extra points: the pencil
    must also have no fixed curve component, its two generators must meet
    simply at the 13 prescribed points, and the residual length-three
    complete-intersection scheme must be reduced and disjoint from them.
    Under these open conditions Bézout gives exactly three residual points,
    and every quartic in the pencil contains them. These conditions are also
    the necessary-and-sufficient scheme-theoretic form of the intended
    "sufficiently general" hypothesis.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the full pencil and residual-intersection argument. Verified that
    a (4,4) complete intersection has degree-four ideal space spanned by its
    two generators, so the stated finite 16-point base locus forces the
    thirteen prescribed points to impose 13 independent conditions. Also
    checked the line/conic/cubic fixed-component failure examples by Bézout.
---

::: {.problem}
Generalize (4.5) as follows: given 13 points $P_1, \ldots, P_{13}$ in the plane, there are three additional determined points $P_{14}, P_{15}, P_{16}$, such that all quartic curves through $P_1, \ldots, P_{13}$ also pass through $P_{14}, P_{15}, P_{16}$.
What hypotheses are necessary on $P_1, \ldots, P_{13}$ for this to be true?
:::

::: {.solution}
Let
$$
Z=P_1+\cdots+P_{13}\subseteq\PP^2
$$
be the reduced zero-dimensional subscheme consisting of the thirteen
prescribed points, and put
$$
V=H^0\bigl(\PP^2,\mathcal I_Z(4)\bigr).
$$

The clean hypothesis is that the thirteen points are **sufficiently
general for quartics**, in the following precise sense:

1. they impose independent conditions on quartics, so $\dim V=2$;
2. the pencil $\PP(V)$ has no fixed curve component;
3. for two generators $F_0,F_1$ of $V$, their complete intersection is
   reduced at the thirteen prescribed points and has a reduced residual
   length-three scheme disjoint from $Z$.

These are open conditions on a thirteen-tuple of points. We prove that they
are sufficient, and then explain in what sense they are necessary.

<1>1. The vector space of plane quartics has dimension
$$
\boxed{15}.
$$

::: {.proof}
A homogeneous quartic in three variables has
$$
\binom{4+2}{2}=15
$$
monomials. Hence
$$
h^0\bigl(\PP^2,\OO_{\PP^2}(4)\bigr)=15.
$$
:::

<1>2. Under hypothesis (1), the quartics through
$$
P_1,\ldots,P_{13}
$$
form a projective pencil.

::: {.proof}
Each prescribed reduced point gives one linear evaluation condition on a
quartic. Independence means that the evaluation map has rank $13$.
Therefore
$$
\dim V=15-13=2,
$$
so
$$
\PP(V)\cong\PP^1.
$$
Choose a basis
$$
F_0,F_1\in V.
$$
Every quartic through the thirteen points has equation
$$
\lambda F_0+\mu F_1=0
$$
for some $[\lambda:\mu]\in\PP^1$.
:::

<1>3. Under hypothesis (2), the scheme
$$
B=V(F_0,F_1)
$$
has length
$$
\boxed{16}.
$$

::: {.proof}
The two quartics have no common curve component. Bézout therefore says that
their scheme-theoretic intersection is zero-dimensional of length
$$
4\cdot4=16.
$$
:::

<1>4. Under hypothesis (3), there are exactly three distinct points
$$
P_{14},P_{15},P_{16}
$$
such that
$$
\boxed{
B
=
\{P_1,\ldots,P_{13},P_{14},P_{15},P_{16}\}}
$$
as a reduced scheme.

::: {.proof}
The thirteen prescribed points lie in $B$ because both $F_0$ and $F_1$
belong to $V$. Hypothesis (3) says that each contributes intersection length
one and that the residual scheme is reduced and disjoint from them.

By step <1>3 the total length is $16$. Removing the $13$ prescribed reduced
points therefore leaves a reduced residual scheme of length
$$
16-13=3.
$$
Write its three points as
$$
P_{14},P_{15},P_{16}.
$$
:::

<1>5. Every quartic through $P_1,\ldots,P_{13}$ also passes through
$$
P_{14},P_{15},P_{16}.
$$

::: {.proof}
By step <1>2 every such quartic is
$$
F_{\lambda,\mu}=\lambda F_0+\mu F_1.
$$
At every point of the base scheme $B$ one has
$$
F_0=F_1=0,
$$
and therefore
$$
F_{\lambda,\mu}=0.
$$
In particular every member of the pencil contains the three residual points
of step <1>4.
:::

<1>6. The three additional points are determined by the original thirteen,
not by the chosen basis $F_0,F_1$ of the pencil.

::: {.proof}
The common zero scheme
$$
\operatorname{Bs}|V|
=
\bigcap_{F\in V}V(F)
$$
is intrinsic to the vector space $V$. Since $F_0,F_1$ span $V$, it equals
$$
V(F_0,F_1)=B.
$$
Thus the residual scheme
$$
B\setminus Z
$$
is determined by $Z$, and under hypothesis (3) it consists precisely of the
three points $P_{14},P_{15},P_{16}$.
:::

<1>7. Hypotheses (1)--(3) hold for a general thirteen-tuple of points in
$\PP^2$.

::: {.proof}
Independence of the thirteen evaluation conditions is an open condition,
and it is nonempty because thirteen general points impose the expected
number of conditions on quartics.

Inside that locus, having a fixed curve component is a proper closed
special condition. For a general pencil without a fixed component, two
general generators meet transversely by the usual generic-transversality
statement for plane curves; in particular the complete intersection is
reduced at the prescribed simple base points and at its residual points.
Hence the residual length-three scheme is three distinct points for a
general thirteen-tuple.
:::

<1>8. For the assertion in the problem to mean **exactly three additional
determined points and no fixed curve component**, hypotheses (1)--(3) are
also necessary.

::: {.proof}
Suppose the quartics through the thirteen points have finite common base
locus consisting of exactly the thirteen prescribed reduced points and three
additional distinct reduced points. Choose two general members
$$
F_0,F_1
$$
of this system. They have no common curve component, so Bézout gives a
length-$16$ complete intersection. The sixteen stated base points already
account for all that length, so the intersection is reduced at them and has
no further point. This gives hypotheses (2)--(3).

Moreover a complete intersection of two quartics has ideal generated by
$F_0,F_1$. In degree $4$ this means
$$
H^0\bigl(\mathcal I_B(4)\bigr)
=
\operatorname{span}\{F_0,F_1\},
$$
because any degree-$4$ element of $(F_0,F_1)$ is a scalar linear combination
of the two generators. Every quartic through the original thirteen points
passes through the three additional determined base points, hence through
$B$. Therefore
$$
V=H^0\bigl(\mathcal I_B(4)\bigr)
$$
has dimension $2$. Thus the thirteen points impose exactly $13$ independent
conditions, which is hypothesis (1).
:::

<1>9. Some concrete failures explain why the general-position hypotheses
cannot be omitted.

::: {.proof}
If five of the thirteen points are collinear, every quartic through them
contains that line, because a degree-$4$ polynomial restricted to the line
has five zeros. Thus the quartic system has a fixed component rather than
three isolated residual base points.

Similarly, nine points on an irreducible conic force that conic to be a
component of every quartic through them, by Bézout, and thirteen points on an
irreducible cubic force that cubic to be a component. These are typical
violations of hypothesis (2).

Even when the pencil has no fixed component, tangency of the two generators
at a prescribed or residual base point makes the length-$3$ residual scheme
nonreduced, so one no longer obtains three distinct additional points. This
is precisely what hypothesis (3) excludes.
:::

<1>10. Q.E.D.

::: {.proof}
Steps <1>1--<1>6 prove the asserted three determined points under the precise
general-position hypotheses. Step <1>7 shows these hypotheses hold for a
general thirteen-tuple, and steps <1>8--<1>9 explain their necessity and the
failure modes excluded by them.
:::
:::
