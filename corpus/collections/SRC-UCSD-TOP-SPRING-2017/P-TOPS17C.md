---
schema: qual/card@1
id: P-TOPS17C
kind: problem
title: "Homology of the mapping torus as the cokernel of id - f_*"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mapping Torus
  - Exact Sequences
relations: []
review: draft
---

::: {.problem}
Let $Y$ be a space, let $f : Y \to Y$ be a self-mapping of $Y$, and let $X$ be the mapping torus of $f$, that is, the space obtained from $Y \times I$ by identifying $(y, 1) \sim (f(y), 0)$ for each point $y \in Y$.
Prove that $H_1(X; \mathbb{Z}) \cong H_1(Y; \mathbb{Z}) / \operatorname{im}(\operatorname{id} - f_*)$, where $f_*$ is the induced map $H_1(Y; \mathbb{Z}) \to H_1(Y; \mathbb{Z})$.
:::

::: {.solution}
<1>1. The statement as printed is false, already for $Y=\{*\}$.
::: {.proof}
Then $f=\operatorname{id}_Y$, the mapping torus is $X\cong S^1$, and hence $H_1(X;\mathbb Z)\cong\mathbb Z$. The displayed quotient in the problem is $H_1(Y)/\operatorname{im}(\operatorname{id}-f_*)=0$.
:::

<1>2. The correct general statement is the Wang exact sequence
$$
H_1(Y)\xrightarrow{\operatorname{id}-f_*}H_1(Y)\longrightarrow H_1(X)\longrightarrow
H_0(Y)\xrightarrow{\operatorname{id}-f_*}H_0(Y).
$$
::: {.proof}
View the mapping torus as the homotopy coequalizer of $\operatorname{id}_Y$ and $f$. Its standard mapping-cone chain model is the cone of $\operatorname{id}-f_*:C_*(Y)\to C_*(Y)$, shifted in the usual way. The associated long exact homology sequence is precisely the displayed Wang sequence.
:::

<1>3. Consequently there is a short exact sequence
$$
0\to \operatorname{coker}(\operatorname{id}-f_*:H_1(Y)\to H_1(Y))
\to H_1(X)
\to \ker(\operatorname{id}-f_*:H_0(Y)\to H_0(Y))\to0.
$$
::: {.proof}
Take the exact portion in <1>2 and identify the kernel and cokernel at the adjacent terms.
:::

<1>4. If $Y$ is path-connected, then $f_*$ is the identity on $H_0(Y)\cong\mathbb Z$, so
$$
\boxed{H_1(X;\mathbb Z)\cong
H_1(Y;\mathbb Z)/\operatorname{im}(\operatorname{id}-f_*)\oplus\mathbb Z.}
$$
::: {.proof}
The kernel on $H_0$ is then all of $\mathbb Z$. The short exact sequence in <1>3 splits because $\mathbb Z$ is free abelian. Thus the omitted $\mathbb Z$ summand is unavoidable.
:::
:::
