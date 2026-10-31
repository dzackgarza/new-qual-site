---
schema: qual/card@1
id: P-PRACT20-W3-05
kind: problem
title: Sum of the power series $\sum n^2x^n$
classification:
  areas:
  - prelim
  topics:
  - Power Series
relations: []
review: draft
---

::: {.problem}
Find the value of $\sum_{n=1}^{\infty} n^{2} x^{n}$ wherever the series converges.
:::

::: {.solution}
The series $\sum n^2x^n$ has radius of convergence $1$ by the ratio test, and it diverges at $x=\pm1$ because its terms do not tend to $0$; so it converges exactly for $\abs{x}<1$. The geometric series converges for $\abs{x}<1$, and we can differentiate it term by term without changing the radius of convergence. We see

$$
\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n,\tag{1}
$$

$$
\implies\frac{1}{(1-x)^2}=\sum_{n=1}^{\infty}nx^{n-1},\tag{2}
$$

$$
\implies\frac{2}{(1-x)^3}=\sum_{n=2}^{\infty}n(n-1)x^{n-2}.\tag{3}
$$

Since $n^2=n(n-1)+n$, our series can be rewritten

$$
\sum_{n=1}^{\infty}n^2x^n=\left(\sum_{n=2}^{\infty}n(n-1)x^n\right)+\left(\sum_{n=1}^{\infty}nx^n\right).
$$

These two sums are evaluated by multiplying (3) by $x^2$ and (2) by $x$. Thus

$$
\sum_{n=1}^{\infty}n^2x^n=\frac{2x^2}{(1-x)^3}+\frac{x}{(1-x)^2}=\frac{x+x^2}{(1-x)^3}.
$$
:::
