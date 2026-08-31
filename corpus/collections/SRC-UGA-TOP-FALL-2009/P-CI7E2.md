---
schema: qual/card@1
id: P-CI7E2
kind: problem
title: Closed subsets and quotients $X/A$ of a normal space are normal
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Quotient Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $A$ be a closed subset of a normal topological space $X$.
Show that both $A$ and the quotient $X/A$ are normal.
:::

::: {.solution}
<1>1. $A$ is normal.
<2>1. Let $C, D \subseteq A$ be disjoint closed subsets of $A$.
::: {.proof}
take two disjoint closed subsets of $A$.
:::
<2>2. Since $A$ is closed in $X$, $C$ and $D$ are closed in $X$.
::: {.proof}
closed in a closed subspace implies closed in $X$.
:::
<2>3. Since $X$ is normal, there are disjoint open sets $U, V$ in $X$ with $C \subseteq U$ and $D \subseteq V$.
::: {.proof}
normality of $X$.
:::
<2>4. Then $U \cap A$ and $V \cap A$ are disjoint open sets in $A$ separating $C$ and $D$.
::: {.proof}
<2>3.
:::
<2>5. Hence $A$ is normal.
::: {.proof}
<2>1–<2>4.
:::

<1>2. $X/A$ is normal.
<2>1. The quotient map $q: X \to X/A$ is a closed map.
::: {.proof}
for a closed set $C \subseteq X$, $q^{-1}(q(C)) = C \cup A$ (if $C$ meets $A$) or $C$ (if $C$ is disjoint from $A$); in either case $q^{-1}(q(C))$ is closed in $X$ (since $A$ and $C$ are closed), so $q(C)$ is closed in $X/A$ by the definition of the quotient topology.
:::
<2>2. The image of a normal space under a closed continuous surjection is normal.
::: {.proof}
standard theorem (if $f: X \to Y$ is a closed continuous surjection and $X$ is normal, then $Y$ is normal).
:::
<2>3. Hence $X/A$ is normal.
::: {.proof}
<2>1 and <2>2.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
