---
schema: qual/card@1
id: P-JHUFA01RAC
kind: problem
title: '$L^{4/3}$ boundedness plus convergence in measure implies $L^1$ convergence'
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
  note: Checked against Problem 3 of the JHU Real Analysis Qualifying Exam, Fall 2001, in the preserved exam compilation.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $(f_n)$ be real-valued functions in $L^{4/3}(0,1)$ such that $f_n\to0$ in measure and
\[
\int_0^1 |f_n(x)|^{4/3}\,dx\le1
\qquad(n\ge1).
\]
Show that
\[
\int_0^1|f_n(x)|\,dx\longrightarrow0.
\]
:::

::: {.solution}
Fix $\varepsilon>0$. Choose $\eta=\varepsilon/2$ and split
\[
\int_0^1|f_n|
=
\int_{\{|f_n|\le\eta\}}|f_n|
+
\int_{\{|f_n|>\eta\}}|f_n|.
\]
The first term satisfies
\[
\int_{\{|f_n|\le\eta\}}|f_n|\le\eta=\frac\varepsilon2.
\]
For the second term, Hölder's inequality with exponents $4/3$ and $4$ gives
\[
\begin{aligned}
\int_{\{|f_n|>\eta\}}|f_n|
&\le
\left(\int_0^1|f_n|^{4/3}\right)^{3/4}
 m\{|f_n|>\eta\}^{1/4}\\
&\le m\{|f_n|>\eta\}^{1/4}.
\end{aligned}
\]
Because $f_n\to0$ in measure,
\[
m\{|f_n|>\eta\}\longrightarrow0.
\]
Hence for all sufficiently large $n$,
\[
m\{|f_n|>\eta\}^{1/4}<\frac\varepsilon2.
\]
Therefore
\[
\int_0^1|f_n|<\varepsilon
\]
for all sufficiently large $n$, proving $f_n\to0$ in $L^1(0,1)$.
:::
