---
schema: qual/card@1
id: E-SS7.EX-1
kind: problem
title: "Bounded partial sums give convergence of the Dirichlet series for Re(s) > 0"
classification:
  areas:
  - complex-analysis
  topics: ['Zeta Function', 'Prime Number Theorem', 'Dirichlet Series']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
1. Suppose that $\{ a _ { n } \} _ { n = 1 } ^ { \infty }$ is a sequence of real numbers such that the partial sums

$$
A _ {n} = a _ {1} + \dots + a _ {n}
$$

are bounded.
Prove that the Dirichlet series

$$
\sum_ {n = 1} ^ {\infty} \frac {a _ {n}}{n ^ {s}}
$$

converges for $\operatorname { R e } ( s ) > 0$ and defines a holomorphic function in this half-plane.

[Hint: Use summation by parts to compare the original (non-absolutely convergent) series to the (absolutely convergent) series $\sum A _ { n } ( n ^ { - s } - ( n + 1 ) ^ { - s } )$ . An estimate for the term in parentheses is provided by the mean value theorem. To prove that the series is analytic, show that the partial sums converge uniformly on every compact subset of the half-plane $\operatorname { R e } ( s ) > 0 . ]$
:::

::: solution
Let $A_n=\sum_{j=1}^n a_j$ and suppose $|A_n|\le M$. For $N\ge1$, summation by parts gives
\[
\sum_{n=1}^N\frac{a_n}{n^s}
=A_NN^{-s}+\sum_{n=1}^{N-1}A_n\bigl(n^{-s}-(n+1)^{-s}\bigr).
\tag{1}
\]
If $\sigma=\Re s>0$, then $A_NN^{-s}\to0$.

Also
\[
n^{-s}-(n+1)^{-s}
=s\int_n^{n+1}x^{-s-1}\,dx,
\]
so
\[
|n^{-s}-(n+1)^{-s}|\le |s|n^{-\sigma-1}.
\]
Thus the series on the right of (1) converges absolutely for every $\sigma>0$, proving convergence of the original Dirichlet series.

To prove holomorphy, let $K$ be a compact subset of $\Re s>0$. Then for some $\delta>0$ and $C>0$,
\[
\Re s\ge\delta,\qquad |s|\le C\qquad(s\in K).
\]
Hence uniformly on $K$,
\[
|A_n(n^{-s}-(n+1)^{-s})|
\le MCn^{-1-\delta}.
\]
The Weierstrass $M$-test gives uniform convergence on $K$ of the holomorphic series in (1); the boundary term tends to zero uniformly as well. Therefore the Dirichlet series defines a holomorphic function on $\Re s>0$.
:::
