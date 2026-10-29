---
schema: qual/card@1
id: E-8EX2G
kind: problem
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

::: {.solution}
::: pf

::: pf-step

The real projective plane is a quotient of the closed disc.

::: pf-proof

::: pf-step

The real projective plane $\RP^2$ is homeomorphic to the closed unit disc $D^2 = \{x \in \RR^2 \mid \|x\| \le 1\}$ modulo the antipodal identification on its boundary:
        $$\RP^2 \cong D^2 / \sim, \quad \text{where } x \sim -x \text{ for } x \in S^1 = \partial D^2.$$

:::

::: pf-step

Let $q: D^2 \to \RP^2$ be the canonical quotient map.

:::

:::

:::

::: {.pf-step #y-is-annulus-quotient}

Deleting an open disc $U$ from $\RP^2$ leaves the quotient $A/\sim$ of a closed annulus $A$.

::: pf-proof

::: pf-step

Let $D_{1/2} = \{x \in \RR^2 \mid \|x\| < 1/2\}$ be the open central disc of radius $1/2$.

:::

::: pf-step

Since $D_{1/2} \subset \operatorname{Int}(D^2)$ contains no boundary points, $U = q(D_{1/2})$ is an open topological disc in $\RP^2$.

:::

::: pf-step

The punctured space $Y = \RP^2 \setminus U$ is homeomorphic to the quotient of the closed annulus $A = \{x \in \RR^2 \mid 1/2 \le \|x\| \le 1\}$ by the boundary identification $x \sim -x$ on the outer boundary circle $\|x\| = 1$.

:::

:::

:::

::: {.pf-step #annulus-quotient-is-mobius}

The identified annulus $A/\sim$ is homeomorphic to the Möbius strip $M$.

::: pf-proof

::: pf-step

In polar coordinates $(r, \theta)$ on $A$, the equivalence relation identifies $(1, \theta) \sim (1, \theta + \pi)$ for all $\theta \in [0, \pi]$, while leaving points with $1/2 \le r < 1$ un-identified.

:::

::: pf-step

Cut the annulus along the segments $\theta = 0$ and $\theta = \pi$.

:::

::: pf-step

Consider the semi-annulus $R = [0, \pi] \times [1/2, 1]$.

:::

::: pf-step

The outer arc $(1, \theta)$ connects $(1, 0)$ to $(1, \pi) \sim (1, 0)$, forming a continuous strip.

:::

::: pf-step

The radial edges at $\theta = 0$ and $\theta = \pi$ are glued with a reversal of orientation on the radial parameter, exactly realizing the standard quotient presentation of the Möbius strip:
        $$M = ([0, 1] \times [-1, 1]) / \sim, \quad (0, t) \sim (1, -t).$$

:::

::: pf-step

The inner boundary circle $r = 1/2$ becomes the single continuous boundary circle $\partial M$.

:::

::: pf-step

Hence $Y = A/\sim$ is homeomorphic to $M$.

:::

:::

:::

::: pf-step

The space obtained by deleting an open disc from $\RP^2$ is homeomorphic to the Möbius band $M$.

::: pf-proof

By step [](#y-is-annulus-quotient){.pf-ref}, $\RP^2 \setminus U \cong A/\sim$, and by step [](#annulus-quotient-is-mobius){.pf-ref}, $A/\sim \cong M$.

:::

:::

:::

:::
