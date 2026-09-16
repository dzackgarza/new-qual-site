---
schema: qual/card@1
id: P-IMVV7
kind: problem
title: Permutations, combinations, and the number of injections from a $k$-set to
  an $n$-set
classification:
  areas:
  - prelim
  topics:
  - Combinatorics
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $k$ and $n$ be positive integers with $k \le n$.
Give the definitions for the permutations and for the combinations of $k$ elements from an $n$-element set, and state formulas for the numbers of these.
Derive a formula for the number of one-to-one functions from a $k$-element set to an $n$-element set.
:::

::: {.solution}
A permutation of $k$ elements chosen from an $n$-element set is an ordered list of $k$ distinct elements. Its number is
\[
P(n,k)=n(n-1)\cdots(n-k+1)=\frac{n!}{(n-k)!}.
\]

A combination of $k$ elements from an $n$-element set is an unordered $k$-element subset. Its number is
\[
\binom nk=\frac{n!}{k!(n-k)!}.
\]

Let $X$ be a $k$-element set and $Y$ an $n$-element set. Fix an ordering $x_1,\ldots,x_k$ of $X$. An injective function $f:X\to Y$ is determined uniquely by the ordered list
\[
(f(x_1),\ldots,f(x_k)),
\]
whose entries must be distinct. Conversely every ordered list of $k$ distinct elements of $Y$ defines an injection. Therefore the number of injections is
\[
P(n,k)=\frac{n!}{(n-k)!}.
\]
:::
