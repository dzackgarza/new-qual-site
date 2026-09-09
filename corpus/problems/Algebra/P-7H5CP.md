---
schema: qual/card@1
id: P-7H5CP
kind: problem
title: $p$-groups are nilpotent
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Nilpotent Groups
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

::: problem
- Show that every finite $p$-group is nilpotent.
:::


::: {.solution}
Let $G$ be a finite $p$-group. We prove that its upper central series reaches $G$.

<1>1. Every nontrivial quotient of $G$ has nontrivial center.
::: {.proof}
If $N\trianglelefteq G$ and $G/N\ne1$, then $G/N$ is again a finite $p$-group. Every finite $p$-group has nontrivial center by the class equation. Hence
\[
Z(G/N)\ne1.
\]
:::

<1>2. Define the upper central series by
\[
Z_0(G)=1,
\qquad
Z_{i+1}(G)/Z_i(G)=Z(G/Z_i(G)).
\]
As long as $Z_i(G)\ne G$, one has
\[
Z_i(G)<Z_{i+1}(G).
\]
::: {.proof}
If $Z_i(G)\ne G$, then the quotient $G/Z_i(G)$ is a nontrivial finite $p$-group. By <1>1 its center is nontrivial. Therefore
\[
Z_{i+1}(G)/Z_i(G)=Z(G/Z_i(G))\ne1,
\]
which is equivalent to the strict inclusion.
:::

<1>3. The upper central series reaches $G$ after finitely many steps.
::: {.proof}
Every $Z_i(G)$ is a subgroup of the finite group $G$. By <1>2, until the series reaches $G$ its order strictly increases. More precisely, each quotient
\[
Z_{i+1}(G)/Z_i(G)
\]
is a nontrivial $p$-group, so its order is at least $p$. If $|G|=p^n$, there can therefore be at most $n$ strict inclusions. Hence for some $c\le n$,
\[
Z_c(G)=G.
\]
:::

<1>4. Therefore $G$ is nilpotent.
::: {.proof}
A group is nilpotent precisely when its upper central series reaches the whole group after finitely many steps. This is exactly <1>3.
:::
:::
