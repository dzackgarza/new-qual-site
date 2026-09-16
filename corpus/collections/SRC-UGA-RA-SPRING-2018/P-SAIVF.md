---
schema: qual/card@1
id: P-SAIVF
kind: problem
title: A function in $L^2([0,1])$ orthogonal to every polynomial vanishes a.e.
classification:
  areas:
  - real-analysis
  topics:
  - Stone-Weierstrass
  - Density
  - L²
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the UGA Spring 2018 real-analysis qualifying exam recorded by SRC-UGA-RA-SPRING-2018.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---


::: {.problem}
Let $f\in L^2([0,1])$ and suppose
\[
\int_0^1 f(x)x^n\,dx=0
\qquad\text{for every integer }n\ge0.
\]
Show that $f=0$ almost everywhere.
:::

::: {.solution}
By linearity,
\[
\int_0^1 f(x)p(x)\,dx=0
\]
for every polynomial $p$.

Polynomials are dense in $C([0,1])$ by the Weierstrass approximation theorem, and $C([0,1])$ is dense in $L^2([0,1])$. Hence polynomials are dense in $L^2([0,1])$.

Choose polynomials $p_j$ such that
\[
\|f-p_j\|_2\longrightarrow0.
\]
Since $f$ is orthogonal to every polynomial,
\[
\langle f,p_j\rangle=0.
\]
Therefore
\[
\begin{aligned}
\|f\|_2^2
&=\langle f,f\rangle\\
&=\langle f,f-p_j\rangle\\
&\le \|f\|_2\,\|f-p_j\|_2
\end{aligned}
\]
by Cauchy--Schwarz. Letting $j\to\infty$ gives
\[
\|f\|_2^2=0.
\]
Hence
\[
\boxed{f=0\text{ almost everywhere}.}
\]
:::
