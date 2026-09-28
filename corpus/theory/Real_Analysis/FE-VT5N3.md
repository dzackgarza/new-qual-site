---
schema: qual/card@1
id: FE-VT5N3
kind: example
title: A sequence of functions that converges a.e. but not in $L^1$, uniformly, or pointwise
prompts:
- Give a sequence that converges a.e. but not in $L^1$, uniformly, or pointwise.
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - L¹
  - Counterexamples
relations: []
review: draft
---

::: {.example}
For $n\geq 1$ let
$$
f_n \coloneqq n \chi_{[0, 1/n]}\colon\RR\to\RR.
$$

- For $x<0$, $f_n(x) = 0$ for all $n$; for $x>0$, $f_n(x) = 0$ for all $n > 1/x$. Hence $f_n\to 0$ at every $x\neq 0$, so $f_n\to 0$ almost everywhere.

- $f_n(0) = n\to\infty$, so $(f_n)$ does not [[D-IYDZU|converge pointwise]] on $\RR$, and in particular does not [[D-YZC3C|converge uniformly]].

- $\int_\RR\abs{f_n - 0}\dx = 1$ for every $n$, so $f_n\not\to 0$ in $L^1(\RR)$.
:::
