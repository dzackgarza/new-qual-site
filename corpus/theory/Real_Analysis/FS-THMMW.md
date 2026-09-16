---
schema: qual/card@1
id: FS-THMMW
kind: strategy
title: Negating uniform convergence of a sequence of functions
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Counterexamples
relations: []
review: draft
---

::: {.strategy}
Let $S$ be a set, and let $f_n\colon S\to\CC$ for $n\geq1$ and $f\colon S\to\CC$ be functions.
To show that $(f_n)$ does not [[D-YZC3C|converge uniformly]] to $f$ on $S$, exhibit $\varepsilon>0$ and, for infinitely many $n$, a point $x_n\in S$ with $\abs{f_n(x_n) - f(x_n)} \geq \varepsilon$.
:::

::: {.example}
On $S=(0,\infty)$, the functions $f_n(x)=\frac{1}{1+nx}$ converge pointwise to $f=0$, but not uniformly: with $\varepsilon=\frac12$ and $x_n=\frac1n$, $\abs{f_n(x_n)-f(x_n)}=\frac{1}{2}$ for every $n$.
:::
