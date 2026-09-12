---
schema: qual/card@1
id: P-TOPF10B
kind: problem
title: "Double covers of the Klein bottle"
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Surfaces
relations: []
review: draft
---

::: problem
How many distinct double covers does the Klein bottle have?
Can you identify any of them?
:::

::: {.solution}
<1>1. Connected double covers of the Klein bottle $K$ correspond to nonzero homomorphisms
$$
\pi_1(K)\longrightarrow\mathbb Z/2.
$$
::: {.proof}
An index-$2$ subgroup is automatically normal and is the kernel of the quotient map to $\mathbb Z/2$; conversely every nonzero map has index-$2$ kernel.
:::

<1>2. Since
$$
H_1(K;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/2,
$$
we have
$$
\operatorname{Hom}(\pi_1(K),\mathbb Z/2)
\cong\operatorname{Hom}(H_1(K),\mathbb Z/2)\cong(\mathbb Z/2)^2.
$$
::: {.proof}
Every homomorphism to an abelian group factors through abelianization. Both summands admit an independent map to $\mathbb Z/2$.
:::

<1>3. Hence there are exactly three connected double covers.
::: {.proof}
The vector space $(\mathbb Z/2)^2$ has three nonzero elements.
:::

<1>4. One is the orientation double cover $T^2\to K$; the other two have total space homeomorphic to the Klein bottle.
::: {.proof}
Using $\pi_1(K)=\langle a,b\mid aba^{-1}=b^{-1}\rangle$, the orientation character sends the orientation-reversing generator $a$ to $1$ and $b$ to $0$; its kernel $\langle a^2,b\rangle\cong\mathbb Z^2$ is the torus group. The other two index-$2$ kernels have Klein-bottle group and hence correspond to double covers with Klein-bottle total space.
:::

<1>5. Thus
$$
\boxed{3\text{ connected double covers}}
$$
exist up to equivalence. Including the disconnected trivial two-sheeted cover gives $4$ double covers in total.
::: {.proof}
The zero homomorphism corresponds to $K\sqcup K\to K$.
:::
:::
