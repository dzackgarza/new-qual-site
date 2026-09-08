---
schema: qual/card@1
id: P-JHUFA11ANF
kind: problem
title: "Fourier-transform integrals over finite- and infinite-measure sets"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 6 of the JHU Analysis Qualifying Exam, September 2011, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f_j,f\in L^2(\mathbb R^n)$ and suppose
\[
\|f_j-f\|_2\longrightarrow0.
\]

(a) If $\Omega\subset\mathbb R^n$ has finite measure, prove that
\[
\int_\Omega \widehat f_j(\xi)\,d\xi\longrightarrow\int_\Omega \widehat f(\xi)\,d\xi.
\]

(b) If $|\Omega|=\infty$, must the same conclusion hold? Prove your answer or give a counterexample.
:::

::: {.solution}
<1>1. Finite-measure sets.
::: {.proof}
By Plancherel's theorem,
\[
\|\widehat f_j-\widehat f\|_2=\|f_j-f\|_2\longrightarrow0
\]
for the unitary Fourier-transform normalization, and in any standard normalization the two norms differ only by a fixed constant. Since $|\Omega|<\infty$, Cauchy--Schwarz gives
\[
\left|\int_\Omega(\widehat f_j-\widehat f)(\xi)\,d\xi\right|
\le |\Omega|^{1/2}\,\|\widehat f_j-\widehat f\|_2\longrightarrow0.
\]
This proves part (a).
:::

<1>2. Infinite-measure sets: the conclusion can fail.
::: {.proof}
Assume $|\Omega|=\infty$. Choose measurable sets $E_j\subset\Omega$ with
\[
0<|E_j|<\infty,
\qquad
|E_j|\longrightarrow\infty.
\]
Define
\[
g_j(\xi)=\frac{\mathbf1_{E_j}(\xi)}{|E_j|}.
\]
Then
\[
\|g_j\|_2^2=\frac1{|E_j|}\longrightarrow0,
\qquad
\int_\Omega g_j(\xi)\,d\xi=1.
\]
By Plancherel, for each $j$ there exists $f_j\in L^2(\mathbb R^n)$ with Fourier transform $g_j$. Taking $f=0$, we have
\[
\|f_j-f\|_2\to0,
\]
but
\[
\int_\Omega \widehat f_j=1
\qquad\text{for every }j,
\]
while $\int_\Omega\widehat f=0$. Thus the conclusion in part (a) need not hold when $|\Omega|=\infty$.
:::
:::
