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
- Why is the set-theoretic image not usable?
- What is the scheme-theoretic closure of a locally closed subscheme?
---

::: {.definition}
For $f: X \to Y$, the image of $f$ \dfn{lies in} a closed subscheme $Z \subseteq Y$ with ideal sheaf $\mci_Z$ if the composite $\mci_Z \to \OO_Y \to f_* \OO_X$ is zero, equivalently if $f$ factors through $Z$.
The \dfn{scheme-theoretic image} of $f$ is the smallest closed subscheme of $Y$ in which the image of $f$ lies, the intersection of all such $Z$.
When $\mci \da \ker(\OO_Y \to f_* \OO_X)$ is quasicoherent — for instance when $f$ is quasicompact and quasiseparated — this ideal sheaf defines it.
:::

::: {.definition title="Constructible set"}
In a Noetherian topological space $X$, the \dfn{constructible} subsets form the smallest family of subsets containing every open set and closed under finite intersections and complements.
A subset of $X$ is constructible if and only if it is a finite disjoint union of locally closed subsets.
[@Har10a, Exercise II.3.18]
:::

::: {.definition title="Scheme-theoretic closure"}
The \dfn{scheme-theoretic closure} of a locally closed immersion $i \colon X \to Y$ is the scheme-theoretic image of $i$.
:::

::: {.proposition}
If $X$ is reduced, the scheme-theoretic image is $\closure{f(X)}$ with its reduced induced structure.
For $f: \Spec B \to \Spec A$ induced by $\varphi: A \to B$, the image is $\Spec(A/\ker \varphi)$.
:::

::: {.remark}
The set-theoretic image is not usable because it need not be closed, nor open, nor even locally closed: $\AA^2 \to \AA^2$, $(x,y) \mapsto (x, xy)$, has image the plane minus the $y$-axis plus the origin.
Chevalley's theorem is the rescue — the image of a constructible set under a finite-type morphism of Noetherian schemes is constructible — and it is the expected follow-up.

The nonreduced case is where the definition earns its keep: the image of $\Spec k[\eps]/\eps^2 \to \AA^1$ hitting the origin with a nonzero tangent direction is the double point, not the reduced point, because the kernel of $k[t] \to k[\eps]/\eps^2$ is $(t^2)$.
Taking closures of point sets would lose exactly that.
:::
