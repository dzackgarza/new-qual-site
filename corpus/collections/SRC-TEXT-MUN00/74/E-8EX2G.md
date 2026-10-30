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
Take $M$ to be the quotient of the rectangle $[0,\pi] \times [1/2, 3/2]$ by $(0, s) \sim (\pi, 2 - s)$; the affine map $(\theta, s) \mapsto (\theta/\pi, 3/2 - s)$ carries this to the presentation $[0,1] \times [0,1]$ with $(0,y) \sim (1, 1-y)$.
Write points of the plane in polar coordinates $(r, \theta)$, with $\theta$ taken mod $2\pi$.

::: pf

::: {.pf-step #disc-model}
$P^2$ is homeomorphic to the quotient of the closed unit disc $D^2$ by $x \sim -x$ for $\norm{x} = 1$.

::: pf-proof
The map $h \colon D^2 \to S^2$, $h(x) = (x, \sqrt{1 - \norm{x}^2})$, followed by the quotient $S^2 \to P^2$, is continuous and surjective, because every antipodal pair has a point with nonnegative last coordinate.
Two points of $D^2$ have the same image exactly when they are equal or are antipodal points of $\partial D^2$.
As $D^2$ is compact and $P^2$ is Hausdorff, the map is closed, hence a quotient map, and induces the homeomorphism.
:::

:::

::: {.pf-step #annulus}
Let $q \colon D^2 \to P^2$ be the quotient map of step [](#disc-model){.pf-ref} and $U = q(\{\norm{x} < 1/2\})$.
Then $U$ is an open disc in $P^2$, and $Y = P^2 \setminus U$ is homeomorphic to the quotient $A/{\sim}$ of the closed annulus $A = \{1/2 \le \norm{x} \le 1\}$ by $x \sim -x$ for $\norm{x} = 1$.

::: pf-proof
The set $\{\norm{x} < 1/2\}$ is open and saturated, so $U$ is open, and $q$ is injective on it, so $q$ maps it homeomorphically onto $U$ (an injective restriction of a quotient map to an open saturated set is a quotient map onto its image).
$A$ is saturated with $q(A) = Y$, so $q\restrict_A \colon A \to Y$ is a continuous surjection from a compact space to a Hausdorff space, hence a quotient map, and its identifications are exactly $x \sim -x$ on $\norm{x} = 1$.
:::

:::

::: {.pf-step #map}
The map $\Phi \colon [0,\pi] \times [1/2, 3/2] \to A/{\sim}$ given by $\Phi(\theta, s) = [(s, \theta)]$ for $s \le 1$ and $\Phi(\theta, s) = [(2 - s, \theta + \pi)]$ for $s \ge 1$ is well defined, continuous and surjective.

::: pf-proof
At $s = 1$ the two formulas give the classes of $(1, \theta)$ and $(1, \theta + \pi)$, which are equal, so the pasting lemma gives a continuous map.
The first formula covers the half annulus $\theta \in [0, \pi]$ and the second the half annulus $\theta \in [\pi, 2\pi]$, so $\Phi$ is surjective.
:::

:::

::: {.pf-step #fibres}
$\Phi(\theta, s) = \Phi(\theta', s')$ with $(\theta, s) \neq (\theta', s')$ holds exactly when $\{\theta, \theta'\} = \{0, \pi\}$ and $s' = 2 - s$.

::: pf-proof
For $s < 1$, $\Phi(\theta, s)$ is the class of the single point at radius $s$ and angle $\theta \in [0, \pi]$; for $s > 1$, it is the single point at radius $2 - s < 1$ and angle $\theta + \pi \in [\pi, 2\pi]$.
Points at radius $r < 1$ are unidentified in $A/{\sim}$, so two such values agree only when the angles agree mod $2\pi$: either $(\theta, s) = (\theta', s')$, or one angle is $0 \equiv 2\pi$ and the other $\pi$, that is $\{\theta, \theta'\} = \{0, \pi\}$ and $s' = 2 - s$.
For $s = 1$, $\Phi(\theta, 1)$ is the class $\{(1, \theta), (1, \theta + \pi)\}$, and $\theta \mapsto$ this class is injective on $[0, \pi)$ with $\Phi(\pi, 1) = \Phi(0, 1)$, which is the case $s = s' = 1$ of the stated rule.
Conversely, $\Phi(0, s) = \Phi(\pi, 2 - s)$ for every $s$, by the two formulas.
:::

:::

::: pf-qed
By step [](#fibres){.pf-ref}, $\Phi$ identifies exactly the points $(0, s) \sim (\pi, 2 - s)$, so it induces a continuous bijection $M \to A/{\sim}$.
$M$ is compact and $A/{\sim} \cong Y \subset P^2$ is Hausdorff by step [](#annulus){.pf-ref}, so this bijection is a homeomorphism, and $M \cong P^2 \setminus U$.
:::

:::

:::
