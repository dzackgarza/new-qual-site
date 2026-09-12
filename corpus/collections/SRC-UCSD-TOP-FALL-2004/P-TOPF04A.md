---
schema: qual/card@1
id: P-TOPF04A
kind: problem
title: "A space with the homology and fundamental group of the torus but not homotopy equivalent to it"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Fundamental Group
  - Homotopy Type
relations: []
review: draft
---

::: problem
Find a space $X$ that has the same integral homology and fundamental group as the torus $S^1 \times S^1$, but is not homotopy equivalent to the torus.
Prove that $X$ is not homotopy equivalent to the torus.
:::

::: {.solution}
<1>1. Start with the torus $T=T^2$, choose a generator $a\in\pi_1(T)\cong\mathbb Z^2$, and attach a $2$-cell by the constant map. The resulting space is
$$
T\vee S^2.
$$
::: {.proof}
A trivially attached $2$-cell is a wedged $2$-sphere and does not change the fundamental group.
:::

<1>2. In the universal cover, the lifts of this new $2$-cell form a free rank-one module over
$$
\Lambda=\mathbb Z[\pi_1(T)]\cong\mathbb Z[a^{\pm1},b^{\pm1}].
$$
Let $e$ denote one lift.
::: {.proof}
Deck transformations translate a chosen lift through all lifts, so the cellular $2$-chains contributed by this cell are $\Lambda e$.
:::

<1>3. Attach one $3$-cell to $T\vee S^2$ along a map representing the element
$$
(2-a)e\in\pi_2(T\vee S^2).
$$
Call the resulting space $X$.
::: {.proof}
Since $T$ is aspherical, the universal cover of $T\vee S^2$ is obtained from the contractible plane by wedging a $2$-sphere at every lift of the basepoint. Hence
$$
\pi_2(T\vee S^2)\cong H_2(\widetilde{T\vee S^2})\cong\Lambda e,
$$
so the indicated element is represented by an attaching map $S^2\to T\vee S^2$.
:::

<1>4. The fundamental group of $X$ is still $\mathbb Z^2$.
::: {.proof}
Cells of dimensions $2$ and $3$ attached as above do not add generators to $\pi_1$, and the $2$-cell was attached trivially, so no relation is imposed on $\pi_1(T)$.
:::

<1>5. The added cells do not change ordinary integral homology.
::: {.proof}
In the ordinary cellular chain complex, the boundary coefficient of the new $3$-cell on the new $2$-cell is the augmentation
$$
\varepsilon(2-a)=2-1=1.
$$
Thus the new cellular summand is
$$
0\to\mathbb Z\xrightarrow{1}\mathbb Z\to0,
$$
which is acyclic. Therefore
$$
H_*(X;\mathbb Z)\cong H_*(T^2;\mathbb Z).
$$
:::

<1>6. Nevertheless $X$ is not homotopy-equivalent to $T^2$.
::: {.proof}
In the universal cover, the corresponding cellular boundary is multiplication by $2-a$ on $\Lambda$:
$$
\Lambda\xrightarrow{\,2-a\,}\Lambda.
$$
Hence the new contribution to $H_2(\widetilde X)$ is
$$
\Lambda/(2-a)\Lambda,
$$
which is nonzero because $2-a$ is not a unit in the Laurent polynomial ring $\Lambda$. Thus $\widetilde X$ is not contractible. But $T^2$ is aspherical and its universal cover is contractible. Homotopy-equivalent connected CW complexes have homotopy-equivalent universal covers, so $X\not\simeq T^2$.
:::

<1>7. Therefore $X$ has the same integral homology and fundamental group as the torus but a different homotopy type.
::: {.proof}
Combine <1>4--<1>6.
:::
:::
