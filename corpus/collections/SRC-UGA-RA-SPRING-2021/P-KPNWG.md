---
schema: qual/card@1
id: P-KPNWG
kind: problem
title: $\lim_{n\to\infty}\int_0^n\frac{\cos(x/n)}{x^2+\cos(x/n)}\,dx$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Problem 2 of the official UGA January 2021 Analysis qualifying examination DOCX.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Replaced the legacy DCT domination by the uniform integrable bound obtained from cos(x/n) at least cos(1) on the integration range 0<x<n.
---

::: {.problem}
Calculate the following limit, justifying each step of your calculation:
\[
L \da \lim_{n\to \infty} \int_0^n { \cos\qty{x\over n} \over x^2 + \cos\qty{x\over n} }\dx
.\]
:::


::: {.solution}
For $x>0$, define
\[
F_n(x)=\mathbf1_{(0,n)}(x)
\frac{\cos(x/n)}{x^2+\cos(x/n)}.
\]
For each fixed $x>0$, eventually $x<n$, and then $x/n\to0$. Hence
\[
F_n(x)\longrightarrow\frac1{x^2+1}.
\]

Whenever $0<x<n$, one has $0<x/n<1$, so
\[
\cos(x/n)\ge\cos1>0.
\]
Therefore
\[
0\le F_n(x)\le\frac1{x^2+\cos1}.
\]
For $x\ge n$, $F_n(x)=0$, so the same bound holds. Since
\[
x\longmapsto\frac1{x^2+\cos1}
\]
belongs to $L^1(0,\infty)$, dominated convergence yields
\[
L=\int_0^\infty\frac{dx}{1+x^2}
=\left[\arctan x\right]_0^\infty
=\boxed{\frac\pi2}.
\]
:::

