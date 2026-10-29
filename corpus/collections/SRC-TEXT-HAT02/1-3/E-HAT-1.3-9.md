---
schema: qual/card@1
id: E-HAT-1.3-9
kind: problem
title: Maps to $S^1$ from spaces with finite fundamental group
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}
Show that if a path-connected, locally path-connected space $X$ has $\pi_1(X)$ finite, then every map $f: X \to S^1$ is nullhomotopic.
:::

::: {.solution}
::: pf

::: {.pf-step #s1}
The induced homomorphism $f_*: \pi_1(X, x_0) \to \pi_1(S^1, f(x_0))$ is trivial.

::: pf-proof

::: pf-step
Fix a basepoint $x_0 \in X$ and let $s_0 = f(x_0) \in S^1$.
:::

::: pf-step
The induced map $f_*: \pi_1(X, x_0) \to \pi_1(S^1, s_0) \cong \ZZ$ is a group homomorphism.
:::

::: pf-step
The image $f_*(\pi_1(X, x_0))$ is a subgroup of $\ZZ$.
:::

::: pf-step
By the First Isomorphism Theorem for groups, $|f_*(\pi_1(X, x_0))|$ divides $|\pi_1(X, x_0)| < \infty$, so the image is a finite subgroup of $\ZZ$.
:::

::: pf-step
Since $\ZZ$ is infinite cyclic and torsion-free, its only finite subgroup is the trivial subgroup $\{0\}$.
:::

::: pf-step
Thus $f_*(\pi_1(X, x_0)) = \{0\}$.
:::

:::

:::

::: {.pf-step #lift}
$f$ lifts to a map $\widetilde{f}: X \to \RR$ with $p \circ \widetilde{f} = f$, where $p: \RR \to S^1$ is the universal covering.

::: pf-proof

::: pf-step
Let $p: \RR \to S^1$ be the standard universal covering map given by $p(t) = e^{2\pi i t}$, and choose $t_0 \in \RR$ with $p(t_0) = s_0$.
:::

::: pf-step
The fundamental group of the total space is trivial: $p_*(\pi_1(\RR, t_0)) = \{0\}$.
:::

::: pf-step
From step [](#s1){.pf-ref}, we have $f_*(\pi_1(X, x_0)) = \{0\} \subseteq p_*(\pi_1(\RR, t_0))$.
:::

::: pf-step
Since $X$ is path-connected and locally path-connected, the Covering Space Lifting Criterion applies: there exists a unique continuous map $\widetilde{f}: X \to \RR$ such that
$$p \circ \widetilde{f} = f \quad \text{and} \quad \widetilde{f}(x_0) = t_0.$$
:::

:::

:::

::: pf-step
$f$ is nullhomotopic.

::: pf-proof

::: pf-step
The codomain $\RR$ is convex and contractible.
:::

::: pf-step
Define the straight-line homotopy $\widetilde{H}: X \times [0, 1] \to \RR$ by
$$\widetilde{H}(x, t) = (1 - t) \widetilde{f}(x) + t \cdot 0.$$
:::

::: pf-step
The map $\widetilde{H}$ is continuous, with $\widetilde{H}(x, 0) = \widetilde{f}(x)$ and $\widetilde{H}(x, 1) = 0$ (the constant map to $0 \in \RR$).
:::

::: pf-step
Define $H: X \times [0, 1] \to S^1$ by post-composing with the covering map:
$$H(x, t) = p(\widetilde{H}(x, t)) = e^{2\pi i \widetilde{H}(x, t)}.$$
:::

::: pf-step
Since $p$ and $\widetilde{H}$ are continuous, $H$ is a continuous homotopy.
:::

::: pf-step
Evaluating at the endpoints:
$$H(x, 0) = p(\widetilde{f}(x)) = f(x), \qquad H(x, 1) = p(0) = e^0 = 1.$$
:::

::: pf-step
Thus $H$ is a homotopy between $f$ and the constant map $c_1(x) = 1$.
:::

:::

:::

:::
:::
