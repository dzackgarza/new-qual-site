---
schema: qual/card@1
id: P-JHUSP05ANC
kind: problem
title: $L^p$ inclusions on finite- and infinite-measure spaces
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the JHU Analysis Qualifying Exam, Spring 2005, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Prove or find a counterexample to each statement:

(a) $L^2(\mathbb R)\subset L^1(\mathbb R)$;

(b) $L^1(\mathbb R)\subset L^2(\mathbb R)$;

(c) $L^2([0,1])\subset L^1([0,1])$;

(d) $L^1([0,1])\subset L^2([0,1])$.
:::

::: {.solution}
The answers are: (a) false, (b) false, (c) true, and (d) false.

<1>1. Statement (a) is false.
::: {.proof}
Let
\[
f(x)=\frac{\mathbf 1_{[1,\infty)}(x)}{x}.
\]
Then
\[
\int_1^\infty |f(x)|^2\,dx=\int_1^\infty x^{-2}\,dx<\infty,
\]
so $f\in L^2(\mathbb R)$, whereas
\[
\int_1^\infty |f(x)|\,dx=\int_1^\infty x^{-1}\,dx=\infty.
\]
Thus $f\notin L^1(\mathbb R)$.
:::

<1>2. Statement (b) is false.
::: {.proof}
Let
\[
g(x)=x^{-2/3}\mathbf 1_{(0,1)}(x).
\]
Then
\[
\int_0^1 |g(x)|\,dx=\int_0^1x^{-2/3}\,dx<\infty,
\]
so $g\in L^1(\mathbb R)$, but
\[
\int_0^1 |g(x)|^2\,dx=\int_0^1x^{-4/3}\,dx=\infty.
\]
Hence $g\notin L^2(\mathbb R)$.
:::

<1>3. Statement (c) is true.
::: {.proof}
By Cauchy--Schwarz,
\[
\|f\|_{L^1([0,1])}
=\int_0^1|f(x)|\cdot1\,dx
\le \|f\|_{L^2([0,1])}\|1\|_{L^2([0,1])}
=\|f\|_2.
\]
Thus every $L^2([0,1])$ function belongs to $L^1([0,1])$.
:::

<1>4. Statement (d) is false.
::: {.proof}
The same function
\[
g(x)=x^{-2/3},\qquad 0<x<1,
\]
belongs to $L^1([0,1])$ but not to $L^2([0,1])$, by the calculation in <1>2.
:::
:::
