---
schema: qual/card@1
id: P-JHUSP05ANB
kind: problem
title: "An integral operator on L^1[0,1] with kernel 1/t"
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
  date: 2026-09-08
  note: Checked against Problem 2 of the JHU Analysis Qualifying Exam, Spring 2005, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Suppose that $f\in L^1([0,1])$ and define
\[
g(x)=\int_x^1\frac{f(t)}{t}\,dt.
\]
Show that $g\in L^1([0,1])$ and that
\[
\int_0^1 g(x)\,dx=\int_0^1 f(x)\,dx.
\]
:::

::: {.solution}
Consider first the nonnegative integrand
\[
H(x,t)=\mathbf 1_{\{0\le x\le t\le1\}}\frac{|f(t)|}{t}.
\]
Tonelli's theorem gives
\[
\begin{aligned}
\int_0^1\int_x^1\frac{|f(t)|}{t}\,dt\,dx
&=\int_0^1\int_0^t\frac{|f(t)|}{t}\,dx\,dt\\
&=\int_0^1 |f(t)|\,dt<\infty.
\end{aligned}
\]
Hence for almost every $x$ the defining integral for $g(x)$ is absolutely convergent, and moreover
\[
\int_0^1|g(x)|\,dx
\le
\int_0^1\int_x^1\frac{|f(t)|}{t}\,dt\,dx
\le \|f\|_1.
\]
Thus $g\in L^1([0,1])$.

Since the corresponding signed integrand is absolutely integrable on the triangle $0\le x\le t\le1$, Fubini's theorem applies and yields
\[
\begin{aligned}
\int_0^1g(x)\,dx
&=\int_0^1\int_x^1\frac{f(t)}{t}\,dt\,dx\\
&=\int_0^1\int_0^t\frac{f(t)}{t}\,dx\,dt\\
&=\int_0^1 f(t)\,dt.
\end{aligned}
\]
This proves both claims.
:::
