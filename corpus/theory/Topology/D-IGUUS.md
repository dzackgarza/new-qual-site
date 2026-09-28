---
schema: qual/card@1
id: D-IGUUS
kind: definition
title: Wedge sum
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Homology
  - Quotient Spaces
relations: []
review: draft
---

::: {.definition}
Let $(X_\alpha, x_\alpha)_{\alpha\in A}$ be a family of based topological spaces.
The \dfn{wedge sum} $\bigvee_{\alpha\in A} X_\alpha$ is the quotient space of the disjoint union $\coprod_{\alpha\in A} X_\alpha$ obtained by identifying all the basepoints $x_\alpha$ to a single point, which is its basepoint.
For two based spaces, $X\vee Y$ is the quotient of $X\sqcup Y$ identifying $x_0$ with $y_0$.
:::

::: {.proposition}
Let $X$ be a [[D-ZOU5G|CW complex]] with $n$-skeleton $X^n$.
Then $X^n/X^{n-1}$ is homeomorphic to $\bigvee_\alpha S^n_\alpha$, a wedge of $n$-spheres with one sphere for each [[D-MEPE3|$n$-cell]] of $X$.
:::

::: {.proposition}
If each $(X_\alpha, x_\alpha)$ is a good pair, then the inclusions $X_\alpha\hookrightarrow\bigvee_\alpha X_\alpha$ induce an isomorphism
$$
\bigoplus_\alpha\tilde H_n(X_\alpha)\to\tilde H_n\qty{\bigvee_\alpha X_\alpha}
$$
for every $n$.
:::

::: {.concept}
See [@Hat02].
:::
