---
schema: qual/card@1
id: P-AMD-6TSC527D
kind: problem
title: Cellular homology of a tetrahedron with pairwise face identifications
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Cell Complexes
  - Homology
relations: []
review: draft
---

::: {.problem}
Use cellular chain complexes to compute the homology of the space obtained by gluing the faces of a solid tetrahedron as shown, with $ABC$ glued to $ABD$ and $ACD$ glued to $BCD$.

![Tetrahedron with pairwise face identifications](../../../assets/Topology/650_UCSD_Qual_Questions/Quals/assets/2018-02-11%2016_28_51-290.pdf.png)
:::

::: {.solution}
<1>1. The source gluing is the same tetrahedron quotient as the Summer 2007 UCSD problem: $ABC$ is glued to $ABD$ by $A\mapsto A$, $B\mapsto B$, $C\mapsto D$, and $BCD$ is glued to $ACD$ preserving the listed vertex order.
::: {.proof}
These are exactly the affine face maps encoded by the repeated source glyphs; the same quotient is stated explicitly in the retained Summer 2007 source.
:::

<1>2. There are two vertex classes, $A\sim B$ and $C\sim D$. The six edges form three classes: a loop $a=[AB]$ at the first vertex, a loop $c=[CD]$ at the second, and one edge $e=[AC]=[AD]=[BC]=[BD]$ joining them.
::: {.proof}
The first face map identifies $AC\sim AD$ and $BC\sim BD$. The second identifies $BC\sim AC$ and $BD\sim AD$, while also identifying $B\sim A$ and preserving $C\sim C$, $D\sim D$. Thus all four cross-edges form one class.
:::

<1>3. The two face-pairs give two $2$-cells $f_1,f_2$, with cellular boundaries
$$\partial_2(f_1)=a,\qquad \partial_2(f_2)=c$$
(up to signs and the choice of orientations).
::: {.proof}
Traversing $ABC$ gives $AB\cdot BC\cdot CA=aee^{-1}=a$. Traversing $BCD$ gives $BC\cdot CD\cdot DB=ece^{-1}$, whose cellular boundary is $c$ because the two occurrences of $e$ cancel.
:::

<1>4. With bases $(a,c,e)$ for $C_1$ and the two vertex classes for $C_0$, one has
$$\operatorname{rank}\partial_1=1,\qquad \ker\partial_1=\langle a,c\rangle=\operatorname{im}\partial_2.$$
::: {.proof}
The loops $a,c$ have zero boundary, while $e$ joins the two distinct vertex classes. By <1>3, the image of $\partial_2$ is exactly the span of $a,c$.
:::

<1>5. The map $\partial_2:C_2\cong\mathbb Z^2\to C_1$ is injective, and therefore the top boundary $\partial_3:C_3\cong\mathbb Z\to C_2$ is zero.
::: {.proof}
The two images $a,c$ are independent, so $\partial_2$ is injective. Since $\partial_2\partial_3=0$, injectivity forces $\partial_3=0$.
:::

<1>6. Hence
$$\boxed{H_i(X;\mathbb Z)\cong\begin{cases}
\mathbb Z,&i=0,3,\\
0,&i=1,2\text{ or }i>3.
\end{cases}}$$
::: {.proof}
The quotient is connected, so $H_0\cong\mathbb Z$. The equality in <1>4 gives $H_1=0$; injectivity in <1>5 gives $H_2=0$; and $\partial_3=0$ gives $H_3\cong\mathbb Z$.
:::
:::
