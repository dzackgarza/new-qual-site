---
schema: qual/card@1
id: P-AGRHURW
kind: problem
title: Riemann--Hurwitz from the map on differentials
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Hurwitz
  - Differentials
  - Curves
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Ogus's sequence on the map on differentials, exactness, and the weak Riemann--Hurwitz formula.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Given a nonconstant map between curves over $k$, is there an associated map on differentials?
Is there a resulting exact sequence, and is it short exact?

Prove the weak form of Riemann--Hurwitz.
:::

::: {.solution}
Let
\[
f:X\longrightarrow Y
\]
be a nonconstant morphism of smooth projective integral curves over $k$.
Since $f$ is nonconstant and the curves are projective, $f$ is finite.  Write
\[
n=\deg f=[k(X):k(Y)].
\]

<1>1. There is a canonical right-exact cotangent sequence
\[
\boxed{
f^*\Omega_{Y/k}^1
\xrightarrow{df}
\Omega_{X/k}^1
\longrightarrow
\Omega_{X/Y}^1
\longrightarrow0.
}
\]
::: {.proof}
For every composable pair
\[
X\xrightarrow{f}Y\longrightarrow\operatorname{Spec}k,
\]
the transitivity sequence for Kähler differentials is
\[
f^*\Omega_{Y/k}^1
\longrightarrow
\Omega_{X/k}^1
\longrightarrow
\Omega_{X/Y}^1
\longrightarrow0.
\]
The first arrow is the pullback map on differentials, characterized locally by
\[
df(f^*a)=d(f^\sharp a).
\]
:::

<1>2. If $f$ is separable, the map
\[
df:f^*\Omega_{Y/k}^1\longrightarrow\Omega_{X/k}^1
\]
is injective.  Hence in the separable case the sequence in <1>1 is short exact:
\[
\boxed{
0\longrightarrow f^*\Omega_{Y/k}^1
\longrightarrow\Omega_{X/k}^1
\longrightarrow\Omega_{X/Y}^1
\longrightarrow0.
}
\]
::: {.proof}
Both $f^*\Omega_{Y/k}^1$ and $\Omega_{X/k}^1$ are line bundles because $X$ and $Y$ are smooth curves.

At the generic point, the first map becomes
\[
\Omega_{k(Y)/k}^1\otimes_{k(Y)}k(X)
\longrightarrow
\Omega_{k(X)/k}^1.
\]
For the finite field extension $k(X)/k(Y)$, the transitivity sequence gives
\[
\Omega_{k(Y)/k}^1\otimes k(X)
\longrightarrow
\Omega_{k(X)/k}^1
\longrightarrow
\Omega_{k(X)/k(Y)}^1
\longrightarrow0.
\]
Separability implies
\[
\Omega_{k(X)/k(Y)}^1=0,
\]
and both preceding vector spaces have dimension one over $k(X)$, so the generic map is an isomorphism.  Thus $df$ is a nonzero map of line bundles on the integral curve $X$.

Locally, after trivializing the two line bundles, a nonzero map between them is multiplication by a nonzero element of the local domain $\mathcal O_{X,p}$, hence is injective.  Therefore $df$ is injective everywhere.
:::

<1>3. Separability is necessary for the short exact sequence.
::: {.proof}
In characteristic $p>0$, consider the purely inseparable degree-$p$ map
\[
F:\mathbb P^1_k\longrightarrow\mathbb P^1_k,
\qquad
[X:Y]\longmapsto[X^p:Y^p].
\]
On an affine coordinate $t$,
\[
F^*(dt)=d(t^p)=pt^{p-1}dt=0.
\]
Thus the map
\[
F^*\Omega_{\mathbb P^1/k}^1
\longrightarrow
\Omega_{\mathbb P^1/k}^1
\]
is zero, not injective.  Hence a nonconstant inseparable map need not give a short exact cotangent sequence.
:::

<1>4. Assume from now on that $f$ is separable.  Then $\Omega_{X/Y}^1$ is a torsion sheaf of finite length, supported at the ramification points.
::: {.proof}
By <1>2, $\Omega_{X/Y}^1$ is the cokernel of an injective map between line bundles.  At the generic point that map is an isomorphism, so the cokernel has rank zero.  A coherent rank-zero sheaf on a Noetherian integral curve is torsion and has zero-dimensional support, hence finite length.
:::

<1>5. Taking degrees in the short exact sequence gives
\[
\deg\Omega_{X/k}^1
=\deg f^*\Omega_{Y/k}^1
+\deg(\Omega_{X/Y}^1),
\]
where for a finite-length sheaf $T$ on the curve
\[
\deg T
=\sum_{p\in X}
\length_{\mathcal O_{X,p}}(T_p)[\kappa(p):k].
\]
::: {.proof}
For a short exact sequence on a smooth projective curve
\[
0\to L\to M\to T\to0
\]
with $L,M$ line bundles and $T$ a finite-length torsion sheaf, degree is additive:
\[
\deg M=\deg L+\deg T.
\]
Apply this to the sequence in <1>2.
:::

<1>6. Therefore the weak Riemann--Hurwitz formula is
\[
\boxed{
2g_X-2
=n(2g_Y-2)
+\deg(\Omega_{X/Y}^1).
}
\]
In particular,
\[
\boxed{
2g_X-2\ge n(2g_Y-2).
}
\]
::: {.proof}
For a smooth projective curve $C$,
\[
\deg\Omega_{C/k}^1=2g_C-2.
\]
Also, pullback multiplies the degree of a line bundle by the degree of the finite morphism:
\[
\deg f^*\Omega_{Y/k}^1
=n\deg\Omega_{Y/k}^1
=n(2g_Y-2).
\]
Substitute these identities into <1>5.  The inequality follows because the degree of a finite-length torsion sheaf is nonnegative.
:::

<1>7. The usual local Riemann--Hurwitz formula is obtained by writing
\[
R=\sum_{p\in X}\length_{\mathcal O_{X,p}}(\Omega_{X/Y,p}^1)\,p.
\]
Then
\[
2g_X-2=n(2g_Y-2)+\deg R.
\]
If all ramification is tame, then
\[
\length(\Omega_{X/Y,p}^1)=e_p-1,
\]
so, after base change to an algebraic closure (or directly when $k$ is algebraically closed),
\[
\boxed{
2g_X-2
=n(2g_Y-2)
+\sum_{p\in X}(e_p-1).
}
\]
::: {.proof}
The first equality merely rewrites the finite length in <1>6 as the degree of its associated effective divisor.  The tame local calculation with uniformizers gives the coefficient $e_p-1$ at each ramification point.
:::

<1>8. Q.E.D.
::: {.proof}
Steps <1>1--<1>3 answer the questions about differentials and exactness.  Steps <1>4--<1>6 prove weak Riemann--Hurwitz, and step <1>7 gives the ramification-index form.
:::
:::
