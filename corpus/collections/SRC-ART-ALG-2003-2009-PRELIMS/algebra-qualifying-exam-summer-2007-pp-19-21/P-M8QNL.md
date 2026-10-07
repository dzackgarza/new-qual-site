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
<1>1. Suppose $G/Z(G)=\langle gZ(G)\rangle$ is cyclic.
::: {.proof}
Choose $g\in G$ whose coset generates the cyclic quotient $G/Z(G)$.
:::

<1>2. Any $x\in G$ can be written $x=g^i z$ for some $i\in\ZZ$, $z\in Z(G)$.
::: {.proof}
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

<1>3. Any two elements of $G$ commute.
::: {.proof}
Let
$$
x=g^iz_1,
\qquad
y=g^jz_2
$$
as in step <1>2, with $z_1,z_2\in Z(G)$. Then
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

<1>4. Therefore
$$
\boxed{G\text{ is abelian}}.
$$
::: {.proof}
Step <1>3 shows that every pair of elements of $G$ commutes.
:::

<1>5. Q.E.D.
::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
