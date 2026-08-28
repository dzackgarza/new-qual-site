---
schema: qual/card@1
id: E-8EX2G
kind: exercise
title: The Mobius band is a punctured projective plane
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

The Möbius band $M$ is not a surface, but what is called a "surface with boundary".
Show that $M$ is homeomorphic to the space obtained by deleting an open disc from $P^2$.
:::

::: solution
**Goal:** Prove that deleting an open disc from the real projective plane $\mathbb{R}P^2$ yields a space homeomorphic to the Möbius band $M$.

<1>1. Quotient model of the real projective plane:
    *Proof:*
    <2>1. The real projective plane $\mathbb{R}P^2$ is homeomorphic to the closed unit disc $D^2 = \{x \in \mathbb{R}^2 \mid \|x\| \le 1\}$ modulo the antipodal identification on its boundary:
        $$\mathbb{R}P^2 \cong D^2 / \sim, \quad \text{where } x \sim -x \text{ for } x \in S^1 = \partial D^2.$$
    <2>2. Let $q: D^2 \to \mathbb{R}P^2$ be the canonical quotient map.

<1>2. Deleting an open disc from $\mathbb{R}P^2$:
    *Proof:*
    <2>1. Let $D_{1/2} = \{x \in \mathbb{R}^2 \mid \|x\| < 1/2\}$ be the open central disc of radius $1/2$.
    <2>2. Since $D_{1/2} \subset \operatorname{Int}(D^2)$ contains no boundary points, $U = q(D_{1/2})$ is an open topological disc in $\mathbb{R}P^2$.
    <2>3. The punctured space $Y = \mathbb{R}P^2 \setminus U$ is homeomorphic to the quotient of the closed annulus $A = \{x \in \mathbb{R}^2 \mid 1/2 \le \|x\| \le 1\}$ by the boundary identification $x \sim -x$ on the outer boundary circle $\|x\| = 1$.

<1>3. Homeomorphism between the identified annulus $A/\sim$ and the Möbius strip $M$:
    *Proof:*
    <2>1. In polar coordinates $(r, \theta)$ on $A$, the equivalence relation identifies $(1, \theta) \sim (1, \theta + \pi)$ for all $\theta \in [0, \pi]$, while leaving points with $1/2 \le r < 1$ un-identified.
    <2>2. Cut the annulus along the segments $\theta = 0$ and $\theta = \pi$.
    <2>3. Consider the semi-annulus $R = [0, \pi] \times [1/2, 1]$.
    <2>4. The outer arc $(1, \theta)$ connects $(1, 0)$ to $(1, \pi) \sim (1, 0)$, forming a continuous strip.
    <2>5. The radial edges at $\theta = 0$ and $\theta = \pi$ are glued with a reversal of orientation on the radial parameter, exactly realizing the standard quotient presentation of the Möbius strip:
        $$M = ([0, 1] \times [-1, 1]) / \sim, \quad (0, t) \sim (1, -t).$$
    <2>6. The inner boundary circle $r = 1/2$ becomes the single continuous boundary circle $\partial M$.
    <2>7. Hence $Y = A/\sim$ is homeomorphic to $M$.

<1>4. Conclusion:
    The space obtained by deleting an open disc from $\mathbb{R}P^2$ is homeomorphic to the Möbius band $M$. Q.E.D.
:::
