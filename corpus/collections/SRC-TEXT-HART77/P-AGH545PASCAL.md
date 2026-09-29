---
schema: qual/card@1
id: P-AGH545PASCAL
kind: problem
title: Pascal's theorem for six points on a conic
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
    Read Hartshorne V.4.5, the retained Egbert Cayley--Bacharach construction,
    and the just-completed V.4.4 nine-point argument. The two reducible
    cubics AB' union BC' union CA' and A'B union B'C union C'A meet at the
    six points on the conic together with P,Q,R. The cubic consisting of the
    conic and the line PQ contains the six vertices plus P,Q, so
    Cayley--Bacharach forces R onto it; in the nondegenerate configuration R
    is not on the conic, hence R lies on PQ. Collinearity is a closed
    determinant condition, so the identity extends to every specialization
    for which the stated intersections remain well-defined.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete nine-point configuration and checked every entry of
    the intersection table. The Cayley--Bacharach application is on the
    reduced nondegenerate locus; the final determinant argument makes the
    specialization step precise on the irreducible six-fold product of a
    smooth conic and by closure in the universal conic family.
---

::: {.problem}
Prove Pascal's theorem: if $A, B, C, A^{\prime}, B^{\prime}, C^{\prime}$ are any six points on a conic, then the points $P=A B^{\prime} \cdot A^{\prime} B$, $Q=A C^{\prime} \cdot A^{\prime} C$, and $R=B C^{\prime} \cdot B^{\prime} C$ are collinear.

![Pascal's theorem: the six points $A, B, C, A^{\prime}, B^{\prime}, C^{\prime}$ on a conic and the collinear points $P, Q, R$.](../../../assets/algebraic-geometry/curves-and-surfaces/pascal-theorem-six-points-on-conic.png){width=350px}
:::

::: {.solution}
Let
$$
K\subseteq\PP^2
$$
be the conic containing
$$
A,B,C,A',B',C'.
$$
We first treat the open configuration in which the six points are distinct
and all the side intersections in the statement are distinct and
well-defined.

::: pf

::: {.pf-step #nine-intersection-points}
Form the two reducible cubics
$$
X=AB'\cup BC'\cup CA'
$$
and
$$
Y=A'B\cup B'C\cup C'A.
$$
Their nine pairwise line intersections are exactly
$$
A,B,C,A',B',C',P,Q,R.
$$

::: pf-proof
Write the three components of $X$ as rows and those of $Y$ as columns. Their
pairwise intersections are
$$
\begin{array}{c|ccc}
 & A'B & B'C & C'A\\ \hline
AB' & P & B' & A\\
BC' & B & R & C'\\
CA' & A' & C & Q.
\end{array}
$$
Indeed, for example,
$$
AB'\cap A'B=P,
\qquad
BC'\cap B'C=R,
\qquad
CA'\cap C'A=Q,
$$
by the definitions in the problem; the remaining six intersections are the
six named points on $K$.

For a general such configuration the two cubics have no common line
component. Hence Bezout gives
$$
\deg(X\cap Y)=3\cdot3=9,
$$
and the table lists all nine points of their complete intersection.
:::

:::

::: {.pf-step #eight-points-on-conic-union-line}
The reducible cubic
$$
Z=K\cup PQ
$$
contains eight of the nine points of $X\cap Y$:
$$
A,B,C,A',B',C',P,Q.
$$

::: pf-proof
The first six points lie on the conic $K$ by hypothesis, while $P$ and $Q$
lie on the line $PQ$ by definition. Thus all eight lie on the cubic
$K\cup PQ$.
:::

:::

::: {.pf-step #r-lies-on-z}
The ninth point $R$ lies on $Z$.

::: pf-proof
Apply the Cayley--Bacharach theorem to the complete intersection of the two
cubics $X$ and $Y$. Any cubic through eight of the nine intersection points
passes through the ninth. By step [](#eight-points-on-conic-union-line){.pf-ref}, $Z$ passes through eight of them.
Therefore
$$
R\in Z=K\cup PQ.
$$
:::

:::

::: {.pf-step #r-not-on-conic}
In the nondegenerate configuration,
$$
R\notin K.
$$

::: pf-proof
By definition,
$$
R\in BC'.
$$
The line $BC'$ already meets the conic $K$ at the two distinct points
$$
B
\qquad\text{and}\qquad
C'.
$$
If $R$ were a third distinct point of $BC'\cap K$, then a line and a conic
would have at least three distinct intersection points, contradicting
Bezout. In the present open configuration $R$ is distinct from $B,C'$, so
indeed $R\notin K$.
:::

:::

::: {.pf-step #pqr-collinear-nondegenerate}
Therefore
$$
\boxed{P,Q,R\text{ are collinear}.}
$$

::: pf-proof
Step [](#r-lies-on-z){.pf-ref} gives
$$
R\in K\cup PQ,
$$
while step [](#r-not-on-conic){.pf-ref} excludes the conic component. Hence
$$
R\in PQ.
$$
This is precisely Pascal's collinearity assertion for the nondegenerate
configuration.
:::

:::

::: {.pf-step #extends-to-degenerate-case}
The same collinearity holds for every specialization for which the
three points $P,Q,R$ in the statement are defined.

::: pf-proof
The construction is algebraic in the six points. On any affine coordinate
chart, the intersection point of two distinct lines is given by their cross
product, so homogeneous coordinates of $P,Q,R$ are polynomial expressions
in homogeneous coordinates of
$$
A,B,C,A',B',C'.
$$
Collinearity is the vanishing of the determinant
$$
\det(P,Q,R).
$$
After substituting those cross-product expressions, this determinant is a
multihomogeneous polynomial in the coordinates of the six points. For a
fixed nonsingular conic $K$, the parameter space
$$
K^6
$$
is irreducible, and the nondegenerate configurations used in steps
[](#nine-intersection-points){.pf-ref}, [](#eight-points-on-conic-union-line){.pf-ref}, [](#r-lies-on-z){.pf-ref}, [](#r-not-on-conic){.pf-ref} and [](#pqr-collinear-nondegenerate){.pf-ref} form a nonempty dense open subset. The determinant vanishes on
that dense open subset, hence on all of $K^6$. Therefore every specialization
on $K$ for which the three line intersections remain defined also satisfies
$$
\det(P,Q,R)=0.
$$

The same closed-condition argument in the universal family of plane conics
extends the identity to a degenerate conic whenever the three intersections
in the statement remain defined. If adjacent marked points coalesce, the
usual limiting formulation replaces their secant by the tangent to the
conic, and the same specialization gives the degenerate Pascal identity.
:::

:::

::: pf-qed
Steps [](#nine-intersection-points){.pf-ref}, [](#eight-points-on-conic-union-line){.pf-ref}, [](#r-lies-on-z){.pf-ref}, [](#r-not-on-conic){.pf-ref} and [](#pqr-collinear-nondegenerate){.pf-ref} prove Pascal's theorem by Cayley--Bacharach on the dense
nondegenerate locus, and step [](#extends-to-degenerate-case){.pf-ref} extends the identity to all well-defined
specializations.
:::

:::
:::
