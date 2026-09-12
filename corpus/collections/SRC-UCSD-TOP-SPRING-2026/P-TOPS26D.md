---
schema: qual/card@1
id: P-TOPS26D
kind: problem
title: Homology of $X \times \mathbb{RP}^4$ with given $H_*(X)$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Product Topology
relations: []
review: draft
---

::: problem
Let $X$ be a topological space with homology groups
\[
H_k(X; \mathbb{Z}) =
\begin{cases}
\mathbb{Z} & \text{if } k = 0, \\
\mathbb{Z}_6 & \text{if } k = 3, \\
0 & \text{otherwise.}
\end{cases}
\]
Compute the homology groups $H_\bullet(X \times \mathbb{RP}^4; \mathbb{Z})$ and $H_\bullet(X \times \mathbb{RP}^4; \mathbb{Z}_2)$.
:::

::: {.solution}
<1>1. The integral homology of $\mathbb{RP}^4$ is $H_0=\mathbb Z$, $H_1=H_3=\mathbb Z/2$, and zero otherwise.
::: {.proof}
This is the standard cellular calculation for real projective space.
:::

<1>2. The integral Künneth theorem gives
$$\boxed{H_k(X\times\mathbb{RP}^4;\mathbb Z)\cong\begin{cases}
\mathbb Z,&k=0,\\
\mathbb Z/2,&k=1,\\
\mathbb Z/6,&k=3,\\
\mathbb Z/2,&k=4,\\
\mathbb Z/2,&k=5,\\
\mathbb Z/2,&k=6,7,\\
0,&\text{otherwise.}
\end{cases}}$$
::: {.proof}
Tensor terms from $H_3(X)=\mathbb Z/6$ with $H_1,H_3(\mathbb{RP}^4)=\mathbb Z/2$ contribute $\mathbb Z/2$ in degrees $4,6$. Tor terms $\operatorname{Tor}(\mathbb Z/6,\mathbb Z/2)=\mathbb Z/2$ contribute one degree higher, in degrees $5,7$. The base-factor terms contribute degrees $0,1,3$.
:::

<1>3. With $\mathbb F_2$ coefficients, $H_i(X;\mathbb F_2)\cong\mathbb F_2$ for $i=0,3,4$, while $H_j(\mathbb{RP}^4;\mathbb F_2)\cong\mathbb F_2$ for $0\le j\le4$.
::: {.proof}
Apply the homology UCT to $X$: the $\mathbb Z/6$ in degree $3$ contributes by tensor in degree $3$ and by Tor in degree $4$. Real projective space has one mod-$2$ cellular generator in each degree and zero cellular differential.
:::

<1>4. Hence the mod-$2$ Betti numbers of the product are the coefficients of
$$(1+t^3+t^4)(1+t+t^2+t^3+t^4),$$
namely
$$\boxed{(1,1,1,2,3,2,2,2,1)}$$
in degrees $0$ through $8$.
::: {.proof}
Over a field, Künneth is the graded tensor product, so Poincaré polynomials multiply.
:::
:::
