---
schema: qual/card@1
id: P-CLHXQ
kind: problem
title: Simplicial homology of $S^2$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
---

::: problem
2. $S^2$ ![1513072379449](../../assets/Topology/650_UCSD_Qual_Questions/Quals/assets/1513072379449.png) So we have $C_0 = 1,2,3,4,5,6$ $C_1 = 12,14,15,16,23,25,26,34,35,36,45,46$ $C_2 = 126, 236, 346, 146, 125, 235, 345, 145$

$C_3 = \emptyset$

And $0 \xrightarrow{\del_3} C_2 \xrightarrow{\del_2} C_1 \xrightarrow{\del_1} C_0 \xrightarrow{\del_0} 0 \cong 0 \xrightarrow{\del_3} \ZZ^{8} \xrightarrow{\del_2} \ZZ^{12} \xrightarrow{\del_1} \ZZ^{6} \xrightarrow{\del_0} 0$ We have $\del_1([ij]) = j-i$ and $\del_2([ijk]) = jk -ik +ij$.

We know in advance we should have $\prod H_n = (\cdots,0, \ZZ, 0, \ZZ)$.

For $H_0 = \frac{\ker \del_0}{\im \del_1} = \frac{C_0}{\left<\theset{j-i \mid i < j}\right>}$.
In the quotient, we see $1=6=3=2=5=4$ by just taking the indicated walk on the graph, so there is one generator in the quotient and $H_0 \cong \ZZ$.

For $H_1 = \frac{\ker \del_1}{\im \del_2}$, we just note that there are 6 2-cycles, so each are in the kernel of $\del_1$, but each of them comes from a 2-cell, so is in the image of $\del_2$.
So both groups in question are $\ZZ^8$, and the quotient is zero.
For $H_3 = \frac{\ker\del_2}{\im\del_3}$, since $\im\del_3 = 0$, we can just look at $\del_3([123456]) = 23456 - 13456 + 12456 - 12356 +12346 - 12345$.
This is an element (and the only one) that goes to zero under $\del_2$, it generates $\ker\del_2$.
So there is one generator, and $H_3 =\ZZ$.
:::

::: {.solution}
<1>1. The listed triangulation has $V=6$, $E=12$, and $F=8$, and its underlying space is $S^2$.
::: {.proof}
The eight listed triangles form the indicated triangulated sphere; each edge lies in exactly two triangles.
:::

<1>2. Since the complex is connected, $H_0\cong\mathbb Z$.
::: {.proof}
Zeroth simplicial homology of a connected complex is $\mathbb Z$.
:::

<1>3. The oriented sum of all eight triangular faces, with coherent orientations, is a $2$-cycle generating $H_2\cong\mathbb Z$.
::: {.proof}
Every edge occurs twice with opposite induced orientations, so the boundary cancels. For a connected triangulated closed orientable surface this fundamental cycle generates top homology.
:::

<1>4. Euler characteristic gives
$$2=V-E+F=\operatorname{rank}H_0-\operatorname{rank}H_1+\operatorname{rank}H_2,$$
so $H_1=0$.
::: {.proof}
The chain groups are free, and $H_0,H_2$ each have rank $1$. Since the underlying sphere has no torsion in $H_1$ (equivalently, compute the boundary matrix), its rank-zero first homology vanishes.
:::

<1>5. Thus
$$\boxed{H_k(S^2;\mathbb Z)\cong\begin{cases}\mathbb Z,&k=0,2,\\0,&\text{otherwise.}\end{cases}}$$
::: {.proof}
There are no simplices above dimension $2$.
:::
:::
