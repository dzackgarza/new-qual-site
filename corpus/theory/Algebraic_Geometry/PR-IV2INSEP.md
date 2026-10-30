---
schema: qual/card@1
id: PR-IV2INSEP
kind: proposition
title: Purely inseparable morphisms of smooth curves are relative Frobenius
slogan: 'A purely inseparable degree-$p^n$ morphism of smooth proper curves is the $n$-fold relative Frobenius after identifying the target with the Frobenius twist.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Purely Inseparable Extensions
  - Frobenius
  - Curves
relations:
- kind: uses
  target: D-IV2FROBTWIST
- kind: related-to
  target: T-LKT0U
review: draft
prompts:
- What does a purely inseparable morphism of curves look like?
- Does the genus change under a purely inseparable extension?
- Why can Riemann--Hurwitz not be applied to such a morphism?
---

::: {.proposition}
Let $k$ be an algebraically closed field of characteristic $p>0$, and let $f\colon X\to Y$ be a finite nonconstant morphism of smooth projective curves over $k$. Suppose the extension $k(X)/k(Y)$ is purely inseparable of degree $p^n$.
Then there is a unique $k$-isomorphism
$$
\alpha\colon Y\xrightarrow{\sim}X^{(p^n)}
$$
such that
$$
\alpha\circ f=F_{X/k}^{(n)}\colon X\longrightarrow X^{(p^n)}.
$$
Consequently $g(X)=g(Y)$. Since $k$ is perfect, $X^{(p^n)}$ and $X$ are isomorphic as abstract schemes, although they need not be isomorphic as $k$-schemes.
:::

::: {.proof}
Put $K=k(X)$ and $L=k(Y)$. Pure inseparability of degree $p^n$ implies
$$
K^{p^n}\subseteq L\subseteq K.
$$
By the [[D-IV2FROBTWIST|degree of relative Frobenius]], $[K:K^{p^n}]=p^n$. Since also $[K:L]=p^n$, the tower formula gives
$$
L=K^{p^n}.
$$
The $n$-fold relative Frobenius has target $X^{(p^n)}$ with function field $K^{p^n}$. Thus $Y$ and $X^{(p^n)}$ are the smooth projective models of the same one-variable function field over $k$, giving the unique isomorphism $\alpha$ for which $\alpha\circ f=F_{X/k}^{(n)}$.

The twist $X^{(p^n)}$ is obtained by base change along the field automorphism $F_k^n$, so
$$
\dim_k H^1(X^{(p^n)},\OO_{X^{(p^n)}})
=
\dim_k H^1(X,\OO_X).
$$
Hence $g(Y)=g(X)$.
:::

::: {.remark title="Differentials and Riemann--Hurwitz"}
For the purely inseparable map above, the morphism
$$
f^*\Omega_{Y/k}\longrightarrow\Omega_{X/k}
$$
is zero: on function fields every element of $L=K^{p^n}$ is a $p^n$-th power, whose differential vanishes. Hence
$$
\Omega_{X/Y}\cong\Omega_{X/k},
$$
which has rank one rather than being a torsion sheaf. The [[D-IV2RAM|ramification divisor]], defined from the lengths of the torsion sheaf $\Omega_{X/Y}$ for a separable morphism, is therefore not defined in this way for $f$, and the [[T-LKT0U|proof of Riemann--Hurwitz]] does not apply.

More generally, every finite nonconstant morphism of smooth projective curves in characteristic $p$ factors as
$$
X\xrightarrow{F_{X/k}^{(n)}}X^{(p^n)}\longrightarrow Y,
$$
where the second morphism induces a separable extension of function fields. Relative Frobenius preserves genus, while Riemann--Hurwitz gives $g(X^{(p^n)})\geq g(Y)$ for the separable factor. Therefore $g(X)\geq g(Y)$ for every such finite morphism, as used in the proof of [[T-IV2LUROTH|Lüroth's theorem]].
:::
