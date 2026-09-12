---
schema: qual/card@1
id: D-MORIMM
kind: definition
title: Open, closed, and locally closed immersions
classification:
  areas:
  - algebraic-geometry
  topics:
  - Immersions
  - Closed Subschemes
  - Morphisms
relations:
- kind: related-to
  target: D-VKR54
review: draft
prompts:
- What is an open immersion of schemes?
- What is a closed immersion of schemes?
- What is a closed subscheme?
---

::: {.definition title="Open immersion"}
$f : X \to Y$ is an **open immersion** if it induces an isomorphism of $X$ onto an open subscheme $U \subseteq Y$, meaning $\abs{U} \subseteq \abs{Y}$ is open and $\OO_U = \ro{\OO_Y}{U}$.
:::

::: {.definition title="Closed immersion"}
$f : X \to Y$ is a **closed immersion** if $\abs{f}$ is a homeomorphism onto a closed subset of $\abs{Y}$ and $f^\sharp : \OO_Y \to f_* \OO_X$ is surjective as a map of sheaves.
A **closed subscheme** is an equivalence class of closed immersions, where two are identified when they fit into a commuting triangle.
An **immersion** is a morphism making $X$ isomorphic to an open subscheme of a closed subscheme of $Y$.
:::

::: {.remark}
The underlying closed subset does not determine a closed subscheme.
The closed immersions $\Spec k \to \Spec k[\varepsilon]/(\varepsilon^2)$ and $\Spec k[\varepsilon]/(\varepsilon^2) \to \Spec k[\varepsilon]/(\varepsilon^2)$ have the same one-point image, but their sheaf maps distinguish the reduced point from the nonreduced one.
Surjectivity of $f^\sharp$ is what makes closed subschemes of $\Spec A$ correspond to ideals of $A$ rather than to closed subsets, so that $V(x)$ and $V(x^2)$ are different subschemes of $\AA^1$.

An immersion need be neither open nor closed: $\ts{xy = 0} \sm \ts{0}$ is a locally closed subscheme of $\AA^2$ that is neither open nor closed.
:::
