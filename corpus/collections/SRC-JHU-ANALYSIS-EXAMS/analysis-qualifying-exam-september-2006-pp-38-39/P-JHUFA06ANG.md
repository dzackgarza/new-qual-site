---
schema: qual/card@1
id: P-JHUFA06ANG
kind: problem
title: '$L^2$ boundedness and vanishing $L^1$ norm imply weak convergence to $0$'
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
  note: Checked against Problem 7 of the JHU Analysis Qualifying Exam, September 2006, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $(f_j)$ be functions in $L^2([0,1])$ satisfying
\[
\int_0^1 |f_j|\le \frac1j,
\qquad
\int_0^1 |f_j|^2\le1.
\]
Prove that $f_j\rightharpoonup0$ weakly in $L^2([0,1])$.
:::

::: {.solution}
Fix $g\in L^2([0,1])$ and $\varepsilon>0$. For $M>0$, define the truncation
\[
g_M=g\mathbf1_{\{|g|\le M\}}.
\]
Then $g_M\in L^\infty$ and
\[
\|g-g_M\|_2\longrightarrow0
\qquad(M\to\infty).
\]
Choose $M$ so large that
\[
\|g-g_M\|_2<\frac{\varepsilon}{2}.
\]
For every $j$, Cauchy--Schwarz and the uniform $L^2$ bound give
\[
\left|\int_0^1 f_j(g-g_M)\right|
\le \|f_j\|_2\|g-g_M\|_2
<\frac{\varepsilon}{2}.
\]
On the bounded part,
\[
\left|\int_0^1 f_jg_M\right|
\le \|g_M\|_\infty\|f_j\|_1
\le \frac{M}{j}.
\]
Hence for all sufficiently large $j$, this is $<\varepsilon/2$. Therefore
\[
\left|\int_0^1 f_j g\right|<\varepsilon
\]
for all sufficiently large $j$. Since $g\in L^2([0,1])$ was arbitrary,
\[
f_j\rightharpoonup0
\qquad\text{in }L^2([0,1]).
\]
:::
