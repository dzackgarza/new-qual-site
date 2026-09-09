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

<1>1. Conjugation gives an action of $G$ on $N$.
::: {.proof}
Normality of $N$ gives $gng^{-1}\in N$ for all $g\in G$ and $n\in N$, so
\[
g\cdot n=gng^{-1}
\]
defines the action.
:::

<1>2. The fixed-point set of this action is $N\cap Z(G)$.
::: {.proof}
An element $n\in N$ is fixed by every $g\in G$ exactly when $gng^{-1}=n$ for every $g$, which is equivalent to $n\in Z(G)$.
:::

<1>3. Every nontrivial orbit has cardinality divisible by $p$.
::: {.proof}
For $n\in N$, orbit-stabilizer gives
\[
|G\cdot n|=[G:C_G(n)].
\]
This index divides the order of the $p$-group $G$, so it is a power of $p$. If the orbit has more than one element, its cardinality is therefore divisible by $p$.
:::

<1>4. The intersection $N\cap Z(G)$ has cardinality divisible by $p$.
::: {.proof}
The orbit decomposition of $N$ gives
\[
|N|=|N\cap Z(G)|+\sum_i |\mathcal O_i|,
\]
where the $\mathcal O_i$ are the nontrivial orbits. Since $N$ is a nontrivial subgroup of a finite $p$-group, $p\mid |N|$, and by <1>3 each summand in the sum is divisible by $p$. Hence
\[
|N\cap Z(G)|\equiv0\pmod p.
\]
:::

<1>5. Therefore $N\cap Z(G)$ is nontrivial.
::: {.proof}
The intersection contains the identity. If it were trivial, its cardinality would be $1$, contradicting <1>4. Thus $N\cap Z(G)\neq\{1\}$.
:::
:::
