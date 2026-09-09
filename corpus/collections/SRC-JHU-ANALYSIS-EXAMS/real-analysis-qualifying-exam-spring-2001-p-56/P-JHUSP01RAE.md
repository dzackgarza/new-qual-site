---
schema: qual/card@1
id: P-JHUSP01RAE
kind: problem
title: "Integral operators with continuous kernel map the unit ball of C[0,1] to a precompact set"
classification:
  areas:
  - real-analysis
  topics:
  - Compact Operators
  - Integral Operators
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the JHU Real Analysis Qualifying Exam, Spring 2001, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $K\in C([0,1]\times[0,1])$ and define
\[
Tf(x)=\int_0^1K(x,y)f(y)\,dy
\]
for $f\in C([0,1])$. Prove that $Tf\in C([0,1])$. Moreover, prove that
\[
\Omega=\{Tf:\|f\|_\infty\le1\}
\]
is precompact in $C([0,1])$ with the supremum norm.
:::

::: {.solution}
Fix $f\in C([0,1])$. Since $K$ is uniformly continuous on the compact square, if $x_n\to x$, then
\[
\sup_{y\in[0,1]}|K(x_n,y)-K(x,y)|\longrightarrow0.
\]
Hence
\[
|Tf(x_n)-Tf(x)|
\le\|f\|_\infty\sup_y|K(x_n,y)-K(x,y)|\longrightarrow0.
\]
Thus $Tf$ is continuous.

Now let $\|f\|_\infty\le1$. Since $K$ is bounded,
\[
|Tf(x)|\le\int_0^1|K(x,y)|\,dy\le\|K\|_\infty,
\]
so the family $\Omega$ is uniformly bounded. Also, for $x,x'\in[0,1]$,
\[
|Tf(x)-Tf(x')|
\le\int_0^1|K(x,y)-K(x',y)|\,dy
\le\sup_y|K(x,y)-K(x',y)|.
\]
The right-hand side tends to $0$ as $x'\to x$, uniformly in all $f$ with $\|f\|_\infty\le1$, again by uniform continuity of $K$. Thus $\Omega$ is equicontinuous.

By the Arzelà--Ascoli theorem, every sequence in $\Omega$ has a uniformly convergent subsequence whose limit lies in $C([0,1])$. Therefore $\Omega$ is precompact in the supremum norm.
:::
