---
schema: qual/card@1
id: E-HAT-3.1-12
kind: exercise
title: Hatcher Section 3.1 Exercise 12
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: exercise
Show $H^k(X, X^n; G) = 0$ if $X$ is a CW complex and $k \leq n$, by using the cohomology version of the second proof of the corresponding result for homology in Lemma 2.34.
:::

::: solution
**Goal:** Prove $H^k(X, X^n; G) = 0$ for all $k \le n$ by adapting the second proof of Lemma 2.34 (induction on skeletons using long exact sequences of triples).

<1>1. Base case and relative cohomology of consecutive skeletons $(X^m, X^{m-1})$:
    *Proof:*
    <2>1. For $m = n$, the pair is $(X^n, X^n)$, so $H^k(X^n, X^n; G) = 0$ for all $k$.
    <2>2. For any $m \ge 1$, the quotient space $X^m / X^{m-1}$ is a wedge sum of $m$-spheres $\bigvee_\alpha S^m_\alpha$, one for each $m$-cell of $X$.
    <2>3. Since $(X^m, X^{m-1})$ is a good pair:
    $$H^j(X^m, X^{m-1}; G) \cong \widetilde{H}^j(X^m / X^{m-1}; G) \cong \prod_\alpha \widetilde{H}^j(S^m; G) \cong \begin{cases} \prod_\alpha G & j = m, \\ 0 & j \neq m. \end{cases}$$

<1>2. Induction step on finite skeletons $X^m$ for $m \ge n$:
    *Proof:*
    <2>1. For $m > n$, consider the long exact sequence in cohomology for the triple $(X^m, X^{m-1}, X^n)$:
    $$\cdots \to H^k(X^m, X^{m-1}; G) \to H^k(X^m, X^n; G) \to H^k(X^{m-1}, X^n; G) \to H^{k+1}(X^m, X^{m-1}; G) \to \cdots$$
    <2>2. If $k < m$, then $H^k(X^m, X^{m-1}; G) = 0$ by step 1.3.
    <2>3. If additionally $k + 1 < m$ (i.e. $k < m - 1$), then $H^{k+1}(X^m, X^{m-1}; G) = 0$ as well.
    <2>4. In the boundary case $k = m - 1$, the map $H^{m-1}(X^{m-1}, X^n; G) \to H^m(X^m, X^{m-1}; G)$ is the cellular coboundary $d^{m-1}$, which is injective on the image of $H^{m-1}(X^m, X^n; G)$.
    <2>5. By induction on $m \ge n$: for $m = n$, $H^k(X^n, X^n; G) = 0$.
    <2>6. For any $m > n$ and any fixed $k \le n$, we have $k \le n \le m - 1 < m$.
    <2>7. Thus $H^k(X^m, X^n; G) \cong H^k(X^{m-1}, X^n; G) \cong \cdots \cong H^k(X^n, X^n; G) = 0$.
    <2>8. Hence $H^k(X^m, X^n; G) = 0$ for all $m \ge n$ and all $k \le n$.

<1>3. Passing from finite skeletons to the full complex $X$:
    *Proof:*
    <2>1. If $X$ is finite-dimensional, $X = X^N$ for some $N$, so $H^k(X, X^n; G) = H^k(X^N, X^n; G) = 0$ by <1>2.
    <2>2. In the general case where $X$ is infinite-dimensional, the Milnor $\varprojlim^1$ short exact sequence for the tower of skeletons $\{X^m\}_{m \ge n}$ gives:
    $$0 \to {\varprojlim}^1 H^{k-1}(X^m, X^n; G) \to H^k(X, X^n; G) \to \varprojlim H^k(X^m, X^n; G) \to 0.$$
    <2>3. For any fixed $k \le n$, step 2.8 gives $H^k(X^m, X^n; G) = 0$ and $H^{k-1}(X^m, X^n; G) = 0$ for all $m \ge n$.
    <2>4. Thus both the inverse limit $\varprojlim 0 = 0$ and the derived limit ${\varprojlim}^1 0 = 0$ vanish.
    <2>5. Therefore $H^k(X, X^n; G) = 0$ for all $k \le n$.
:::
