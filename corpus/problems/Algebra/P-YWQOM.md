---
schema: qual/card@1
id: P-YWQOM
kind: problem
title: Groups of order $pqr$ have a normal Sylow subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - Simple Groups
relations: []
review: draft
---

::: {.problem}
Let $G$ have order $pqr$ with primes $p<q<r$. Show that $G$ has a normal Sylow subgroup. In particular, show that $G$ is not simple.
:::

::: {.solution}
Let $n_q$ and $n_r$ be the numbers of Sylow $q$- and Sylow $r$-subgroups of $G$.

::: pf

::: {.pf-step #nr}

If $n_r\ne 1$, then $n_r=pq$.

::: pf-proof

By the Sylow theorems, $n_r\mid pq$ and $n_r\equiv1\pmod r$. The divisors of $pq$ are $1,p,q,pq$, and $p,q$ are less than $r$ and greater than $1$, so neither is $\equiv 1\pmod r$.

:::

:::

::: {.pf-step #nq}

If $n_q\ne 1$, then $n_q\ge r$.

::: pf-proof

By the Sylow theorems, $n_q\mid pr$ and $n_q\equiv1\pmod q$. Since $1<p<q$, $p\not\equiv1\pmod q$, so $n_q\in\{r,pr\}$.

:::

:::

::: {.pf-step #count}

$n_q=1$ or $n_r=1$.

::: pf-proof

Suppose $n_q\ne1$ and $n_r\ne1$. Distinct subgroups of prime order intersect trivially, and an element of order $r$ does not have order $q$. By step [](#nr){.pf-ref}, the Sylow $r$-subgroups contain $pq(r-1)$ elements of order $r$, and by step [](#nq){.pf-ref} the Sylow $q$-subgroups contain at least $r(q-1)$ elements of order $q$. Since $r>q$ and $q-1\ge p$,
$$
r(q-1)>q(q-1)\ge pq>pq-1,
$$
so these elements number more than $pq(r-1)+pq-1=pqr-1$, the number of nonidentity elements of $G$. This is a contradiction.

:::

:::

::: pf-step

$G$ has a normal Sylow subgroup, and $G$ is not simple.

::: pf-proof

By step [](#count){.pf-ref}, a Sylow $q$- or Sylow $r$-subgroup is the unique one of its order, hence normal. It has prime order, so it is nontrivial and proper in $G$, and $G$ is not simple.

:::

:::

:::

:::
