---
schema: qual/card@1
id: P-AMD-PYAZZ4MG
kind: problem
title: $f\simeq g$ implies $X\cup_f B^2 \simeq X\cup_g B^2$
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
**REVISIT** Let $f,g : S^1 \rightarrow X$, $P = X \cup_f B^2 \cong X \coprod B^2 / \sim$, where $x \sim f(x)$, $Q = X \cup_g B^2$.
Show that $f\simeq g \implies P\simeq Q$.
:::

::: {.solution}
<1>1. Let $H:S^1\times I\to X$ be a homotopy from $f$ to $g$.
::: {.proof}
This is the hypothesis $f\simeq g$.
:::

<1>2. Form
$$
R=X\cup_H(S^1\times I)\cup_g B^2,
$$
where $S^1\times\{0\}$ is attached to $X$ by $f$, $S^1\times\{1\}$ is attached to $X$ by $g$, and the boundary of the disk is attached along the top circle.
::: {.proof}
This is the mapping-cylinder construction for the homotopy, followed by attachment of the $2$-cell at the $g$ end.
:::

<1>3. Collapsing the cylinder $S^1\times I$ toward its bottom end gives a deformation retraction
$$
R\simeq X\cup_f B^2=P.
$$
::: {.proof}
Under the bottomward collapse, the disk together with the cylinder is again a disk whose boundary is identified with $X$ by $f$. The homotopy $H$ specifies the attaching points throughout the collapse, so it descends to the quotient.
:::

<1>4. Collapsing the same cylinder toward its top end gives a deformation retraction
$$
R\simeq X\cup_g B^2=Q.
$$
::: {.proof}
The analogous topward collapse leaves the disk attached by $g$.
:::

<1>5. Therefore
$$
\boxed{X\cup_f B^2\simeq X\cup_g B^2}.
$$
::: {.proof}
Both spaces are homotopy-equivalent to $R$ by <1>3--<1>4.
:::
:::
