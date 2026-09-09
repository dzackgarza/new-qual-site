---
schema: qual/card@1
id: E-AMD-TM3LMADH
kind: problem
title: Nontrivial normal subgroups of a finite $p$-group meet the center
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Normal Subgroups
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
Show that in a finite $p$-group, every nontrivial normal subgroup intersects the center nontrivially.
:::


::: {.solution}
Let $G$ be a finite $p$-group and let $1\neq N\trianglelefteq G$.

<1>1. Conjugation by $G$ defines an action of $G$ on $N$.
::: {.proof}
Because $N$ is normal, $gng^{-1}\in N$ for every $g\in G$ and $n\in N$. Hence $g\cdot n:=gng^{-1}$ defines a $G$-action on $N$.
:::

<1>2. Every non-singleton orbit has cardinality divisible by $p$.
::: {.proof}
For $n\in N$, orbit-stabilizer gives $|G\cdot n|=[G:C_G(n)]$. Since $G$ is a $p$-group, each orbit size is a power of $p$; hence every orbit of size greater than $1$ has size divisible by $p$.
:::

<1>3. The fixed points are exactly $N\cap Z(G)$.
::: {.proof}
An element $n\in N$ is fixed by every $g\in G$ exactly when $gng^{-1}=n$ for every $g$, equivalently when $n\in Z(G)$. Thus $N^G=N\cap Z(G)$.
:::

<1>4. The cardinality of $N\cap Z(G)$ is divisible by $p$.
::: {.proof}
Partition $N$ into conjugation orbits. By <1>2 and <1>3,
\[
|N|=|N\cap Z(G)|+\sum_i |\mathcal O_i|,
\]
where every $\mathcal O_i$ is a non-singleton orbit and therefore has size divisible by $p$. Since $N$ is a nontrivial subgroup of a finite $p$-group, $p\mid |N|$. Hence
\[
|N\cap Z(G)|\equiv |N|\equiv0\pmod p.
\]
:::

<1>5. Therefore $N\cap Z(G)$ is nontrivial.
::: {.proof}
The identity lies in $N\cap Z(G)$. By <1>4 its cardinality is divisible by $p$, so it cannot have cardinality $1$. Hence $N\cap Z(G)\neq\{1\}$.
:::
:::
