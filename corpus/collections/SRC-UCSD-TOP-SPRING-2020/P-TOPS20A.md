---
schema: qual/card@1
id: P-TOPS20A
kind: problem
title: Index-$2$ subgroups of $\mathbb Z*(\mathbb Z\oplus\mathbb Z)$ via covering spaces
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Free Products
  - Fundamental Group
relations: []
review: draft
---

::: problem
Consider the group $G = \mathbb{Z} * (\mathbb{Z} \oplus \mathbb{Z})$ (here $*$ means the free product).
Realize $G$ as the fundamental group of some topological space.
Then classify (up to isomorphism) all subgroups of $G$ of index two.
:::

::: {.solution}
<1>1. Realize
$$G=\mathbb Z*(\mathbb Z\oplus\mathbb Z)$$
as
$$\boxed{G\cong\pi_1(S^1\vee T^2).}$$
::: {.proof}
Van Kampen gives the free product of the fundamental groups of the wedge summands: $\pi_1(S^1)=\mathbb Z$ and $\pi_1(T^2)=\mathbb Z^2$.
:::

<1>2. Every index-$2$ subgroup $K$ is normal and is the kernel of a nonzero homomorphism
$$\phi:G\to\mathbb Z/2.$$
There are $2^3-1=7$ such kernels.
::: {.proof}
An index-$2$ subgroup is normal, and the quotient is $\mathbb Z/2$. Since $G_{\mathrm{ab}}\cong\mathbb Z^3$, homomorphisms to $\mathbb Z/2$ are specified by three bits, not all zero.
:::

<1>3. Write $G=A*B$ with $A\cong\mathbb Z$ and $B\cong\mathbb Z^2$. If $\phi|_A\ne0$ and $\phi|_B=0$, then
$$\boxed{K\cong\mathbb Z*\mathbb Z^2*\mathbb Z^2.}$$
::: {.proof}
Use the Bass--Serre tree of $A*B$. In the quotient by $K$, there is one $A$-vertex (because $\phi(A)=\mathbb Z/2$), two $B$-vertices (because $\phi(B)=0$), and two edges. The underlying quotient graph is a tree, so there is no additional free factor. The $A$-vertex group is $K\cap A=2\mathbb Z\cong\mathbb Z$, while each $B$-vertex group is a copy of $B\cong\mathbb Z^2$.
:::

<1>4. If $\phi|_B\ne0$ (whether or not $\phi|_A$ is zero), then
$$\boxed{K\cong F_2*\mathbb Z^2.}$$
::: {.proof}
If $\phi|_A=0$, the quotient graph has two $A$-vertices, one $B$-vertex, and two edges, hence is a tree. Its vertex groups are two copies of $\mathbb Z$ and $\ker(\phi|_B)\cong\mathbb Z^2$, giving $\mathbb Z*\mathbb Z*\mathbb Z^2\cong F_2*\mathbb Z^2$. If both restrictions are nonzero, the quotient graph has one vertex of each type and two edges, so its graph rank is $1$; the vertex groups are $\mathbb Z$ and $\mathbb Z^2$, giving $\mathbb Z*\mathbb Z^2*\mathbb Z\cong F_2*\mathbb Z^2$.
:::

<1>5. Thus, up to abstract group isomorphism, the index-$2$ subgroups have exactly two types:
$$\boxed{\mathbb Z*\mathbb Z^2*\mathbb Z^2\quad\text{and}\quad F_2*\mathbb Z^2.}$$
::: {.proof}
The first occurs for the unique nonzero $\phi$ that is nontrivial only on the $\mathbb Z$ factor. The other six nonzero homomorphisms have nontrivial restriction to $B$ or fall into the second case. The two types are nonisomorphic, for example because their abelianizations have ranks $5$ and $4$ respectively.
:::
:::
