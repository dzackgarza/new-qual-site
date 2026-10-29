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

::: {.problem}
Let $G$ be a group of order $p^2q$, where $p$ and $q$ are primes. Show that $G$ has a normal Sylow subgroup.
:::

::: {.solution}
Write $n_r$ for the number of Sylow $r$-subgroups of $G$.

::: pf

::: pf-step
If $p=q$, then $G$ is a normal Sylow $p$-subgroup of itself.

::: pf-proof
Then $\abs{G}=p^3$, so $G$ is its own Sylow $p$-subgroup.
:::

:::

::: pf-step
If $p>q$, the Sylow $p$-subgroup is normal.

::: pf-proof
By the Sylow theorems, $n_p\mid q$ and $n_p\equiv1\pmod p$, so $n_p\in\{1,q\}$. Since $1<q<p$, $q\not\equiv1\pmod p$, so $n_p=1$.
:::

:::

::: {.pf-step #small-q}
If $p<q$, then either the Sylow $q$-subgroup is normal or $(p,q)=(2,3)$.

::: pf-proof
By the Sylow theorems, $n_q\mid p^2$ and $n_q\equiv1\pmod q$, so $n_q\in\{1,p,p^2\}$. Since $1<p<q$, $n_q\ne p$. If $n_q=p^2$, then $q\mid p^2-1=(p-1)(p+1)$; as $q>p-1>0$, this forces $q\mid p+1$, so $q=p+1$. The only primes differing by $1$ are $2$ and $3$.
:::

:::

::: pf-step
If $(p,q)=(2,3)$, so that $\abs{G}=12$, a Sylow subgroup of $G$ is normal.

::: pf-proof
If $n_3=1$, the Sylow $3$-subgroup is normal. Otherwise $n_3=4$. Distinct subgroups of order $3$ meet only in the identity, so they contain $4\cdot2=8$ elements of order $3$, and exactly $3$ nonidentity elements of $G$ have order other than $3$. A Sylow $2$-subgroup has order $4$, and its three nonidentity elements have order $2$ or $4$, so it consists of the identity and exactly these three elements. Hence $n_2=1$, and the Sylow $2$-subgroup is normal.
:::

:::

:::

:::
