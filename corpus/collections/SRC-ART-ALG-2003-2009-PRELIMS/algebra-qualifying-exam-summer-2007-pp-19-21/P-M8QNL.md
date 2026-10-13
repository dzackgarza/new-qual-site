---
schema: qual/card@1
id: P-M8QNL
kind: problem
title: If $G/Z(G)$ is cyclic then $G$ is abelian
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---
::: {.problem}
Let $G$ be a group with center $Z(G)$.
Show that if $G/Z(G)$ is cyclic, then $G$ is abelian.
:::

::: {.solution}

::: pf

::: pf-step

Suppose $G/Z(G)=\langle gZ(G)\rangle$ is cyclic.

::: pf-proof

Choose $g\in G$ whose coset generates the cyclic quotient $G/Z(G)$.

:::

:::

::: {.pf-step #s2}

Any $x\in G$ can be written $x=g^i z$ for some $i\in\ZZ$, $z\in Z(G)$.

::: pf-proof

Because $gZ(G)$ generates $G/Z(G)$, there is an integer $i$ such that
$$
xZ(G)=g^iZ(G).
$$
Hence
$$
g^{-i}x\in Z(G).
$$
Writing $z=g^{-i}x$ gives
$$
x=g^iz
$$
with $z\in Z(G)$.

:::

:::

::: {.pf-step #s3}

Any two elements of $G$ commute.

::: pf-proof

Let
$$
x=g^iz_1,
\qquad
y=g^jz_2
$$
as in step [](#s2){.pf-ref}, with $z_1,z_2\in Z(G)$. Then
$$
\begin{aligned}
xy
&=g^iz_1g^jz_2\\
&=g^{i+j}z_1z_2\\
&=g^{j+i}z_2z_1\\
&=g^jz_2g^iz_1\\
&=yx.
\end{aligned}
$$
The middle equalities use that powers of $g$ commute and that $z_1,z_2$ are central.

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{G\text{ is abelian}}.
$$

::: pf-proof

Step [](#s3){.pf-ref} shows that every pair of elements of $G$ commutes.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
