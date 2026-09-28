---
schema: qual/card@1
id: P-AGH5413DELPEZZO4
kind: problem
title: The 16 lines on the degree four Del Pezzo surface and its equations
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Blowups
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.13, the retained Egbert solution, the degree-four
    Del Pezzo blowup model from V.4.7, and the immediately preceding Kodaira
    vanishing exercise V.4.12. Cross-checked the standard description against
    Dolgachev's treatment of quartic Del Pezzo surfaces. The 16 displayed
    lines are the five exceptional curves, ten transforms of pairwise joining
    lines, and the transform of the conic through all five points. For the
    equations, Riemann--Roch and V.4.12 give h^0(-2K_X)=13, so at least two
    independent quadrics contain the anticanonical image; their degree-four
    complete intersection must equal the degree-four surface X.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
---

::: {.problem}
Let $X$ be the Del Pezzo surface of degree 4 in $\PP^4$ obtained by blowing up 5 points of $\PP^2$ (4.7).

a. Show that $X$ contains 16 lines.

b. Show that $X$ is a complete intersection of two quadric hypersurfaces in $\PP^4$ (the converse follows from (4.7.1)).
:::

::: {.solution}
Let
$$
\pi:X\longrightarrow\PP^2
$$
be the blowup of the five points $P_1,\ldots,P_5$ in general position. Write
$L$ for the pullback of a line and $E_i$ for the exceptional curves. The
anticanonical embedding of (4.7) is given by
$$
H=-K_X=3L-E_1-\cdots-E_5,
\qquad
H^2=4.
$$

<1>1. The five exceptional curves $E_i$ are lines in the anticanonical
embedding.

::: {.proof}
The intersection form on the blowup is
$$
L^2=1,
\qquad
L\cdot E_i=0,
\qquad
E_i\cdot E_j=0\ (i\ne j),
\qquad
E_i^2=-1.
$$
Hence
$$
H\cdot E_i=1.
$$
Each $E_i\cong\PP^1$, and the very ample divisor $H$ embeds it as a curve of
degree one in $\PP^4$. Thus every $E_i$ is a line on $X$.
:::

<1>2. For every pair $1\le i<j\le5$, the strict transform of the line through
$P_i$ and $P_j$ is a line on $X$.

::: {.proof}
Because the five points are in general position, the line through $P_i,P_j$
contains none of the other three points. Its strict transform $L_{ij}$ has
class
$$
L-E_i-E_j.
$$
Therefore
$$
H\cdot L_{ij}
=(3L-E_1-\cdots-E_5)\cdot(L-E_i-E_j)
=3-1-1
=1.
$$
The curve $L_{ij}$ is isomorphic to $\PP^1$, so the anticanonical embedding
maps it to a line. There are
$$
\binom52=10
$$
such curves.
:::

<1>3. The strict transform of the conic through $P_1,\ldots,P_5$ is a line
on $X$.

::: {.proof}
Five points in general position determine a unique conic $Q$. It is
irreducible: if it were the union of two lines, one of those lines would
contain at least three of the five points, contrary to general position.
Thus $Q$ is a nonsingular conic and its strict transform $\widetilde Q$ has
class
$$
2L-E_1-\cdots-E_5.
$$
Consequently
$$
H\cdot\widetilde Q=6-5=1.
$$
Since $\widetilde Q\cong\PP^1$, it is mapped to a line by the anticanonical
embedding.
:::

<1>4. The surface $X$ contains 16 distinct lines.

::: {.proof}
Steps <1>1--<1>3 give respectively
$$
5,
\qquad
10,
\qquad
1
$$
lines. Their divisor classes are respectively
$$
E_i,
\qquad
L-E_i-E_j,
\qquad
2L-E_1-\cdots-E_5,
$$
so they are distinct. Hence $X$ contains
$$
\boxed{5+10+1=16}
$$
lines. This proves part (a).
:::

<1>5. One has
$$
\boxed{h^0(X,\OO_X(2H))=13.}
$$

::: {.proof}
The surface $X$ is rational, so
$$
\chi(\OO_X)=1.
$$
Riemann--Roch on a nonsingular projective surface gives, for $D=2H=-2K_X$,
$$
\begin{aligned}
\chi(\OO_X(2H))
&=\chi(\OO_X)+\frac12(2H)\cdot(2H-K_X)\\
&=1+\frac12(2H)\cdot3H\\
&=1+3H^2\\
&=13.
\end{aligned}
$$

By Serre duality,
$$
H^2(X,\OO_X(2H))
\cong
H^0(X,\OO_X(K_X-2H))^*
=H^0(X,\OO_X(-3H))^*
=0,
$$
because $H$ is ample. Also
$$
H^1(X,\OO_X(2H))
\cong
H^1(X,\OO_X(-3H))^*
=0
$$
by [[P-AGH5412KODAIRAVANISH|Exercise V.4.12]], applied to the ample divisor
$3H$. Thus $h^0(X,\OO_X(2H))=\chi(\OO_X(2H))=13$.
:::

<1>6. At least two linearly independent quadric hypersurfaces of $\PP^4$
contain $X$.

::: {.proof}
The anticanonical embedding satisfies
$$
\OO_X(1)=\OO_X(H),
$$
so restriction of quadratic forms gives a linear map
$$
H^0(\PP^4,\OO_{\PP^4}(2))
\longrightarrow
H^0(X,\OO_X(2H)).
$$
The source has dimension
$$
\binom{4+2}{2}=15,
$$
whereas step <1>5 gives dimension $13$ for the target. Hence the kernel has
dimension at least two. Choose linearly independent quadrics
$$
Q_1,Q_2
$$
from this kernel. Then
$$
X\subseteq Q_1\cap Q_2.
$$
:::

<1>7. The quadrics $Q_1$ and $Q_2$ have no common hypersurface component.

::: {.proof}
If two independent quadrics in $\PP^4$ have a common hypersurface component,
that component is a hyperplane: their equations have a common linear factor.
Thus their intersection is the union of that hyperplane and a codimension-two
linear space. Since the irreducible surface $X$ is contained in this union, it
would be contained in one of those two linear subspaces. This is impossible:
the complete anticanonical linear system embeds $X$ nondegenerately in
$\PP^4$. Hence $Q_1,Q_2$ form a regular sequence and their intersection is a
pure surface complete intersection.
:::

<1>8. One has
$$
\boxed{X=Q_1\cap Q_2}
$$
scheme-theoretically.

::: {.proof}
By step <1>7, the complete intersection
$$
Y=Q_1\cap Q_2
$$
is a pure two-dimensional scheme of degree
$$
\deg Y=2\cdot2=4.
$$
On the other hand, the degree of the anticanonically embedded surface is
$$
\deg X=H^2=4.
$$
Step <1>6 gives $X\subseteq Y$. Since $Y$ is pure of the same dimension as
the irreducible reduced surface $X$, the component of $Y$ supported on $X$
already contributes at least $\deg X=4$ to the degree of $Y$. Equality of the
degrees leaves neither another two-dimensional component nor a nonreduced
multiplicity along $X$. Thus $Y=X$ as schemes.

Therefore $X$ is the complete intersection of two quadric hypersurfaces in
$\PP^4$, proving part (b).
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>4 proves part (a), and steps <1>5--<1>8 prove part (b).
:::
:::
