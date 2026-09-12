---
schema: qual/card@1
id: P-DUKEBA14-4
kind: problem
title: The max and Euclidean metrics induce the same topology on $\mathbb R^n$
classification:
  areas: [real-analysis]
  topics: [Metric Spaces]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Part I, Problem 4 of the preserved Duke Winter 2014 Basic Analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
On $\mathbb R^n$ define
\[
\rho_1(x,y)=\max_{1\le j\le n}|x^j-y^j|,
\qquad
\rho_2(x,y)=\left(\sum_{j=1}^n|x^j-y^j|^2\right)^{1/2}.
\]
Prove that a set $U\subset\mathbb R^n$ is $\rho_1$-open if and only if it is $\rho_2$-open.
:::

::: solution
<1>1. Compare the two metrics.
::: proof
For every $x,y\in\mathbb R^n$,
\[
\rho_1(x,y)\le\rho_2(x,y)\le\sqrt n\,\rho_1(x,y).
\]
The first inequality holds because each coordinate difference is bounded by the Euclidean norm; the second follows by bounding all $n$ summands by $\rho_1(x,y)^2$.
:::

<1>2. Compare metric balls.
::: proof
The inequalities imply
\[
B_{\rho_2}(x,r)\subseteq B_{\rho_1}(x,r)
\]
and
\[
B_{\rho_1}\!\left(x,\frac r{\sqrt n}\right)
\subseteq B_{\rho_2}(x,r).
\]
Thus every neighborhood for either metric contains a neighborhood for the other. Consequently the two metrics induce exactly the same open sets.
:::
:::
