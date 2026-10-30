---
schema: qual/card@1
id: P-TEDZR
kind: problem
title: Homology of a solid torus minus two disjoint solid tori
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Let $L \subseteq V$ be the disjoint union of two solid tori ($S^1 \times B^2$) lying inside a larger solid torus $V = S^1 \times B^2$ as shown in the source figure, and let $X = V - \mathring{L}$ be the complement, obtained by removing the interior of $L$.
Compute $H_*(X;\ZZ)$.
:::

::: {.solution}

::: pf

::: pf-step
Realize the ambient solid torus as
$$
V=S^3\setminus\operatorname{int}N(U),
$$
where $U$ is an unknot.

::: pf-proof
The exterior of an unknot in $S^3$ is a solid torus.
:::

:::

::: pf-step
If the two removed solid tori are tubular neighborhoods of disjoint knots $K_1,K_2\subset V$, then $X$ is the exterior of the three-component link
$$
L=U\sqcup K_1\sqcup K_2\subset S^3.
$$

::: pf-proof
Removing the interiors of the three disjoint tubular neighborhoods $N(U),N(K_1),N(K_2)$ from $S^3$ gives exactly the stated complement in $V$.
:::

:::

::: {.pf-step #alexander-duality}
Alexander duality gives
$$
\widetilde H_i(S^3\setminus L;\ZZ)
\cong
\widetilde H^{2-i}(L;\ZZ).
$$

::: pf-proof
Apply Alexander duality to the compact locally contractible subset $L\subset S^3$.
:::

:::

::: {.pf-step #link-cohomology}
Since $L$ is a disjoint union of three circles,
$$
\widetilde H^0(L)\cong\ZZ^2,
\qquad
H^1(L)\cong\ZZ^3.
$$

::: pf-proof
Three connected components give reduced degree-zero rank two, and each circle contributes one degree-one class.
:::

:::

::: pf-step
Consequently
$$
\boxed{H_i(X;\ZZ)\cong
\begin{cases}
\ZZ,&i=0,\\
\ZZ^3,&i=1,\\
\ZZ^2,&i=2,\\
0,&i\ge3.
\end{cases}}
$$

::: pf-proof
The compact link exterior deformation-retracts onto the complement $S^3\setminus L$. Apply steps [](#alexander-duality){.pf-ref} and [](#link-cohomology){.pf-ref}.
:::

:::

:::

:::
