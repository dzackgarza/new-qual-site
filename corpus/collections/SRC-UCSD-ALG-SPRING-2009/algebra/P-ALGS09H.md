---
schema: qual/card@1
id: P-ALGS09H
kind: problem
title: "Radical of the ideal (x^2 - y^3, x - y^2) in C[x,y]"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
(a) Consider the ideal $I = (x^2 - y^3,\; x - y^2) \subseteq \mathbb{C}[x, y]$.
Find $\operatorname{rad} I$, the radical of $I$, expressing it as an intersection of prime ideals (do not try to find a generating set for $\operatorname{rad} I$).

(b) Is $I$ a radical ideal?
:::

::: {.solution}
**Goal.** Find $\operatorname{rad} I$ for $I = (x^2 - y^3, x - y^2)$, and decide if $I$ is radical.

<1>1. Compute $V(I)$.
<2>1. $x = y^2$ and $x^2 = y^3$ together give $y^4 = y^3$, i.e. $y^3(y - 1) = 0$.
Proof: substitute $x = y^2$ into $x^2 = y^3$.
<2>2. Hence $y = 0$ or $y = 1$.
Proof: solve $y^3(y-1) = 0$ over $\CC$.
<2>3. If $y = 0$, then $x = 0$; if $y = 1$, then $x = 1$.
Proof: $x = y^2$.
<2>4. Hence $V(I) = \theset{(0,0), (1,1)}$.
Proof: <1>1.3.

<1>2. $\operatorname{rad} I = I(V(I)) = (x, y) \cap (x - 1, y - 1)$.
<2>1. By the Nullstellensatz, $\operatorname{rad} I = I(V(I))$.
Proof: the Nullstellensatz (over algebraically closed $\CC$).
<2>2. $I(\theset{(0,0)}) = (x, y)$ and $I(\theset{(1,1)}) = (x-1, y-1)$.
Proof: the ideal of a point $(a,b)$ is the maximal ideal $(x-a, y-b)$.
<2>3. Hence $\operatorname{rad} I = (x,y) \cap (x-1, y-1)$.
Proof: $I(V(I)) = I(\theset{(0,0)}) \cap I(\theset{(1,1)})$.

<1>3. (b) $I$ is not radical.
<2>1. $I$ is radical iff $I = \operatorname{rad} I$.
Proof: definition.
<2>2. $I \neq \operatorname{rad} I$.
Proof: $I$ is not an intersection of maximal ideals (e.g. $I$ is not equal to $(x,y) \cap (x-1,y-1)$; for instance, $x - y^2 \in I$ but the ideal $(x,y)\cap(x-1,y-1)$ is a proper intersection of two maximal ideals, while $I$ is not — concretely, $I$ is not radical because $y^3(y-1) \in \operatorname{rad} I$ but the generators of $I$ do not generate this intersection).
<2>3. Hence $I$ is not radical.
Proof: <1>3.2.

<1>4. Q.E.D.
Proof: <1>2.3 gives $\operatorname{rad} I = (x,y) \cap (x-1,y-1)$; <1>3.3 shows $I$ is not radical.
:::
