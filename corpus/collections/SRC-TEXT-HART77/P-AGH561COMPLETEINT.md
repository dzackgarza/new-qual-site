---
schema: qual/card@1
id: P-AGH561COMPLETEINT
kind: problem
title: Complete intersection surfaces are of general type with finitely many exceptions
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Canonical Divisor
  - Adjunction
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the current Hartshorne V.6.1 transcription and collection context,
    together with the complete-intersection adjunction formula recorded from
    Hartshorne II.8.4 in P-AGH284COMPINT and the complete-intersection
    cohomology vanishing recorded from Hartshorne III.5 in P-AGH355COMPINT.
    The retained Hartshorne solution attachment ends before Chapter V, and
    the separate AG Solutions extraction is unreadable, so there is no usable
    retained V.6.1 source solution to incorporate. The proof below is an
    independent computation in the nonsingular surface-classification setting
    of the exercise.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Recomputed a=sum d_i-n-1 from adjunction and independently enumerated
    every tuple with a<=0 from 2(n-2)<=sum d_i<=n+1. Checked the three
    negative cases have K^2 equal to 8, 3, and 4 and hence are the stated
    del Pezzo surfaces. Checked the three zero cases have trivial canonical
    bundle and H^1(O_X)=0 by the complete-intersection cohomology result,
    hence are K3 surfaces of polarization degrees 4, 6, and 8.
---

::: {.problem}
Let $X$ be a surface in $\PP^n$, $n \geqslant 3$, defined as the complete intersection of hypersurfaces of degrees $d_1, \ldots, d_{n-2}$, with each $d_i \geqslant 2$.
Show that for all but finitely many choices of $\left(n, d_1, \ldots, d_{n-2}\right)$, the surface $X$ is of general type.
List the exceptional cases, and where they fit into the classification picture.
:::

::: {.solution}
Write
$$
H=\OO_X(1)
$$
for the hyperplane class and put
$$
a=\sum_{i=1}^{n-2}d_i-n-1.
$$

<1>1. The canonical class of $X$ is
$$
\boxed{K_X\sim aH}.
$$

::: {.proof}
For a nonsingular complete intersection of hypersurfaces of degrees
$d_1,\ldots,d_{n-2}$ in $\PP^n$, the adjunction formula
[[P-AGH284COMPINT]] gives
$$
\omega_X
\cong
\OO_X\left(\sum_{i=1}^{n-2}d_i-n-1\right).
$$
With the notation fixed above, this is
$$
\omega_X\cong\OO_X(a),
$$
or equivalently
$$
K_X\sim aH.
$$
:::

<1>2. If $a>0$, then $X$ is of general type.

::: {.proof}
The hyperplane class $H$ is ample on $X$. Hence for $a>0$ the canonical
divisor
$$
K_X\sim aH
$$
is ample. Every ample divisor is big, so $K_X$ is big. Therefore $X$ is
of general type.
:::

<1>3. If $X$ is not covered by step <1>2, then, up to permuting the
$d_i$, its degree data are exactly
$$
\boxed{
\left\{
(3;2),\,
(3;3),\,
(3;4),\,
(4;2,2),\,
(4;2,3),\,
(5;2,2,2)
\right\}.
}
$$

::: {.proof}
The exceptional condition is
$$
a\le0,
$$
equivalently
$$
\sum_{i=1}^{n-2}d_i\le n+1.
$$
Since every $d_i\ge2$ and there are $n-2$ of them,
$$
\sum_{i=1}^{n-2}d_i\ge2(n-2)=2n-4.
$$
Thus an exceptional tuple must satisfy
$$
2n-4\le n+1,
$$
so
$$
n\le5.
$$

For $n=3$ there is one degree $d_1\ge2$, and
$$
d_1\le4,
$$
giving
$$
d_1=2,3,4.
$$

