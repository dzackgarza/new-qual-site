---
schema: qual/card@1
id: P-PS4CG
kind: problem
title: A group of order $p^2q$ has a normal Sylow subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Classification
  - Simple Groups
relations: []
review: draft
---

::: problem
Let $G$ be a group of order $p^2q$, where $p$ and $q$ are primes. Show that $G$ has a normal Sylow subgroup.
:::

::: {.solution}
If $p=q$, then $G$ itself is the unique Sylow $p$-subgroup, so assume $p\ne q$.

<1>1. If $p>q$, the Sylow $p$-subgroup is normal.
::: {.proof}
Sylow gives
\[
n_p\mid q,
\qquad
n_p\equiv1\pmod p.
\]
Thus $n_p\in\{1,q\}$. Since $q<p$, the value $q$ cannot be congruent to $1$ modulo $p$, so $n_p=1$.
:::

<1>2. Suppose $p<q$. Then either the Sylow $q$-subgroup is normal or $(p,q)=(2,3)$.
::: {.proof}
Sylow gives
\[
n_q\mid p^2,
\qquad
n_q\equiv1\pmod q.
\]
Hence $n_q\in\{1,p,p^2\}$. Since $1<p<q$, the value $p$ is impossible. If $n_q=p^2$, then
\[
q\mid p^2-1=(p-1)(p+1).
\]
Because $q>p$, this forces $q\mid p+1$, hence $q=p+1$. The only consecutive primes are $2$ and $3$.
:::

<1>3. In the exceptional order-$12$ case, a Sylow subgroup is still normal.
::: {.proof}
If the Sylow $3$-subgroup is unique, we are done. Otherwise $n_3=4$. The four order-$3$ subgroups intersect only in the identity, so they contribute $4(3-1)=8$ nonidentity elements. Exactly three nonidentity elements remain.

Every Sylow $2$-subgroup has order $4$, and its three nonidentity elements cannot lie in an order-$3$ subgroup. Hence every Sylow $2$-subgroup consists of the identity together with exactly those same three remaining elements. Therefore the Sylow $2$-subgroup is unique and normal.
:::

Thus every group of order $p^2q$ has a normal Sylow subgroup.
:::
