---
schema: qual/card@1
id: P-JHUFA11ANH
kind: problem
title: 'No convolution identity in $L^1(\RR^n)$'
classification:
  areas:
  - real-analysis
  topics:
  - L1 Spaces
  - Integration
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 8 of the JHU Analysis Qualifying Exam, September 2011, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Show that there is no $I\in L^1(\mathbb R^n)$ such that
\[
f*I=f
\qquad\text{for every }f\in L^1(\mathbb R^n).
\]
:::

::: {.solution}
Suppose, for contradiction, that such an $I$ exists.
Taking Fourier transforms and using
\[
\widehat{f*I}=\widehat f\,\widehat I,
\]
we obtain
\[
\widehat f(\xi)\widehat I(\xi)=\widehat f(\xi)
\qquad\text{for every }f\in L^1(\mathbb R^n)
\]
and every $\xi\in\mathbb R^n$.

Choose one fixed Gaussian $f(x)=e^{-\pi|x|^2}$.
It belongs to $L^1(\mathbb R^n)$ and its Fourier transform is another Gaussian, in particular
\[
\widehat f(\xi)\ne0
\qquad\text{for every }\xi.
\]
Therefore
\[
\widehat I(\xi)=1
\qquad\text{for every }\xi\in\mathbb R^n.
\]
But $I\in L^1(\mathbb R^n)$, so the Riemann--Lebesgue lemma implies
\[
\widehat I(\xi)\longrightarrow0
\qquad(|\xi|\to\infty),
\]
contradicting $\widehat I\equiv1$.
Hence no such convolution identity element exists in $L^1(\mathbb R^n)$.
:::
