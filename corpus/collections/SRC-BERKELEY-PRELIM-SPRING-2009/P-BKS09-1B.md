---
schema: qual/card@1
id: P-BKS09-1B
kind: problem
title: Higher derivative test for local extrema
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in f and math delimiters against s09solutions.pdf page 4 problem 1B.
---

::: {.problem}
Let $I \subseteq \mathbb{R}$ be an open interval, and let $f : I \to \mathbb{R}$ have continuous $k$-th derivatives $f^{[k]}$ on $I$ for $k \leq n - 1$. Let $a \in I$ be a point such that $f^{[k]}(a) = 0$ for all $1 \leq k \leq n - 1$, $f^{[n]}(a)$ exists and $f^{[n]}(a) > 0$. Prove that $f$ has a local minimum at $a$ if $n$ is even, and has no local extremum at $a$ if $n$ is odd.
:::
