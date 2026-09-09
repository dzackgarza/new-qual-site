---
schema: qual/card@1
id: P-RAF18E
kind: problem
title: "Interpolation of L^p convergence and weak convergence"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the official UCSD Fall 2018 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $1 < p < \infty$, and $\{f_n\}_n \subset L^p([0,1], m)$ be a sequence such that $M := \sup_n \|f_n\|_p < \infty$ and $\lim_{n \to \infty} \|f_n\|_1 = 0$.

1. Prove that $\lim_{n \to \infty} \|f_n\|_r = 0$ for every $r \in [1, p)$.

2. Let $1 < q < \infty$ such that $1/p + 1/q = 1$.
   Prove that $\lim_{n \to \infty} \int_0^1 f_n g\,dm = 0$ for every $g \in L^q([0,1], m)$.
:::

::: solution
<1>1. Interpolate between $L^1$ and $L^p$.
::: proof
Fix $r\in[1,p)$. Choose $\theta\in(0,1]$ so that
\[
\frac1r=\theta+\frac{1-\theta}{p}.
\]
For $r>1$, Hölder's inequality gives the interpolation estimate
\[
\|f_n\|_r\le \|f_n\|_1^\theta\|f_n\|_p^{1-\theta}.
\]
For $r=1$ this is exactly the given hypothesis. Since
\[
\sup_n\|f_n\|_p=M<\infty
\]
and $\|f_n\|_1\to0$, we obtain
\[
\|f_n\|_r\le M^{1-\theta}\|f_n\|_1^\theta\longrightarrow0.
\]
Thus
\[
\boxed{\|f_n\|_r\to0\quad\text{for every }1\le r<p.}
\]
:::

<1>2. Prove weak convergence in $L^p$.
::: proof
Let $g\in L^q([0,1])$ and fix $\varepsilon>0$. Since bounded functions are dense in $L^q([0,1])$, choose $h\in L^\infty([0,1])$ with
\[
\|g-h\|_q<\frac{\varepsilon}{2M}
\]
when $M>0$; if $M=0$, the conclusion is immediate.

Then Hölder's inequality gives
\[
\left|\int_0^1 f_n(g-h)\,dm\right|
\le \|f_n\|_p\|g-h\|_q
<\frac\varepsilon2.
\]
On the other hand,
\[
\left|\int_0^1 f_n h\,dm\right|
\le \|h\|_\infty\|f_n\|_1\longrightarrow0.
\]
Hence for all sufficiently large $n$,
\[
\left|\int_0^1 f_ng\,dm\right|<\varepsilon.
\]
Therefore
\[
\boxed{\int_0^1 f_ng\,dm\longrightarrow0\quad\text{for every }g\in L^q([0,1]).}
\]
:::
:::
