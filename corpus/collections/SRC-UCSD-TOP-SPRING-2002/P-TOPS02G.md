---
schema: qual/card@1
id: P-TOPS02G
kind: problem
title: "Vanishing cup products lift to the mapping cone"
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
  - Mapping Cone
relations: []
review: draft
---

::: {.problem}
If all $n$-fold cup products vanish on $H^*(Y)$ and $f : X \to Y$ is a continuous map, prove all $n+1$ fold cup products vanish in $H^*(C_f)$ where $C_f$ is the mapping cone of $f$.
:::

::: {.solution}

::: pf

::: pf-step

Write the mapping cone as
$$
C_f=Y\cup_f CX,
$$
where $CX$ is contractible.

::: pf-proof

This is the definition of the mapping cone.

:::

:::

::: {.pf-step #s2}

Let $\alpha_1,\ldots,\alpha_{n+1}\in H^{>0}(C_f)$.
The restriction of
$$
\alpha_1\smile\cdots\smile\alpha_n
$$
to $Y$ is zero.

::: pf-proof

Restriction is a ring homomorphism. By hypothesis every $n$-fold cup product of positive-degree classes in $H^*(Y)$ vanishes.

:::

:::

::: pf-step

Hence there exists
$$
u\in H^*(C_f,Y)
$$
whose image in $H^*(C_f)$ is $\alpha_1\smile\cdots\smile\alpha_n$.

::: pf-proof

In the long exact sequence of the pair $(C_f,Y)$, the kernel of the restriction map $H^*(C_f)\to H^*(Y)$ is the image of $H^*(C_f,Y)$. Apply step [](#s2){.pf-ref}.

:::

:::

::: pf-step

Since $\alpha_{n+1}$ has positive degree and $CX$ is contractible, its restriction to $CX$ is zero. Therefore there exists
$$
v\in H^*(C_f,CX)
$$
which maps to $\alpha_{n+1}$.

::: pf-proof

Again use the long exact sequence of a pair, now $(C_f,CX)$, together with $H^{>0}(CX)=0$.

:::

:::

::: {.pf-step #s5}

The relative cup product satisfies
$$
u\smile v\in H^*(C_f,Y\cup CX)=H^*(C_f,C_f)=0.
$$

::: pf-proof

Relative cup product sends
$$
H^p(C_f,Y)\times H^q(C_f,CX)
\longrightarrow H^{p+q}(C_f,Y\cup CX).
$$
But $Y\cup CX=C_f$.

:::

:::

::: pf-step

Mapping step [](#s5){.pf-ref} to absolute cohomology gives
$$
\boxed{\alpha_1\smile\cdots\smile\alpha_{n+1}=0.}
$$

::: pf-proof

Naturality of the relative cup product identifies the image of $u\smile v$ with the cup product of the absolute images of $u$ and $v$, namely the displayed $(n+1)$-fold product.

:::

:::

:::

:::
