---
schema: qual/card@1
id: P-JHUMAY11ANK
kind: problem
title: "Schur's test with weights"
classification:
  areas:
  - real-analysis
  topics:
  - Operator Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the JHU Analysis Qualifying Exam, May 2011, in the preserved exam collection.
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
Tf(x)=\int_{\mathbb R^n}K(x,y)f(y)\,dy,
\]
where $K\ge0$ is measurable. Suppose there are measurable functions $p,q>0$ and constants $\alpha,\beta>0$ such that
\[
\int K(x,y)q(y)\,dy\le\alpha p(x)
\]
for almost every $x$, and
\[
\int p(x)K(x,y)\,dx\le\beta q(y)
\]
for almost every $y$. Prove
\[
\|Tf\|_2\le\sqrt{\alpha\beta}\,\|f\|_2.
\]
:::

::: {.solution}
For almost every $x$, weighted Cauchy--Schwarz gives
\[
\begin{aligned}
|Tf(x)|^2
&=\left|\int K(x,y)^{1/2}q(y)^{1/2}\,K(x,y)^{1/2}q(y)^{-1/2}f(y)\,dy\right|^2\\
&\le\left(\int K(x,y)q(y)\,dy\right)
\left(\int K(x,y)\frac{|f(y)|^2}{q(y)}\,dy\right)\\
&\le\alpha p(x)\int K(x,y)\frac{|f(y)|^2}{q(y)}\,dy.
\end{aligned}
\]
Integrating in $x$ and applying Tonelli,
\[
\begin{aligned}
\|Tf\|_2^2
&\le\alpha\int\int p(x)K(x,y)\frac{|f(y)|^2}{q(y)}\,dy\,dx\\
&=\alpha\int\frac{|f(y)|^2}{q(y)}\left(\int p(x)K(x,y)\,dx\right)dy\\
&\le\alpha\beta\int|f(y)|^2\,dy.
\end{aligned}
\]
Taking square roots gives the claimed estimate.
:::
