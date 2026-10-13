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
\deg\operatorname{div}(f)=0.
$$
Hence degree descends through the divisor--line-bundle correspondence to a homomorphism $\deg\colon\Pic(C)\to\ZZ$.
If $k$ is algebraically closed, its kernel is $\Pic^0(C)$.
:::

::: {.remark}
A nonconstant $f\in K(C)$ defines a morphism $f\colon C\to\PP^1_k$. Since $C$ is projective and $f$ is nonconstant, this morphism is finite. The divisor of $f$ is
$$
\operatorname{div}(f)=f^*[0]-f^*[\infty],
$$
and both pullback divisors have degree $\deg f$. Therefore $\deg\operatorname{div}(f)=0$.

On $\AA^1_k$, the rational function $x$ has divisor $[0]$ and degree one. Thus properness is essential for the degree-zero statement about principal divisors.
:::
