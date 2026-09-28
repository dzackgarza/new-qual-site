---
schema: qual/card@1
id: P-TOPS02I
kind: problem
title: "Fundamental group of the figure-eight is not abelian"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
---

::: {.problem}
Let $S^1 \vee S^1$ be the one point union of circles.
Prove $\pi_1(S^1 \vee S^1, x_0)$ is not abelian.
:::

::: {.solution}
<1>1. The standard CW structure on $S^1\vee S^1$ has one $0$-cell and two $1$-cells, so
$$
\pi_1(S^1\vee S^1,x_0)\cong F(a,b),
$$
the free group on two generators.
::: {.proof}
This is the cellular form of van Kampen's theorem for a wedge of two circles.
:::

<1>2. The elements $ab$ and $ba$ are distinct in $F(a,b)$.
::: {.proof}
Both words are already reduced, and reduced words in a free group represent the same element only when they are identical letter-for-letter.
:::

<1>3. Hence $ab\ne ba$, so $\pi_1(S^1\vee S^1,x_0)$ is not abelian.
::: {.proof}
An abelian group would satisfy $ab=ba$ for all elements.
:::
:::
