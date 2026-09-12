---
schema: qual/card@1
id: P-UCTOP-SU12-2
kind: problem
title: Homology of S^2 × I glued by antipodal map
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

Let $X$ be the space obtained by gluing the two ends of $S^2 \times I$ via the antipodal map of $S^2$.
Compute its homology $H_*(X; \mathbb{Z})$.

::: {.solution}
<1>1. The space $X$ is the mapping torus of the antipodal map
$$
A:S^2\to S^2.
$$
::: {.proof}
By definition,
$$
X=S^2\times[0,1]/(x,1)\sim(Ax,0).
$$
:::

<1>2. On homology, $A_*$ is the identity on $H_0(S^2)$ and multiplication by $-1$ on $H_2(S^2)$.
::: {.proof}
The antipodal map on $S^n$ has degree $(-1)^{n+1}$, so on $S^2$ its degree is $-1$.
:::

<1>3. The Wang exact sequence gives
$$
H_i(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,1,\\
\mathbb Z/2,&i=2,\\
0,&i\ge3.
\end{cases}
$$
::: {.proof}
The relevant map on $H_2(S^2)\cong\mathbb Z$ is
$$
I-A_*=1-(-1)=2,
$$
while on $H_0(S^2)$ it is zero. Thus the Wang sequence gives
$$
H_3(X)=\ker(2:\mathbb Z\to\mathbb Z)=0,
$$
$$
H_2(X)=\operatorname{coker}(2:\mathbb Z\to\mathbb Z)\cong\mathbb Z/2,
$$
and
$$
H_1(X)\cong\ker(0:\mathbb Z\to\mathbb Z)\cong\mathbb Z.
$$
Connectedness gives $H_0(X)\cong\mathbb Z$.
:::
:::
