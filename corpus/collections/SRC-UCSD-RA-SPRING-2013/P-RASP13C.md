---
schema: qual/card@1
id: P-RASP13C
kind: problem
title: "A signed measure with vanishing polynomial moments is zero"
classification:
  areas:
  - real-analysis
  topics:
  - Signed Measures
  - Polynomials
  - Density of Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the official UCSD Spring 2013 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $f : [0, 1] \to \mathbb{R}$ be a continuous function.
Define the signed Borel measure $\mu$ on $[0, 1]$ by $d\mu = f \, dm$.
Assume
$$
\int_{[0,1]} x^n \, d\mu = 0, \quad n = 0, 1, 2, \ldots
$$
Prove that $\mu = 0$.
:::

::: solution
::: proof
By linearity, the moment hypothesis implies
\[
\int_0^1 p(x)f(x)\,dx=0
\]
for every real polynomial $p$.

Since $f\in C([0,1])$, the Weierstrass approximation theorem gives polynomials $p_k$ such that
\[
\|p_k-f\|_\infty\longrightarrow0.
\]
Therefore
\[
\left|\int_0^1(p_k-f)f\,dx\right|
\le \|p_k-f\|_\infty\int_0^1|f(x)|\,dx
\longrightarrow0.
\]
But
\[
\int_0^1p_kf\,dx=0
\]
for every $k$, so passing to the limit gives
\[
\int_0^1 f(x)^2\,dx=0.
\]
Hence $f=0$ almost everywhere. Since $f$ is continuous, it follows that $f\equiv0$ on $[0,1]$.

Thus for every Borel set $E$,
\[
\mu(E)=\int_E f\,dm=0,
\]
and therefore
\[
\boxed{\mu=0.}
\]
:::
:::
