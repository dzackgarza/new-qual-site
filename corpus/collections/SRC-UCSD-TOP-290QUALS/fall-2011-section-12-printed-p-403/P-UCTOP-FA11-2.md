---
schema: qual/card@1
id: P-UCTOP-FA11-2
kind: problem
title: Fundamental group of cylinder with antipodal identification
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
---

Consider the space $X$ obtained from the cylinder $S^1 \times I$ by identifying antipodal points of the circle $S^1 \times \{0\}$, and similarly identifying antipodal points of $S^1 \times \{1\}$.
Calculate the fundamental group of $X$.

::: {.solution}
<1>1. Split the cylinder at its middle circle $C=S^1\times\{1/2\}$. Each half of the quotient is the mapping cylinder of the degree-$2$ map $S^1\to S^1$, $z\mapsto z^2$.
::: {.proof}
At either boundary, identifying antipodal points makes the quotient boundary circle $S^1/(z\sim-z)\cong S^1$, and the quotient map from a nearby copy of $S^1$ to that boundary has degree $2$. Thus each half-cylinder with its boundary identification is a mapping cylinder of that degree-$2$ map.
:::

<1>2. Hence $X$ is homotopy equivalent to the double mapping cylinder
$$
S^1\xleftarrow{\,2\,}S^1\xrightarrow{\,2\,}S^1.
$$
::: {.proof}
Each mapping cylinder deformation-retracts onto its target circle while retaining the common domain circle as the gluing locus. The union is the homotopy pushout of the two degree-$2$ maps.
:::

<1>3. Van Kampen gives
$$
\pi_1(X)\cong \mathbb Z*_{2\mathbb Z}\mathbb Z
\cong\langle a,b\mid a^2=b^2\rangle.
$$
::: {.proof}
Let $a$ and $b$ generate the two target circles and let $c$ generate the middle circle. The two attaching maps send $c$ to $a^2$ and $b^2$. Thus
$$
\pi_1(X)\cong\langle a,b,c\mid c=a^2,\ c=b^2\rangle,
$$
and eliminating $c$ yields the displayed presentation.
:::
:::
