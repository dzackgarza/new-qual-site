---
schema: qual/card@1
id: P-PAQ4K
kind: problem
title: Convergence of positive continuous functions and Fatou-type inequality
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Assume that $f_1, f_2, \ldots$ is a sequence of positive continuous functions defined on $[0,1]$ with

$$f(x) = \lim_{n \to \infty} f_n(x) \text{ for every } x \in [0,1]$$

and

$$\int_0^1 f_n(x) \, dx = 1.$$

(a) Is it always true that $\int_0^1 f(x) \, dx \leq 1$?
Provide a proof if it is true or provide a counterexample if it is false.

(b) Is it always true that $\int_0^1 f(x) \, dx \geq 1$?
Provide a proof if it is true or provide a counterexample if it is false.
:::

::: {.solution}
<1>1. (a) Yes: $\int_0^1f\le1$.

::: {.proof}
The $f_n$ are nonnegative and measurable, and $f=\liminf_nf_n$ pointwise, so Fatou's lemma gives $\int_0^1f\le\liminf_n\int_0^1f_n=1$.
:::

<1>2. (b) No: $g_n\da\bigl(1-\frac1n\bigr)T_n+\frac1n$, with $T_n$ the tent of height $2n$ on $[0,\frac1n]$, is a counterexample.

::: {.proof}
Let $T_n(x)=4n^2x$ on $[0,\frac1{2n}]$, $T_n(x)=4n-4n^2x$ on $[\frac1{2n},\frac1n]$, and $T_n=0$ on $[\frac1n,1]$; it is continuous with $\int_0^1T_n=\frac12\cdot\frac1n\cdot2n=1$. So $g_n$ is continuous, $g_n\ge\frac1n>0$, and $\int_0^1g_n=\bigl(1-\frac1n\bigr)+\frac1n=1$. For $x\in(0,1]$, $T_n(x)=0$ once $n>1/x$, and $T_n(0)=0$, so $g_n(x)=\frac1n\to0$ for every $x$. The limit is $f=0$, with $\int_0^1f=0<1$.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 answer parts (a) and (b).
:::
:::
