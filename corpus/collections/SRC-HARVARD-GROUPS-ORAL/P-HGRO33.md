---
schema: qual/card@1
id: P-HGRO33
kind: problem
title: Subgroups of a group of order 30
classification:
  areas: [algebra]
  topics: [Sylow Theory]
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
What can be said about the subgroups of a group of order $30$?
:::

::: {.solution}
Let $G$ be a group of order $30=2\cdot3\cdot5$, and let $n_p$ be the number
of Sylow $p$-subgroups.

<1>1. $n_3=1$ or $n_5=1$.

::: {.proof}
Sylow's theorems give $n_5\in\{1,6\}$ and $n_3\in\{1,10\}$. Distinct
subgroups of prime order meet trivially, so $n_5=6$ and $n_3=10$ would give
$6\cdot4=24$ elements of order $5$ and $10\cdot2=20$ elements of order $3$,
more than $30$.
:::

<1>2. $G$ has a normal cyclic subgroup $H$ of order $15$, and $n_3=n_5=1$.

::: {.proof}
By step <1>1 one of the Sylow subgroups $P_3$, $P_5$ is normal, so
$H=P_3P_5$ is a subgroup of order $15$. Every group of order $15$ is cyclic,
and $[G:H]=2$, so $H\trianglelefteq G$. The subgroups of orders $3$ and $5$
of the cyclic group $H$ are characteristic in $H$, hence normal in $G$; they
are the unique Sylow $3$- and $5$-subgroups of $G$.
:::

<1>3. $G\cong\ZZ/15\rtimes_\theta\ZZ/2$ for some
$\theta\colon\ZZ/2\to\Aut(\ZZ/15)\cong\ZZ/2\times\ZZ/4$, and $G$ is
isomorphic to exactly one of
$$
\ZZ/30,\qquad D_{15},\qquad S_3\times\ZZ/5,\qquad D_5\times\ZZ/3,
$$
where $D_m$ is the dihedral group of order $2m$.

::: {.proof}
A Sylow $2$-subgroup $P_2$ has order $2$ and meets $H$ trivially, so
$G=H\rtimes P_2$. The automorphism $\theta(1)$ of
$\ZZ/15\cong\ZZ/3\times\ZZ/5$ has order dividing $2$, so it acts on each
factor by $\pm1$; the four sign choices give the four listed groups, which
are distinguished by the number of elements of order $2$: $1$, $15$, $3$,
and $5$.
:::

<1>4. $G$ has subgroups of every order dividing $30$. The subgroups of orders
$3$, $5$, and $15$ are unique and normal; the subgroups of order $6$ are the
groups $P_3P_2$, isomorphic to $\ZZ/6$ or $S_3$, and those of order $10$ are
the groups $P_5P_2$, isomorphic to $\ZZ/10$ or $D_5$.

::: {.proof}
Steps <1>2 and <1>3 give the subgroups of orders $3$, $5$, $15$, and $2$.
Since $P_3$ and $P_5$ are normal, $P_3P_2$ and $P_5P_2$ are subgroups of
orders $6$ and $10$ for each Sylow $2$-subgroup $P_2$. A subgroup of order
$6$ or $10$ contains a Sylow $2$-subgroup $P_2$ of $G$ and the unique
subgroup of order $3$ or $5$, so it is of this form; it is cyclic when $P_2$
centralizes $P_3$ or $P_5$ and dihedral otherwise.
:::
:::
