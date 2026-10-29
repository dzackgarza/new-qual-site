---
schema: qual/card@1
id: T-RA-WORKSHOP-D7-6-7
kind: theorem
title: Stone--Weierstrass theorem
slogan: 'A self-adjoint subalgebra of $C(K)$ that separates points and vanishes at no point is uniformly dense in $C(K)$.'
classification:
  areas:
  - real-analysis
  topics:
  - Density
  - Stone-Weierstrass
  - Function Spaces
  - Polynomials
  - Uniform Convergence
relations: []
review: draft
---

::: {.theorem}
Let $K$ be a [[D-EILKJ|compact]] metric space, let $C(K)$ be the algebra of continuous functions $K\to\CC$, and let $\mathcal A\subseteq C(K)$ be a subalgebra, that is, a complex vector subspace closed under pointwise multiplication.
Suppose that

- $\mathcal A$ is self-adjoint: $\bar g\in\mathcal A$ for every $g\in\mathcal A$;

- $\mathcal A$ separates points of $K$: for all $x\neq y$ in $K$ there exists $g\in\mathcal A$ with $g(x)\neq g(y)$;

- $\mathcal A$ vanishes at no point of $K$: for every $x\in K$ there exists $g\in\mathcal A$ with $g(x)\neq0$.

Then for every $f\in C(K)$ there exist $f_n\in\mathcal A$ such that $f_n\to f$ [[D-YZC3C|uniformly]] on $K$.
[@Rud76].
:::

::: {.remark}
For $K=[a,b]$ and $\mathcal A$ the polynomials with complex coefficients, the hypotheses hold because $\mathcal A$ contains $1$ and $x$, and the theorem gives the [[T-3QNBQ|Weierstrass approximation theorem]].
:::
