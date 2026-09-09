---
schema: qual/card@1
id: P-UCTOP-FA12-4
kind: problem
title: Homology of exterior of knotted solid torus via Mayer-Vietoris
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

Let $N$ be a knotted solid torus in $S^3$, let $T$ be its boundary torus, and let $X$ be its exterior (that is, the closure of $S^3 - N$). Use Mayer-Vietoris to compute the homology $H_*(X; \mathbb{Z})$.

::: {.solution}
<1>1. Let $X$ be the exterior of the knotted solid torus $N$. Then
$$
S^3=N\cup X,\qquad N\cap X=T^2,\qquad N\simeq S^1.
$$
::: {.proof}
By definition $X$ is the closure of the complement of the interior of $N$, and the common boundary is the torus $T=\partial N=\partial X$.
:::

<1>2. The Mayer--Vietoris sequence in degree $1$ gives
$$
0\to H_1(T^2)\to H_1(N)\oplus H_1(X)\to0.
$$
::: {.proof}
Since $H_2(S^3)=H_1(S^3)=0$, the relevant exact segment is
$$
0\to H_1(T^2)\to H_1(N)\oplus H_1(X)\to0.
$$
Thus $\mathbb Z^2\cong\mathbb Z\oplus H_1(X)$, so $H_1(X)\cong\mathbb Z$.
:::

<1>3. The degree-$3$ and degree-$2$ part of Mayer--Vietoris gives
$$
0\to H_3(X)\to\mathbb Z\xrightarrow{\partial}\mathbb Z\to H_2(X)\to0.
$$
::: {.proof}
Use $H_3(T^2)=0$, $H_3(N)=0$, $H_3(S^3)=\mathbb Z$, $H_2(T^2)=\mathbb Z$, $H_2(N)=0$, and $H_2(S^3)=0$.
:::

<1>4. The connecting map $\partial:H_3(S^3)\to H_2(T^2)$ is an isomorphism.
::: {.proof}
The fundamental class $[S^3]$ is sent to the oriented common boundary class $[T^2]$ of the decomposition into the two compact $3$-manifolds $N$ and $X$. Both groups are infinite cyclic, and this boundary class is a generator.
:::

<1>5. Hence
$$
H_i(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,1,\\
0,&i\ge2.
\end{cases}
$$
::: {.proof}
By <1>3--<1>4, $H_3(X)=H_2(X)=0$. By <1>2, $H_1(X)=\mathbb Z$, and $X$ is connected so $H_0(X)=\mathbb Z$.
:::
:::
