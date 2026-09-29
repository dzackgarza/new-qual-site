---
schema: qual/card@1
id: P-AGH437NODALPLANEQUARTICNOTAPROJECTION
kind: problem
title: A nodal plane curve need not be a projection of a nonsingular space curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Embeddings
  - Genus
  - Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.3.7 together with IV.1.8 and IV.3.6. Independently
    checked the projective closure, Jacobian, tangent cone, and irreducibility
    of the displayed quartic. The contradiction route agrees with standard
    solutions: a hypothetical smooth space-curve source would be the
    normalization, hence have degree 4 and genus 2, which IV.3.6 excludes.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
In view of (3.10), one might ask conversely, is every plane curve with nodes a projection of a nonsingular curve in $\PP^3$?
Show that the curve $xy+x^4+y^4=0$ (assume $\characteristic k \neq 2$) gives a counterexample.
:::

::: {.solution}
Let
$$
C\subseteq\PP_k^2
$$
be the projective closure of the displayed affine curve.
In homogeneous coordinates $[x:y:z]$ it is
$$
C
=
V(F),
\qquad
F=x^4+y^4+xyz^2.
$$
Put
$$
P=[0:0:1].
$$

::: pf

::: {.pf-step #s1}

The only singular point of $C$ is $P$.

::: pf-proof

The partial derivatives are
$$
F_x=4x^3+yz^2,
\qquad
F_y=4y^3+xz^2,
\qquad
F_z=2xyz.
$$
Because $\operatorname{char}k\ne2$, both $2$ and $4$ are nonzero in $k$.

First suppose $z=0$.
A singular point would satisfy
$$
x^4+y^4=0,
\qquad
4x^3=0,
\qquad
4y^3=0,
$$
which forces
$$
x=y=0,
$$
impossible in projective space.
Thus no point at infinity is singular.

Now work on the affine chart $z=1$.
At a singular point,
$$
y+4x^3=0,
\qquad
x+4y^3=0.
$$
Multiplying the first equality by $x$ and the second by $y$ gives
$$
xy+4x^4=0,
\qquad
xy+4y^4=0.
$$
Hence
$$
x^4=y^4=-\frac{xy}{4}.
$$
Substituting in
$$
xy+x^4+y^4=0
$$
gives
$$
\frac{xy}{2}=0.
$$
Since $2\ne0$, one has $xy=0$.
The two derivative equations then force
$$
x=y=0.
$$
Thus $P$ is the unique singular point.

:::

:::

::: {.pf-step #s2}

The singularity of $C$ at $P$ is an ordinary node.

::: pf-proof

On the affine chart $z=1$, a local equation at $P$ is
$$
f(x,y)=xy+x^4+y^4.
$$
Its lowest-degree nonzero homogeneous part is
$$
xy.
$$
Therefore the tangent cone is
$$
V(xy)=V(x)\cup V(y),
$$
the union of two distinct lines.
Hence $P$ is an ordinary double point, that is, a node.

:::

:::

::: {.pf-step #s3}

The quartic $C$ is integral.

::: pf-proof

First, $F$ is squarefree.
Indeed, if an irreducible polynomial $G$ occurred in $F$ with multiplicity at least $2$, then $G$ would divide each partial derivative of $F$.
Every point of the positive-dimensional curve $V(G)$ would then be singular on $C$, contradicting step [](#s1){.pf-ref}, which found only the single singular point $P$.
Thus $C$ is reduced.

Step [](#s1){.pf-ref} says that different irreducible components of $C$ could meet only at $P$.
Step [](#s2){.pf-ref} says that at $P$ there are exactly two smooth local branches meeting transversely, so if $C$ were reducible it would have exactly two irreducible components
$$
C_1,\ C_2
$$
meeting only at $P$, with
$$
I_P(C_1,C_2)=1.
$$

By Bézout's theorem,
$$
\deg C_1\deg C_2
=
\sum_{Q\in C_1\cap C_2}I_Q(C_1,C_2)
=1.
$$
Thus both components would be lines, making
$$
\deg C=2,
$$
contrary to the quartic equation.
Hence $C$ is irreducible.
Since $F$ is a single irreducible equation in the polynomial ring over a field, and we have already shown it squarefree, $C$ is integral.

:::

:::

::: {.pf-step #s4}

The normalization $\widetilde C$ has genus
$$
\boxed{g(\widetilde C)=2}.
$$

::: pf-proof

An integral plane quartic has arithmetic genus
$$
p_a(C)
=
\frac{(4-1)(4-2)}2
=3.
$$
By step [](#s1){.pf-ref}, $P$ is its only singularity, and by step [](#s2){.pf-ref} it is a node.
Exercise [[P-AGH418ARITHGENUSSINGULAR|IV.1.8]] gives
$$
\delta_P=1
$$
and
$$
p_a(C)
=
g(\widetilde C)+\delta_P.
$$
Therefore
$$
g(\widetilde C)=3-1=2.
$$

:::

:::

::: {.pf-step #s5}

Suppose, for contradiction, that $C$ is the image of a nonsingular curve
$$
X\subseteq\PP^3
$$
under a birational linear projection
$$
\pi:X\longrightarrow C.
$$
Then $X\cong\widetilde C$.

::: pf-proof

The smooth curve $X$ is normal.
Since $\pi$ is birational onto the integral curve $C$, the universal property of normalization factors it as
$$
X
\longrightarrow
\widetilde C
\longrightarrow
C.
$$
The first map is a birational morphism between nonsingular projective curves.
Such a morphism is an isomorphism.
Hence
$$
X\cong\widetilde C.
$$
By step [](#s4){.pf-ref},
$$
g(X)=2.
$$

:::

:::

::: {.pf-step #s6}

The hypothetical space curve $X$ has degree
$$
\boxed{\deg X=4}.
$$

::: pf-proof

Projection from a point outside $X$ is defined by a three-dimensional subspace of
$$
H^0(X,\mco_X(1)),
$$
and the pullback of the hyperplane bundle on the target plane is
$$
\pi^*\mco_C(1)\cong\mco_X(1).
$$
Since $\pi$ is birational, it has degree one on function fields, so degrees of line bundles are preserved.
More explicitly, a nonconstant morphism of projective curves is finite, and therefore
$$
\deg\mco_X(1)
=
\deg\mco_C(1).
$$
The right-hand side is the degree of the plane quartic, namely $4$.
Therefore
$$
\deg X=4.
$$

:::

:::

::: {.pf-step #s7}

The curve $C$ cannot be a birational projection of a nonsingular curve in $\PP^3$.

::: pf-proof

Steps [](#s5){.pf-ref} and [](#s6){.pf-ref} would produce a nonsingular curve in $\PP^3$ with
$$
\deg X=4,
\qquad
g(X)=2.
$$
But [[P-AGH436CURVESOFDEGREEFOUR|Exercise IV.3.6(a)]] classifies nonsingular degree-$4$ curves: in $\PP^3$ their genus is either $0$ or $1$, never $2$.
This contradiction proves that no such projection exists.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} show that the displayed curve is an integral plane quartic with exactly one node.
Steps [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} show that it cannot arise as the birational projection of any nonsingular curve in $\PP^3$.
Hence it is the required counterexample.

:::

:::

:::
