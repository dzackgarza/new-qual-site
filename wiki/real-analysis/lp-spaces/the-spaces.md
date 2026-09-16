---
title: The spaces
order: 10
topics:
- Lp Spaces
- Density
- Dual Spaces
- L²
- L∞
- L2 Spaces
---

# The spaces

Let $(X,\mu)$ be a measure space and $1\leq p\leq\infty$.
If $\mu(X)<\infty$ and $1\le p<q\le\infty$, then $L^q(\mu)\subseteq L^p(\mu)$.
For Lebesgue measure on $\RR$ neither of $L^p$ and $L^q$ contains the other, and for counting measure on $\NN$, $\ell^p\subseteq\ell^q$.

For $1<p<\infty$ and $q=p/(p-1)$, the map $g\mapsto\qty{f\mapsto\int fg\,d\mu}$ is an isometric isomorphism $L^q\cong(L^p)^*$; for $p=1$ this holds when $\mu$ is $\sigma$-finite.
For Lebesgue measure on $[0,1]$, the corresponding map $L^1\to(L^\infty)^*$ is not surjective.
By the Riesz--Fischer theorem, $L^p$ is complete for $1\leq p\leq\infty$.

[[PR-NFB7Q]]

[[T-4KKSH]]

[[FT-GQRV2]]

[[T-5BFVS]]

[[PR-N7YFV]]

[[PR-TWF4F]]

[[PR-JX4YU]]

[[PR-3W4FO]]

## Approximation and translation

For Lebesgue measure on $\RR^d$ and $1\leq p<\infty$, continuous functions with compact support are dense in $L^p$, and $\norm{f(\wait+h)-f}_p\to0$ as $h\to0$ for every $f\in L^p$.

[[PR-XAVMU]]

[[PR-HLPMX]] [[PR-EHL3O]]

[[T-5YROQ]]

[[PR-O4AY4]]

[[PR-2KEIE]]

[[T-G543T]]

[[PR-TNFL4]]

[[T-S3C3S]]

## Density and duality arguments

An identity between quantities that depend continuously on $f\in L^p$ holds on $L^p$ once it holds on a dense subclass, such as $C_c(\RR^d)$.
For $1\leq p<\infty$ and $f\in L^p$, if $\int fg=0$ for every $g$ in a dense subset of $L^q$, then $f=0$ almost everywhere.

[[E-IAQ6D]]

[[FT-4ED3Q]]

[[PR-C626A]]

::: {.remark title="Consequences of the Riesz--Fischer proof"}
The proof of the Riesz--Fischer theorem shows that every sequence converging in $L^p$, $1\leq p<\infty$, has a subsequence converging almost everywhere to the same limit.

:::
