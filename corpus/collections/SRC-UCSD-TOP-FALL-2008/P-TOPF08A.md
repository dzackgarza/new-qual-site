---
schema: qual/card@1
id: P-TOPF08A
kind: problem
title: A $2$-dimensional CW complex with $\pi_1=\langle a,b\mid a^2=b^3\rangle$
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
Construct a connected two dimensional CW complex $X$ with fundamental group with the presentation:
$$
\pi_1(X) = \langle a, b \mid a^2 = b^3 \rangle.
$$
:::

::: {.solution}
<1>1. Start with a wedge of two circles
$$
X^{(1)}=S^1_a\vee S^1_b.
$$
::: {.proof}
Its fundamental group is the free group $F(a,b)$.
:::

<1>2. Attach one $2$-cell by an attaching map whose boundary loop represents the word
$$
a^2b^{-3}.
$$
Let
$$
X=(S^1_a\vee S^1_b)\cup_{a^2b^{-3}}D^2.
$$
::: {.proof}
Every word in the free group is represented by a loop in the wedge, so this attachment is well-defined and produces a connected $2$-dimensional CW complex.
:::

<1>3. Van Kampen's theorem gives
$$
\boxed{\pi_1(X)\cong\langle a,b\mid a^2b^{-3}=1\rangle
=\langle a,b\mid a^2=b^3\rangle.}
$$
::: {.proof}
Attaching a $2$-cell kills the normal closure of its attaching word and imposes no other relations.
:::
:::
