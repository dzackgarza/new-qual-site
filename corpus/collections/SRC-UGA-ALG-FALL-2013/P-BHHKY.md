---
schema: qual/card@1
id: P-BHHKY
kind: problem
title: Classification of groups of order $30$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
---

::: {.problem}
Let $G$ be a group of order 30.

a. Show that $G$ has a subgroup of order 15.

b. Show that every group of order 15 is cyclic.

c. Show that $G$ is isomorphic to some semidirect product $\ZZ_{15} \semidirect \ZZ_2$.

d. Exhibit three nonisomorphic groups of order 30 and prove that they are not isomorphic.
You are not required to use your answer to (c).
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every group of order $30$ has a subgroup $H$ of order $15$.


::: pf-proof

By Sylow's theorems, $n_3\in\{1,10\}$ and $n_5\in\{1,6\}$. If both were greater than one, distinct Sylow $3$-subgroups would contribute $20$ nonidentity elements and distinct Sylow $5$-subgroups would contribute another $24$, impossible in a group of order $30$. Thus one of the two Sylow subgroups is normal. Its product with a Sylow subgroup for the other prime is a subgroup of order $3\cdot5=15$, since their intersection is trivial.

:::

:::

::: {.pf-step #s1-2}

Every group of order $15$ is cyclic.


::: pf-proof

For $\cardinality{H}=15$, Sylow's theorems give $n_5\mid3$, $n_5\equiv1\pmod5$, $n_3\mid5$, and $n_3\equiv1\pmod3$. Thus both counts equal one. Their normal Sylow subgroups of orders $5$ and $3$ have trivial intersection and generate $H$, so $H\cong C_5\times C_3\cong C_{15}$.

:::

:::

::: {.pf-step #s1-3}

Every group of order $30$ is isomorphic to $C_{15}\rtimes C_2$ for some action of $C_2$ on $C_{15}$.


::: pf-proof

The subgroup $H$ in step [](#s1-1){.pf-ref} has index two and is therefore normal, and by step [](#s1-2){.pf-ref} it is cyclic of order $15$. Cauchy's theorem provides an element $s$ of order two. Since $H$ has odd order, $H\cap\langle s\rangle=1$, and $H\langle s\rangle$ has order $30$. The multiplication map identifies $G$ with the semidirect product for the conjugation action of $\langle s\rangle$ on $H$.

:::

:::

::: {.pf-step #s1-4}

Three pairwise nonisomorphic groups of order $30$ are
$$
\boxed{C_{30},\quad C_3\times D_{10},\quad D_{30}},
$$
where $D_{2n}$ denotes the dihedral group of order $2n$.


::: pf-proof

All three groups have order $30$. Their respective numbers of elements of order two are $1$, $5$, and $15$: a cyclic group of order $30$ has one involution; when $5$ is odd the dihedral group $D_{10}$ has five involutions, its reflections, and the $C_3$ factor adds none; similarly $D_{30}$ has fifteen reflections and no rotational involutions. Different involution counts are preserved under isomorphism, so the examples are pairwise nonisomorphic.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} establish parts (a)--(d), respectively.

:::

:::

:::
