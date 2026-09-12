---
schema: qual/card@1
id: P-BKF18-2B
kind: problem
title: A real polynomial forced to have a nonreal zero
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
Suppose $p$ is a nonconstant real polynomial such that for some real $a$, $p(a)\ne0$ and $p'(a)=p''(a)=0$.
Prove that $p$ has at least one nonreal zero.
:::

::: {.solution}
Observe that if $q ( z )$ is a real-rooted polynomial with distinct roots, then by Rolle’s theorem $q ^ { \prime } ( z )$ is also real-rooted (since it has degree one less than the degree of $q )$ and has the property that between every two roots of $q ^ { \prime }$ there is a root of q. Since polynomials with distinct roots are dense in the set of real-rooted polynomials, this implies that if $q$ is any real-rooted polynomial and $q ^ { \prime } ( z )$ has a double root at z then $q ( z ) = 0$

For the given polynomial $p ^ { \prime } ( z )$ has a double root at $^ { a , }$ but $\boldsymbol { p } ( \boldsymbol { a } ) \neq 0$ , so $p$ cannot be real-rooted.
:::
