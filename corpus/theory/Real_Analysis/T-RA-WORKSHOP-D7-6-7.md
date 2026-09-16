---
schema: qual/card@1
id: T-RA-WORKSHOP-D7-6-7
kind: theorem
title: Weierstrass approximation and Stone--Weierstrass theorems
classification:
  areas:
  - real-analysis
  topics:
  - Density
  - Function Spaces
  - Polynomials
  - Uniform Convergence
relations: []
review: draft
---

::: {.theorem}
(a) Let $a<b$ and let $f\colon[a,b]\to\CC$ be continuous.
Then there exist polynomials $P_n$ with complex coefficients such that $P_n\to f$ [[D-YZC3C|uniformly]] on $[a,b]$.
If $f$ is real-valued, the $P_n$ may be taken with real coefficients.

(b) Let $K$ be a [[D-EILKJ|compact]] metric space, let $C(K)$ be the algebra of continuous functions $K\to\CC$, and let $\mathcal A\subseteq C(K)$ be a subalgebra, that is, a complex vector subspace closed under pointwise multiplication.
Suppose that

- $\mathcal A$ is self-adjoint: $\bar g\in\mathcal A$ for every $g\in\mathcal A$;

- $\mathcal A$ separates points of $K$: for all $x\neq y$ in $K$ there exists $g\in\mathcal A$ with $g(x)\neq g(y)$;

- $\mathcal A$ vanishes at no point of $K$: for every $x\in K$ there exists $g\in\mathcal A$ with $g(x)\neq0$.

Then for every $f\in C(K)$ there exist $f_n\in\mathcal A$ such that $f_n\to f$ uniformly on $K$.
[@Rud76].
:::
