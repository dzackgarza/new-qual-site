---
schema: qual/card@1
id: E-O0HKU
kind: problem
title: Maps from compact to Hausdorff spaces are closed
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Show that if $f: X \to Y$ is continuous, where $X$ is compact and $Y$ is Hausdorff, then $f$ is a closed map (that is, $f$ carries closed sets to closed sets).
:::

::: {.solution}

::: pf

::: {.pf-step #c-closed-subset}
Let $C \subseteq X$ be an arbitrary closed subset.

::: pf-proof
setup.
:::

:::

::: {.pf-step #c-compact}
$C$ is a compact subspace of $X$.

::: pf-proof

::: {.pf-step #x-compact-hypothesis}
$X$ is compact by hypothesis.

::: pf-proof
hypothesis.
:::

:::

::: {.pf-step #closed-subset-of-compact-is-compact}
Every closed subset of a compact topological space is compact.

::: pf-proof
if $\mathcal{U}$ is an open cover of $C$, then $\mathcal{U} \cup \{X \setminus C\}$ is an open cover of $X$; the finite subcover of $X$ yields a finite subcover of $C$.
:::

:::

::: pf-step
Hence $C$ is compact.

::: pf-proof
Steps [](#x-compact-hypothesis){.pf-ref} and [](#closed-subset-of-compact-is-compact){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #fc-compact}
The image $f(C)$ is a compact subspace of $Y$.

::: pf-proof

::: {.pf-step #f-continuous-hypothesis}
$f: X \to Y$ is continuous.

::: pf-proof
hypothesis.
:::

:::

::: {.pf-step #continuous-image-of-compact-is-compact}
The continuous image of any compact space is compact.

::: pf-proof
if $\{V_\alpha\}$ is an open cover of $f(C)$, then $\{f^{-1}(V_\alpha)\}$ is an open cover of $C$; a finite subcover of $C$ maps under $f$ to a finite subcover of $f(C)$.
:::

:::

::: pf-step
Hence $f(C)$ is compact in $Y$.

::: pf-proof
Steps [](#c-compact){.pf-ref}, [](#f-continuous-hypothesis){.pf-ref}, and [](#continuous-image-of-compact-is-compact){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #fc-closed}
$f(C)$ is a closed subset of $Y$.

::: pf-proof

::: {.pf-step #y-hausdorff-hypothesis}
$Y$ is Hausdorff by hypothesis.

::: pf-proof
hypothesis.
:::

:::

::: {.pf-step #compact-subset-of-hausdorff-is-closed}
Every compact subset of a Hausdorff space is closed.

::: pf-proof
for any $y_0 \notin f(C)$, Hausdorff separation gives disjoint open neighborhoods $U_x$ of $x \in f(C)$ and $V_x$ of $y_0$; compactness of $f(C)$ yields a finite subcover $\bigcup_{i=1}^n U_{x_i} \supset f(C)$, and the intersection $\bigcap_{i=1}^n V_{x_i}$ is an open neighborhood of $y_0$ disjoint from $f(C)$.
:::

:::

::: pf-step
Hence $f(C)$ is closed in $Y$.

::: pf-proof
Steps [](#fc-compact){.pf-ref}, [](#y-hausdorff-hypothesis){.pf-ref}, and [](#compact-subset-of-hausdorff-is-closed){.pf-ref}.
:::

:::

:::

:::

::: pf-step
Conclusion: $f$ maps every closed set $C \subseteq X$ to a closed set $f(C) \subseteq Y$, so $f$ is a closed map.

::: pf-proof
Steps [](#c-closed-subset){.pf-ref} and [](#fc-closed){.pf-ref}.
Q.E.D.
:::

:::

:::

:::
