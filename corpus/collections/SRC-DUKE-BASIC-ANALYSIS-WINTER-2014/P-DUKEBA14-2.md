---
schema: qual/card@1
id: P-DUKEBA14-2
kind: problem
title: A nonnegative continuous function with zero integral vanishes identically
classification:
  areas: [real-analysis]
  topics: [Riemann Integration, Continuity]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Part I, Problem 2 of the preserved Duke Winter 2014 Basic Analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $f:[0,1]\to[0,\infty)$ be continuous and suppose
\[
\int_0^1 f(t)\,dt=0.
\]
Prove that $f(x)=0$ for every $x\in[0,1]$.
:::

::: solution
<1>1. Assume that $f$ is positive somewhere.
::: proof
Suppose $f(x_0)>0$ for some $x_0\in[0,1]$. Set
\[
\varepsilon:=\frac{f(x_0)}2>0.
\]
By continuity there is $\delta>0$ such that
\[
|x-x_0|<\delta,
\qquad x\in[0,1],
\]
implies
\[
f(x)>\varepsilon.
\]
:::

<1>2. Integrate on that neighborhood.
::: proof
The interval
\[
I=(x_0-\delta,x_0+\delta)\cap[0,1]
\]
has positive length. Since $f\ge0$ everywhere and $f\ge\varepsilon$ on $I$,
\[
\int_0^1f(t)\,dt
\ge \int_I f(t)\,dt
\ge \varepsilon\,m(I)>0,
\]
contrary to the hypothesis.

Therefore no such $x_0$ exists, and
\[
\boxed{f\equiv0.}
\]
:::
:::
