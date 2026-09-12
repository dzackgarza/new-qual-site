---
schema: qual/card@1
id: P-6NA4D
kind: problem
title: Groups of order $p^2q$ are solvable
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Sylow Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against a Rutgers Algebra assignment identifying the problem as Hungerford II.8.9.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that any group of order $p^2q$ (for primes $p,q$) is solvable.
:::

::: solution
Let $|G|=p^2q$ with $p,q$ prime.

<1>1. If $p=q$, then $G$ is solvable.
::: proof
In this case $|G|=p^3$, so $G$ is a finite $p$-group. Every finite $p$-group
is nilpotent, hence solvable.
:::

Assume henceforth that $p\ne q$.

<1>2. At least one Sylow subgroup of $G$ is normal.
::: proof
Let $n_p$ and $n_q$ denote the numbers of Sylow $p$- and $q$-subgroups.
Sylow's theorems give
\[
n_p\mid q,\qquad n_p\equiv1\pmod p,
\]
and
\[
n_q\mid p^2,\qquad n_q\equiv1\pmod q.
\]

If $p>q$, then $n_p$ is either $1$ or $q$, but $q<p$ prevents
$q\equiv1\pmod p$. Thus $n_p=1$.

Suppose $p<q$. If $n_q=1$, we are done. Otherwise $n_q$ is $p$ or $p^2$.
Since $p<q$, the congruence $n_q\equiv1\pmod q$ excludes $n_q=p$, so
$n_q=p^2$. Hence
\[
q\mid p^2-1=(p-1)(p+1).
\]
Because $q>p$, the prime $q$ cannot divide $p-1$, so $q\mid p+1$. Thus
$q=p+1$. The only consecutive primes with the smaller one prime and $p+1$
also prime are $p=2$, $q=3$.

It remains to consider $|G|=12$. If $n_3=4$, then the four Sylow
$3$-subgroups have pairwise trivial intersection and contribute
\[
4(3-1)=8
\]
nonidentity elements. Only three nonidentity elements remain. Any Sylow
$2$-subgroup has order $4$ and hence already contains three nonidentity
elements, so every Sylow $2$-subgroup must consist of the identity together with
those same three remaining elements. Therefore the Sylow $2$-subgroup is unique
and normal. Thus in all cases at least one Sylow subgroup is normal.
:::

<1>3. A normal Sylow subgroup $N$ of $G$ is solvable, and so is $G/N$.
::: proof
The possible orders of $N$ are $p^2$ or $q$. A group of prime order is cyclic,
and every group of order $p^2$ is abelian. Hence $N$ is abelian and therefore
solvable.

The quotient has the complementary order: if $|N|=p^2$, then $|G/N|=q$; if
$|N|=q$, then $|G/N|=p^2$. Thus $G/N$ is likewise abelian and solvable.
:::

<1>4. Therefore $G$ is solvable.
::: proof
A group with a solvable normal subgroup and solvable quotient is solvable.
Apply this extension criterion to the normal Sylow subgroup supplied by <1>2
and use <1>3.
:::
:::
