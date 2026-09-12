---
schema: qual/card@1
id: E-PCAYG
kind: problem
title: Banach fixed point theorem for contractions of complete metric spaces
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

If $(X, d)$ is a metric space, recall that a map $f: X \to X$ is called a contraction if there is a number $\alpha < 1$ such that

$$
d(f(x), f(y)) \leq \alpha \, d(x, y)
$$

for all $x, y \in X$.
Show that if $f$ is a contraction of a complete metric space, then there is a unique point $x \in X$ such that $f(x) = x$.
Compare [[E-70TGS]].
:::

::: {.solution}
Choose \(x_0\in X\) and define
\[
x_{n+1}=f(x_n).
\]
If \(c=d(x_1,x_0)\), repeated use of the contraction inequality gives
\[
d(x_{n+1},x_n)\le \alpha^n c.
\]
Hence for \(m>n\),
\[
d(x_m,x_n)
\le\sum_{k=n}^{m-1}d(x_{k+1},x_k)
\le c\sum_{k=n}^{m-1}\alpha^k
\le \frac{c\alpha^n}{1-\alpha}.
\]
The right side tends to \(0\), so \((x_n)\) is Cauchy. Completeness gives \(x_n\to x\in X\).

The contraction inequality implies that \(f\) is Lipschitz, hence continuous. Therefore
\[
f(x)=f\left(\lim_nx_n\right)
 =\lim_nf(x_n)
 =\lim_nx_{n+1}
 =x.
\]
Thus a fixed point exists.

If \(x\) and \(y\) are fixed points, then
\[
d(x,y)=d(f(x),f(y))\le\alpha d(x,y).
\]
Since \(\alpha<1\), this forces \(d(x,y)=0\), hence \(x=y\). The fixed point is unique.
:::
