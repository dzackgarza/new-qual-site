---
schema: qual/card@1
id: P-P6D6X
kind: problem
title: $f_n\to f$ almost everywhere in $L^1$ with $\int|f_n|\to\int|f|$ implies $\int
  f_n\to\int f$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Fatou
  - L¹
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the UGA Spring 2018 real-analysis qualifying exam recorded by SRC-UGA-RA-SPRING-2018.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---


::: {.problem}
Suppose that

- $f_n,f\in L^1$,
- $f_n\to f$ almost everywhere, and
- $\int |f_n|\to\int |f|$.

Show that $\int f_n\to\int f$.
:::

::: {.solution}
Define
\[
g_n:=|f_n|+|f|-|f_n-f|.
\]
By the triangle inequality,
\[
g_n\ge0.
\]
Since $f_n\to f$ almost everywhere,
\[
g_n\longrightarrow 2|f|
\qquad\text{almost everywhere}.
\]
Fatou's lemma therefore gives
\[
2\int |f|
\le \liminf_{n\to\infty}\int g_n.
\]
But
\[
\int g_n
=\int|f_n|+\int|f|-\int|f_n-f|.
\]
Using the hypothesis
\[
\int|f_n|\to\int|f|,
\]
we obtain
\[
2\int|f|
\le
2\int|f|-\limsup_{n\to\infty}\int|f_n-f|.
\]
Hence
\[
\limsup_{n\to\infty}\int|f_n-f|\le0.
\]
Since these integrals are nonnegative,
\[
\int|f_n-f|\longrightarrow0.
\]
Thus $f_n\to f$ in $L^1$. Finally,
\[
\left|\int f_n-\int f\right|
\le \int|f_n-f|\longrightarrow0,
\]
so
\[
\boxed{\int f_n\longrightarrow\int f.}
\]
:::
