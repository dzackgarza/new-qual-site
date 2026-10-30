---
schema: qual/card@1
id: P-TOPF09B
kind: problem
title: "Fundamental group and homology of a space from gluing a hexagon and triangle"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homology
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
A solid hexagon and a solid triangle are glued together along their edges, according to the following scheme.
Calculate the fundamental group and the homology of the resulting space $X$.

In the scheme, the hexagon's edges read $a,b,c,a,b,c$ clockwise, each arrow pointing clockwise, and the triangle's edges read $a,b,c$ counterclockwise, each arrow pointing counterclockwise.
:::

::: {.remark}
The diagram is not in the machine extraction. The edge labels and arrows above were read from the page image of the source PDF.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The $1$-skeleton of $X$ has three vertices and three edges, and it is a circle traversed once by the loop $abc$.

::: pf-proof

In both polygons the head of $a$ is the tail of $b$, the head of $b$ is the tail of $c$, and the head of $c$ is the tail of $a$. These are the only vertex identifications, so the vertices fall into three classes $u=\text{tail}(a)$, $v=\text{tail}(b)$, $w=\text{tail}(c)$. The edges $a:u\to v$, $b:v\to w$, $c:w\to u$ form a triangle graph, which is a circle; the loop $abc$ goes once around it.

:::

:::

::: {.pf-step #s2}

The triangle attaches along a degree-$\pm1$ map to this circle, and the hexagon along a degree-$\pm2$ map.

::: pf-proof

The triangle boundary traverses $abc$ once and the hexagon boundary traverses $abc$ twice, by step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

$X\simeq S^2$.

::: pf-proof

The circle with the triangle attached by a degree-$\pm1$ map is a closed disk $D$, which is contractible. The hexagon is then attached along a map $S^1\to D$, and every such map is homotopic to a constant map. Attaching a $2$-cell along homotopic maps gives homotopy-equivalent spaces, and attaching a $2$-cell to a contractible space along a constant map gives $D\vee S^2\simeq S^2$.

:::

:::

::: {.pf-step #s4}

The cellular chain complex confirms the homology: $C_2=\ZZ^2\to C_1=\ZZ^3\to C_0=\ZZ^3$ with
$$
\partial_2(\text{hexagon})=2(a+b+c),\qquad \partial_2(\text{triangle})=\pm(a+b+c),
$$
so $\ker\partial_1=\ZZ(a+b+c)=\operatorname{im}\partial_2$ and $\ker\partial_2\cong\ZZ$.

::: pf-proof

The $1$-skeleton is a connected graph with three vertices and three edges, so $\ker\partial_1$ has rank $3-3+1=1$ and is spanned by the cycle $a+b+c$. The two columns of $\partial_2$ are $2$ and $\pm1$ times this cycle, so the image is the whole cycle group and the kernel has rank $1$.

:::

:::

::: pf-qed

By steps [](#s3){.pf-ref} and [](#s4){.pf-ref},
$$
\boxed{\pi_1(X)=1,\qquad H_k(X;\ZZ)\cong\begin{cases}\ZZ,&k=0,2,\\0,&\text{otherwise}.\end{cases}}
$$

:::

:::

:::
