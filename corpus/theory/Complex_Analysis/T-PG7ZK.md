---
schema: qual/card@1
id: T-PG7ZK
kind: theorem
title: An entire function of polynomial growth is a polynomial
slogan: 'If $\sup_{\abs z=R}\abs{f(z)}\le AR^k+B$ for every $R>0$, then $f$ is a polynomial of degree at most $k$.'
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Cauchy Estimates
  - Liouville's Theorem
relations: []
review: draft
---

::: {.theorem}
Let $f$ be [[D-E7A5W|entire]], let $k\geq0$ be an integer, and suppose there are constants $A,B>0$ with
$$
\sup_{\abs z=R}\abs{f(z)}\leq AR^k+B \qquad\text{for every } R>0.
$$
Then $f$ is a polynomial of degree at most $k$.

This is [@SS03, ch. 3, §8, Exercise 15(a)].

The hypothesis is the growth condition $\abs{f(z)}\leq C\abs z^k$ for large $\abs z$: such a bound gives the displayed one with $B$ absorbing the values on a bounded set, and conversely the displayed bound at $R=\abs z$ gives it for large $\abs z$.
The case $k=0$ is Liouville's theorem, and the proof is the Cauchy estimate for $f^{(k+1)}$ with $R\to\infty$.
:::
