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
$f : X \to Y$ is an \dfn{open immersion} if it induces an isomorphism of $X$ onto an open subscheme $U \subseteq Y$, meaning $\abs{U} \subseteq \abs{Y}$ is open and $\OO_U = \ro{\OO_Y}{U}$.
:::

::: {.definition title="Closed immersion"}
$f : X \to Y$ is a \dfn{closed immersion} if $\abs{f}$ is a homeomorphism onto a closed subset of $\abs{Y}$ and $f^\sharp : \OO_Y \to f_* \OO_X$ is surjective as a map of sheaves.
A \dfn{closed subscheme} is an equivalence class of closed immersions, where two are identified when they fit into a commuting triangle.
An \dfn{immersion} is a morphism making $X$ isomorphic to an open subscheme of a closed subscheme of $Y$.
:::

::: {.definition title="Locally closed immersion"}
A morphism $f \colon X \to Y$ is a \dfn{locally closed immersion} if it factors as $X \to U \to Y$ with $X \to U$ a closed immersion and $U \to Y$ an open immersion.
:::

::: {.proposition}
Every immersion is a locally closed immersion, and a quasicompact locally closed immersion is an immersion; in particular the two notions agree when $Y$ is locally Noetherian.
:::

::: {.remark}
A homeomorphism onto a closed subset need not be a closed immersion: the structure morphism $\Spec k[\varepsilon]/(\varepsilon^2)\to\Spec k$ is a homeomorphism of one-point spaces, and $k\to k[\varepsilon]/(\varepsilon^2)$ is not surjective.
Closed subschemes of $\Spec A$ correspond bijectively to ideals of $A$ [@Har10a, Corollary II.5.10]; so $V(x)$ and $V(x^2)$ are distinct closed subschemes of $\AA^1$ with the same underlying point.

The inclusion $\ts{xy = 0} \sm \ts{0}\to\AA^2$ is a locally closed immersion that is neither an open nor a closed immersion.
:::
