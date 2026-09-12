---
schema: qual/card@1
id: P-XEEUX
kind: problem
title: Consider the function $f(x) = \frac{x}{1-x^2}$,
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Uniform Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked directly against Problem 1 of the preserved UNL May 2016 qualifying-exam source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
  note: "Replaced the prior continuity argument: it omitted the factor 1+xy in the difference quotient and the structured solution appealed to quotient-continuity despite the problem's epsilon-delta-only instruction."
---

::: {.problem}
Consider
\[
f(x)=\frac{x}{1-x^2},\qquad x\in(0,1).
\]

1. Using only the $\varepsilon$--$\delta$ definition, prove that $f$ is continuous on $(0,1)$.
2. Is $f$ uniformly continuous on $(0,1)$? Justify your answer.
:::

::: {.solution}
<1>1. Prove continuity at an arbitrary $x_0\in(0,1)$ directly from the definition.
::: {.proof}
Fix $x_0\in(0,1)$ and $\varepsilon>0$. For $x\in(0,1)$,
\[
\begin{aligned}
|f(x)-f(x_0)|
&=\left|\frac{x}{1-x^2}-\frac{x_0}{1-x_0^2}\right|\\
&=\frac{|x-x_0|\,|1+x x_0|}{(1-x^2)(1-x_0^2)}.
\end{aligned}
\]
Choose
\[
\delta
:=\min\left\{\frac{1-x_0}{2},\frac{\varepsilon(1-x_0)^2}{4}\right\}.
\]
If $|x-x_0|<\delta$, then
\[
x<x_0+\frac{1-x_0}{2}=\frac{1+x_0}{2},
\]
so
\[
1-x>\frac{1-x_0}{2}.
\]
Also $1+x\ge1$, $1+x_0\ge1$, and $|1+x x_0|\le2$. Hence
\[
(1-x^2)(1-x_0^2)
=(1-x)(1+x)(1-x_0)(1+x_0)
\ge \frac{(1-x_0)^2}{2}.
\]
Therefore
\[
|f(x)-f(x_0)|
\le \frac{4|x-x_0|}{(1-x_0)^2}
<\varepsilon.
\]
Thus $f$ is continuous at $x_0$. Since $x_0$ was arbitrary, $f$ is continuous on $(0,1)$.
:::

<1>2. $f$ is not uniformly continuous on $(0,1)$.
::: {.proof}
For $n\ge1$, set
\[
x_n=\frac{n}{n+1},
\qquad
y_n=\frac{n+1}{n+2}.
\]
Then
\[
|x_n-y_n|=\frac{1}{(n+1)(n+2)}\longrightarrow0.
\]
On the other hand,
\[
f(x_n)=\frac{n(n+1)}{2n+1},
\qquad
f(y_n)=\frac{(n+1)(n+2)}{2n+3},
\]
so
\[
|f(y_n)-f(x_n)|
=\frac{2(n+1)^2}{(2n+1)(2n+3)}
\longrightarrow\frac12.
\]
If $f$ were uniformly continuous, taking $\varepsilon=1/4$ would force
\[
|f(y_n)-f(x_n)|<\frac14
\]
for all sufficiently large $n$, because $|x_n-y_n|\to0$. This contradicts the displayed limit. Therefore
\[
\boxed{f\text{ is not uniformly continuous on }(0,1)}.
\]
:::
:::
