---
schema: qual/card@1
id: P-JHUU51RA1
kind: problem
title: "Quantitative Riemann-Lebesgue decay under vanishing endpoint conditions"
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
  note: Checked against entry 1 of the JHU Real Analysis Qualifying Exam on p. 51 of the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f:[0,2]\to\mathbb R$ be $C^1$ and suppose
\[
f(0)=f'(0)=f(2)=f'(2)=0.
\]
Prove that for every $\varepsilon>0$ there exists $t_\varepsilon>0$ such that
\[
\left|\int_0^2 f(x)e^{itx}\,dx\right|\le\frac{\varepsilon}{t}
\qquad(t\ge t_\varepsilon).
\]
:::

::: {.solution}
For $t>0$, integration by parts and the endpoint conditions on $f$ give
\[
\begin{aligned}
\int_0^2 f(x)e^{itx}\,dx
&=\left[\frac{f(x)e^{itx}}{it}\right]_0^2
-\frac1{it}\int_0^2 f'(x)e^{itx}\,dx\\
&=-\frac1{it}\int_0^2 f'(x)e^{itx}\,dx.
\end{aligned}
\]
Since $f'$ is continuous on $[0,2]$, it belongs to $L^1([0,2])$. By the Riemann--Lebesgue lemma,
\[
\int_0^2 f'(x)e^{itx}\,dx\longrightarrow0
\qquad(t\to\infty).
\]
Therefore, for the given $\varepsilon>0$, there exists $t_\varepsilon>0$ such that
\[
\left|\int_0^2 f'(x)e^{itx}\,dx\right|\le\varepsilon
\qquad(t\ge t_\varepsilon).
\]
Substituting into the integration-by-parts identity yields
\[
\left|\int_0^2 f(x)e^{itx}\,dx\right|
\le\frac{\varepsilon}{t}
\qquad(t\ge t_\varepsilon).
\]
The conditions $f'(0)=f'(2)=0$ are stronger than needed for this argument; the stated result follows already from $f(0)=f(2)=0$ and $f'\in L^1$.
:::
