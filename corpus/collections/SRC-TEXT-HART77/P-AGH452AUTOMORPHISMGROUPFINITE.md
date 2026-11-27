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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 4.5.2, printed p. 95,
    rendered as page images from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne IV.5.2, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed the count $n(n+1)(g-1)+(n+1)d$ of 4.4.6 at $n=g-1$, $d=2g-2$, giving $g(g-1)^2+2g(g-1)$, and checked it against $2g+2$ at $g=3$ ($24$ against $8$) and in general; and checked that the hyperelliptic involution achieves the Lefschetz bound exactly.
    Not checked: Yang's Solutions outside printed p. 95; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The card now carries a published-solution remark naming Yang Pi-Yeh's
    Solution 4.5.2 at printed p. 95; it had none before. No
    step, statement or hypothesis of the card changes.
- event: source-corrected
  by: chatgpt
  date: 2026-11-27
  note: >-
    Re-read Hartshorne, Exercise IV.5.2 (printed p. 348), and Yang Pi-Yeh,
    Solution 4.5.2 (printed p. 95), in their online text reproductions.
    The latter has two gaps: the hyperelliptic involution fixes every
    ramification point, and the canonical hyperosculation formula is the
    degree of a weighted divisor, not a count of distinct points. The
    existing step s2 correctly uses the quadratic function-field extension;
    steps s4 and s5 correctly prove the strict lower bound for distinct
    Weierstrass points in the nonhyperelliptic case. Step s3 now uses the
    characteristic-zero Weierstrass divisor theorem of Dembélé, Algebra &
    Number Theory 14 (2020), Theorem 2.2 (printed p. 2716), applicable also
    to genus three, where the canonical embedding is in the plane. The
    gap-sequence calculation is made explicit and the source remark no
    longer endorses either invalid inference. The prior audit is retained.
---

::: {.problem}
If $X$ is a curve of genus $\geq 2$ over a field of characteristic 0, show that the group $\Aut X$ of automorphisms of $X$ is finite.

Hint: If $X$ is hyperelliptic, use the unique $g_2^1$ and show that $\Aut X$ permutes the ramification points of the 2-fold covering $X \to \PP^1$.
If $X$ is not hyperelliptic, show that $\Aut X$ permutes the hyperosculation points (Ex. 4.6) of the canonical embedding.
Cf. (Ex. 2.5).
:::

::: {.solution}
It is enough to prove finiteness after extending the ground field to an algebraic closure: base change preserves the genus and gives an injection
$$
\Aut_k(X)\hookrightarrow\Aut_{\bar k}(X_{\bar k}).
$$
Thus assume from now on that $k$ is algebraically closed of characteristic $0$.

::: pf

