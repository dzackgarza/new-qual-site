---
schema: qual/card@1
id: P-TOPS18A
kind: problem
title: "Kernel of a surjection from Z/2 * Z/3 to S_3 is a free group of rank 2"
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Free Groups
  - Free Products
relations: []
review: draft
---

::: {.problem}
Let $S_3$ be the symmetric group on $3$ letters.
If we pick elements $\tau, \sigma \in S_3$ of orders $2$ and $3$ respectively, we get a surjective homomorphism $\theta : \mathbb{Z}_2 * \mathbb{Z}_3 \to S_3$.
By constructing a suitable covering space of a $2$-complex, show that the kernel of $\theta$ is a free group of rank $2$.
:::

::: {.solution}
<1>1. Let $G=\mathbb Z/2*\mathbb Z/3=\langle a,b\mid a^2=b^3=1\rangle$ and $K=\ker\theta$. Since $\theta$ is onto $S_3$, $K$ has index $6$.
::: {.proof}
The quotient $G/K$ is $S_3$, which has six elements.
:::

<1>2. Use the Bass--Serre tree $T$ for the free product $G=(\mathbb Z/2)*(\mathbb Z/3)$. Its vertices are the cosets of the two factors and its edges are the elements of $G$, with an edge $g$ joining $g(\mathbb Z/2)$ to $g(\mathbb Z/3)$.
::: {.proof}
This is the standard tree associated to a free product. The stabilizers of the two types of vertices are conjugates of the factors, while edge stabilizers are trivial.
:::

<1>3. The subgroup $K$ acts freely on $T$.
::: {.proof}
Any vertex stabilizer in $K$ is the intersection of $K$ with a conjugate of a finite factor. Since $K$ is the kernel of a map that is injective on each factor (their chosen generators retain orders $2$ and $3$ in $S_3$), these intersections are trivial. Edge stabilizers are already trivial.
:::

<1>4. The quotient graph $K\backslash T$ has $3$ vertices of the $\mathbb Z/2$ type, $2$ vertices of the $\mathbb Z/3$ type, and $6$ edges.
::: {.proof}
Because $K$ is normal with quotient $S_3$, the two vertex sets are the coset spaces $S_3/\langle\tau\rangle$ and $S_3/\langle\sigma\rangle$, of cardinalities $3$ and $2$. The edges correspond to elements of $S_3$, hence there are $6$.
:::

<1>5. Therefore $K\backslash T$ is a connected graph of rank
$$6-(3+2)+1=2.$$
::: {.proof}
For a connected finite graph, the rank of its free fundamental group is $E-V+1$.
:::

<1>6. Since $T$ is simply connected and $K$ acts freely, it is the universal cover of $K\backslash T$, so
$$\boxed{K\cong\pi_1(K\backslash T)\cong F_2.}$$
::: {.proof}
The deck group of the covering $T\to K\backslash T$ is exactly $K$, and <1>5 computes the fundamental group of the quotient graph.
:::
:::
