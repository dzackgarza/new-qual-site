---
schema: qual/card@1
id: E-71YOD
kind: problem
title: Regular spaces have disjoint closure neighborhoods of points
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that if $X$ is regular, every pair of points of $X$ have neighborhoods whose closures are disjoint.
:::

::: {.solution}
**Goal:** Prove that in a regular ($T_3$) topological space $X$, every pair of distinct points possesses open neighborhoods with disjoint closures (i.e. $X$ is an Urysohn / $T_{2\frac{1}{2}}$ space).

::: pf

::: {.pf-step #separate-by-disjoint-opens}
Separation of distinct points by disjoint open sets:
Let $x, y \in X$ be distinct points ($x \neq y$).
There exist disjoint open sets $U_0, V_0 \subseteq X$ such that $x \in U_0$ and $y \in V_0$.

::: pf-proof

::: pf-step
In a regular space, one-point sets are closed ($T_1$ axiom), so $\{y\}$ is closed in $X$.
:::

::: pf-step
Because $x \neq y$, $x \notin \{y\}$.
:::

::: pf-step
By regularity of $X$, there exist disjoint open sets $U_0$ containing $x$ and $V_0$ containing $\{y\}$ such that $U_0 \cap V_0 = \varnothing$.
:::

:::

:::

::: {.pf-step #shrink-to-closed-containment}
Shrinking to open neighborhoods with closed containment:
There exist open neighborhoods $U \subseteq X$ of $x$ and $V \subseteq X$ of $y$ such that $\overline{U} \subseteq U_0$ and $\overline{V} \subseteq V_0$.

::: pf-proof

::: pf-step
By the standard characterization of regularity (Munkres Lemma 31.1), for any point $p$ and open neighborhood $W$ of $p$, there exists an open neighborhood $N$ of $p$ with $\overline{N} \subseteq W$.
:::

::: pf-step
Applying this to the point $x$ and its open neighborhood $U_0$, there exists an open neighborhood $U$ of $x$ such that $\overline{U} \subseteq U_0$.
:::

::: pf-step
Applying this to the point $y$ and its open neighborhood $V_0$, there exists an open neighborhood $V$ of $y$ such that $\overline{V} \subseteq V_0$.
:::

:::

:::

::: pf-step
Disjointness of the closures:

::: pf-proof

::: pf-step
By step [](#shrink-to-closed-containment){.pf-ref}, $\overline{U} \subseteq U_0$ and $\overline{V} \subseteq V_0$.
:::

::: pf-step
Therefore:
$$\overline{U} \cap \overline{V} \subseteq U_0 \cap V_0.$$
:::

::: pf-step
By step [](#separate-by-disjoint-opens){.pf-ref}, $U_0 \cap V_0 = \varnothing$, so $\overline{U} \cap \overline{V} = \varnothing$.
:::

:::

:::

::: pf-step
Conclusion:
$U$ and $V$ are open neighborhoods of $x$ and $y$ respectively with $\overline{U} \cap \overline{V} = \varnothing$. Q.E.D.
:::

:::

:::
