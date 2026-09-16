---
schema: qual/card@1
id: D-YD6DH
kind: definition
title: Fundamental group
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space, $x_0\in X$, and $I = [0,1]$.
Let $L$ be the set of [[D-J6XOC|loops]] at $x_0$, the continuous maps $\alpha\colon I\to X$ with $\alpha(0) = \alpha(1) = x_0$.
For $\alpha,\beta\in L$ write $\alpha\homotopic\beta$ if $\alpha$ and $\beta$ are [[D-Z7I7F|homotopic rel endpoints]]: there is a continuous $H\colon I\cross I\to X$ with
$$
H(s, 0) = \alpha(s),\qquad H(s, 1) = \beta(s),\qquad H(0, t) = H(1, t) = x_0
$$
for all $s, t\in I$.
The \dfn{fundamental group} of $X$ at $x_0$ is the set $\pi_1(X, x_0)\coloneqq L/\homotopic$ with the product $[\alpha][\beta]\coloneqq[\alpha\cdot\beta]$, where
$$
(\alpha \cdot \beta )(s) \coloneqq
\begin{cases}
\alpha (2s), & s \in [0, 1/2], \\
\beta (2s-1), & s \in [1/2, 1].
\end{cases}
$$
:::

::: {.proposition}
Let $X$ be a topological space and $x_0\in X$.

(a) The relation $\homotopic$ is an equivalence relation on $L$.

(b) For $\alpha, \beta\in L$, the concatenation $\alpha\cdot\beta$ is a loop at $x_0$, and its class depends only on $[\alpha]$ and $[\beta]$.

(c) With this product, $\pi_1(X, x_0)$ is a group; its identity is the class of the constant loop $c_{x_0}(t) = x_0$, and the inverse of $[\alpha]$ is $[\bar\alpha]$, where $\bar\alpha(t)\coloneqq\alpha(1-t)$.
:::

::: {.concept}
[@Hat02, §1.1, Proposition 1.3].
:::
