---
schema: qual/card@1
id: P-HCAO26
kind: problem
title: Invariants encoded by the Hilbert polynomial
classification:
  areas:
  - algebra
  topics:
  - Hilbert Polynomials
  - Krull Dimension
  - Algebraic Geometry
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
What invariants are encoded by the Hilbert polynomial?
:::

::: {.solution}
Let $S=k[x_0,\ldots,x_n]$ be the standard graded polynomial ring over a field
$k$. For a finitely generated graded $S$-module $M$, the Hilbert function
$h_M(d)=\dim_kM_d$ agrees for all $d\gg0$ with a unique polynomial
$P_M\in\QQ[d]$, the Hilbert polynomial of $M$. For a nonempty closed subscheme
$X\subseteq\PP^n$ with saturated homogeneous ideal $I(X)$, put
$P_X=P_{S/I(X)}$ and $r=\deg P_X$.

<1>1. $\dim X=r$, equivalently $\dim S/I(X)=r+1$.

::: {.proof}
For a finitely generated graded module over $S$, the degree of the Hilbert
polynomial is one less than the Krull dimension of the module; and
$\dim X=\dim S/I(X)-1$.
:::

<1>2. Write $P_X(d)=\sum_{i=0}^ra_i\binom{d}{i}$ with $a_i\in\ZZ$. Then
$a_r=\deg X$, so
$$
P_X(d)=\frac{\deg X}{r!}\,d^r+O(d^{r-1}).
$$
For $k$ algebraically closed and $X$ a variety, $\deg X$ is the number of
points of $X\cap L$ for a general linear subspace $L\subseteq\PP^n$ of
dimension $n-r$.

::: {.proof}
A polynomial in $\QQ[d]$ taking integer values for $d\gg0$ is an integer
combination of the $\binom{d}{i}$, and the degree of $X$ is defined as $a_r$.
The intersection count is the degree of $X\cap L$, a zero-dimensional scheme
whose Hilbert polynomial is the constant $a_r$ for general $L$.
:::

<1>3. For every $d\in\ZZ$,
$$
P_M(d)=\chi\bigl(\PP^n,\widetilde M(d)\bigr)
=\sum_{i=0}^n(-1)^i\dim_kH^i\bigl(\PP^n,\widetilde M(d)\bigr).
$$
In particular $P_X(d)=\chi(X,\mathcal O_X(d))$ and
$P_X(0)=\chi(X,\mathcal O_X)$.

::: {.proof}
The function $d\mapsto\chi(\PP^n,\widetilde M(d))$ is a polynomial in $d$. For
$d\gg0$, Serre vanishing gives $H^i(\PP^n,\widetilde M(d))=0$ for $i>0$, and
$M_d\to H^0(\PP^n,\widetilde M(d))$ is an isomorphism. Two polynomials that
agree for all $d\gg0$ are equal.
:::

<1>4. The arithmetic genus is $p_a(X)=(-1)^r\bigl(P_X(0)-1\bigr)$. If $X$ is a
smooth geometrically connected projective curve of genus $g$, then
$P_X(d)=(\deg X)\,d+1-g$.

::: {.proof}
The first formula is the definition of $p_a$. For the curve, step <1>3 gives
$P_X(d)=\chi(X,\mathcal O_X(d))$, and Riemann--Roch for the line bundle
$\mathcal O_X(d)$ of degree $d\deg X$ gives $d\deg X+1-g$.
:::

<1>5. In a flat family of closed subschemes of $\PP^n$ over a connected base,
the Hilbert polynomial of the fibers is constant, and the closed subschemes of
$\PP^n$ with Hilbert polynomial $P$ are parametrized by the projective Hilbert
scheme $\operatorname{Hilb}^P(\PP^n)$.

::: {.proof}
Constancy is the characterization of flatness over an integral Noetherian base
by constancy of the Hilbert polynomial, applied locally on the base; the
parameter space is Grothendieck's Hilbert scheme.
:::
:::
