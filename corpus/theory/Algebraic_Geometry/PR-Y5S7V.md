---
schema: qual/card@1
id: PR-Y5S7V
kind: proposition
title: The degree of a divisor on a projective curve
slogan: 'On a smooth projective curve, zeros and poles balance: every principal divisor has degree zero.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Divisors
  - Degree
  - Curves
relations:
- kind: uses
  target: D-5PQ5W
- kind: uses
  target: D-CRVDEGREES
review: draft
prompts:
- What is the degree of a divisor?
- Why does a principal divisor have degree zero?
---

::: {.proposition}
Let $C$ be a smooth projective integral curve over a field $k$. For a divisor $D=\sum_p n_p p$, its degree is
$$
\deg D=\sum_p n_p[\kappa(p):k]
$$
as in [[D-CRVDEGREES]]. For every $f\in K(C)^\times$,
$$
\deg\operatorname{div}(f)=0
$$
[@Har77, Corollary II.6.10].
Hence degree descends through the divisor--line-bundle correspondence to a homomorphism $\deg\colon\Pic(C)\to\ZZ$.
If $k$ is algebraically closed, its kernel is $\Pic^0(C)$.
:::

::: {.proof}
Let $f\in K(C)^\times$.
If $f\in k^\times$ then $\operatorname{div}(f)=0$.
Otherwise $f$ is nonconstant and defines a nonconstant morphism $f\colon C\to\PP^1_k$, which is finite with $\PP^1_k$ complete nonsingular by [@Har77, Proposition II.6.8], and by the definition of the divisor of a rational function
$$
\operatorname{div}(f)=f^*[0]-f^*[\infty].
$$
The divisors $[0]$ and $[\infty]$ of $\PP^1_k$ have degree $1$, so applying [@Har77, Proposition II.6.9] to the finite morphism $f$ gives
$$
\deg f^*[0]=\deg f\cdot1=\deg f^*[\infty],
$$
and $\deg\operatorname{div}(f)=0$.

Since principal divisors have degree zero, the degree is constant on divisor classes and induces $\deg\colon\CaCl(C)\to\ZZ$, which is the stated homomorphism under $\Pic(C)\cong\CaCl(C)$ ([[PR-DIVLB]], [@Har77, Corollary II.6.10]).
:::

::: {.remark}
A nonconstant $f\in K(C)$ defines a morphism $f\colon C\to\PP^1_k$. Since $C$ is projective and $f$ is nonconstant, this morphism is finite. The divisor of $f$ is
$$
\operatorname{div}(f)=f^*[0]-f^*[\infty],
$$
and both pullback divisors have degree $\deg f$. Therefore $\deg\operatorname{div}(f)=0$.

On $\AA^1_k$, the rational function $x$ has divisor $[0]$ and degree one. Thus properness is essential for the degree-zero statement about principal divisors.
:::
