---
schema: qual/card@1
id: P-JHUFA08ANB
kind: problem
title: 'Integral operators on $L^p$ via Schur-type bounds'
classification:
  areas:
  - real-analysis
  topics:
  - Integral Operators
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the JHU Analysis Qualifying Exam, Fall 2008, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $(X,\mathcal M,\mu)$ and $(Y,\mathcal N,\nu)$ be sigma-finite measure spaces. Let $K:X\times Y\to\mathbb C$ be measurable and suppose
\[
\int_Y |K(x,y)|\,d\nu(y)\le A
\quad\text{for all }x,
\]
and
\[
\int_X |K(x,y)|\,d\mu(x)\le A
\quad\text{for all }y.
\]
Define
\[
Tf(y)=\int_X f(x)K(x,y)\,d\mu(x).
\]
Prove that for every $1\le p\le\infty$,
\[
\|Tf\|_{L^p(\nu)}\le A\|f\|_{L^p(\mu)}.
\]
:::

::: {.solution}
<1>1. The case $p=\infty$.
::: {.proof}
For almost every $y$,
\[
|Tf(y)|\le \|f\|_\infty\int_X|K(x,y)|\,d\mu(x)\le A\|f\|_\infty.
\]
Thus $\|Tf\|_\infty\le A\|f\|_\infty$.
:::

<1>2. The case $1\le p<\infty$.
::: {.proof}
Fix $y$. Hölder's inequality with respect to the finite measure $|K(x,y)|\,d\mu(x)$ gives
\[
|Tf(y)|^p
\le\left(\int_X |f(x)|^p|K(x,y)|\,d\mu(x)\right)
\left(\int_X |K(x,y)|\,d\mu(x)\right)^{p-1}.
\]
By the kernel bound,
\[
|Tf(y)|^p\le A^{p-1}\int_X |f(x)|^p|K(x,y)|\,d\mu(x).
\]
Integrating in $y$ and using Tonelli,
\[
\begin{aligned}
\|Tf\|_p^p
&\le A^{p-1}\int_Y\int_X |f(x)|^p|K(x,y)|\,d\mu(x)\,d\nu(y)\\
&=A^{p-1}\int_X |f(x)|^p\left(\int_Y|K(x,y)|\,d\nu(y)\right)d\mu(x)\\
&\le A^p\|f\|_p^p.
\end{aligned}
\]
Taking $p$th roots gives
\[
\|Tf\|_p\le A\|f\|_p.
\]
:::
:::
