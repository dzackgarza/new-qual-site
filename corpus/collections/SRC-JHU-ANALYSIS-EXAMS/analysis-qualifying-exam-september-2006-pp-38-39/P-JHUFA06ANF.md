---
schema: qual/card@1
id: P-JHUFA06ANF
kind: problem
title: 'The oscillatory integral $\int_0^2 f(x)e^{itx}\,dx$ is $o(1/t)$ under endpoint vanishing'
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
  note: Checked against Problem 6 of the JHU Analysis Qualifying Exam, September 2006, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Suppose $f\in C^1([0,2])$ and
$$
f(0)=f'(0)=f(2)=f'(2)=0.
$$
Prove that for every $\varepsilon>0$ there exists $T_\varepsilon$ such that for all $t>T_\varepsilon$,
$$
\abs{\int_0^2 f(x)e^{itx}\,dx}\le \frac{\varepsilon}{t}.
$$
:::

::: {.solution}
Since $f(0)=f(2)=0$, integration by parts gives, for $t\ne0$,
$$
\int_0^2 f(x)e^{itx}\,dx
=-\frac1{it}\int_0^2 f'(x)e^{itx}\,dx.
$$
Because $f'\in C([0,2])\subset L^1([0,2])$, the Riemann--Lebesgue lemma yields
$$
\int_0^2 f'(x)e^{itx}\,dx\longrightarrow0
\qquad(t\to\infty).
$$
Hence for the given $\varepsilon>0$ there exists $T_\varepsilon$ such that
$$
\abs{\int_0^2 f'(x)e^{itx}\,dx}<\varepsilon
\qquad(t>T_\varepsilon).
$$
Therefore, for $t>T_\varepsilon$,
$$
\abs{\int_0^2 f(x)e^{itx}\,dx}
=\frac1t\abs{\int_0^2 f'(x)e^{itx}\,dx}
<\frac{\varepsilon}{t}.
$$
This proves the claim.
:::
