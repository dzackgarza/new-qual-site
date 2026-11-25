---
schema: qual/card@1
id: T-SVF2W
kind: theorem
title: Equivalent conditions for a holomorphic function to vanish identically
slogan: 'For a holomorphic function on a connected domain, accumulating zeros, infinite-order vanishing, and identically zero are equivalent.'
classification:
  areas:
  - complex-analysis
  topics:
  - Identity Theorem
  - Zeros
relations: []
review: draft
---

::: {.theorem}
Let $\Omega\subseteq\CC$ be a nonempty connected open set and let $f$ be [[D-E7A5W|holomorphic]] on $\Omega$.
The following are equivalent.

(i) $f(z)=0$ for all $z\in\Omega$.

(ii) There are $z_0\in\Omega$ and a sequence $(z_k)_{k\geq1}$ of distinct points of $\Omega$ with $z_k\to z_0$ and $f(z_k)=0$ for all $k$.

(iii) There is $z_0\in\Omega$ with $f^{(n)}(z_0)=0$ for all $n\geq0$.

Condition (ii) is the form usually called the identity theorem [@SS03, ch. 2, Theorem 4.8].
:::

::: {.corollary}
Let $\Omega\subseteq\CC$ be a connected open set and let $S\subseteq\Omega$ have a [[D-TFSPT|limit point]] in $\Omega$.

(a) If $f$ and $g$ are [[D-V6UQJ|analytic]] on $\Omega$ and $f(z)=g(z)$ for all $z\in S$, then $f(z)=g(z)$ for all $z\in\Omega$; this is (ii) applied to $f-g$.

(b) If $F\colon\Omega\times\Omega\to\CC$ is holomorphic in each variable separately and $F(z,w)=0$ for all $z,w\in S$, then $F(z,w)=0$ for all $z,w\in\Omega$.

For (b), fixing $w\in S$ shows $z\mapsto F(z,w)$ vanishes on $\Omega$ by (a), and then fixing $z\in\Omega$ shows $w\mapsto F(z,w)$ vanishes on $\Omega$ by (a) again.
:::
