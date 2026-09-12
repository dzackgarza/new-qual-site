---
schema: qual/card@1
id: P-2TOZB
kind: problem
title: Free modules over domains are torsion-free, but not conversely
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Torsion
  - Integral Domains
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against an independent reproduction of the Hungerford IV.6 exercise statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that every free module over a unital integral domain is torsion-free.
Show that the converse is false.
:::

::: solution
<1>1. Every free module over a unital integral domain is torsion-free.
::: proof
Let $R$ be a unital integral domain and let $F$ be a free $R$-module with basis
$B$. Suppose $0\ne r\in R$ and $x\in F$ satisfy $rx=0$. Write the unique finite
basis expansion
\[
x=\sum_{i=1}^n a_i b_i,
\]
where the $b_i\in B$ are distinct. Then
\[
0=rx=\sum_{i=1}^n (ra_i)b_i.
\]
Linear independence of $B$ gives $ra_i=0$ for every $i$. Since $R$ is an
integral domain and $r\ne0$, each $a_i=0$. Thus $x=0$. Hence $F$ has no
nonzero torsion element.
:::

<1>2. The converse is false.
::: proof
Take $R=\ZZ$ and the $\ZZ$-module $\QQ$. It is torsion-free: if
$0\ne n\in\ZZ$ and $q\in\QQ$ satisfy $nq=0$, then $q=0$.

We show that $\QQ$ is not free as a $\ZZ$-module. Suppose it had a basis $B$,
and choose $b\in B$. Since $\QQ$ is divisible, there exists $c\in\QQ$ with
$2c=b$. Express
\[
c=\sum_{i=1}^m n_i b_i
\]
in the basis, where $n_i\in\ZZ$. Multiplying by $2$ gives
\[
b=\sum_{i=1}^m 2n_i b_i.
\]
By uniqueness of basis coordinates, the coefficient of $b$ on the right must be
$1$. But every coefficient there is even, a contradiction. Thus $\QQ$ is
torsion-free but not free.
:::
:::
