---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-06
kind: problem
title: Uniform continuity of the logarithm on $(0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Continuity
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
(January 2009 #2a, obfuscated) Is $f(x)=\ln x$ uniformly continuous on $(0,1]$?
Prove your answer.
:::

::: {.solution}

::: pf

::: pf-step

The function $\ln:(0,1]\to\RR$ is not uniformly continuous.

::: pf-proof

For every integer $n\geq1$, set $x_n=e^{-n}$ and $y_n=e^{-(n+1)}$. Both points belong to $(0,1]$, and
$$
\abs{x_n-y_n}=(1-e^{-1})e^{-n}\longrightarrow0,
\qquad
\abs{\ln x_n-\ln y_n}=1.
$$
Suppose that $\ln$ were uniformly continuous. Applying its definition with $\varepsilon=1/2$ would give $\delta>0$ such that $\abs{x-y}<\delta$ implies $\abs{\ln x-\ln y}<1/2$. Choosing $n$ sufficiently large that $\abs{x_n-y_n}<\delta$ contradicts the displayed equality.

:::

:::

:::

:::

::: {.remark}
Another example is $g:(0,\pi]\to\RR$, $g(x)=\sin(1/x)$. For $n\geq1$, take $u_n=(\pi/2+2\pi n)^{-1}$ and $v_n=(3\pi/2+2\pi n)^{-1}$. Both lie in $(0,\pi]$, and $\abs{u_n-v_n}\to0$, whereas $g(u_n)=1$ and $g(v_n)=-1$. Hence $g$ is not uniformly continuous.
:::
