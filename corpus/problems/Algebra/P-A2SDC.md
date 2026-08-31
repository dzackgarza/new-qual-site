---
schema: qual/card@1
id: P-A2SDC
kind: problem
title: Subgroups of index two are normal
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Prove that a subgroup of index two is normal.
:::

::: {.solution}
<1>1. Partition of $G$ into left and right cosets:
<2>1. Let $H \le G$ be a subgroup of index $[G : H] = 2$.
::: {.proof}
hypothesis.
:::
<2>2. Since there are exactly two left cosets and $H = eH$ is one of them, the other left coset for any $g \in G \setminus H$ must be the complement of $H$ in $G$:
\[
gH = G \setminus H \quad \text{for all } g \notin H.
\]
::: {.proof}
left cosets partition $G$.
:::
<2>3. Similarly, since there are exactly two right cosets, the other right coset for any $g \in G \setminus H$ is the complement of $H$ in $G$:
\[
Hg = G \setminus H \quad \text{for all } g \notin H.
\]
::: {.proof}
right cosets partition $G$.
:::

<1>2. Equality of left and right cosets:
<2>1. If $g \in H$, then $gH = H = Hg$.
::: {.proof}
closure of subgroup under multiplication.
:::
<2>2. If $g \in G \setminus H$, then by <2>2 and <2>3:
\[
gH = G \setminus H = Hg.
\]
::: {.proof}
both equal the set-theoretic complement $G \setminus H$.
:::
<2>3. Thus $gH = Hg$ for every $g \in G$.
::: {.proof}
<2>1 and <2>2 exhaust all cases $g \in G$.
:::

<1>3. Deduce normality:
<2>1. Multiplying $gH = Hg$ on the right by $g^{-1}$ yields:
\[
g H g^{-1} = H \quad \text{for all } g \in G.
\]
Thus $H$ is a normal subgroup of $G$ ($H \trianglelefteq G$).
::: {.proof}
definition of normal subgroup.
:::

<1>4. Conclusion:
Every subgroup of index two is normal. Q.E.D.
::: {.proof}
<1>1 through <1>3.
:::
:::
