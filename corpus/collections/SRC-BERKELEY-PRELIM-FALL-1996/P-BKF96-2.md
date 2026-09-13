---
schema: qual/card@1
id: P-BKF96-2
kind: problem
title: An upper-semicontinuous function on a compact interval is bounded above
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
A real-valued function $f$ on a closed bounded interval $[a,b]$ is **upper semicontinuous** if for every $\varepsilon>0$ and $p\in[a,b]$ there exists $\delta>0$ such that
\[
x\in[a,b],\quad |x-p|<\delta
\quad\Longrightarrow\quad
f(x)<f(p)+\varepsilon.
\]
Prove that an upper-semicontinuous function is bounded above on $[a,b]$.
:::
