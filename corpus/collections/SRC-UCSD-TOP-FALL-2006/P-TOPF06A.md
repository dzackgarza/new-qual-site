---
schema: qual/card@1
id: P-TOPF06A
kind: problem
title: A $2$-dimensional CW complex with $\pi_1=\langle a,b,c\mid abca=cb\rangle$
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
Construct a $2$-dimensional connected CW complex $X$ with one $0$-cell and one $2$-cell, whose fundamental group has the presentation:
$$
\pi_1(X) = \langle a, b, c \mid abca = cb \rangle.
$$
You may express $X$ as the identification space of a polygon.
:::

::: {.solution}
<1>1. Take a wedge of three circles
$$
X^{(1)}=S^1_a\vee S^1_b\vee S^1_c.
$$
::: {.proof}
This is a connected CW complex with one $0$-cell and three $1$-cells, and its fundamental group is the free group $F(a,b,c)$.
:::

<1>2. Attach one $2$-cell along a loop representing
$$
r=abcac^{-1}b^{-1}.
$$
::: {.proof}
The desired relation $abca=cb$ is equivalent to $abcac^{-1}b^{-1}=1$. Every word in $F(a,b,c)$ is represented by a based loop in the wedge.
:::

<1>3. Then
$$
X=(S^1_a\vee S^1_b\vee S^1_c)\cup_r D^2
$$
is a connected $2$-dimensional CW complex with one $0$-cell and one $2$-cell, and
$$
\boxed{\pi_1(X)\cong\langle a,b,c\mid abca=cb\rangle}.
$$
::: {.proof}
By van Kampen, attaching the $2$-cell quotients $F(a,b,c)$ by the normal closure of $r$, which imposes exactly the displayed relation.
:::
:::