For $n=4$ there are two degrees at least $2$ with
$$
d_1+d_2\le5.
$$
Up to order, the only possibilities are
$$
(d_1,d_2)=(2,2),(2,3).
$$

For $n=5$ there are three degrees at least $2$ with
$$
d_1+d_2+d_3\le6,
$$
so necessarily
$$
(d_1,d_2,d_3)=(2,2,2).
$$
There are no possibilities for $n\ge6$.
:::

<1>4. The three exceptional tuples with $a<0$ are del Pezzo surfaces:
$$
\begin{array}{c|c|c|c}
(n;d_i) & K_X & K_X^2 & \text{surface}\\
\hline
(3;2) & -2H & 8 & \text{quadric surface}\\
(3;3) & -H & 3 & \text{cubic surface}\\
(4;2,2) & -H & 4 & \text{intersection of two quadrics}.
\end{array}
$$

::: {.proof}
For each of these tuples step <1>1 gives $-K_X$ as a positive multiple
of the ample hyperplane class. Hence $-K_X$ is ample, so $X$ is a del
Pezzo surface.

For a complete-intersection surface,
$$
H^2=\deg X=\prod_i d_i.
$$
Consequently
$$
K_X^2=a^2H^2.
$$
For the quadric in $\PP^3$, one has $a=-2$ and $H^2=2$, so
$$
K_X^2=8.
$$
For the cubic in $\PP^3$, one has $a=-1$ and $H^2=3$, so
$$
K_X^2=3.
$$
For the $(2,2)$ complete intersection in $\PP^4$, one has $a=-1$ and
$H^2=4$, so
$$
K_X^2=4.
$$

Thus these are the del Pezzo surfaces of degrees $8$, $3$, and $4$,
respectively. Over the algebraically closed ground field, the smooth
quadric is $\PP^1\times\PP^1$, while the cubic surface and the degree-$4$
del Pezzo surface are the familiar rational del Pezzo surfaces. Hence
these cases lie in the $\kappa=-\infty$ part of the surface
classification.
:::

<1>5. The three exceptional tuples with $a=0$ are K3 surfaces:
$$
\begin{array}{c|c}
(n;d_i) & H^2\\
\hline
(3;4) & 4\\
(4;2,3) & 6\\
(5;2,2,2) & 8.
\end{array}
$$

::: {.proof}
For these three tuples,
$$
\sum_i d_i=n+1,
$$
so step <1>1 gives
$$
\omega_X\cong\OO_X.
$$

The complete-intersection cohomology calculation
[[P-AGH355COMPINT]] applies to a surface and gives
$$
H^1(X,\OO_X)=0.
$$
It also gives
$$
H^0(X,\OO_X)=k.
$$
Hence
$$
q(X)=0
$$
and, since $\omega_X\cong\OO_X$,
$$
p_g(X)
=
h^0(X,\omega_X)
=
h^0(X,\OO_X)
=1.
$$
Thus these are K3 surfaces in the surface-classification picture, and
they lie in the $\kappa=0$ class.

Their indicated polarization degrees are simply
$$
H^2=\deg X=\prod_i d_i,
$$
namely $4$, $6$, and $8$.
:::

<1>6. All other degree data give surfaces of general type, while the six
tuples in step <1>3 are precisely the del Pezzo and K3 exceptions listed
in steps <1>4 and <1>5.

::: {.proof}
Step <1>3 exhausts every tuple for which $a\le0$. Therefore every tuple
not in that list has $a>0$, and step <1>2 makes $X$ of general type.
Among the six exceptions, step <1>4 classifies the three cases with
$a<0$, and step <1>5 classifies the three cases with $a=0$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>1 computes the canonical class. Steps <1>2--<1>3 reduce the
problem to exactly six exceptional degree patterns. Steps <1>4--<1>5
place those exceptions in the del Pezzo and K3 parts of the surface
classification, and step <1>6 proves that every remaining case is of
general type.
:::
:::
