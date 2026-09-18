---
schema: qual/card@1
id: P-AGH446HYPEROSCULATIONPOINTS
kind: problem
title: Counting inflection and hyperosculation points, and the $d^2$ points of order $d$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Hurwitz
  - Genus
  - Elliptic Curves
  - Embeddings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.6 together with the ramification calculation in
    IV.2.3. The proof packages Hurwitz and the requested induction as the
    characteristic-zero Wronskian formula for a g^n_d, then applies the
    complete linear series |dP_0| on an elliptic curve.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
a. Let $X$ be a curve of genus $g$ embedded birationally in $\PP^2$ as a curve of degree $d$ with $r$ nodes. Generalize the method of (Ex. 2.3) to show that $X$ has
$$
6(g-1)+ 3d
$$
inflection points. A node does not count as an inflection point. Assume $\characteristic k=0$.

b. Now let $X$ be a curve of genus $g$ embedded as a curve of degree $d$ in $\PP^n$, $n \geq 3$, not contained in any $\PP^{n-1}$. For each point $P \in X$, there is a hyperplane $H$ containing $P$, such that $P$ counts at least $n$ times in the intersection $H \intersect X$. This is called an **osculating** hyperplane at $P$. It generalizes the notion of tangent line for curves in $\PP^2$.

    If $P$ counts at least $n+1$ times in $H \intersect X$, we say $H$ is a **hyperosculating hyperplane**, and that $P$ is a **hyperosculation point**. Use Hurwitz's theorem as above, and induction on $n$, to show that $X$ has
$$
n(n+1)(g-1)+(n+1) d
$$
hyperosculation points.

c. If $X$ is an elliptic curve, for any $d \geq 3$, embed $X$ as a curve of degree $d$ in $\PP^{d-1}$, and conclude that $X$ has exactly $d^2$ points of order $d$ in its group law.
:::

::: {.solution}
We count inflection and hyperosculation points with their natural
ramification weights.  The characteristic-zero hypothesis is used in the
Wronskian calculation below.

<1>1. Let $L$ be a line bundle of degree $d$ on a smooth curve $X$ of genus
$g$, and let
$$
V\subseteq H^0(X,L),
\qquad
\dim V=n+1,
$$
be a base-point-free linear series.  Its ramification divisor has degree
$$
\boxed{
(n+1)d+n(n+1)(g-1).
}
$$

::: {.proof}
Fix a point $P\in X$, a local parameter $t$, and a local frame of $L$.
Write a basis of $V$ locally as functions
$$
f_0,\ldots,f_n.
$$
In characteristic zero form the Wronskian
$$
W
=
\det\left(
\frac{1}{i!}\frac{d^i f_j}{dt^i}
\right)_{0\leq i,j\leq n}.
$$
Under a change of local frame of $L$ the determinant transforms by the
inverse $(n+1)$st power of the transition function, and under a change of
parameter it transforms by the inverse
$$
1+2+\cdots+n
=
\frac{n(n+1)}2
$$
power of the canonical transition function.  Hence the local Wronskians
glue to a global section of
$$
L^{\otimes(n+1)}
\otimes
\omega_X^{\otimes n(n+1)/2}.
$$
Its zero divisor therefore has degree
$$
\begin{aligned}
(n+1)\deg L
&+
\frac{n(n+1)}2\deg\omega_X\\
&=(n+1)d
+n(n+1)(g-1).
\end{aligned}
$$

To identify the zero order, choose a basis adapted to $P$ with strictly
increasing vanishing orders
$$
0\leq a_0(P)<a_1(P)<\cdots<a_n(P).
$$
The lowest term of the determinant is a nonzero Vandermonde multiple of
$$
t^{\sum_i(a_i(P)-i)},
$$
so
$$
\operatorname{ord}_P(W)
=
\sum_{i=0}^n(a_i(P)-i).
$$
This is the usual ramification weight.

For $n=1$ this is precisely the ramification divisor in
Riemann--Hurwitz.  Passing from order $n-1$ jets to order $n$ jets adds the
line bundle
$$
L\otimes\omega_X^{\otimes n},
$$
whose degree is $d+n(2g-2)$; thus the displayed formula is also exactly the
induction on $n$ requested in the exercise.
:::

<1>2. For a nondegenerate map to $\PP^n$, a point is a
hyperosculation point exactly when the Wronskian of step <1>1 vanishes there.

::: {.proof}
The hyperplanes in $\PP^n$ correspond to the sections in $V$.
At $P$, the largest possible order of contact of a hyperplane section is
$$
a_n(P).
$$
Because the $a_i(P)$ are distinct nonnegative integers,
$$
a_i(P)\geq i.
$$
Thus an osculating hyperplane has contact at least $n$, and
hyperosculation occurs exactly when
$$
a_n(P)\geq n+1.
$$
This happens if and only if some $a_i(P)>i$, which by step <1>1 is equivalent
to
$$
\operatorname{ord}_P(W)>0.
$$
Its natural multiplicity as a hyperosculation point is the ramification
weight
$$
\sum_i(a_i(P)-i).
$$
:::

<1>3. In part (a), the total inflection weight is
$$
\boxed{
6(g-1)+3d.
}
$$

::: {.proof}
Let
$$
\nu:X\longrightarrow C\subseteq\PP^2
$$
be the normalization of the nodal plane model, and put
$$
L=\nu^*\OO_C(1).
$$
Then
$$
\deg L=d,
$$
and the three coordinate linear forms give a base-point-free
$g^2_d$ on $X$.  Apply step <1>1 with $n=2$:
$$
\deg R_V
=
3d+6(g-1).
$$

