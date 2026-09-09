---
schema: qual/card@1
id: P-JVAGD
kind: problem
title: 'Layer-cake formula with an absolutely continuous weight: $\int_{\RR}\varphi\circ f\,dx=\int_0^\infty m(\{f>t\})\varphi''(t)\,dt$'
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
  note: Checked against Problem 1 of the JHU Analysis Qualifying Exam, Spring 2017. The statement uses varphi-prime; the card title incorrectly had varphi-double-prime and was corrected.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f:\mathbb R\to[0,\infty)$ be measurable, and let
\[
\varphi:[0,\infty)\to[0,\infty)
\]
be nondecreasing and absolutely continuous on $[0,T]$ for every finite $T$. Assume $\varphi(0)=0$. Prove that
\[
\int_{\mathbb R}\varphi(f(x))\,dx
=
\int_0^\infty m(\{x:f(x)>t\})\varphi'(t)\,dt.
\]
:::

::: {.solution}
Since $\varphi$ is nondecreasing and absolutely continuous on every compact interval, one has
\[
\varphi'(t)\ge0
\qquad\text{for almost every }t\ge0,
\]
and for every $s\ge0$,
\[
\varphi(s)-\varphi(0)=\int_0^s\varphi'(t)\,dt.
\]
Because $\varphi(0)=0$,
\[
\varphi(s)=\int_0^\infty \mathbf1_{\{t<s\}}\varphi'(t)\,dt.
\]
Substituting $s=f(x)$ gives
\[
\varphi(f(x))
=
\int_0^\infty \mathbf1_{\{t<f(x)\}}\varphi'(t)\,dt.
\]
The integrand is nonnegative and measurable on $\mathbb R\times[0,\infty)$, so Tonelli's theorem yields
\[
\begin{aligned}
\int_{\mathbb R}\varphi(f(x))\,dx
&=\int_{\mathbb R}\int_0^\infty
\mathbf1_{\{t<f(x)\}}\varphi'(t)\,dt\,dx\\
&=\int_0^\infty\int_{\mathbb R}
\mathbf1_{\{f(x)>t\}}\,dx\,\varphi'(t)\,dt\\
&=\int_0^\infty
m(\{x:f(x)>t\})\varphi'(t)\,dt.
\end{aligned}
\]
The equality is valid in $[0,\infty]$, so no separate integrability assumption is needed.
:::
