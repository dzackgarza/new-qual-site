---
schema: qual/card@1
id: P-AGXHWSUPPORT
kind: problem
title: The support of a section is closed, while the support of a sheaf need not be
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Support
  - Skyscraper Sheaves
relations: []
review: draft
---

::: {.problem}
Let $\mcf\in \Sh(X)$ and $s\in \mcf(U)$ be a section, and define
$$
\begin{aligned}
\supp s &\coloneqq \theset{p\in U \st s_p \neq 0} \subseteq U \\
\supp \mcf &\coloneqq \theset{p\in X \st \mcf_p\neq 0} \subseteq  X
\end{aligned}
,$$
where $s_p$ denotes the germ of $s$ in the stalk $\mcf_p$.
Show that $\supp s$ is closed in $U$ but $\supp \mcf$ need not be closed in $X$.
:::

::: {.solution}
::: pf

::: pf-step
$\supp s$ is closed in $U$.

::: pf-proof
Let $p \in U \sm \supp s$, so $s_p = 0$.
By the definition of the stalk, there is an open neighborhood $W \subseteq U$ of $p$ with $s\restrict_W = 0$.
Then $s_{p'} = 0$ for every $p' \in W$, so $W \subseteq U \sm \supp s$.
Hence $U \sm \supp s$ is open in $U$.
:::

:::

::: pf-step
$\supp \mcf$ need not be closed in $X$.

::: pf-proof

::: {.pf-step #sheaf-f}
Fix $q \in X$ and an abelian group $A \neq 0$, and let $\mcf$ be the sheafification of the presheaf
$$
P(U) \coloneqq
\begin{cases}
A & q \notin U \\
0 & q \in U,
\end{cases}
$$
with identity restriction maps between opens that omit $q$ and zero maps otherwise.
Then $\supp \mcf = X \sm \cl_X(\theset{q})$.

::: pf-proof
Sheafification preserves stalks, so $\mcf_p = P_p = \colim_{U \ni p} P(U)$.
If $p \notin \cl_X(\theset{q})$, some open $U \ni p$ omits $q$.
Every open $V \subseteq U$ also omits $q$, so $P(V) = A$ with identity transition maps, and $\mcf_p = A \neq 0$.
If $p \in \cl_X(\theset{q})$, every open $U \ni p$ contains $q$, so $P(U) = 0$ and $\mcf_p = 0$.
:::

:::

::: pf-step
For $X = \AA^1_k$ with $k$ infinite and $q = 0$, the set $\supp \mcf$ is not closed.

::: pf-proof
The point $0 = V(x)$ is closed, so step [](#sheaf-f){.pf-ref} gives $\supp \mcf = \AA^1 \sm \theset{0} = D(x)$.
The proper closed subsets of $\AA^1_k$ are finite sets of points, together with the empty set.
The set $D(x)$ is a proper subset that contains the infinitely many closed points $x - a$ with $a \in \units{k}$, so it is not closed.
:::

:::

:::

:::

:::
:::
