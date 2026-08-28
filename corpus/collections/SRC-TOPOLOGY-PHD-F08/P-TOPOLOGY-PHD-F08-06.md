---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-06
kind: problem
title: Closed-map and open-map criteria for identification maps
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.problem}
Define the term identification map in the category of topological spaces.
Let $\pi:X\to Y$ be a surjective, continuous map of topological spaces.
Suppose that $\pi$ maps closed sets to closed sets.
Show that $\pi$ is an identification map.
What happens if we replace closed sets by open sets?
Justify your answers.
:::

::: solution
**Goal:** Define an identification map and prove that any surjective continuous map that is either closed or open is an identification map.

<1>1. Definition of an identification (quotient) map:
    A map $\pi: X \to Y$ between topological spaces is an **identification map** (or quotient map) if:
    1. $\pi$ is surjective,
    2. A subset $U \subseteq Y$ is open in $Y$ if and only if $\pi^{-1}(U)$ is open in $X$.
    *(Equivalently, since $\pi^{-1}(Y \setminus F) = X \setminus \pi^{-1}(F)$, a subset $F \subseteq Y$ is closed in $Y$ if and only if $\pi^{-1}(F)$ is closed in $X$.)*

<1>2. Closed surjective continuous maps are identification maps:
    Let $\pi: X \to Y$ be surjective, continuous, and closed. Then $\pi$ is an identification map.
    *Proof:*
    <2>1. $\pi$ is surjective by assumption.
    <2>2. We verify that for any $F \subseteq Y$, $F$ is closed in $Y \iff \pi^{-1}(F)$ is closed in $X$.
    <2>3. ($\implies$) If $F$ is closed in $Y$, then $\pi^{-1}(F)$ is closed in $X$ because $\pi$ is continuous.
    <2>4. ($\impliedby$) Suppose $\pi^{-1}(F)$ is closed in $X$. Since $\pi$ is a closed map, the image $\pi(\pi^{-1}(F))$ is closed in $Y$.
    <2>5. Since $\pi$ is surjective, $\pi(\pi^{-1}(F)) = F$. Thus $F$ is closed in $Y$.
    <2>6. Hence $F$ is closed in $Y \iff \pi^{-1}(F)$ is closed in $X$, so $\pi$ is an identification map.

<1>3. Open surjective continuous maps are identification maps:
    If we replace closed sets with open sets, $\pi$ is also an identification map: any surjective, continuous, and open map $\pi: X \to Y$ is an identification map.
    *Proof:*
    <2>1. $\pi$ is surjective by assumption.
    <2>2. We verify that for any $U \subseteq Y$, $U$ is open in $Y \iff \pi^{-1}(U)$ is open in $X$.
    <2>3. ($\implies$) If $U$ is open in $Y$, then $\pi^{-1}(U)$ is open in $X$ because $\pi$ is continuous.
    <2>4. ($\impliedby$) Suppose $\pi^{-1}(U)$ is open in $X$. Since $\pi$ is an open map, the image $\pi(\pi^{-1}(U))$ is open in $Y$.
    <2>5. Since $\pi$ is surjective, $\pi(\pi^{-1}(U)) = U$. Thus $U$ is open in $Y$.
    <2>6. Hence $U$ is open in $Y \iff \pi^{-1}(U)$ is open in $X$, so $\pi$ is an identification map. Q.E.D.
:::

::: remark
The source page prints a colon immediately before the arrow in the map notation; the map is rendered here with the conventional $\to$ notation.
:::
