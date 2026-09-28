---
schema: qual/card@1
id: P-TOPS11B
kind: problem
title: "Fundamental group of a cylinder with antipodal points identified on each boundary circle"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
Consider the space $X$ obtained from the cylinder $S^1 \times I$ by identifying antipodal points of the circle $S^1 \times \{0\}$, and similarly identifying antipodal points of $S^1 \times \{1\}$.
Calculate the fundamental group of $X$.
:::

::: {.solution}
<1>1. After the antipodal identification, each boundary circle becomes another circle, and the quotient map from the original boundary circle has degree $2$.
::: {.proof}
The quotient $S^1/(z\sim-z)$ is $S^1$, with quotient map represented by $z\mapsto z^2$.
:::

<1>2. Thus $X$ is the double mapping cylinder of two degree-$2$ maps
$$
S^1\xrightarrow{2}S^1,
\qquad
S^1\xrightarrow{2}S^1.
$$
::: {.proof}
The original cylinder supplies the common $S^1\times I$, and at each end its boundary circle is mapped to the corresponding quotient circle by the degree-$2$ map.
:::

<1>3. Van Kampen gives
$$
\pi_1(X)\cong \mathbb Z*_{2\mathbb Z}\mathbb Z.
$$
::: {.proof}
The fundamental group of a double mapping cylinder is the amalgamated free product of the two endpoint groups over the fundamental group of the common cylinder circle. Each inclusion sends the generator to twice the endpoint generator.
:::

<1>4. Therefore
$$
\boxed{\pi_1(X)\cong\langle a,b\mid a^2=b^2\rangle.}
$$
::: {.proof}
The amalgamation identifies the image $2a$ with $2b$, which in multiplicative notation is the relation $a^2=b^2$.
:::
:::
