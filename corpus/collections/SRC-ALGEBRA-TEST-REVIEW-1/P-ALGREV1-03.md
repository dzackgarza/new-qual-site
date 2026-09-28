---
schema: qual/card@1
id: P-ALGREV1-03
kind: problem
title: Intersections of normal subgroups
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the card with Review1.md, open-ended question 3."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Proved arbitrary intersections of normal subgroups are normal by conjugating an element inside every subgroup."
---

::: {.problem}
Prove or disprove that normal subgroups are closed under intersection.
:::

::: {.solution}
The assertion is true; in fact an arbitrary intersection of normal subgroups
is normal.

<1>1. The intersection of normal subgroups is a subgroup.
::: {.proof}
Let $\{N_i\}_{i\in I}$ be normal subgroups of $G$ and put
$$
N=\bigcap_{i\in I}N_i.
$$
Every $N_i$ contains the identity, so $N$ does as well. If $x,y\in N$, then
$x,y\in N_i$ for every $i$, hence
$$
xy^{-1}\in N_i
$$
for every $i$. Therefore $xy^{-1}\in N$, so $N\le G$.
:::

<1>2. The intersection is invariant under conjugation.
::: {.proof}
Let $g\in G$ and $x\in N$. Since $x\in N_i$ for every $i$ and each $N_i$ is
normal,
$$
gxg^{-1}\in N_i
$$
for every $i$. Hence
$$
gxg^{-1}\in\bigcap_{i\in I}N_i=N.
$$
Thus $gNg^{-1}\subseteq N$. Replacing $g$ by $g^{-1}$ gives the reverse
inclusion, so $gNg^{-1}=N$.
:::

<1>3. Therefore normal subgroups are closed under intersection.
::: {.proof}
Steps <1>1 and <1>2 show
$$
\boxed{\bigcap_{i\in I}N_i\trianglelefteq G.}
$$
In particular, the intersection of any two normal subgroups is normal.
:::
:::
