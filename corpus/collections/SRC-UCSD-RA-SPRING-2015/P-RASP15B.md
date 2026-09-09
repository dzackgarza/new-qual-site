---
schema: qual/card@1
id: P-RASP15B
kind: problem
title: "L^p characterization via distribution function"
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
  note: Checked against Problem 2 of the official UCSD Spring 2015 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $(X, \mathcal{M}, \mu)$ be a measure space.
Prove that for any $0 < p < \infty$, $f \in L^p$ if and only if
$$
\sum_{k=-\infty}^{\infty} 2^{kp} \lambda_f(2^k) < \infty
$$
where $\lambda_f(\alpha) = \mu(\{x : |f|(x) > \alpha\})$.
:::

::: solution
::: proof
Since all terms are nonnegative, Tonelli's theorem gives
\[
\begin{aligned}
\sum_{k\in\mathbb Z}2^{kp}\lambda_f(2^k)
&=\sum_{k\in\mathbb Z}2^{kp}
\int_X\mathbf1_{\{|f|>2^k\}}\,d\mu\\
&=\int_X
\sum_{k\in\mathbb Z}2^{kp}
\mathbf1_{\{2^k<|f(x)|\}}\,d\mu(x).
\end{aligned}
\]

Fix $a>0$. Choose $m\in\mathbb Z$ so that
\[
2^m<a\le2^{m+1}.
\]
Then
\[
\sum_{k\in\mathbb Z}2^{kp}\mathbf1_{\{2^k<a\}}
=\sum_{k=-\infty}^m2^{kp}
=\frac{2^{mp}}{1-2^{-p}}.
\]
Since
\[
2^{mp}<a^p\le2^{(m+1)p},
\]
we obtain the two-sided comparison
\[
\frac{2^{-p}}{1-2^{-p}}a^p
\le
\sum_{k\in\mathbb Z}2^{kp}\mathbf1_{\{2^k<a\}}
\le
\frac1{1-2^{-p}}a^p.
\]
The same inequalities are trivial for $a=0$, and both sides are infinite for $a=\infty$.

Applying this pointwise with $a=|f(x)|$ and integrating gives
\[
\frac{2^{-p}}{1-2^{-p}}\|f\|_p^p
\le
\sum_{k\in\mathbb Z}2^{kp}\lambda_f(2^k)
\le
\frac1{1-2^{-p}}\|f\|_p^p.
\]
Therefore
\[
\boxed{
f\in L^p
\iff
\sum_{k=-\infty}^{\infty}2^{kp}\lambda_f(2^k)<\infty.}
\]
:::
:::
