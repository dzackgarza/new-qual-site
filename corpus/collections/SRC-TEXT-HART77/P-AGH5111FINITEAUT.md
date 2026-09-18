---
schema: qual/card@1
id: P-AGH5111FINITEAUT
kind: problem
title: Finiteness of effective classes of fixed degree, and finiteness of the automorphism group of a curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Intersection Theory
  - Adjunction
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.1.11, the retained Egbert companion sketch, and the local
    Hodge-index, Nakai--Moishezon, adjunction, and diagonal calculations. The
    companion sketch does not supply the required boundedness argument in
    Num(X). The proof below decomposes numerical classes into the ample
    direction and its negative-definite orthogonal complement; adjunction makes
    the orthogonal component of every irreducible curve of bounded H-degree
    uniformly bounded, after which lattice discreteness and the bounded number
    of effective components give finiteness.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
In this problem, we assume that $X$ is a surface for which $\Num X$ is finitely generated (i.e., any surface, if you accept the Néron-Severi theorem (Ex.
1.7)).

a. If $H$ is an ample divisor on $X$, and $d \in \ZZ$, show that the set of effective divisors $D$ with $D . H=d$, modulo numerical equivalence, is a finite set.

Hint: Use the adjunction formula, the fact that $p_a$ of an irreducible curve is $\geqslant 0$, and the fact that the intersection pairing is negative definite on $H^{\perp}$ in $\Num X$.

b. Now let $C$ be a curve of genus $g \geqslant 2$, and use (a) to show that the group of automorphisms of $C$ is finite, as follows.
Given an automorphism $\sigma$ of $C$, let $\Gamma \subseteq X=C \times C$ be its graph.
First show that if $\Gamma \equiv \Delta$, then $\Gamma=\Delta$, using the fact that $\Delta^2<0$, since $g \geqslant 2$ (Ex.
1.6). Then use (a). Cf.
(V, Ex.
2.5).
:::

::: {.solution}
Let
$$
N=\Num X,
\qquad
N_\RR=N\tensor_\ZZ\RR.
$$
Since $N$ is finitely generated and numerical equivalence has no torsion,
$N$ is a lattice in the finite-dimensional real vector space $N_\RR$.

<1>1. The intersection form is negative definite on
$$
H^\perp=\{v\in N_\RR:v\cdot H=0\},
$$
and
$$
N_\RR=\RR H\oplus H^\perp.
$$

::: {.proof}
The Hodge index theorem [[T-SRFHODGE]] says that every nonzero class in
$H^\perp$ has negative square. Thus the restriction of the intersection form
to $H^\perp$ is negative definite. Since $H^2>0$ by the Nakai--Moishezon
criterion [[T-SRFNAKAI]], the line $\RR H$ meets $H^\perp$ trivially, and every
$v\in N_\RR$ decomposes uniquely as
$$
v=\frac{v\cdot H}{H^2}H+
\left(v-\frac{v\cdot H}{H^2}H\right).
$$
The second summand is orthogonal to $H$.
:::

<1>2. Put
$$
K_X=\frac{K_X\cdot H}{H^2}H+z,
\qquad z\in H^\perp,
$$
and define the positive-definite norm on $H^\perp$ by
$$
\|v\|^2=-v^2.
$$
If $C$ is an irreducible curve and $h=C\cdot H$, writing
$$
C=\frac h{H^2}H+y,
\qquad y\in H^\perp,
$$
gives
$$
\|y\|^2
\leq
2+\frac{h^2+h(K_X\cdot H)}{H^2}+\|z\|\,\|y\|.
$$

::: {.proof}
Adjunction gives
$$
2p_a(C)-2=C^2+K_X\cdot C.
$$
Since $C$ is an integral projective curve, $p_a(C)\geq0$, hence
$$
C^2+K_X\cdot C\geq-2.
$$
Using the orthogonal decompositions in step <1>2,
$$
C^2=\frac{h^2}{H^2}-\|y\|^2
$$
and
$$
K_X\cdot C
=
\frac{h(K_X\cdot H)}{H^2}+z\cdot y.
$$
Therefore
$$
\|y\|^2
\leq
2+\frac{h^2+h(K_X\cdot H)}{H^2}+z\cdot y.
$$
The positive-definite inner product
$$
(u,v)_+=-u\cdot v
$$
on $H^\perp$ satisfies Cauchy--Schwarz, so
$$
z\cdot y\leq|z\cdot y|\leq\|z\|\,\|y\|.
$$
Substitution proves the displayed estimate.
:::

<1>3. For each integer $d\geq1$, the numerical classes of irreducible curves
$C$ satisfying
$$
1\leq C\cdot H\leq d
$$
form a finite set.

::: {.proof}
For such a curve, the integer
$$
h=C\cdot H
$$
belongs to the finite set $\{1,\ldots,d\}$. In step <1>2 the quantity
$$
A_h=2+\frac{h^2+h(K_X\cdot H)}{H^2}
$$
therefore ranges over a finite set of real numbers. If $t=\|y\|$, the estimate
of step <1>2 is
$$
t^2-\|z\|t\leq A_h.
$$
The left side tends to $+\infty$ as $t\to+\infty$. Hence there is a constant
$R_d$ such that every such curve has
$$
\|y\|\leq R_d.
$$
Its coefficient $h/H^2$ in the $H$-direction is also bounded because
$1\leq h\leq d$. Thus all these classes lie in a bounded subset of $N_\RR$.
The lattice $N\subseteq N_\RR$ is discrete, so a bounded subset contains only
finitely many lattice points. This proves the claim.
:::

