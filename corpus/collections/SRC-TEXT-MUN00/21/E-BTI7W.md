---
schema: qual/card@1
id: E-BTI7W
kind: problem
title: Pointwise but not uniform convergence to the zero function
classification:
  areas:
  - topology
  topics:
  - Uniform Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $f_n: \mathbb{R} \to \mathbb{R}$ be the function

$$
f_n(x) = \frac{1}{n^3[x - (1/n)]^2 + 1}.
$$

Let $f: \mathbb{R} \to \mathbb{R}$ be the zero function.

(a) Show that $f_n(x) \to f(x)$ for each $x \in \mathbb{R}$.

(b) Show that $f_n$ does not converge uniformly to $f$.
(This shows that the converse of Theorem 21.6 does not hold; the limit function $f$ may be continuous even though the convergence is not uniform.)
:::

::: {.solution}
(a) Fix $x\in\mathbb R$. If $x=0$, then
\[
f_n(0)=\frac1{n+1}\longrightarrow0.
\]
If $x\ne0$, then $x-1/n\to x$, so for all sufficiently large $n$,
\[
|x-1/n|\ge |x|/2.
\]
Hence
\[
0\le f_n(x)\le\frac1{n^3x^2/4+1}\longrightarrow0.
\]
Thus $f_n(x)\to0$ for every fixed $x$.

(b) At the moving point $x=1/n$,
\[
f_n(1/n)=1.
\]
Therefore
\[
\sup_{x\in\mathbb R}|f_n(x)-0|=1
\]
for every $n$. In particular the supremum error does not tend to zero, so the convergence is not uniform.
:::
