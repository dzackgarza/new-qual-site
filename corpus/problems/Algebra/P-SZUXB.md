---
schema: qual/card@1
id: P-SZUXB
kind: problem
title: Groups of order $p^2q^2$ with $q\nmid(p^2-1)$ and $p\nmid(q^2-1)$ are abelian
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Abelian Groups
  - Classification
relations: []
review: draft
---

::: {.problem}
Let $p\ne q$ be primes. Show that a group $G$ of order $p^2q^2$ is abelian if
$$
q\nmid(p^2-1)\qquad\text{and}\qquad p\nmid(q^2-1).
$$
:::

::: {.solution}

Let $n_p$ and $n_q$ be the numbers of Sylow $p$- and Sylow $q$-subgroups of $G$.

::: pf

::: {.pf-step #P-normal}

The Sylow $p$-subgroup $P$ is unique, hence normal.

::: pf-proof

By Sylow's theorems, $n_p\mid q^2$ and $n_p\equiv1\pmod p$, so $n_p\in\{1,q,q^2\}$. If $n_p=q$ or $n_p=q^2$, then $q^2\equiv1\pmod p$, that is, $p\mid(q^2-1)$, contrary to hypothesis. So $n_p=1$.

:::

:::

::: {.pf-step #Q-normal}

The Sylow $q$-subgroup $Q$ is unique, hence normal.

::: pf-proof

Symmetrically, $n_q\in\{1,p,p^2\}$, and $n_q=p$ or $n_q=p^2$ would give $q\mid(p^2-1)$. So $n_q=1$.

:::

:::

::: pf-qed

By steps [](#P-normal){.pf-ref} and [](#Q-normal){.pf-ref}, $P,Q\normal G$, so $[P,Q]\le P\cap Q=1$ because $\abs{P}$ and $\abs{Q}$ are coprime. Hence $P$ and $Q$ commute elementwise, and $\abs{PQ}=\abs{P}\abs{Q}=\abs{G}$, so $G=P\times Q$. Every group of order the square of a prime is abelian, so $P$ and $Q$ are abelian, and therefore $G$ is abelian.

:::

:::

:::
