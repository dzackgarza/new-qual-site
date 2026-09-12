---
schema: qual/card@1
id: D-SCHIMG
kind: definition
title: The scheme-theoretic image of a morphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Subschemes
  - Morphisms Of Schemes
  - Ideal Sheaves
relations:
- kind: uses
  target: D-SCHSUB
- kind: uses
  target: D-SCHRED
review: draft
prompts:
- What is the scheme-theoretic image of a morphism?
- How does the scheme-theoretic image differ from the set-theoretic image?
---

::: {.definition}
For $f: X \to Y$, the **scheme-theoretic image** is the smallest closed subscheme of $Y$ through which $f$ factors.
When $\mci \da \ker(\OO_Y \to f_* \OO_X)$ is quasicoherent — for instance when $f$ is quasicompact and quasiseparated — this ideal sheaf defines it.
:::

::: {.proposition}
If $X$ is reduced, the scheme-theoretic image is $\closure{f(X)}$ with its reduced induced structure.
For $f: \Spec B \to \Spec A$ induced by $\varphi: A \to B$, the image is $\Spec(A/\ker \varphi)$.
:::

::: {.remark}
The set-theoretic image need not be locally closed: $\AA^2 \to \AA^2$, $(x,y) \mapsto (x, xy)$, has image the plane minus the $y$-axis plus the origin.
By Chevalley's theorem, the image of a constructible set under a finite-type morphism of Noetherian schemes is constructible.

The scheme-theoretic image of $\Spec k[\eps]/\eps^2 \to \AA^1$ hitting the origin with a nonzero tangent direction is the double point, because the kernel of $k[t] \to k[\eps]/\eps^2$ is $(t^2)$.
Taking closures of point sets would lose exactly that.
:::