::: {.pf-step #s1}

A nonidentity automorphism of a genus-$g$ curve fixes at most
$$
\boxed{2g+2}
$$
points.

::: pf-proof

Let
$$
1\ne\sigma\in\Aut X.
$$
Choose $P\in X$ with $\sigma(P)\ne P$.
Riemann--Roch gives
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
Its only possible pole is $P$, of order at most $g+1$; since $X$ is projective and $h$ is nonconstant, it actually has a pole there.

Put
$$
u=h-\sigma^*h.
$$
The poles of $\sigma^*h$ are supported at $\sigma^{-1}(P)$, which is different from $P$.
Hence $u\ne0$, and
$$
\deg(u)_\infty\le2g+2.
$$
If $Q$ is fixed by $\sigma$, then $Q$ is neither $P$ nor $\sigma^{-1}(P)$ and
$$
u(Q)
=
h(Q)-h(\sigma(Q))
=0.
$$
Thus every fixed point is a zero of $u$.
A nonzero rational function has zero divisor and pole divisor of the same degree, so $\sigma$ has at most $2g+2$ fixed points.

:::

:::

::: {.pf-step #s2}

If $X$ is hyperelliptic, then $\Aut X$ is finite.

::: pf-proof

Choose the hyperelliptic map
$$
f:X\longrightarrow\PP^1,
\qquad
\deg f=2.
$$
The $g^1_2$ is unique.
Indeed, if
$$
f,h:X\longrightarrow\PP^1
$$
were two degree-$2$ maps defining distinct pencils, consider
$$
(f,h):X\longrightarrow\PP^1\times\PP^1
$$
and let $\delta$ be its generic degree onto its image.
Since $\delta$ divides the degrees of both projections, $\delta$ is $1$ or $2$.
If $\delta=2$, then both projections from the image have degree $1$, so the image is a curve of bidegree $(1,1)$ and the two maps differ only by an automorphism of $\PP^1$.
That would give the same pencil.
Thus distinct pencils force $\delta=1$.

The product map is therefore birational onto a curve of bidegree $(2,2)$.
Such a curve has arithmetic genus
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
In characteristic $0$ the quadratic cover is separable and every ramification index is $2$; hence it has $2g+2$ distinct branch points on $\PP^1$.
The automorphism $\bar\sigma$ permutes this finite branch set.

The subgroup of $\PGL_2(k)$ preserving a set of at least three points is finite: its action on that set is faithful because an automorphism of $\PP^1$ fixing three distinct points is the identity.
The kernel of
$$
\Aut X\longrightarrow\PGL_2(k)
$$
consists of automorphisms of the separable quadratic extension
$$
k(X)/k(\PP^1),
$$
so it has order at most $2$.
Hence $\Aut X$ is finite.

:::

:::

::: {.pf-step #s3}

Suppose now that $X$ is not hyperelliptic.
The canonical system embeds
$$
X\hookrightarrow\PP^{g-1}
$$
as a curve of degree $2g-2$, and its hyperosculation divisor $W$ has degree
$$
\boxed{\deg W=g^3-g.}
$$

::: pf-proof

By Hartshorne, Proposition IV.5.2, the canonical bundle of a nonhyperelliptic curve is very ample. In the canonical embedding, hyperplane sections correspond to nonzero canonical sections, and their intersection multiplicities at $P$ are the vanishing orders of those sections. Hence a hyperosculation point is precisely a point at which some canonical section vanishes to order at least $g$, i.e. a Weierstrass point.

For the strictly increasing canonical vanishing orders $a_1,\ldots,a_g$ at $P$, write $w(P)=\sum_{i=1}^g(a_i-i+1)$ for its Weierstrass weight. The characteristic-zero Weierstrass divisor theorem (Dembélé, [*An intriguing hyperelliptic Shimura curve quotient of genus 16*](https://doi.org/10.2140/ant.2020.14.2713), Theorem 2.2) gives the effective divisor
$$
W=\sum_{P\in X}w(P)P
\sim\frac{g(g+1)}2 K.
$$
Since $\deg K=2g-2$, this gives
$$
\deg W=\frac{g(g+1)}2(2g-2)=g^3-g.
$$
In particular $W$ has finite support, and this formula counts points with their weights, not as distinct points. It applies also when $g=3$ and the canonical curve is a plane quartic.

:::

:::

::: {.pf-step #s4}

At every point $P\in X$, its canonical hyperosculation weight $w(P)$ satisfies
$$
w(P)\le\frac{g(g-1)}2,
$$
and equality would force $X$ to be hyperelliptic.
Hence in the present case
$$
\boxed{
w(P)\le\frac{g(g-1)}2-1.
}
$$

::: pf-proof

Let
$$
1=n_1<n_2<\cdots<n_g\le2g-1
$$
be the gap sequence at $P$. By Riemann--Roch, $\ell((2g-1)P)=g$, and $\ell(nP)-\ell((n-1)P)=1$ for every $n\ge2g$. Each jump in dimension is either zero or one, and $\ell(0)=1$, so there are exactly $g$ positive gaps, all at most $2g-1$. The first integer is a gap because a function with one simple pole would give a degree-one map to $\PP^1$.

Subtracting the two Riemann--Roch formulas for $nP$ and $(n-1)P$ shows that $n$ is a gap exactly when
$$
\ell(K-(n-1)P)-\ell(K-nP)=1.
$$
Thus the vanishing orders of the canonical series are
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
for every $i$.
For $i=g$ this is the usual gap bound $n_g\le2g-1$.
If $i<g$ and $n_i\ge2i$, then among
$$
1,\ldots,2i-1
$$
there are at most $i-1$ gaps.
Thus there are at least $i$ positive nongaps in this range, and therefore
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
If equality holds, then every inequality above is an equality, so the gap sequence is
$$
1,3,5,\ldots,2g-1.
$$
In particular $2$ is a nongap at $P$.
Hence there is a nonconstant rational function with pole divisor at most $2P$, giving a finite map
$$
X\longrightarrow\PP^1
$$
of degree at most $2$.
Since $g\ge2$, its degree cannot be $1$, so it has degree $2$ and $X$ is hyperelliptic.
This is excluded, proving the strict bound.

:::

:::

::: {.pf-step #s5}

A nonhyperelliptic curve has more than $2g+2$ distinct hyperosculation points.

::: pf-proof

Let
$$
S=\operatorname{Supp} W,
\qquad
N=\size S.
$$
By steps [](#s3){.pf-ref} and [](#s4){.pf-ref},
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

:::

::: {.pf-step #s6}

If $X$ is nonhyperelliptic, then $\Aut X$ is finite.

::: pf-proof

Every automorphism preserves the canonical linear system, hence preserves its vanishing sequences and permutes the finite set $S$ of hyperosculation points.
Thus there is a homomorphism
$$
\Aut X\longrightarrow\Sym(S).
$$
If an automorphism lies in the kernel, it fixes every point of $S$.
Step [](#s5){.pf-ref} gives more than $2g+2$ such fixed points, so step [](#s1){.pf-ref} forces the automorphism to be the identity.
Hence the homomorphism is injective.
Since $S$ is finite, so is $\Sym(S)$, and therefore $\Aut X$ is finite.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves the hyperelliptic case, and steps [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} prove the nonhyperelliptic case.
These exhaust all curves of genus at least $2$.

:::

:::

:::

::: {.remark title="Published solution"}
Yang Pi-Yeh, [*Hartshorne Solutions*](https://github.com/lfwin/Hartshorne-Solutions/blob/master/Hartshorne_Solution.pdf), Solution 4.5.2, separates the two cases as the hint suggests. In the hyperelliptic case, the unique degree-two pencil makes the automorphism group act on the branch points. The kernel of the action is not trivial: the hyperelliptic involution fixes all $2g+2$ ramification points. Step [](#s2){.pf-ref} supplies the missing argument: the kernel has order at most two, as it acts by automorphisms of a separable quadratic function-field extension, and the image is finite.

In the nonhyperelliptic case, the source uses the canonical embedding and a fixed-point bound. But $g^3-g$ is the total Weierstrass weight, not necessarily the number of distinct hyperosculation points. The conclusion follows only after bounding each point's weight, as in steps [](#s4){.pf-ref} and [](#s5){.pf-ref}. These show that there are strictly more than $2g+2$ distinct points, so the fixed-point argument of step [](#s1){.pf-ref} proves faithfulness. Neither case assumes the automorphism group is already finite.
:::
