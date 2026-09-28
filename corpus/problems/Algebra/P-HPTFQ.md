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
---

::: {.problem}
- Prove Cauchy's theorem.

> Induce on $\size G$.
> Assume $\size G > p$ and pick $g\neq 1$.
> If $p\divides \size g$, use cyclic group theory, so assume otherwise.
> Use that $\size G = \size G/N \size N$ so $p$ divides $\size G/N$, apply IH to get an element of order $p$ in the quotient.
> Then $y\not\in N$ but $y^p\in N$, so $\gens{y}\neq \gens{y^p}$ since $y^p\in N \implies \gens{y^p} \subseteq N$.
> Get $p\divides \size \gens{y}$, apply IH.
:::

::: {.solution}
Cauchy's theorem: if $G$ is a finite group and $p$ is a prime dividing $|G|$, then $G$ has an element of order $p$.

Let $X=\{(g_1,\dots,g_p)\in G^p: g_1g_2\cdots g_p=1\}$, and let $C_p=\langle\sigma\rangle$ act on $X$ by $\sigma(g_1,\dots,g_p)=(g_2,\dots,g_p,g_1)$.

<1>1. $|X|=|G|^{p-1}$, so $p\mid|X|$.

::: {.proof}
$g_1,\dots,g_{p-1}$ are arbitrary and determine $g_p=(g_1\cdots g_{p-1})^{-1}$.
The cyclic shift preserves $X$, since $g_2\cdots g_pg_1=g_1^{-1}(g_1\cdots g_p)g_1=1$.
:::

<1>2. Every $C_p$-orbit in $X$ has size $1$ or $p$, and the orbits of size $1$ are the tuples $(g,\dots,g)$ with $g^p=1$.

::: {.proof}
Orbit sizes divide $|C_p|=p$.
A tuple is fixed by $\sigma$ exactly when all its entries are equal, and $(g,\dots,g)\in X$ exactly when $g^p=1$.
:::

<1>3. Q.E.D.

::: {.proof}
Let $F$ be the set of fixed tuples.
By steps <1>1 and <1>2, $|F|\equiv|X|\equiv0\pmod p$, and $(1,\dots,1)\in F$, so $|F|\ge p\ge2$.
Hence some $(g,\dots,g)\in F$ has $g\neq1$ and $g^p=1$, and $g$ has order $p$.
:::
:::
