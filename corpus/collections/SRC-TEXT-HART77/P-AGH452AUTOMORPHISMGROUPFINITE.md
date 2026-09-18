---
schema: qual/card@1
id: P-AGH452AUTOMORPHISMGROUPFINITE
kind: problem
title: $\Aut X$ is finite for a curve of genus $\geq 2$ in characteristic $0$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Canonical Divisor
  - Hyperelliptic Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.5.2 together with IV.1.7, IV.4.6, and the cited
    Hurwitz exercise IV.2.5. Cross-checked the fixed-point bound via the
    Riemann--Roch argument and the characteristic-zero Weierstrass divisor
    degree and maximal-weight bound.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
If $X$ is a curve of genus $\geq 2$ over a field of characteristic 0, show that the group $\Aut X$ of automorphisms of $X$ is finite.

Hint: If $X$ is hyperelliptic, use the unique $g_2^1$ and show that $\Aut X$ permutes the ramification points of the 2-fold covering $X \to \PP^1$.
If $X$ is not hyperelliptic, show that $\Aut X$ permutes the hyperosculation points (Ex.
4.6) of the canonical embedding.
Cf.
(Ex.
2.5).
:::

::: {.solution}
It is enough to prove finiteness after extending the ground field to an
algebraic closure: base change preserves the genus and gives an injection
$$
\Aut_k(X)\hookrightarrow\Aut_{\bar k}(X_{\bar k}).
$$
Thus assume from now on that $k$ is algebraically closed of characteristic
$0$.

<1>1. A nonidentity automorphism of a genus-$g$ curve fixes at most
$$
\boxed{2g+2}
$$
points.

::: {.proof}
Let
$$
1\ne\sigma\in\Aut X.
$$
Choose $P\in X$ with $\sigma(P)\ne P$.  Riemann--Roch gives
$$
\ell((g+1)P)
\ge
(g+1)+1-g
=2,
$$
so there is a nonconstant function
$$
h\in L((g+1)P).
$$
Its only possible pole is $P$, of order at most $g+1$; since $X$ is
projective and $h$ is nonconstant, it actually has a pole there.

Put
$$
u=h-\sigma^*h.
$$
The poles of $\sigma^*h$ are supported at $\sigma^{-1}(P)$, which is
different from $P$.  Hence $u\ne0$, and
$$
\deg(u)_\infty\le2g+2.
$$
If $Q$ is fixed by $\sigma$, then $Q$ is neither $P$ nor
$\sigma^{-1}(P)$ and
$$
u(Q)
=
h(Q)-h(\sigma(Q))
=0.
$$
Thus every fixed point is a zero of $u$.  A nonzero rational function has
zero divisor and pole divisor of the same degree, so $\sigma$ has at most
$2g+2$ fixed points.
:::

<1>2. If $X$ is hyperelliptic, then $\Aut X$ is finite.

::: {.proof}
Choose the hyperelliptic map
$$
f:X\longrightarrow\PP^1,
\qquad
\deg f=2.
$$
The $g^1_2$ is unique.  Indeed, if
$$
f,h:X\longrightarrow\PP^1
$$
were two degree-$2$ maps defining distinct pencils, consider
$$
(f,h):X\longrightarrow\PP^1\times\PP^1
$$
and let $\delta$ be its generic degree onto its image.  Since $\delta$
divides the degrees of both projections, $\delta$ is $1$ or $2$.  If
$\delta=2$, then both projections from the image have degree $1$, so the
image is a curve of bidegree $(1,1)$ and the two maps differ only by an
automorphism of $\PP^1$.  That would give the same pencil.  Thus distinct
pencils force $\delta=1$.

The product map is therefore birational onto a curve of bidegree $(2,2)$.
Such a curve has
arithmetic genus
$$
(2-1)(2-1)=1,
$$
so its normalization would have genus at most $1$, contrary to $g\ge2$.

Therefore every $\sigma\in\Aut X$ induces a unique
$$
\bar\sigma\in\Aut\PP^1
$$
such that
$$
f\circ\sigma=\bar\sigma\circ f.
$$
Riemann--Hurwitz gives
$$
2g-2
=
2(-2)+\deg R_f,
$$
so
$$
\deg R_f=2g+2.
$$
In characteristic $0$ the quadratic cover is separable and every ramification
index is $2$; hence it has $2g+2$ distinct branch points on $\PP^1$.
The automorphism $\bar\sigma$ permutes this finite branch set.

The subgroup of $\PGL_2(k)$ preserving a set of at least three points is
finite: its action on that set is faithful because an automorphism of
$\PP^1$ fixing three distinct points is the identity.  The kernel of
$$
\Aut X\longrightarrow\PGL_2(k)
$$
consists of automorphisms of the separable quadratic extension
$$
k(X)/k(\PP^1),
$$
so it has order at most $2$.  Hence $\Aut X$ is finite.
:::

