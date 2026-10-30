---
schema: qual/card@1
id: P-RAF18E
kind: problem
title: 'Interpolation of $L^p$ convergence and weak convergence'
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

::: {.problem}
Let $1 < p < \infty$, and $\{f_n\}_n \subset L^p([0,1], m)$ be a sequence such that $M := \sup_n \norm{f_n}_p < \infty$ and $\lim_{n \to \infty} \norm{f_n}_1 = 0$.

1. Prove that $\lim_{n \to \infty} \norm{f_n}_r = 0$ for every $r \in [1, p)$.

2. Let $1 < q < \infty$ such that $1/p + 1/q = 1$.
   Prove that $\lim_{n \to \infty} \int_0^1 f_n g\,dm = 0$ for every $g \in L^q([0,1], m)$.
:::

::: {.solution}

::: pf

::: pf-step

Interpolate between $L^1$ and $L^p$.

::: pf-proof

Fix $r\in[1,p)$. Choose $\theta\in(0,1]$ so that
$$
\frac1r=\theta+\frac{1-\theta}{p}.
$$
For $r>1$, Hölder's inequality gives the interpolation estimate
$$
\norm{f_n}_r\le \norm{f_n}_1^\theta\norm{f_n}_p^{1-\theta}.
$$
For $r=1$ this is exactly the given hypothesis. Since
$$
\sup_n\norm{f_n}_p=M<\infty
$$
and $\norm{f_n}_1\to0$, we obtain
$$
\norm{f_n}_r\le M^{1-\theta}\norm{f_n}_1^\theta\longrightarrow0.
$$
Thus
$$
\boxed{\norm{f_n}_r\to0\quad\text{for every }1\le r<p.}
$$

:::

:::

::: pf-step

Prove weak convergence in $L^p$.

::: pf-proof

Let $g\in L^q([0,1])$ and fix $\varepsilon>0$. Since bounded functions are dense in $L^q([0,1])$, choose $h\in L^\infty([0,1])$ with
$$
\norm{g-h}_q<\frac{\varepsilon}{2M}
$$
when $M>0$; if $M=0$, the conclusion is immediate.

Then Hölder's inequality gives
$$
\abs{\int_0^1 f_n(g-h)\,dm}
\le \norm{f_n}_p\norm{g-h}_q
<\frac\varepsilon2.
$$
On the other hand,
$$
\abs{\int_0^1 f_n h\,dm}
\le \norm{h}_\infty\norm{f_n}_1\longrightarrow0.
$$
Hence for all sufficiently large $n$,
$$
\abs{\int_0^1 f_ng\,dm}<\varepsilon.
$$
Therefore
$$
\boxed{\int_0^1 f_ng\,dm\longrightarrow0\quad\text{for every }g\in L^q([0,1]).}
$$

:::

:::

:::

:::
