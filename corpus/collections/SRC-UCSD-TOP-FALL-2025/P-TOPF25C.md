---
schema: qual/card@1
id: P-TOPF25C
kind: problem
title: Homology of $\RP^2 \times X$ with given $H_*(X)$
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
H_k(X; \ZZ) =
\begin{cases}
\ZZ_4 & \text{if } k = 2, \\
\ZZ & \text{if } k = 0, \\
0 & \text{otherwise.}
\end{cases}
\]
Compute $H_*(\RP^2 \times X; \ZZ)$ and $H_*(\RP^2 \times X; \ZZ_2)$.
:::

::: {.solution}

::: pf

::: pf-step

Integrally,
$$H_*(\RP^2;\ZZ):\quad H_0=\ZZ,\ H_1=\ZZ/2,$$
with all higher groups zero.

::: pf-proof

This is the standard cellular homology calculation for $\RP^2$.

:::

:::

::: pf-step

The integral Künneth theorem gives
$$\boxed{H_k(\RP^2\times X;\ZZ)\cong
\begin{cases}
\ZZ,&k=0,\\
\ZZ/2,&k=1,3,4,\\
\ZZ/4,&k=2,\\
0,&\text{otherwise.}
\end{cases}}$$

::: pf-proof

The tensor terms give $\ZZ$ in degree $0$, $\ZZ/2$ in degree $1$, $\ZZ/4$ in degree $2$, and
$$(\ZZ/2)\otimes(\ZZ/4)\cong\ZZ/2$$
in degree $3$. The only nonzero Tor term is
$$\operatorname{Tor}(\ZZ/2,\ZZ/4)\cong\ZZ/2,$$
appearing one degree higher, in degree $4$. The Künneth short exact sequences split (noncanonically).

:::

:::

::: pf-step

With $\FF_2$ coefficients,
$$H_i(X;\FF_2)\cong
\begin{cases}
\FF_2,&i=0,2,3,\\
0,&\text{otherwise.}
\end{cases}$$

::: pf-proof

The homology UCT gives
$$0\to H_i(X;\ZZ)\otimes\FF_2\to H_i(X;\FF_2)\to \operatorname{Tor}(H_{i-1}(X;\ZZ),\FF_2)\to0.$$
The $\ZZ/4$ in degree $2$ contributes one $\FF_2$ in degree $2$ by tensor and one in degree $3$ by Tor.

:::

:::

::: pf-step

Since $H_i(\RP^2;\FF_2)\cong\FF_2$ for $i=0,1,2$, the field-coefficient Künneth theorem yields
$$\boxed{\dim_{\FF_2}H_k(\RP^2\times X;\FF_2)=(1,1,2,2,2,1)}$$
for $k=0,1,2,3,4,5$, and zero otherwise.

::: pf-proof

Multiply the Poincaré polynomials
$$(1+t+t^2)(1+t^2+t^3)=1+t+2t^2+2t^3+2t^4+t^5.$$

:::

:::

:::

:::
