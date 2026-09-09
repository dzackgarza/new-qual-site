---
schema: qual/card@1
id: P-EA67C
kind: problem
title: Absolute continuity of the Lebesgue integral
classification:
  areas:
  - real-analysis
  topics:
  - Absolute Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 1 of the Spring 2016 JHU analysis qualifying exam in the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Prove the absolute continuity of the Lebesgue integral; in other words, prove that if $f$ is integrable on $\mathbb{R}^d$, then for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$\int_E |f| < \epsilon \quad \text{whenever} \quad m(E) < \delta.$$

::: solution
<1>1. Truncate the integrable function.
::: proof
Fix $\varepsilon>0$. Since $f\in L^1(\mathbb R^d)$,
\[
\int_{\{|f|>M\}}|f|\,dx\longrightarrow0
\qquad(M\to\infty).
\]
Choose $M>0$ so large that
\[
\int_{\{|f|>M\}}|f|<\frac\varepsilon2.
\]
:::

<1>2. Control the integral on a small measurable set.
::: proof
Let
\[
\delta:=\frac{\varepsilon}{2M}.
\]
If $m(E)<\delta$, split
\[
E=E\cap\{|f|\le M\}\;\cup\;E\cap\{|f|>M\}.
\]
Then
\[
\begin{aligned}
\int_E|f|
&\le \int_{E\cap\{|f|\le M\}}|f|
+\int_{\{|f|>M\}}|f|\\
&\le M\,m(E)+\frac\varepsilon2\\
&<M\delta+\frac\varepsilon2
=\varepsilon.
\end{aligned}
\]
Thus
\[
\boxed{
m(E)<\delta\Longrightarrow\int_E|f|<\varepsilon.}
\]
:::
:::