<1>4. If $d<0$, there is no effective divisor $D$ with $D\cdot H=d$; if
$d=0$, the only such effective divisor is $D=0$.

::: {.proof}
Write a nonzero effective divisor as
$$
D=\sum_i n_iC_i,
\qquad n_i>0,
$$
with distinct irreducible curves $C_i$. Ampleness gives
$$
H\cdot C_i>0
$$
for every $i$ by Nakai--Moishezon. These intersection numbers are positive
integers, so
$$
D\cdot H=\sum_i n_i(H\cdot C_i)>0.
$$
The assertions follow.
:::

<1>5. For every integer $d>0$, only finitely many numerical classes of
effective divisors satisfy $D\cdot H=d$.

::: {.proof}
Write
$$
D=\sum_i n_iC_i
$$
as in step <1>4. Then
$$
d=D\cdot H=\sum_i n_i(C_i\cdot H).
$$
Consequently every component satisfies
$$
1\leq C_i\cdot H\leq d,
$$
so by step <1>3 its numerical class belongs to a fixed finite set $S_d$.
Moreover,
$$
\sum_i n_i\leq d
$$
because every $C_i\cdot H$ is at least one. Hence $[D]$ is a sum of at most
$d$ elements of the finite set $S_d$, counted with repetition. There are only
finitely many such sums in the abelian group $N$. Together with step <1>4,
this proves part (a) for every integer $d$.
:::

<1>6. Let $C$ have genus $g\geq2$, let $X=C\times C$, and let
$\Gamma_\sigma$ be the graph of an automorphism $\sigma$ of $C$. Then
$$
\Gamma_\sigma^2=\Delta^2=2-2g<0.
$$

::: {.proof}
The graph embedding has normal bundle $\sigma^*T_C$: for a graph of a morphism
$u:C\to C$, the normal sequence identifies the quotient of
$T_C\oplus u^*T_C$ by the graph of $du$ with $u^*T_C$. Since $\sigma$ is an
automorphism,
$$
\deg\sigma^*T_C=\deg T_C=2-2g.
$$
The self-intersection of a smooth curve on a smooth surface is the degree of
its normal bundle. Thus $\Gamma_\sigma^2=2-2g$. The equality
$\Delta^2=2-2g$ is Exercise V.1.6, [[P-AGH516DIAGONAL]].
:::

<1>7. If
$$
\Gamma_\sigma\equiv\Delta,
$$
then
$$
\Gamma_\sigma=\Delta
$$
and therefore $\sigma=\id_C$.

::: {.proof}
Numerical equivalence would give
$$
\Gamma_\sigma\cdot\Delta=\Delta^2=2-2g<0.
$$
If the two irreducible curves $\Gamma_\sigma$ and $\Delta$ were distinct,
their intersection number would be a sum of nonnegative local intersection
multiplicities, hence would be nonnegative. This contradiction shows
$$
\Gamma_\sigma=\Delta.
$$
Equality of the two graphs means $\sigma(P)=P$ for every $P$, so
$\sigma=\id_C$.
:::

<1>8. Distinct automorphisms of $C$ have numerically inequivalent graphs.

::: {.proof}
Suppose
$$
\Gamma_\sigma\equiv\Gamma_\tau.
$$
The surface automorphism
$$
\id_C\times\tau^{-1}:C\times C\longrightarrow C\times C
$$
preserves intersection numbers and therefore numerical equivalence. It sends
$\Gamma_\tau$ to $\Delta$ and $\Gamma_\sigma$ to
$\Gamma_{\tau^{-1}\circ\sigma}$. Hence
$$
\Gamma_{\tau^{-1}\circ\sigma}\equiv\Delta.
$$
Step <1>7 gives $\tau^{-1}\circ\sigma=\id_C$, so $\sigma=\tau$.
:::

<1>9. Every graph $\Gamma_\sigma$ has
$$
\Gamma_\sigma\cdot(l+m)=2,
$$
where
$$
l=C\times\{P\},
\qquad
m=\{P\}\times C.
$$

::: {.proof}
The graph of an automorphism meets $m$ once because fixing its first coordinate
determines a unique point of the graph. It meets $l$ once because
$\sigma^{-1}(P)$ is a single point and an automorphism has degree one. Thus
$$
\Gamma_\sigma\cdot l
=
\Gamma_\sigma\cdot m
=1.
$$
Exercise V.1.9, [[P-AGH519HODGEINDEX]], proves that $l+m$ is ample. The
displayed equality follows.
:::

<1>10. The automorphism group of $C$ is finite:
$$
\boxed{|\Aut C|<\infty}.
$$

::: {.proof}
By step <1>9, all graph divisors are effective and have fixed intersection
degree two with the ample divisor $l+m$. Part (a), proved in steps
<1>1--<1>5, says that only finitely many numerical equivalence classes of such
effective divisors exist. Step <1>8 says the map
$$
\Aut C\longrightarrow\Num(C\times C),
\qquad
\sigma\longmapsto[\Gamma_\sigma]
$$
is injective. Hence $\Aut C$ is finite, proving part (b).
:::

<1>11. Q.E.D.

::: {.proof}
Steps <1>1--<1>5 prove part (a), and steps <1>6--<1>10 prove part (b).
:::
:::
