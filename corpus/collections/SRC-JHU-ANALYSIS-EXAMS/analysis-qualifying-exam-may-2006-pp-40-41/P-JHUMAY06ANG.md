---
schema: qual/card@1
id: P-JHUMAY06ANG
kind: problem
title: 'Separating $L^1$ and $L^2$ on $\RR$ and $(0,1)$'
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
  note: Checked against Problem 7 of the JHU Analysis Qualifying Exam, May 2006, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
(a) Give a function in $L^2(\mathbb R)$ that is not in $L^1(\mathbb R)$.

(b) Give a function in $L^1((0,1))$ that is not in $L^2((0,1))$.
:::

::: {.solution}
For (a), take
\[
f(x)=(1+|x|)^{-3/4}.
\]
Then
\[
|f(x)|^2=(1+|x|)^{-3/2},
\]
which is integrable on $\mathbb R$, while $(1+|x|)^{-3/4}$ is not integrable at infinity. Hence
\[
f\in L^2(\mathbb R)\setminus L^1(\mathbb R).
\]

For (b), take
\[
g(x)=x^{-3/4},
\qquad 0<x<1.
\]
Since $3/4<1$,
\[
\int_0^1x^{-3/4}\,dx<\infty,
\]
so $g\in L^1((0,1))$. But
\[
|g(x)|^2=x^{-3/2},
\]
and
\[
\int_0^1x^{-3/2}\,dx=\infty.
\]
Thus
\[
g\in L^1((0,1))\setminus L^2((0,1)).
\]
:::
