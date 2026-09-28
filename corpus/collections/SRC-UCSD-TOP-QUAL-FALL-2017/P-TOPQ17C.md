---
schema: qual/card@1
id: P-TOPQ17C
kind: problem
title: "Homology of the mapping torus of the antipodal map on S^2"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mapping Torus
  - Spheres
relations: []
review: draft
---

::: {.problem}
Let $X$ be the space obtained by gluing the two ends of $S^2 \times I$ via the antipodal map of $S^2$.
Compute its homology $H_*(X; \mathbb{Z})$.
:::

::: {.solution}
<1>1. For the mapping torus $T_f$ of $f:S^2\to S^2$, the Wang sequence gives short exact pieces
$$0\to\operatorname{coker}(1-f_*:H_k(S^2)\to H_k(S^2))\to H_k(T_f)\to\ker(1-f_*:H_{k-1}(S^2)\to H_{k-1}(S^2))\to0.$$
::: {.proof}
This is the homology long exact sequence of a mapping torus.
:::

<1>2. The antipodal map on $S^2$ has degree $-1$, so it acts by $-1$ on $H_2(S^2)=\mathbb Z$ and by $1$ on $H_0(S^2)=\mathbb Z$.
::: {.proof}
The antipodal map on $S^n$ has degree $(-1)^{n+1}$.
:::

<1>3. Hence
$$\boxed{H_k(X;\mathbb Z)\cong\begin{cases}\mathbb Z,&k=0,1,\\\mathbb Z/2,&k=2,\\0,&k\ge3.\end{cases}}$$
::: {.proof}
On $H_2$, $1-f_*$ is multiplication by $2$, giving cokernel $\mathbb Z/2$ and zero kernel. On $H_0$, $1-f_*=0$, giving the $H_1\cong\mathbb Z$ term. There is no top $H_3$ because the monodromy reverses the fiber orientation.
:::
:::
