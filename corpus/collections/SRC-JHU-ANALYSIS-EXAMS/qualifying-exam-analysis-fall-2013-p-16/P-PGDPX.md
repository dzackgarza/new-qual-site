---
schema: qual/card@1
id: P-PGDPX
kind: problem
title: Integral equals integral of distribution function
classification:
  areas:
  - real-analysis
  topics:
  - Lebesgue Integration
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved JHU Fall 2013 Analysis qualifying exam packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Let $f \in L^1(\mathbb{R})$ and define $E_\alpha = \{x : |f(x)| > \alpha\}$.
Prove that

$$\int_{\mathbb{R}} |f(x)| \, dx = \int_0^\infty m(E_\alpha) \, d\alpha.$$

::: {.solution}
For every $x\in\mathbb R$,
\[
|f(x)|=\int_0^\infty \mathbf1_{\{\alpha<|f(x)|\}}\,d\alpha.
\]
The integrand
\[
(x,\alpha)\longmapsto \mathbf1_{\{\alpha<|f(x)|\}}
\]
is nonnegative and measurable on $\mathbb R\times(0,\infty)$. Tonelli's theorem therefore gives
\[
\begin{aligned}
\int_{\mathbb R}|f(x)|\,dx
&=\int_{\mathbb R}\int_0^\infty
\mathbf1_{\{\alpha<|f(x)|\}}\,d\alpha\,dx\\
&=\int_0^\infty\int_{\mathbb R}
\mathbf1_{\{|f(x)|>\alpha\}}\,dx\,d\alpha\\
&=\int_0^\infty m(E_\alpha)\,d\alpha.
\end{aligned}
\]
Thus
\[
\boxed{\int_{\mathbb R}|f|=\int_0^\infty m(E_\alpha)\,d\alpha.}
\]
:::
