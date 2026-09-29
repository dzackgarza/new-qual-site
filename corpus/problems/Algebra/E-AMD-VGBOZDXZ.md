---
schema: qual/card@1
id: E-AMD-VGBOZDXZ
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
Show that every nontrivial normal subgroup of a finite $p$-group meets the center nontrivially.

> Hint: let $G$ act on the normal subgroup by conjugation and count the orbits.
:::


::: {.solution}
Let $1\neq N\trianglelefteq G$, where $G$ is a finite $p$-group.

::: pf

::: pf-step
Conjugation gives an action of $G$ on $N$.

::: pf-proof
Normality of $N$ gives $gng^{-1}\in N$ for all $g\in G$ and $n\in N$, so
\[
g\cdot n=gng^{-1}
\]
defines the action.
:::

:::

::: pf-step
The fixed-point set of this action is $N\cap Z(G)$.

::: pf-proof
An element $n\in N$ is fixed by every $g\in G$ exactly when $gng^{-1}=n$ for every $g$, which is equivalent to $n\in Z(G)$.
:::

:::

::: {.pf-step #nontrivial-orbit-div-by-p}
Every nontrivial orbit has cardinality divisible by $p$.

::: pf-proof
For $n\in N$, orbit-stabilizer gives
\[
|G\cdot n|=[G:C_G(n)].
\]
This index divides the order of the $p$-group $G$, so it is a power of $p$. If the orbit has more than one element, its cardinality is therefore divisible by $p$.
:::

:::

::: {.pf-step #n-cap-z-div-by-p}
The intersection $N\cap Z(G)$ has cardinality divisible by $p$.

::: pf-proof
The orbit decomposition of $N$ gives
\[
|N|=|N\cap Z(G)|+\sum_i |\mathcal O_i|,
\]
where the $\mathcal O_i$ are the nontrivial orbits. Since $N$ is a nontrivial subgroup of a finite $p$-group, $p\mid |N|$, and by step [](#nontrivial-orbit-div-by-p){.pf-ref} each summand in the sum is divisible by $p$. Hence
\[
|N\cap Z(G)|\equiv0\pmod p.
\]
:::

:::

::: pf-step
Therefore $N\cap Z(G)$ is nontrivial.

::: pf-proof
The intersection contains the identity. If it were trivial, its cardinality would be $1$, contradicting step [](#n-cap-z-div-by-p){.pf-ref}. Thus $N\cap Z(G)\neq\{1\}$.
:::

:::

:::

:::
