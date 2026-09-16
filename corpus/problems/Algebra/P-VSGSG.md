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
::: {.problem}
Let $p,q$ be distinct primes, and let $k$ denote the smallest positive integer such that $p\mid q^k-1$. Show that no group of order $pq^k$ is simple.
:::

::: {.solution}
Let $G$ have order $pq^k$.

Let $n_p$ be the number of Sylow $p$-subgroups. Sylow gives
\[
n_p\mid q^k,
\qquad
n_p\equiv1\pmod p.
\]
Hence $n_p=q^j$ for some $0\le j\le k$. If $j=0$, then $n_p=1$, so the Sylow $p$-subgroup is normal and $G$ is not simple.

Suppose therefore that $j>0$. Since $q^j\equiv1\pmod p$, the minimality of $k$ forces $j\ge k$. Thus $j=k$ and
\[
n_p=q^k.
\]
Distinct Sylow $p$-subgroups have trivial intersection because they have prime order. Therefore they contribute
\[
q^k(p-1)
\]
nonidentity elements. Since $|G|=pq^k$, exactly
\[
pq^k-q^k(p-1)=q^k
\]
elements remain.

Any Sylow $q$-subgroup has order $q^k$ and contains no nonidentity element of order $p$, so it is contained in this remaining set of $q^k$ elements. Hence there is only one Sylow $q$-subgroup. It is normal.

In all cases $G$ has a nontrivial proper normal Sylow subgroup, so $G$ is not simple.
:::
