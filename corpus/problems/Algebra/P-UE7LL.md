---
schema: qual/card@1
id: P-UE7LL
kind: problem
title: Groups of order $p^2 q$ have a nontrivial normal subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - Classification
relations: []
review: draft
---

::: {.problem}
Let $p,q$ be primes and let $\abs{G}=p^2q$. Show that $G$ has a nontrivial proper normal subgroup.
:::

::: {.solution}

::: pf

::: {.pf-step #equal}
If $p=q$, then $G$ has a nontrivial proper normal subgroup.

::: pf-proof
$G$ is a $p$-group of order $p^3$, so its center $Z(G)$ is nontrivial.
If $Z(G)\ne G$, then $Z(G)$ is a nontrivial proper normal subgroup.
If $Z(G)=G$, then $G$ is abelian, and by Cauchy's theorem it has a subgroup of order $p$, which is normal and proper.
:::

:::

::: {.pf-step #p-larger}
If $p>q$, then the Sylow $p$-subgroup is normal.

::: pf-proof
By Sylow's theorems $n_p\divides q$ and $n_p\equiv1\pmod p$. Since $q<p$, $n_p=1$.
:::

:::

::: {.pf-step #q-larger}
If $p<q$ and $\abs{G}\ne12$, then the Sylow $q$-subgroup is normal.

::: pf-proof
By Sylow's theorems $n_q\divides p^2$ and $n_q\equiv1\pmod q$, so $n_q\in\{1,p,p^2\}$.
$n_q=p$ is impossible because $1<p<q$.
If $n_q=p^2$, then $q\divides p^2-1=(p-1)(p+1)$, and since $q>p-1$, $q\divides p+1$, so $q=p+1$.
The only primes differing by $1$ are $p=2$, $q=3$, which gives $\abs{G}=12$. Hence $n_q=1$.
:::

:::

::: {.pf-step #twelve}
If $\abs{G}=12$, then $G$ has a normal Sylow $3$-subgroup or a normal Sylow $2$-subgroup.

::: pf-proof
If $n_3=1$, the Sylow $3$-subgroup is normal. Otherwise $n_3=4$, and since distinct subgroups of order $3$ meet trivially, they contain $4\cdot2=8$ elements of order $3$.
The remaining four elements must form every Sylow $2$-subgroup, which has order $4$ and contains no element of order $3$.
So the Sylow $2$-subgroup is unique and therefore normal.
:::

:::

::: pf-step
$G$ has a nontrivial proper normal subgroup.

::: pf-proof
Steps [](#equal){.pf-ref}, [](#p-larger){.pf-ref}, [](#q-larger){.pf-ref} and [](#twelve){.pf-ref} cover all cases, and a Sylow subgroup of $G$ is nontrivial and proper when $p\ne q$.
:::

:::

:::

:::
