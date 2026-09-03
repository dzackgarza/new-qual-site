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

::: solution
**Goal:** Prove that in a regular ($T_3$) topological space $X$, every pair of distinct points possesses open neighborhoods with disjoint closures (i.e. $X$ is an Urysohn / $T_{2\frac{1}{2}}$ space).

<1>1. Separation of distinct points by disjoint open sets:
    Let $x, y \in X$ be distinct points ($x \neq y$).
    There exist disjoint open sets $U_0, V_0 \subseteq X$ such that $x \in U_0$ and $y \in V_0$.
    *Proof:*
    <2>1. In a regular space, one-point sets are closed ($T_1$ axiom), so $\{y\}$ is closed in $X$.
    <2>2. Because $x \neq y$, $x \notin \{y\}$.
    <2>3. By regularity of $X$, there exist disjoint open sets $U_0$ containing $x$ and $V_0$ containing $\{y\}$ such that $U_0 \cap V_0 = \varnothing$.

<1>2. Shrinking to open neighborhoods with closed containment:
    There exist open neighborhoods $U \subseteq X$ of $x$ and $V \subseteq X$ of $y$ such that $\overline{U} \subseteq U_0$ and $\overline{V} \subseteq V_0$.
    *Proof:*
    <2>1. By the standard characterization of regularity (Munkres Lemma 31.1), for any point $p$ and open neighborhood $W$ of $p$, there exists an open neighborhood $N$ of $p$ with $\overline{N} \subseteq W$.
    <2>2. Applying this to the point $x$ and its open neighborhood $U_0$, there exists an open neighborhood $U$ of $x$ such that $\overline{U} \subseteq U_0$.
    <2>3. Applying this to the point $y$ and its open neighborhood $V_0$, there exists an open neighborhood $V$ of $y$ such that $\overline{V} \subseteq V_0$.

<1>3. Disjointness of the closures:
    *Proof:*
    <2>1. By <1>2, $\overline{U} \subseteq U_0$ and $\overline{V} \subseteq V_0$.
    <2>2. Therefore:
        $$\overline{U} \cap \overline{V} \subseteq U_0 \cap V_0.$$
    <2>3. By <1>1, $U_0 \cap V_0 = \varnothing$, so $\overline{U} \cap \overline{V} = \varnothing$.

<1>4. Conclusion:
    $U$ and $V$ are open neighborhoods of $x$ and $y$ respectively with $\overline{U} \cap \overline{V} = \varnothing$. Q.E.D.
:::
