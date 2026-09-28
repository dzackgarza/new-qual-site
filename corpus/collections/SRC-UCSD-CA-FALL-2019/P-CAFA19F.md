---
schema: qual/card@1
id: P-CAFA19F
kind: problem
title: "Analytic functions on C minus origin with subquadratic growth"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Find all analytic functions $f$ on $\mathbb{C} \setminus \{0\}$ with the following property: There is some constant $C > 0$ such that $|f(z)| \leq C|z|^2 + \frac{C}{|z|^{1/2}}$ for all $z \in \mathbb{C} \setminus \{0\}$.
:::

::: {.solution}
Write the Laurent expansion about $0$,
\[
f(z)=\sum_{n=-\infty}^{\infty}a_nz^n.
\]
For $m\ge1$, Cauchy's formula on $|z|=r<1$ gives
\[
|a_{-m}|
\le r^m\max_{|z|=r}|f(z)|
\le C(r^{m+2}+r^{m-1/2}).
\]
Letting $r\downarrow0$ yields $a_{-m}=0$ for every $m\ge1$. Thus the
singularity at $0$ is removable and $f$ extends to an entire function.

For $R\ge1$,
\[
M(R):=\max_{|z|=R}|f(z)|\le C R^2+C R^{-1/2}\le2CR^2.
\]
Cauchy's estimate gives, for $n\ge3$,
\[
|f^{(n)}(0)|\le \frac{n!M(R)}{R^n}
\le 2Cn!R^{2-n}.
\]
Letting $R\to\infty$ shows $f^{(n)}(0)=0$ for every $n\ge3$. Therefore
\[
f(z)=a+bz+cz^2.
\]
Conversely, every polynomial of degree at most $2$ satisfies the required
estimate for a sufficiently large constant $C$. Hence these are exactly the
solutions.
:::
