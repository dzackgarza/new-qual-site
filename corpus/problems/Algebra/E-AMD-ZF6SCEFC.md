---
schema: qual/card@1
id: E-AMD-ZF6SCEFC
kind: problem
title: Groups of order $p^2q^2$ are abelian when $q\nmid p^2-1$ and $p\nmid q^2-1$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Abelian Groups
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}
Show that a group of order $p^2 q^2$ where $q$ does not divide $p^2-1$ and $p$ does not divide $q^2-1$ is abelian.
:::

::: {.solution}
Let $p\neq q$ be primes and $|G|=p^2q^2$, and let $n_p$, $n_q$ be the numbers of Sylow $p$- and $q$-subgroups.

<1>1. The Sylow $p$-subgroup $P$ is normal.

::: {.proof}
By Sylow's theorems, $n_p\mid q^2$ and $n_p\equiv1\pmod p$, so $n_p\in\{1,q,q^2\}$.
If $n_p=q$ or $n_p=q^2$, then $p\mid q-1$ or $p\mid q^2-1$; in both cases $p\mid q^2-1$, contrary to hypothesis.
So $n_p=1$.
:::

<1>2. The Sylow $q$-subgroup $Q$ is normal.

::: {.proof}
Exchange $p$ and $q$ in step <1>1, using $q\nmid p^2-1$.
:::

<1>3. $G\cong P\times Q$.

::: {.proof}
$P\cap Q=1$ since $\gcd(p^2,q^2)=1$, and $|PQ|=|P||Q|=|G|$, so $G=PQ$.
For $x\in P$ and $y\in Q$, normality of $Q$ gives $xyx^{-1}y^{-1}\in Q$ and normality of $P$ gives $x(yx^{-1}y^{-1})\in P$, so $xyx^{-1}y^{-1}\in P\cap Q=1$.
Thus $P$ and $Q$ commute elementwise and $(x,y)\mapsto xy$ is an isomorphism $P\times Q\to G$.
:::

<1>4. Q.E.D.

::: {.proof}
Groups of order $p^2$ and $q^2$ are abelian, so $P$ and $Q$ are abelian, and by step <1>3 so is $G\cong P\times Q$.
:::
:::

::: {.remark}
The hypothesis $p\neq q$ is needed: for $p=q$ both divisibility conditions hold, and a group of order $p^4$ need not be abelian, as the dihedral group of order $16$ shows.
:::
