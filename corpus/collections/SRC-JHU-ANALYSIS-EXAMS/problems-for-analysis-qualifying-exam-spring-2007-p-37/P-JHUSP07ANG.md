---
schema: qual/card@1
id: P-JHUSP07ANG
kind: problem
title: 'Weakly convergent $L^2$ sequences with unbounded norms'
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 7 of the JHU Analysis Qualifying Exam, Spring 2007, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Suppose $(f_n)$ is a sequence in $L^2(\mathbb R)$ that converges weakly to $f\in L^2(\mathbb R)$. Is it possible that
\[
\|f_n\|_{L^2}\longrightarrow\infty?
\]
:::

::: {.solution}
No.

For each $n$, define the bounded linear functional
\[
T_n(g)=\langle f_n,g\rangle_{L^2},
\qquad g\in L^2(\mathbb R).
\]
Weak convergence means that for every fixed $g\in L^2$,
\[
T_n(g)=\langle f_n,g\rangle\longrightarrow\langle f,g\rangle.
\]
Hence for every $g$ the scalar sequence $(T_n(g))$ is bounded. By the Uniform Boundedness Principle,
\[
\sup_n\|T_n\|<\infty.
\]
By the Riesz representation theorem for the Hilbert space $L^2(\mathbb R)$,
\[
\|T_n\|=\|f_n\|_2.
\]
Therefore
\[
\sup_n\|f_n\|_2<\infty.
\]
So a weakly convergent sequence in $L^2$ cannot have norms tending to infinity.
:::
