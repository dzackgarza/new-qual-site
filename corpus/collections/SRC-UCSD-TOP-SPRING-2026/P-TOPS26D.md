---
schema: qual/card@1
id: P-TOPS26D
kind: problem
title: Homology of $X \times \RP^4$ with given $H_*(X)$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Product Topology
relations: []
review: draft
---

::: {.problem}
Let $X$ be a topological space with homology groups
$$
H_k(X; \ZZ) =
\begin{cases}
\ZZ & \text{if } k = 0, \\
\ZZ_6 & \text{if } k = 3, \\
0 & \text{otherwise.}
\end{cases}
$$
Compute the homology groups $H_\bullet(X \times \RP^4; \ZZ)$ and $H_\bullet(X \times \RP^4; \ZZ_2)$.
:::

::: {.solution}

::: pf

::: pf-step
The integral homology of $\RP^4$ is $H_0=\ZZ$, $H_1=H_3=\ZZ/2$, and zero otherwise.

::: pf-proof
This is the standard cellular calculation for real projective space.
:::

:::

::: pf-step
The integral Künneth theorem gives
$$\boxed{H_k(X\times\RP^4;\ZZ)\cong\begin{cases}
\ZZ,&k=0,\\
\ZZ/2,&k=1,\\
\ZZ/6\oplus\ZZ/2,&k=3,\\
\ZZ/2,&k=4,\\
\ZZ/2,&k=5,\\
\ZZ/2,&k=6,7,\\
0,&\text{otherwise.}
\end{cases}}$$

::: pf-proof
Tensor terms from $H_3(X)=\ZZ/6$ with $H_1,H_3(\RP^4)=\ZZ/2$ contribute $\ZZ/2$ in degrees $4,6$. Tor terms $\operatorname{Tor}(\ZZ/6,\ZZ/2)=\ZZ/2$ contribute one degree higher, in degrees $5,7$. The terms $H_0(X)\otimes H_j(\RP^4)$ contribute $\ZZ,\ZZ/2,\ZZ/2$ in degrees $0,1,3$, and $H_3(X)\otimes H_0(\RP^4)$ contributes $\ZZ/6$ in degree $3$.
:::

:::

::: pf-step
With $\FF_2$ coefficients, $H_i(X;\FF_2)\cong\FF_2$ for $i=0,3,4$, while $H_j(\RP^4;\FF_2)\cong\FF_2$ for $0\le j\le4$.

::: pf-proof
Apply the homology UCT to $X$: the $\ZZ/6$ in degree $3$ contributes by tensor in degree $3$ and by Tor in degree $4$. Real projective space has one mod-$2$ cellular generator in each degree and zero cellular differential.
:::

:::

::: pf-step
Hence the mod-$2$ Betti numbers of the product are the coefficients of
$$(1+t^3+t^4)(1+t+t^2+t^3+t^4),$$
namely
$$\boxed{(1,1,1,2,3,2,2,2,1)}$$
in degrees $0$ through $8$.

::: pf-proof
Over a field, Künneth is the graded tensor product, so Poincaré polynomials multiply.
:::

:::

:::

:::
