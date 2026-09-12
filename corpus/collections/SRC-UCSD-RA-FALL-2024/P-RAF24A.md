---
schema: qual/card@1
id: P-RAF24A
kind: problem
title: Rationally invariant measurable set has measure zero or conull complement
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the official UCSD Fall 2024 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $E \subseteq \mathbb{R}$ be (Lebesgue) measurable and satisfy $E + r = E$ for every rational number $r$.
Show that either $E$ or $E^c$ has measure 0.
:::

::: solution
<1>1. Assume both sets have positive measure and localize them.
::: proof
Suppose, toward a contradiction, that
\[
m(E)>0
\qquad\text{and}\qquad
m(E^c)>0.
\]
Since Lebesgue measure is $\sigma$-finite, there exist bounded measurable sets
\[
A\subset E,
\qquad
B\subset E^c
\]
with
\[
0<m(A),m(B)<\infty.
\]
:::

<1>2. Use continuity of translation to find a rational translate with positive overlap.
::: proof
Define
\[
h(t):=m((A+t)\cap B)
=\int_{\mathbb R}\mathbf1_A(x-t)\mathbf1_B(x)\,dx.
\]
Since translations are continuous in $L^1(\mathbb R)$,
\[
|h(t)-h(s)|
\le \|\mathbf1_A(\cdot-t)-\mathbf1_A(\cdot-s)\|_1,
\]
so $h$ is continuous.

Tonelli's theorem gives
\[
\begin{aligned}
\int_{\mathbb R}h(t)\,dt
&=\int_{\mathbb R}\int_{\mathbb R}
\mathbf1_A(x-t)\mathbf1_B(x)\,dx\,dt\\
&=m(A)m(B)>0.
\end{aligned}
\]
Thus $h(t_0)>0$ for some $t_0$. By continuity, $h>0$ on a nonempty open interval around $t_0$. Since $\mathbb Q$ is dense, choose rational $r$ in that interval. Then
\[
m((A+r)\cap B)=h(r)>0.
\]
:::

<1>3. Contradict rational invariance.
::: proof
Because $A\subset E$ and $r\in\mathbb Q$,
\[
A+r\subset E+r=E.
\]
But $B\subset E^c$, so
\[
(A+r)\cap B=\varnothing,
\]
contradicting Step 2. Hence it is impossible for both $E$ and $E^c$ to have positive measure. Therefore
\[
\boxed{m(E)=0\quad\text{or}\quad m(E^c)=0.}
\]
:::
:::
