---
title: The spaces
order: 10
problems:
  topics:
  - Lp Spaces
  - Density
  - Dual Spaces  - L²
  - L∞
  - L2 Spaces

---

# The spaces

$L^p$ remembers size only up to null sets, and the ambient measure space matters to every inclusion statement.
On a finite-measure space, larger exponents give smaller spaces: if $1\le p<q\le\infty$, then $L^q\subseteq L^p$.
On an infinite-measure space there is no general inclusion in either direction.
Check the measure space before using any mnemonic about the exponent.

For $1<p<\infty$ in the standard settings used here, the dual exponent $q=p/(p-1)$ gives $(L^p)^*\cong L^q$.
The endpoint $p=\infty$ is different: the dual of $L^\infty$ is generally larger than $L^1$.
Riesz--Fischer supplies completeness, so these are Banach spaces rather than merely normed spaces.

[[PR-NFB7Q]]

[[T-4KKSH]]

[[FT-GQRV2]]

[[T-5BFVS]]

[[PR-N7YFV]]

[[PR-TWF4F]]

[[PR-JX4YU]]

[[PR-3W4FO]]

## $L^1$ facts

For Lebesgue $L^p(\RR^d)$, the estimates from the integration chapter control approximation and translation.
Spatial tails and absolute continuity let one cut away bad regions; translation continuity then passes estimates from compactly supported or regular functions to arbitrary $L^1$ functions.
The same translation-continuity argument extends to $1\le p<\infty$.

[[PR-XAVMU]]

[[PR-HLPMX]] [[PR-EHL3O]]

[[T-5YROQ]]

[[PR-O4AY4]]

[[PR-2KEIE]]

[[T-G543T]]

[[PR-TNFL4]]

[[T-S3C3S]]

## Techniques

Two recurring proof patterns are density and duality.
Prove an identity first on a dense class such as continuous or compactly supported functions and extend by norm continuity; or test a function against a sufficiently rich family and use duality to show that vanishing of all pairings forces the function itself to vanish almost everywhere.

[[E-IAQ6D]]

[[FR-EM6AL]]

[[PR-C626A]]

::: {.remark title="Riesz--Fischer consequences"}
Riesz--Fischer says that $L^p$ is complete, so every $L^p$-Cauchy sequence converges in $L^p$.
The same proof shows that an $L^p$ convergent sequence has an a.e. convergent subsequence, which is the standard bridge between the two kinds of convergence.
:::
