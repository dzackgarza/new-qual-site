---
schema: qual/card@1
id: P-HPTFQ
kind: problem
title: Cauchy's theorem
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Cosets and Lagrange
  - p-Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'The source reads "Prove Cauchy''s theorem." followed by a quoted induction sketch that takes the quotient by $N=\langle g\rangle$, which is normal only when $G$ is abelian. The statement now states the theorem, and the sketch is a hint restricted to abelian $G$.'
---

::: {.problem}
Prove Cauchy's theorem: if $G$ is a finite group and $p$ is a prime dividing $\abs{G}$, then $G$ has an element of order $p$.
:::

::: {.hint}
For abelian $G$, induct on $\abs{G}$.
Pick $g\neq1$.
If $p$ divides the order of $g$, a power of $g$ has order $p$.
Otherwise $p$ divides $\abs{G/N}$ for $N=\langle g\rangle$, which is normal because $G$ is abelian, and induction gives $yN\in G/N$ of order $p$.
Then $p$ divides the order of $y$, and a power of $y$ has order $p$.
:::

::: {.solution}
Let $X=\{(g_1,\ldots,g_p)\in G^p: g_1g_2\cdots g_p=1\}$, and let $C_p=\langle\sigma\rangle$ act on $X$ by $\sigma(g_1,\ldots,g_p)=(g_2,\ldots,g_p,g_1)$.

::: pf

::: {.pf-step #s1}

$\abs{X}=\abs{G}^{p-1}$, so $p\mid\abs{X}$.

::: pf-proof

The entries $g_1,\ldots,g_{p-1}$ are arbitrary and determine $g_p=(g_1\cdots g_{p-1})^{-1}$.
The cyclic shift preserves $X$, since $g_2\cdots g_pg_1=g_1^{-1}(g_1\cdots g_p)g_1=1$.

:::

:::

::: {.pf-step #s2}

Every $C_p$-orbit in $X$ has size $1$ or $p$, and the orbits of size $1$ are the tuples $(g,\ldots,g)$ with $g^p=1$.

::: pf-proof

Orbit sizes divide $\abs{C_p}=p$.
A tuple is fixed by $\sigma$ exactly when all its entries are equal, and $(g,\ldots,g)\in X$ exactly when $g^p=1$.

:::

:::

::: pf-qed

Let $F$ be the set of fixed tuples.
By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, $\abs{F}\equiv\abs{X}\equiv0\pmod p$, and $(1,\ldots,1)\in F$, so $\abs{F}\ge p\ge2$.
Hence some $(g,\ldots,g)\in F$ has $g\neq1$ and $g^p=1$, and $g$ has order $p$.

:::

:::

:::
