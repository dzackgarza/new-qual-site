---
schema: qual/card@1
id: P-TOPF07B
kind: problem
title: "Covering spaces between surfaces of small genus"
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Surfaces
relations: []
review: draft
---

::: {.problem}
Let $\Sigma_g$ be the closed orientable surface of genus $g$, that is the "$g$-holed torus".
Describe all the possible covering spaces of the form $\Sigma_g \to \Sigma_h$, where $1 \leq g, h \leq 4$, and explain why these are the only possibilities.
:::

::: {.solution}
<1>1. If $p:\Sigma_g\to\Sigma_h$ is a connected $d$-sheeted cover, then
$$
2-2g=d(2-2h),
$$
or equivalently
$$
g-1=d(h-1).
$$
::: {.proof}
Euler characteristic multiplies by the number of sheets of a finite covering, and $\chi(\Sigma_r)=2-2r$.
:::

<1>2. If $h=1$, the equation forces $g=1$, and $T^2$ has connected covers of every positive finite degree.
::: {.proof}
For $h=1$, the right side of $g-1=d(h-1)$ is zero. Conversely, every finite-index subgroup of $\mathbb Z^2$ gives a connected finite cover of the torus, and subgroups of every positive index exist.
:::

<1>3. For $2\le h\le4$ and $1\le g\le4$, the possibilities are
$$
(g,h,d)=(2,2,1),(3,2,2),(4,2,3),(3,3,1),(4,4,1).
$$
::: {.proof}
Solve $g-1=d(h-1)$ with $d\in\mathbb Z_{>0}$ and $g,h\le4$. For $h=2$, $g=1+d$ gives $d=1,2,3$; for $h=3$, $g=1+2d$ gives only $d=1$; for $h=4$, $g=1+3d$ gives only $d=1$.
:::

<1>4. Every listed numerical possibility occurs.
::: {.proof}
The degree-one cases are identities. For $\Sigma_3\to\Sigma_2$ and $\Sigma_4\to\Sigma_2$, choose respectively index-$2$ and index-$3$ subgroups of the surface group (for example kernels of surjections to $\mathbb Z/2$ and $\mathbb Z/3$); the corresponding connected covers have genera $3$ and $4$ by <1>1.
:::
:::
