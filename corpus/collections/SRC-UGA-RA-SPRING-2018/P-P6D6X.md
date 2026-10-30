---
schema: qual/card@1
id: P-P6D6X
kind: problem
title: $f_n\to f$ almost everywhere in $L^1$ with $\int\abs{f_n}\to\int\abs{f}$ implies $\int f_n\to\int f$
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
- $\int \abs{f_n}\to\int \abs{f}$.

Show that $\int f_n\to\int f$.
:::

::: {.solution}
Define
$$
g_n:=\abs{f_n}+\abs{f}-\abs{f_n-f}.
$$
By the triangle inequality,
$$
g_n\ge0.
$$
Since $f_n\to f$ almost everywhere,
$$
g_n\longrightarrow 2\abs{f}
\qquad\text{almost everywhere}.
$$
Fatou's lemma therefore gives
$$
2\int \abs{f}
\le \liminf_{n\to\infty}\int g_n.
$$
But
$$
\int g_n
=\int\abs{f_n}+\int\abs{f}-\int\abs{f_n-f}.
$$
Using the hypothesis
$$
\int\abs{f_n}\to\int\abs{f},
$$
we obtain
$$
2\int\abs{f}
\le
2\int\abs{f}-\limsup_{n\to\infty}\int\abs{f_n-f}.
$$
Hence
$$
\limsup_{n\to\infty}\int\abs{f_n-f}\le0.
$$
Since these integrals are nonnegative,
$$
\int\abs{f_n-f}\longrightarrow0.
$$
Thus $f_n\to f$ in $L^1$. Finally,
$$
\abs{\int f_n-\int f}
\le \int\abs{f_n-f}\longrightarrow0,
$$
so
$$
\boxed{\int f_n\longrightarrow\int f.}
$$
:::
