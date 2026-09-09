---
schema: qual/card@1
id: P-AYZ4J
kind: problem
title: Groups of order $p^2q$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
- Analyze groups of order $p^2 q$.

  > Hint: Consider the cases when $q$ does or does not divide $p^2 - 1$.
:::


::: {.solution}
Let $|G|=p^2q$, where $p$ and $q$ are primes. If $p=q$, then $G$ is a $p$-group, so the interesting case is $p\ne q$. We analyze that case.

<1>1. If $p>q$, the Sylow $p$-subgroup is normal.
::: {.proof}
Let $n_p$ be the number of Sylow $p$-subgroups. Sylow gives
\[
n_p\mid q,
\qquad
n_p\equiv1\pmod p.
\]
Thus $n_p\in\{1,q\}$. Since $1<q<p$, the value $q$ is not congruent to $1$ modulo $p$. Hence $n_p=1$.
:::

<1>2. Suppose $p<q$. Then either the Sylow $q$-subgroup is normal, or $(p,q)=(2,3)$.
::: {.proof}
Sylow gives
\[
n_q\mid p^2,
\qquad
n_q\equiv1\pmod q.
\]
Hence
\[
n_q\in\{1,p,p^2\}.
\]
Since $1<p<q$, the possibility $n_q=p$ is impossible. Thus either $n_q=1$ or $n_q=p^2$.

If $n_q=p^2$, then
\[
p^2\equiv1\pmod q,
\]
so
\[
q\mid(p^2-1)=(p-1)(p+1).
\]
Because $q>p$, one cannot have $q\mid p-1$, hence $q\mid p+1$. But $0<p+1<2q$, so $q=p+1$. The only consecutive primes are $2$ and $3$, giving $(p,q)=(2,3)$.
:::

<1>3. In the exceptional order-$12$ case, $G$ still has a normal Sylow subgroup.
::: {.proof}
Let $|G|=12$. If $n_3=1$, the Sylow $3$-subgroup is normal. Suppose $n_3=4$. Distinct subgroups of order $3$ intersect trivially, so the four Sylow $3$-subgroups contain
\[
4(3-1)=8
\]
nonidentity elements. Thus exactly three nonidentity elements of $G$ lie outside their union.

Any Sylow $2$-subgroup $P$ has order $4$. None of its three nonidentity elements can lie in a subgroup of order $3$. Therefore those three elements must be exactly the three nonidentity elements outside the union of the Sylow $3$-subgroups. Hence every Sylow $2$-subgroup has the same underlying set, so the Sylow $2$-subgroup is unique and normal.
:::

<1>4. Therefore every group of order $p^2q$ with $p\ne q$ has a normal Sylow subgroup.
::: {.proof}
Combine <1>1, <1>2, and <1>3.
:::

<1>5. Such a group is a semidirect product of its Sylow factors.
::: {.proof}
Let $P$ and $Q$ be Sylow subgroups of orders $p^2$ and $q$, respectively. Their intersection is trivial because their orders are coprime.

If $P\trianglelefteq G$, then $PQ$ is a subgroup and
\[
|PQ|=\frac{|P||Q|}{|P\cap Q|}=p^2q=|G|,
\]
so
\[
G=P\rtimes Q.
\]
If instead $Q\trianglelefteq G$, the same argument gives
\[
G=Q\rtimes P.
\]
The groups $P$ are either $C_{p^2}$ or $C_p\times C_p$, while $Q\cong C_q$. Thus the remaining isomorphism analysis is the analysis of the possible homomorphisms from the complement into the automorphism group of the normal Sylow factor. The direct product occurs precisely when the action is trivial.
:::

<1>6. In particular, every group of order $p^2q$ is solvable.
::: {.proof}
Each Sylow factor in <1>5 is abelian: every group of order $p^2$ is abelian, and every group of prime order is cyclic. Hence $G$ has an abelian normal subgroup with abelian quotient, so $G$ is solvable.
:::
:::
