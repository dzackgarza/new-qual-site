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

::: {.definition title="Locally closed immersion"}
A morphism $f \colon X \to Y$ is a \dfn{locally closed immersion} if it factors as $X \to U \to Y$ with $X \to U$ a closed immersion and $U \to Y$ an open immersion.
:::

::: {.proposition}
Every immersion is a locally closed immersion, and a quasicompact locally closed immersion is an immersion; in particular the two notions agree when $Y$ is locally Noetherian.
:::

::: {.remark}
The surjectivity clause is the whole definition, and the examiner asks about it by asking why a homeomorphism onto a closed set is not enough.
The answer is $\Spec k \to \Spec k[\varepsilon]/(\varepsilon^2)$ versus $\Spec k[\varepsilon]/(\varepsilon^2) \to \Spec k[\varepsilon]/(\varepsilon^2)$: the underlying spaces are the same one point, and only the sheaf map distinguishes the reduced point from the fat one.
Surjectivity of $f^\sharp$ is what makes closed subschemes of $\Spec A$ correspond to ideals of $A$ rather than to closed subsets, so that $V(x)$ and $V(x^2)$ are different subschemes of $\AA^1$.

Locally closed is the honest general notion, and it is why "immersion" is not just the two extremes glued: $\ts{xy = 0} \sm \ts{0}$ sits in $\AA^2$ as neither an open nor a closed subscheme.
:::
