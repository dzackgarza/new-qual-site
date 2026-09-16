---
schema: qual/card@1
id: T-FZWEC
kind: theorem
title: Hurwitz's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Hurwitz
  - Zeros
  - Uniform Convergence
relations: []
review: draft
---

::: {.theorem}
Let $\Omega\subseteq\CC$ be open and let $(f_k)_{k\geq1}$ be a sequence of [[D-E7A5W|holomorphic]] functions on $\Omega$ converging [[D-AIQG3|locally uniformly]] on $\Omega$ to $f$.
Suppose $f$ has a [[D-65VIK|zero]] of order $n$ at $z_0\in\Omega$.
Then there is $\delta>0$ such that for all sufficiently large $k$, $f_k$ has exactly $n$ zeros in the disc $\{z : \abs{z-z_0}<\delta\}$, counted with multiplicity.
Moreover, for every $\varepsilon\in(0,\delta)$ there is $K$ such that for all $k\geq K$ these $n$ zeros lie in $\{z : \abs{z-z_0}<\varepsilon\}$.
:::
