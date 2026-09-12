---
schema: qual/card@1
id: P-JHUFA05ANA
kind: problem
title: '$\|f_n\|_2^2\le n^{-2}$ forces $f_n\to0$ a.e.'
classification:
  areas:
  - real-analysis
  topics:
  - Convergence Theorems
  - Borel-Cantelli
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the JHU Analysis Qualifying Exam, September 2005, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $(f_n)$ be Lebesgue-measurable functions on $[0,1]$ satisfying
\[
\int_0^1 |f_n(x)|^2\,dx\le \frac1{n^2}.
\]
Prove that
\[
f_n(x)\longrightarrow0
\qquad\text{for almost every }x\in[0,1].
\]
:::

::: {.solution}
Fix $m\in\mathbb N$ and define
\[
E_{n,m}=\{x\in[0,1]: |f_n(x)|>1/m\}.
\]
By Chebyshev's inequality,
\[
\frac1{m^2}m(E_{n,m})
\le \int_{E_{n,m}} |f_n(x)|^2\,dx
\le \int_0^1 |f_n(x)|^2\,dx
\le \frac1{n^2},
\]
so
\[
m(E_{n,m})\le \frac{m^2}{n^2}.
\]
Hence
\[
\sum_{n=1}^\infty m(E_{n,m})<\infty.
\]
By the first Borel--Cantelli lemma, for almost every $x$ there exists $N_m(x)$ such that
\[
|f_n(x)|\le \frac1m
\qquad(n\ge N_m(x)).
\]
For each $m$, let $N_m$ be the null exceptional set where this conclusion fails, and put
\[
N=\bigcup_{m=1}^\infty N_m.
\]
Then $m(N)=0$. If $x\notin N$ and $\varepsilon>0$, choose $m$ with $1/m<\varepsilon$. For all $n\ge N_m(x)$,
\[
|f_n(x)|\le\frac1m<\varepsilon.
\]
Therefore $f_n(x)\to0$ for every $x\in[0,1]\setminus N$, proving the assertion.
:::
