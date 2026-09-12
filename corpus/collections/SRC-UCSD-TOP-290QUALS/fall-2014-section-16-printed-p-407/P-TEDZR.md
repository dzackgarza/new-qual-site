---
schema: qual/card@1
id: P-TEDZR
kind: problem
title: Homology of a solid torus minus two linked solid tori
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

::: problem
Let $X = S^1 \cross B^2 - L$ where $L$ is two linked solid torii inside a larger solid torus.
Compute $H_*(X)$.
:::

::: {.solution}
<1>1. Realize the ambient solid torus as
$$
V=S^3\setminus\operatorname{int}N(U),
$$
where $U$ is an unknot.
::: {.proof}
The exterior of an unknot in $S^3$ is a solid torus.
:::

<1>2. If the two removed solid tori are tubular neighborhoods of disjoint knots $K_1,K_2\subset V$, then $X$ is the exterior of the three-component link
$$
L=U\sqcup K_1\sqcup K_2\subset S^3.
$$
::: {.proof}
Removing the interiors of the three disjoint tubular neighborhoods $N(U),N(K_1),N(K_2)$ from $S^3$ gives exactly the stated complement in $V$.
:::

<1>3. Alexander duality gives
$$
\widetilde H_i(S^3\setminus L;\mathbb Z)
\cong
\widetilde H^{2-i}(L;\mathbb Z).
$$
::: {.proof}
Apply Alexander duality to the compact locally contractible subset $L\subset S^3$.
:::

<1>4. Since $L$ is a disjoint union of three circles,
$$
\widetilde H^0(L)\cong\mathbb Z^2,
\qquad
H^1(L)\cong\mathbb Z^3.
$$
::: {.proof}
Three connected components give reduced degree-zero rank two, and each circle contributes one degree-one class.
:::

<1>5. Consequently
$$
\boxed{H_i(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z^3,&i=1,\\
\mathbb Z^2,&i=2,\\
0,&i\ge3.
\end{cases}}
$$
::: {.proof}
The compact link exterior deformation-retracts onto the complement $S^3\setminus L$. Apply <1>3--<1>4.
:::
:::
