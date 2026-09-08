---
schema: qual/card@1
id: P-RAF24B
kind: problem
title: Measurable sets with infinite Lebesgue density of an integrable function
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
  note: Checked against Problem 2 of the official UCSD Fall 2024 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
For any $n \in \mathbb{N}$, find all Lebesgue measurable sets $E \subseteq \mathbb{R}^n$ such that there exists some $f_E \in L^1(\mathbb{R}^n)$ satisfying
\[
\lim_{r \to 0} \frac{1}{m(B(r, x))} \int_{B(r, x)} f_E(y)\, dy = \infty
\quad\text{for each } x \in E.
\]
:::

::: solution
<1>1. Necessity: such a set must have measure zero.
::: proof
Suppose there exists $f_E\in L^1(\mathbb R^n)$ such that
\[
\lim_{r\to0}
\frac1{m(B(r,x))}\int_{B(r,x)}f_E(y)\,dy
=\infty
\]
for every $x\in E$.

By the Lebesgue differentiation theorem, for almost every $x\in\mathbb R^n$,
\[
\lim_{r\to0}
\frac1{m(B(r,x))}\int_{B(r,x)}f_E(y)\,dy
=f_E(x),
\]
and $f_E(x)$ is finite almost everywhere because $f_E\in L^1$. Hence the set on which the averages tend to $+\infty$ has measure zero. Therefore
\[
\boxed{m(E)=0.}
\]
:::

<1>2. Sufficiency: every measurable null set has such a function.
::: proof
Assume $m(E)=0$. For every $k\ge1$, choose an open set $U_k\supset E$ such that
\[
m(U_k)<2^{-k}.
\]
Define
\[
f_E:=\sum_{k=1}^\infty \mathbf1_{U_k}.
\]
By Tonelli,
\[
\|f_E\|_1
=\int\sum_{k=1}^\infty\mathbf1_{U_k}
=\sum_{k=1}^\infty m(U_k)
<\infty,
\]
so $f_E\in L^1(\mathbb R^n)$.

Fix $x\in E$ and $N\in\mathbb N$. Since
\[
x\in\bigcap_{k=1}^N U_k
\]
and this finite intersection is open, there exists $r_N(x)>0$ such that
\[
B(r_N(x),x)\subset\bigcap_{k=1}^N U_k.
\]
Therefore, whenever $0<r<r_N(x)$,
\[
f_E(y)\ge N
\qquad\text{for every }y\in B(r,x),
\]
and hence
\[
\frac1{m(B(r,x))}\int_{B(r,x)}f_E(y)\,dy\ge N.
\]
Since $N$ is arbitrary,
\[
\lim_{r\to0}
\frac1{m(B(r,x))}\int_{B(r,x)}f_E(y)\,dy
=\infty.
\]
Thus every measurable null set works.

Consequently the desired sets are exactly
\[
\boxed{\{E\subset\mathbb R^n:E\text{ measurable and }m(E)=0\}.}
\]
:::
:::
