---
schema: qual/card@1
id: P-TOPF25C
kind: problem
title: Homology of $\mathbb{RP}^2 \times X$ with given $H_*(X)$
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
Let $X$ be a space whose homology is given by
\[
H_k(X; \mathbb{Z}) =
\begin{cases}
\mathbb{Z}_4 & \text{if } k = 2, \\
\mathbb{Z} & \text{if } k = 0, \\
0 & \text{otherwise.}
\end{cases}
\]
Compute $H_*(\mathbb{RP}^2 \times X; \mathbb{Z})$ and $H_*(\mathbb{RP}^2 \times X; \mathbb{Z}_2)$.
:::

::: {.solution}
<1>1. Integrally,
$$H_*(\mathbb{RP}^2;\mathbb Z):\quad H_0=\mathbb Z,\ H_1=\mathbb Z/2,$$
with all higher groups zero.
::: {.proof}
This is the standard cellular homology calculation for $\mathbb{RP}^2$.
:::

<1>2. The integral Künneth theorem gives
$$\boxed{H_k(\mathbb{RP}^2\times X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,\\
\mathbb Z/2,&k=1,3,4,\\
\mathbb Z/4,&k=2,\\
0,&\text{otherwise.}
\end{cases}}$$
::: {.proof}
The tensor terms give $\mathbb Z$ in degree $0$, $\mathbb Z/2$ in degree $1$, $\mathbb Z/4$ in degree $2$, and
$$(\mathbb Z/2)\otimes(\mathbb Z/4)\cong\mathbb Z/2$$
in degree $3$. The only nonzero Tor term is
$$\operatorname{Tor}(\mathbb Z/2,\mathbb Z/4)\cong\mathbb Z/2,$$
appearing one degree higher, in degree $4$. The Künneth short exact sequences split (noncanonically).
:::

<1>3. With $\mathbb F_2$ coefficients,
$$H_i(X;\mathbb F_2)\cong
\begin{cases}
\mathbb F_2,&i=0,2,3,\\
0,&\text{otherwise.}
\end{cases}$$
::: {.proof}
The homology UCT gives
$$0\to H_i(X;\mathbb Z)\otimes\mathbb F_2\to H_i(X;\mathbb F_2)\to \operatorname{Tor}(H_{i-1}(X;\mathbb Z),\mathbb F_2)\to0.$$
The $\mathbb Z/4$ in degree $2$ contributes one $\mathbb F_2$ in degree $2$ by tensor and one in degree $3$ by Tor.
:::

<1>4. Since $H_i(\mathbb{RP}^2;\mathbb F_2)\cong\mathbb F_2$ for $i=0,1,2$, the field-coefficient Künneth theorem yields
$$\boxed{\dim_{\mathbb F_2}H_k(\mathbb{RP}^2\times X;\mathbb F_2)=(1,1,2,2,2,1)}$$
for $k=0,1,2,3,4,5$, and zero otherwise.
::: {.proof}
Multiply the Poincaré polynomials
$$(1+t+t^2)(1+t^2+t^3)=1+t+2t^2+2t^3+2t^4+t^5.$$
:::
:::
