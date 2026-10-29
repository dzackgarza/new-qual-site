---
schema: qual/card@1
id: P-VSGSG
kind: problem
title: No simple group of order $pq^k$ when $k$ is least with $p\mid q^k-1$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
relations: []
review: draft
---

::: {.problem}
Let $p,q$ be distinct primes, and let $k$ denote the smallest positive integer such that $p$ divides $q^k - 1$.
Show that no group of order $pq^k$ is simple.
:::

::: {.solution}
Let $G$ have order $pq^k$, and let $n_p$ be the number of Sylow $p$-subgroups of $G$.

::: pf

::: {.pf-step #np}

Either $n_p=1$ or $n_p=q^k$.

::: pf-proof

The Sylow theorems give $n_p\mid q^k$ and $n_p\equiv1\pmod p$, so $n_p=q^j$ for some $0\le j\le k$. If $j>0$, then $p\mid q^j-1$, and the minimality of $k$ forces $j\ge k$, so $j=k$.

:::

:::

::: {.pf-step #nq}

If $n_p=q^k$, then $G$ has a unique Sylow $q$-subgroup.

::: pf-proof

Distinct Sylow $p$-subgroups have prime order, so they intersect trivially and contribute $q^k(p-1)$ elements of order $p$. Exactly $pq^k-q^k(p-1)=q^k$ elements of $G$ do not have order $p$. A Sylow $q$-subgroup has $q^k$ elements, none of order $p$, so it is exactly this set of $q^k$ elements.

:::

:::

::: pf-qed

By steps [](#np){.pf-ref} and [](#nq){.pf-ref}, $G$ has a normal Sylow $p$-subgroup or a normal Sylow $q$-subgroup. Each is nontrivial and proper, so $G$ is not simple.

:::

:::

:::