<1>3. Suppose now that $X$ is not hyperelliptic.  The canonical system
embeds
$$
X\hookrightarrow\PP^{g-1}
$$
as a curve of degree $2g-2$, and its hyperosculation divisor $W$ has degree
$$
\boxed{\deg W=g^3-g.}
$$

::: {.proof}
A nonhyperelliptic curve of genus $g\ge2$ has very ample canonical bundle,
so the complete canonical system gives the stated embedding.  Here
$$
n=g-1,
\qquad
d=\deg K=2g-2.
$$
Applying [[P-AGH446HYPEROSCULATIONPOINTS|Exercise IV.4.6(b)]] gives
$$
\begin{aligned}
\deg W
&=
n(n+1)(g-1)+(n+1)d\\
&=
(g-1)g(g-1)+g(2g-2)\\
&=
g(g-1)(g+1)\\
&=
g^3-g.
\end{aligned}
$$
:::

<1>4. At every point $P\in X$, its canonical hyperosculation weight
$w(P)$ satisfies
$$
w(P)\le\frac{g(g-1)}2,
$$
and equality would force $X$ to be hyperelliptic.  Hence in the present
case
$$
\boxed{
w(P)\le\frac{g(g-1)}2-1.
}
$$

::: {.proof}
Let
$$
1=n_1<n_2<\cdots<n_g\le2g-1
$$
be the gap sequence at $P$.  The vanishing orders of the canonical series
are
$$
n_1-1,\ldots,n_g-1,
$$
so
$$
w(P)
=
\sum_{i=1}^g(n_i-i).
$$

We claim
$$
n_i\le2i-1
$$
for every $i$.  For $i=g$ this is the usual gap bound
$n_g\le2g-1$.  If $i<g$ and $n_i\ge2i$, then among
$$
1,\ldots,2i-1
$$
there are at most $i-1$ gaps.  Thus there are at least $i$ positive
nongaps in this range, and therefore
$$
\ell((2i-1)P)\ge i+1.
$$
Riemann--Roch shows that $(2i-1)P$ is special, since
$$
\ell(K-(2i-1)P)
\ge
(i+1)-(2i-1)-1+g
=
g-i+1
>0.
$$
Clifford's theorem would then give
$$
\ell((2i-1)P)
\le
\frac{2i-1}{2}+1
<
i+1,
$$
a contradiction.

Consequently
$$
w(P)
\le
\sum_{i=1}^g((2i-1)-i)
=
\sum_{i=1}^g(i-1)
=
\frac{g(g-1)}2.
$$
If equality holds, then every inequality above is an equality, so the gap
sequence is
$$
1,3,5,\ldots,2g-1.
$$
In particular $2$ is a nongap at $P$.  Hence there is a nonconstant rational
function with pole divisor at most $2P$, giving a finite map
$$
X\longrightarrow\PP^1
$$
of degree at most $2$.  Since $g\ge2$, its degree cannot be $1$, so it has
degree $2$ and $X$ is hyperelliptic.  This is excluded, proving the strict
bound.
:::

<1>5. A nonhyperelliptic curve has more than $2g+2$ distinct
hyperosculation points.

::: {.proof}
Let
$$
S=\Supp W,
\qquad
N=\size S.
$$
By steps <1>3--<1>4,
$$
g^3-g
=
\sum_{P\in S}w(P)
\le
N\left(\frac{g(g-1)}2-1\right).
$$
Since a nonhyperelliptic curve here has $g\ge3$,
$$
\frac{g(g-1)}2-1
<
\frac{g(g-1)}2.
$$
Therefore
$$
N
>
\frac{g^3-g}{g(g-1)/2}
=
2(g+1)
=
2g+2.
$$
:::

<1>6. If $X$ is nonhyperelliptic, then $\Aut X$ is finite.

::: {.proof}
Every automorphism preserves the canonical linear system, hence preserves
its vanishing sequences and permutes the finite set $S$ of hyperosculation
points.  Thus there is a homomorphism
$$
\Aut X\longrightarrow\operatorname{Sym}(S).
$$
If an automorphism lies in the kernel, it fixes every point of $S$.  Step
<1>5 gives more than $2g+2$ such fixed points, so step <1>1 forces the
automorphism to be the identity.  Hence the homomorphism is injective.
Since $S$ is finite, so is $\operatorname{Sym}(S)$, and therefore
$\Aut X$ is finite.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>2 proves the hyperelliptic case, and steps <1>3--<1>6 prove the
nonhyperelliptic case.  These exhaust all curves of genus at least $2$.
:::
:::
