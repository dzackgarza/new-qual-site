---
schema: qual/card@1
id: P-JHUSP05ANA
kind: problem
title: "Smoothness and decay of the Fourier transform of e^{-|x|}"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the JHU Analysis Qualifying Exam, Spring 2005, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let
\[
f(x)=e^{-|x|},\qquad x\in\mathbb R.
\]

(a) Is $\widehat f\in C^\infty(\mathbb R)$? Prove your answer.

(b) Prove that
\[
|\widehat f(\xi)|\longrightarrow0
\qquad(|\xi|\to\infty).
\]
:::

::: {.solution}
<1>1. The Fourier transform is smooth.
::: {.proof}
For every integer $k\ge0$,
\[
\int_{\mathbb R}|x|^k e^{-|x|}\,dx<\infty.
\]
Thus $x^k f(x)\in L^1(\mathbb R)$ for every $k$.

Using the convention
\[
\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx,
\]
the $k$th formal derivative is
\[
\frac{d^k}{d\xi^k}\widehat f(\xi)
=\int_{\mathbb R}(-2\pi i x)^k f(x)e^{-2\pi i x\xi}\,dx.
\]
For each fixed $k$, the absolute value of the integrand is bounded by
\[
(2\pi)^k|x|^k e^{-|x|}\in L^1(\mathbb R).
\]
Dominated convergence therefore justifies differentiation under the integral sign, and the resulting derivative is continuous by another application of dominated convergence. Hence
\[
\widehat f\in C^\infty(\mathbb R).
\]
The same conclusion holds for any of the standard Fourier-transform normalizations, with the obvious change in constants.
:::

<1>2. The Fourier transform vanishes at infinity.
::: {.proof}
Since $f=e^{-|x|}\in L^1(\mathbb R)$, the Riemann--Lebesgue lemma gives
\[
\widehat f(\xi)\longrightarrow0
\qquad(|\xi|\to\infty).
\]
For completeness, this follows by approximating $f$ in $L^1$ by a function $g\in C_c^1(\mathbb R)$. For such $g$, integration by parts gives
\[
|\widehat g(\xi)|\le \frac{\|g'\|_1}{2\pi|\xi|}
\qquad(\xi\ne0),
\]
while
\[
|\widehat f(\xi)-\widehat g(\xi)|\le\|f-g\|_1.
\]
First choose $g$ so that the latter bound is small, then let $|\xi|\to\infty$. This proves the claimed decay.
:::
:::
