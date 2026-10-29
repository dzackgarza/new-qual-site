---
schema: qual/card@1
id: P-TOPS13D
kind: problem
title: 'Klein bottle sandwich: homology, and homotopy equivalence to $S^2$'
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
  - Homotopy Type
  - Surfaces
relations: []
review: draft
---

::: {.problem}
(a) Consider the CW complex constructed as follows.
First construct a Klein bottle $K$ out of two $2$-cells.
Attach to $K$ two additional $2$-cells.
The two attaching maps $\partial D^2 \to K$ are taken to be homeomorphisms between $\partial D^2$ and the circles $a$ and $b$ respectively.
Call the resulting CW complex $S$.
Calculate $H_*(S, \ZZ)$ using cellular homology.

(b) Show $S$ is homotopy equivalent to $S^2$.
:::

::: {.solution}

::: pf

::: pf-step
Use the standard CW structure on the Klein bottle with one $0$-cell, two $1$-cells $a,b$, and one $2$-cell attached by the word
$$
aba^{-1}b.
$$
After attaching the two extra disks along $a$ and $b$, the cellular chain groups are
$$
C_2\cong\ZZ^3,\qquad C_1\cong\ZZ^2,\qquad C_0\cong\ZZ.
$$

::: pf-proof
The original Klein-bottle $2$-cell and the two newly attached disks give the three generators of $C_2$.
:::

:::

::: pf-step
With respect to the bases $(\text{Klein cell},D_a,D_b)$ and $(a,b)$,
$$
\partial_2=
\begin{pmatrix}
0&1&0\\
2&0&1
\end{pmatrix},
\qquad \partial_1=0.
$$

::: pf-proof
The Klein-bottle attaching word has exponent sums $(0,2)$ in $(a,b)$. The two additional disks have attaching words $a$ and $b$, giving columns $(1,0)$ and $(0,1)$.
:::

:::

::: {.pf-step #homology-of-S}
The matrix $\partial_2$ is surjective and has kernel of rank one. Therefore
$$
\boxed{H_i(S;\ZZ)\cong
\begin{cases}\ZZ,&i=0,2,\\0,&\text{otherwise}.\end{cases}}
$$

::: pf-proof
The last two columns already form the identity matrix on $C_1$, so the cokernel is zero and the kernel of a surjection $\ZZ^3\to\ZZ^2$ is free of rank one.
:::

:::

::: pf-step
The two added disks kill the generators $a$ and $b$ of $\pi_1(K)$, so $S$ is simply connected.

::: pf-proof
Van Kampen adds the relations $a=1$ and $b=1$ to the Klein-bottle presentation.
:::

:::

::: pf-step
Choose a map $S^2\to S$ representing a generator of $H_2(S)$. It is a homology isomorphism.

::: pf-proof
Both spaces are simply connected and have homology $\ZZ$ in degrees $0,2$ and zero otherwise by step [](#homology-of-S){.pf-ref}.
:::

:::

::: pf-step
By the homological Whitehead theorem for simply connected CW complexes,
$$
\boxed{S\simeq S^2.}
$$

::: pf-proof
A homology equivalence between simply connected CW complexes is a homotopy equivalence.
:::

:::

:::

:::
