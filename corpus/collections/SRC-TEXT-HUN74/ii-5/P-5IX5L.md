---
schema: qual/card@1
id: P-5IX5L
kind: problem
title: Unique normal subgroup of index $q$ when $|G|=p^n q$ with $p>q$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against an independent course sheet assigning Hungerford II.5.9 and against the retained collection statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $\left| G \right| = p^n q$ for some primes $p > q$.
Show that $G$ contains a unique normal subgroup of index $q$.
:::

::: solution
Let $P$ be a Sylow $p$-subgroup of $G$. Then $|P|=p^n$, so $[G:P]=q$.

<1>1. The number $n_p$ of Sylow $p$-subgroups is $1$.
::: proof
By Sylow's theorems,
\[
n_p\mid q
\qquad\text{and}\qquad
n_p\equiv1\pmod p.
\]
Since $q$ is prime, $n_p$ is either $1$ or $q$. If $n_p=q$, then
$q\equiv1\pmod p$, so $p$ divides $q-1$. But $0<q-1<p$ because $p>q$, which
is impossible. Hence $n_p=1$.
:::

<1>2. The subgroup $P$ is normal and has index $q$.
::: proof
A unique Sylow subgroup is normal, so <1>1 gives $P\trianglelefteq G$. Also
\[
[G:P]=\frac{p^nq}{p^n}=q.
\]
:::

<1>3. Any subgroup $H\le G$ of index $q$ equals $P$.
::: proof
If $[G:H]=q$, then
\[
|H|=\frac{|G|}{q}=p^n.
\]
Thus $H$ is a Sylow $p$-subgroup. By <1>1 the Sylow $p$-subgroup is unique, so
$H=P$.
:::

<1>4. Therefore $G$ has a unique normal subgroup of index $q$.
::: proof
Existence follows from <1>2, and uniqueness from <1>3.
:::
:::
