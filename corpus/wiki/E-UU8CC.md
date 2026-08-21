---
schema: qual/card@1
id: E-UU8CC
kind: exercise
title: The degree of a map of the circle
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
solved: false
---

We define the degree of a continuous map $h: S^1 \to S^1$ as follows.

Let $b_0$ be the point $(1, 0)$ of $S^1$; choose a generator $\gamma$ for the infinite cyclic group $\pi_1(S^1, b_0)$. If $x_0$ is any point of $S^1$, choose a path $\alpha$ in $S^1$ from $b_0$ to $x_0$, and define $\gamma(x_0) = \hat{\alpha}(\gamma)$. Then $\gamma(x_0)$ generates $\pi_1(S^1, x_0)$. The element $\gamma(x_0)$ is independent of the choice of the path $\alpha$, since the fundamental group of $S^1$ is abelian.

Now given $h: S^1 \to S^1$, choose $x_0 \in S^1$ and let $h(x_0) = x_1$. Consider the homomorphism

$$
h_*: \pi_1(S^1, x_0) \to \pi_1(S^1, x_1).
$$

Since both groups are infinite cyclic, we have

$$
h_*(\gamma(x_0)) = d \cdot \gamma(x_1)
$$

for some integer $d$, if the group is written additively. The integer $d$ is called the degree of $h$ and is denoted by $\deg h$.

The degree of $h$ is independent of the choice of the generator $\gamma$; choosing the other generator would merely change the sign of both sides.

(a) Show that $d$ is independent of the choice of $x_0$.

(b) Show that if $h, k: S^1 \to S^1$ are homotopic, they have the same degree.

(c) Show that $\deg(h \circ k) = (\deg h) \cdot (\deg k)$.

(d) Compute the degrees of the constant map, the identity map, the reflection map $\rho(x_1, x_2) = (x_1, -x_2)$, and the map $h(z) = z^n$, where $z$ is a complex number.

(e) Show that if $h, k: S^1 \to S^1$ have the same degree, they are homotopic.

::: {.remark}
Munkres, *Topology*, §58 Exercise 9 (starred in the text).
:::
