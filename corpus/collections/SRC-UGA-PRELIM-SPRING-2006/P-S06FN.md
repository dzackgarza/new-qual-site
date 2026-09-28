---
schema: qual/card@1
id: P-S06FN
kind: problem
title: $x/(x+n)$ converges pointwise to $0$ on $[0,\infty)$ but not uniformly
classification:
  areas:
  - prelim
  topics:
  - Uniform Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
For each positive integer $n$, let $f_n(x) = \frac{x}{x+n}$ for $x \in [0, \infty)$.
Show that the sequence of functions $\{f_n\}$ converges pointwise on $[0, \infty)$ to the $0$-function but does not converge uniformly.
:::


::: {.solution}
<1>1. For every fixed $x\in[0,\infty)$,
\[
\lim_{n\to\infty} f_n(x)=0.
\]
::: {.proof}
Fix $x\ge0$. Then
\[
f_n(x)=\frac{x}{x+n}.
\]
The numerator is fixed while the denominator tends to $\infty$, so the quotient tends to $0$.
:::

<1>2. Hence $f_n$ converges pointwise on $[0,\infty)$ to the zero function.
::: {.proof}
This is exactly the assertion of <1>1 for every point $x$ in the domain.
:::

<1>3. The convergence is not uniform.
::: {.proof}
Take $\varepsilon=1/4$. For every $n\ge1$, choose $x=n$. Then
\[
|f_n(n)-0|=\frac{n}{n+n}=\frac12>\frac14.
\]
Thus there is no $N$ such that for every $n\ge N$ and every $x\ge0$ one has $|f_n(x)|<1/4$. This is the negation of uniform convergence to $0$.
:::
:::
