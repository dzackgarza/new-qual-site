---
schema: qual/card@1
id: P-APAS23E
kind: problem
title: Isomorphism $D_6 \cong S_3 \times C_2$ and the character table of $D_6$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
  - Group Theory
relations: []
review: draft
---

::: {.problem}
Let $D_6$ be the group of symmetries of a regular hexagon, let $S_3$ be the symmetric group on three objects, and let $C_2$ be the cyclic group of order $2$.

(1) Prove that $D_6$ is isomorphic to the direct product $S_3 \times C_2$.

(2) Calculate the character table of $D_6$.
:::


::: {.solution}

No retained solution set covers this exercise: the card's own decomposition and the table obtained from it are set out step by step.

Let $D_{6}=\langle r,s\mid r^{6}=s^{2}=1,\ srs=r^{-1}\rangle$, $z=r^{3}$ and $H=\langle r^{2},s\rangle$.

::: pf

::: {.pf-step #factors}
$z$ is central of order $2$, $H\cong D_{3}\cong S_{3}$, and $H\cap\langle z\rangle=\{1\}$.

::: pf-proof
$z=r^{3}\ne1$ and $z^{2}=r^{6}=1$, so $z$ has order $2$; it is central because $rz=r^{4}=zr$ and $sz=r^{3}s=r^{-3}s=zs$ using $sr^{k}s=r^{-k}$. In $H$ the element $r^{2}$ has order $3$ and $sr^{2}s=r^{-2}=(r^{2})^{-1}$, so $H$ is a dihedral group of order $6$, isomorphic to $D_{3}$ and hence to $S_{3}$ (the symmetries of a triangle). Finally $H=\{1,r^{2},r^{4},s,r^{2}s,r^{4}s\}$ contains no $r^{3}$, since its elements are of the form $r^{2k}$ or $r^{2k}s$.
:::

:::

::: {.pf-step #product}
$D_{6}=H\times\langle z\rangle\cong S_{3}\times C_{2}$.

::: pf-proof
$H$ and $\langle z\rangle$ are subgroups with $H\cap\langle z\rangle=\{1\}$ and both normal ($H$ has index $2$, and $\langle z\rangle$ is central), so $H\langle z\rangle$ is a subgroup isomorphic to the direct product $H\times\langle z\rangle$. Its order is $6\cdot2=12=\cardinality{D_{6}}$, so it is all of $D_{6}$.
:::

:::

::: {.pf-step #classes}
The conjugacy classes of $D_{6}$ are $\{1\}$, $\{r^{3}\}$, $\{r,r^{5}\}$, $\{r^{2},r^{4}\}$, $\{s,r^{2}s,r^{4}s\}$, $\{rs,r^{3}s,r^{5}s\}$, and they correspond under $D_{6}\cong S_{3}\times C_{2}$ to $(\text{class of }r^{2k}\text{ or }r^{2k}s,\ z^{k})$.

::: pf-proof
$sr^{k}s=r^{-k}$, so conjugating $r^{k}$ by $s$ gives $r^{-k}$, while conjugating by $r^{j}$ fixes $r^{k}$; hence the classes of the rotations are $\{r^{k},r^{-k}\}$, which for $k=1,2$ have two elements and for $k=0,3$ one. The reflections $r^{k}s$ are conjugate to $r^{-k}s$ and to $r^{k+2j}s$, so they fall into the two classes with $k$ even and $k$ odd, of three elements each.
:::

:::

::: {.pf-step #table}
The character table of $D_{6}$, on the classes $1,r^{3},r^{2},r,s,rs$:
$$\begin{array}{c|cccccc} & 1 & r^{3} & r^{2} & r & s & rs\\\hline \chi_{1} & 1&1&1&1&1&1\\ \chi_{2} & 1&-1&1&-1&1&-1\\ \chi_{3} & 1&1&1&1&-1&-1\\ \chi_{4} & 1&-1&1&-1&-1&1\\ \chi_{5} & 2&2&-1&-1&0&0\\ \chi_{6} & 2&-2&-1&1&0&0 \end{array}$$

::: pf-proof
The irreducible characters of $D_{6}\cong S_{3}\times C_{2}$ are exactly the products $\chi_{\alpha}\otimes\varepsilon$ of an irreducible of $S_{3}$ (trivial, sign, standard of dimension $2$) with a character of $C_{2}$ (trivial or sign), by step [](#product){.pf-ref}. Evaluating on the classes of step [](#classes){.pf-ref}: on $r^{2k}$ the $S_{3}$-part is $r^{2k}$ and the $C_{2}$-part is $+$; on $r^{2k}s$ the $S_{3}$-part is $r^{2k}s$ and the $C_{2}$-part is $-$. The $S_{3}$ table is trivial $(1,1,1)$, sign $(1,-1,1)$, standard $(2,0,-1)$ on $1,(12),(123)$, giving the six rows displayed. The sum of squares of the dimensions is $4\cdot1+2\cdot4=12=\cardinality{D_{6}}$, confirming that the six irreducibles are all of them.
:::

:::

::: {.pf-qed}
(1) is step [](#product){.pf-ref} and (2) is step [](#table){.pf-ref}.
:::

:::

:::