At a point whose branch in the plane has tangent-contact order $m\geq2$,
the vanishing sequence of this $g^2_d$ is
$$
0,1,m.
$$
Its ramification weight is therefore
$$
m-2,
$$
which is exactly the usual inflection multiplicity.  In particular an
ordinary node contributes no inflection merely by being a node: each branch
has the generic initial vanishing $0,1,2$ unless it has additional tangent
contact, and only such excess contact contributes.

Thus the ramification divisor is precisely the properly counted inflection
divisor, and its degree is
$$
6(g-1)+3d.
$$
Using
$$
g=\frac{(d-1)(d-2)}2-r,
$$
the same number is
$$
3d(d-2)-6r.
$$
:::

<1>4. In part (b), the total hyperosculation weight is
$$
\boxed{
n(n+1)(g-1)+(n+1)d.
}
$$

::: {.proof}
Take
$$
L=\OO_X(1),
$$
so $\deg L=d$, and let $V$ be the $(n+1)$-dimensional space obtained by
restricting hyperplanes of $\PP^n$ to $X$.  Nondegeneracy means this series
has projective dimension $n$.

By step <1>2 its ramification divisor is exactly the hyperosculation divisor,
with the proper weights.  Step <1>1 gives its degree as
$$
(n+1)d+n(n+1)(g-1),
$$
which is the required formula.
:::

<1>5. For the elliptic curve in part (c), the complete linear system
$$
\abs{dP_0}
$$
embeds $X$ in $\PP^{d-1}$ as a curve of degree $d$.

::: {.proof}
Put
$$
L=\OO_X(dP_0).
$$
Since $g(X)=1$ and $\deg L=d>0$, Riemann--Roch gives
$$
h^0(X,L)=d.
$$
For any $P,Q\in X$, allowing $P=Q$, Riemann--Roch also gives
$$
h^0(X,L(-P))=d-1,
\qquad
h^0(X,L(-P-Q))=d-2,
$$
because both line bundles have positive degree.  Thus sections of $L$
separate distinct points, and taking $Q=P$ shows that they also separate
tangent directions.  Hence $L$ is very ample, so the complete linear system
gives a closed immersion
$$
X\hookrightarrow\PP H^0(X,L)^*
=
\PP^{d-1}.
$$
The pullback of a hyperplane is $L$, hence the embedded curve has degree
$$
\deg L=d.
$$
:::

<1>6. A point $P\in X$ is a hyperosculation point for the embedding of step
<1>5 if and only if
$$
\boxed{d(P-P_0)=0}
$$
in the elliptic-curve group law.

::: {.proof}
Here
$$
n=d-1.
$$
A hyperosculating hyperplane has contact at least
$$
n+1=d
$$
at $P$.  Since a hyperplane section has total degree $d$, this means its
intersection divisor is exactly
$$
dP.
$$
Such a hyperplane exists if and only if
$$
dP\sim dP_0.
$$
Under
$$
X\cong\Pic^0(X),
\qquad
Q\longmapsto[Q-P_0],
$$
this is equivalent to
$$
d(P-P_0)=0.
$$
:::

<1>7. Every point satisfying $d(P-P_0)=0$ has hyperosculation weight exactly
$1$.

::: {.proof}
For
$$
0\leq m\leq d-1,
$$
the line bundle
$$
L(-mP)
$$
has positive degree $d-m$, so Riemann--Roch on the elliptic curve gives
$$
h^0(X,L(-mP))=d-m.
$$

If $d(P-P_0)=0$, then
$$
L(-dP)\cong\OO_X,
$$
so
$$
h^0(X,L(-dP))=1,
\qquad
h^0(X,L(-(d+1)P))=0.
$$
Therefore the vanishing sequence at $P$ is
$$
0,1,\ldots,d-2,d.
$$
Its ramification weight is
$$
d-(d-1)=1.
$$

If $d(P-P_0)\ne0$, then the degree-zero line bundle $L(-dP)$ is nontrivial,
so it has no nonzero global section.  The vanishing sequence is then
$$
0,1,\ldots,d-1,
$$
and the weight is $0$.
:::

<1>8. In characteristic zero, the subgroup of points killed by $d$ has
exactly
$$
\boxed{d^2}
$$
elements.

::: {.proof}
Apply step <1>4 with
$$
g=1,
\qquad
n=d-1,
\qquad
\deg X=d.
$$
The total hyperosculation weight is
$$
n(n+1)(g-1)+(n+1)d
=
0+d^2
=
d^2.
$$
By steps <1>6--<1>7 the hyperosculation divisor is reduced and its support is
exactly
$$
X[d](k)
=
\{P\in X(k):d(P-P_0)=0\}.
$$
Hence this set has exactly $d^2$ points.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>3 proves part (a), step <1>4 proves part (b), and steps
<1>5--<1>8 prove part (c).
:::
:::

::: {.remark title="Meaning of points of order d"}
The $d^2$ points in part (c) are the points **annihilated by $d$**, i.e. the
$d$-torsion subgroup $X[d](k)$.  The phrase "points of order $d$" in the
source cannot mean points of exact group-theoretic order $d$: for example,
$P_0$ is among these $d^2$ points but has order $1$.
:::

::: {.remark title="Characteristic scope"}
The counting argument above uses the characteristic-zero hypothesis.
More generally, if $\characteristic k$ does not divide $d$, the multiplication
map $[d]$ is separable of degree $d^2$, so $X[d](k)$ again has $d^2$ points.
If $\characteristic k=p$ divides $d$, the finite group scheme $X[d]$ still
has degree $d^2$, but its set of geometric points can have fewer than $d^2$
elements.  Thus the literal point-count conclusion requires characteristic
zero, or at least $\characteristic k\nmid d$.
:::
