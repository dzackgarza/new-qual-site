---
schema: qual/card@1
id: P-WESRA08-II4
kind: problem
title: Convergence in measure via a bounded integral gauge
classification:
  areas: [real-analysis]
  topics: [Convergence in Measure, Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked visually against Problem 4 of the Wesleyan Real Analysis Preliminary Examination, July 8, 2008, in analysis_2008-2013.pdf. The source itself prints f in the displayed integrand although the statement concerns the sequence f_n; the card corrects this evident source typo to f_n.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
Let $(X,\mathcal B,\mu)$ be a measure space with $\mu(X)<\infty$. Show that a sequence of measurable functions $(f_n)$ converges to $0$ in measure if and only if
\[
\lim_{n\to\infty}
\int_X \frac{|f_n|}{1+|f_n|}\,d\mu=0.
\]
:::

::: solution
Set
\[
\Phi(t):=\frac{t}{1+t},
\qquad t\ge0.
\]

<1>1. Convergence in measure implies convergence of the integrals.
::: proof
Assume $f_n\to0$ in measure. Fix $\varepsilon>0$. If $\mu(X)=0$, the conclusion is immediate, so assume $\mu(X)>0$.

Choose $\delta>0$ so that
\[
\delta\mu(X)<\frac\varepsilon2.
\]
Split $X$ into the sets where $|f_n|\le\delta$ and $|f_n|>\delta$. Since $0\le\Phi(t)\le t$ and $\Phi(t)\le1$,
\[
\begin{aligned}
\int_X\Phi(|f_n|)\,d\mu
&\le \delta\mu(X)+\mu(\{|f_n|>\delta\}).
\end{aligned}
\]
Convergence in measure gives
\[
\mu(\{|f_n|>\delta\})\longrightarrow0.
\]
Hence the integral is below $\varepsilon$ for all sufficiently large $n$, and therefore
\[
\int_X\frac{|f_n|}{1+|f_n|}\,d\mu\longrightarrow0.
\]
:::

<1>2. Convergence of the integrals implies convergence in measure.
::: proof
Assume
\[
\int_X\Phi(|f_n|)\,d\mu\longrightarrow0.
\]
Fix $\eta>0$. On the set $\{|f_n|>\eta\}$, monotonicity of $\Phi$ gives
\[
\Phi(|f_n|)\ge \frac{\eta}{1+\eta}.
\]
Therefore
\[
\frac{\eta}{1+\eta}\,
\mu(\{|f_n|>\eta\})
\le
\int_X\Phi(|f_n|)\,d\mu.
\]
Thus
\[
\mu(\{|f_n|>\eta\})
\le
\frac{1+\eta}{\eta}
\int_X\frac{|f_n|}{1+|f_n|}\,d\mu
\longrightarrow0.
\]
Since this holds for every $\eta>0$, $f_n\to0$ in measure.
:::
:::
