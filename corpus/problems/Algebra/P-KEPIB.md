---
schema: qual/card@1
id: P-KEPIB
kind: problem
title: Finite field extensions are algebraic
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: problem
- Show that every finite field extension is algebraic.
:::

::: {.solution}
**Goal:** Let $L/K$ be a field extension such that the degree $n = [L : K] = \dim_K(L)$ is finite.
Prove that $L/K$ is an algebraic extension (i.e., every element $\alpha \in L$ is algebraic over $K$).

<1>1. Definitions: <2>1. A field extension $L/K$ is finite if $L$ is finite-dimensional as a vector space over $K$, with dimension denoted by $n = [L : K] < \infty$.
Proof: Standard definition of degree of a field extension.
<2>2. An element $\alpha \in L$ is algebraic over $K$ if there exists a non-zero polynomial $p(x) \in K[x]$ such that $p(\alpha) = 0$.
Proof: Standard definition of an algebraic element.
<2>3. An extension $L/K$ is algebraic if every $\alpha \in L$ is algebraic over $K$.
Proof: Standard definition of an algebraic extension.

<1>2. Linear dependence of powers of an arbitrary element: <2>1. Let $\alpha \in L$ be an arbitrary element.
Proof: Setting an arbitrary element to prove the universal claim.
<2>2. Consider the set of $n+1$ elements $S = \{1, \alpha, \alpha^2, \dots, \alpha^n\} \subset L$.
Proof: Since $n = [L : K] \ge 1$, $S$ contains $n+1$ elements.
<2>3. The set $S$ is linearly dependent over $K$.
Proof: In any $n$-dimensional vector space over $K$, any subset containing strictly more than $n$ elements is linearly dependent.
Here $|S| = n+1 > n = \dim_K(L)$.
<2>4. There exist coefficients $c_0, c_1, \dots, c_n \in K$, not all zero, such that $\sum_{i=0}^n c_i \alpha^i = 0$.
Proof: By definition of linear dependence of the set $S$ over the field $K$.

<1>3. Construction of the annihilating polynomial: <2>1. Define the polynomial $p(x) \in K[x]$ by $p(x) = \sum_{i=0}^n c_i x^i = c_n x^n + \dots + c_1 x + c_0$.
Proof: Since $c_i \in K$ for all $i$, $p(x)$ is a well-defined polynomial in $K[x]$.
<2>2. $p(x)$ is not the zero polynomial, i.e., $p(x) \neq 0$.
Proof: By <1>2.<2>4, not all coefficients $c_i$ are zero.
<2>3. $p(\alpha) = \sum_{i=0}^n c_i \alpha^i = 0$.
Proof: By <1>2.<2>4. <2>4. Therefore, $\alpha$ is algebraic over $K$.
Proof: $\alpha$ is a root of the non-zero polynomial $p(x) \in K[x]$.

<1>4. Conclusion: Since $\alpha \in L$ was arbitrary, every element of $L$ is algebraic over $K$, so $L/K$ is algebraic.
Proof: By <1>2 and <1>3.
:::
