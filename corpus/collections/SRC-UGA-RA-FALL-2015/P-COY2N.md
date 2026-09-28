---
schema: qual/card@1
id: P-COY2N
kind: problem
title: $\sup_{\|g\|_1\le 1}\|fg\|_1=\|f\|_\infty$ for continuous $f$ on $[0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - L∞
  - Norms
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against entry 6 of the UGA Fall 2015 real-analysis qualifying exam recorded by the collection.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $f: [0, 1] \to \RR$ be continuous.
Show that
\[
\sup \left\{\|f g\|_{1} \suchthat g \in L^{1}[0,1],~~ \|g\|_{1} \leq 1\right\}=\|f\|_{\infty}.
\]
:::

::: {.solution}
<1>1. Prove the upper bound.
::: {.proof}
For every $g\in L^1([0,1])$ with $\|g\|_1\le1$,
\[
\|fg\|_1
=\int_0^1|f(x)g(x)|\,dx
\le \|f\|_\infty\|g\|_1
\le \|f\|_\infty.
\]
Hence
\[
\sup_{\|g\|_1\le1}\|fg\|_1\le\|f\|_\infty.
\]
:::

<1>2. Prove the reverse inequality.
::: {.proof}
Since $f$ is continuous on the compact interval $[0,1]$, there is $x_0\in[0,1]$ such that
\[
|f(x_0)|=\|f\|_\infty.
\]
Fix $\varepsilon>0$. By continuity, there is a measurable interval $I\subset[0,1]$ of positive length containing $x_0$ such that
\[
|f(x)|\ge \|f\|_\infty-\varepsilon
\qquad(x\in I).
\]
Set
\[
g=\frac{\mathbf1_I}{m(I)}.
\]
Then $\|g\|_1=1$ and
\[
\|fg\|_1
=\frac1{m(I)}\int_I|f(x)|\,dx
\ge \|f\|_\infty-\varepsilon.
\]
Therefore
\[
\sup_{\|g\|_1\le1}\|fg\|_1\ge \|f\|_\infty-\varepsilon.
\]
Letting $\varepsilon\downarrow0$ gives the reverse inequality. Thus
\[
\boxed{
\sup_{\|g\|_1\le1}\|fg\|_1=\|f\|_\infty.}
\]
:::
:::
