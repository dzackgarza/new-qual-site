---
schema: qual/card@1
id: E-SS2.EX-13
kind: problem
title: "SS 2.13: An entire function with a zero coefficient in every local expansion is a polynomial"
classification:
  areas:
  - complex-analysis
  topics: ["Cauchy's Theorem", 'Contour Integration', 'Residues']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}
13. Suppose $f$ is an analytic function defined everywhere in $\mathbb { C }$ and such that for each $z _ { 0 } \in \mathbb { C }$ at least one coeficient in the expansion

$$
f (z) = \sum_ {n = 0} ^ {\infty} c _ {n} (z - z _ {0}) ^ {n}
$$

is equal to 0. Prove that f is a polynomial.

[Hint: Use the fact that $c _ { n } n ! = f ^ { ( n ) } ( z _ { 0 } )$ and use a countability argument.]
:::

::: {.solution}
For each $n\ge0$, let
\[
Z_n=\{z\in\mathbb C:f^{(n)}(z)=0\}.
\]
By hypothesis, for every $z_0\in\mathbb C$ at least one Taylor coefficient of $f$ at $z_0$ vanishes. Since that coefficient is $f^{(n)}(z_0)/n!$ for some $n$, we have
\[
\mathbb C=\bigcup_{n=0}^\infty Z_n.
\tag{1}
\]

Suppose $f$ were not a polynomial. Then no derivative $f^{(n)}$ could vanish identically, since $f^{(n)}\equiv0$ would imply that $f$ is a polynomial of degree at most $n-1$. Hence, by the isolated-zero theorem, each $Z_n$ is a discrete subset of $\mathbb C$.

Every discrete subset of $\mathbb C$ is countable: for each of its points choose a disc with rational center and rational radius containing no other point of the set, and assign one such disc to that point; there are only countably many rational discs. Thus every $Z_n$ is countable, and so the right side of (1) is countable. This contradicts the uncountability of $\mathbb C$.

Therefore some $f^{(n)}$ is identically zero, and consequently $f$ is a polynomial.
:::
