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
Let $f,g : S^1 \rightarrow X$, $P = X \cup_f B^2 \cong X \coprod B^2 / \sim$, where $x \sim f(x)$ for $x\in S^1=\partial B^2$, $Q = X \cup_g B^2$.
Show that $f\simeq g \implies P\simeq Q$.
:::

::: {.solution}

::: pf

::: {.pf-step #z}

Let $H:S^1\times I\to X$ be a homotopy from $f$ to $g$, and let
$$
Z=X\cup_H(B^2\times I),
$$
the space obtained by attaching $B^2\times I$ to $X$ along $S^1\times I$ by $H$. Then $P$ and $Q$ are the subspaces $X\cup(B^2\times\{0\})$ and $X\cup(B^2\times\{1\})$ of $Z$.

::: pf-proof

On $S^1\times\{0\}$ the attaching map is $H_0=f$, and on $S^1\times\{1\}$ it is $H_1=g$.

:::

:::

::: {.pf-step #pair}

The pair $(B^2\times I,\ S^1\times I\cup B^2\times\{0\})$ admits a deformation retraction of $B^2\times I$ onto $S^1\times I\cup B^2\times\{0\}$.

::: pf-proof

Project $B^2\times I$ radially from the point $(0,2)\in\RR^2\times\RR$. This is Hatcher, Proposition 0.16 and the example before it: $(D^n\times I,\ \partial D^n\times I\cup D^n\times\{0\})$ is a deformation-retract pair.

:::

:::

::: {.pf-step #dr}

$Z$ deformation retracts onto $P$, and likewise onto $Q$.

::: pf-proof

The deformation retraction of Step [](#pair){.pf-ref} is stationary on $S^1\times I$, so it is compatible with the attaching map $H$ and descends to a deformation retraction of $Z$ onto $X\cup_H(S^1\times I\cup B^2\times\{0\})=X\cup_f B^2=P$; extend it by the identity on $X$. Reversing the $I$-coordinate gives the deformation retraction onto $Q$. This is Hatcher, Proposition 0.18.

:::

:::

::: pf-qed

By Step [](#dr){.pf-ref}, the inclusions $P\hookrightarrow Z$ and $Q\hookrightarrow Z$ are homotopy equivalences, so
$$
\boxed{P=X\cup_f B^2\simeq X\cup_g B^2=Q.}
$$

:::

:::

:::
