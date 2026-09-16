---
schema: qual/card@1
id: E-SS3.EX-22
kind: problem
title: No holomorphic function on the disk can extend continuously with boundary values $1/z$
classification:
  areas:
  - complex-analysis
  topics: ['Meromorphic Functions', 'Residue Theorem', 'Argument Principle']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
22. Show that there is no holomorphic function f in the unit disc D that extends continuously to $\partial D$ such that $f ( z ) = 1 / z \ \mathrm { f o r } \ z \in \partial \mathbb { D }$
:::

::: solution
Suppose such an $f$ existed.
Define
\[
h(z)=zf(z)-1.
\]
Then $h$ is holomorphic in $\mathbb D$ and continuous on $\overline{\mathbb D}$.
On the boundary, $f(z)=1/z$, so $h(z)=0$ whenever $|z|=1$.
By the maximum modulus principle,
\[
|h(z)|\le \max_{|\zeta|=1}|h(\zeta)|=0
\]
for every $z\in\mathbb D$.
Hence $h\equiv0$.
But
\[
h(0)=-1,
\]
a contradiction.
Therefore no such $f$ exists.
:::
