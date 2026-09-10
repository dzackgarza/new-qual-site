---
schema: qual/card@1
id: P-TOPSU15B
kind: problem
title: "No compact 4-manifold is homotopy equivalent to the suspension of RP^3"
classification:
  areas:
  - topology
  topics:
  - Homotopy Type
  - Manifolds
  - Suspensions
relations: []
review: draft
---

::: problem
Prove that there is no compact $4$-manifold $M$ (with or without boundary) which is homotopy-equivalent to the suspension $\Sigma \mathbb{RP}^3$.
:::

::: {.solution}
<1>1. Suspension shifts reduced homology, so
$$
\widetilde H_i(\Sigma\mathbb{RP}^3;\mathbb Z)
\cong \widetilde H_{i-1}(\mathbb{RP}^3;\mathbb Z).
$$
Hence
$$
H_2(\Sigma\mathbb{RP}^3)\cong\mathbb Z/2,\qquad
H_4(\Sigma\mathbb{RP}^3)\cong\mathbb Z,\qquad H_1=H_3=0.
$$
::: {.proof}
The integral homology of $\mathbb{RP}^3$ is $H_0=H_3=\mathbb Z$, $H_1=\mathbb Z/2$, and $H_2=0$.
:::

<1>2. If a compact $4$-manifold $M$ were homotopy equivalent to this suspension, then $H_4(M;\mathbb Z)\cong\mathbb Z$. Thus $M$ would be closed and orientable.
::: {.proof}
A compact connected $4$-manifold with nonempty boundary has zero absolute top homology, and a closed nonorientable manifold has zero integral top homology.
:::

<1>3. We would also have $H_1(M)=0$ and $H_2(M)=\mathbb Z/2$.
::: {.proof}
Homotopy equivalence preserves homology; use <1>1.
:::

<1>4. For a closed oriented $4$-manifold with $H_1=0$, the group $H_2$ is torsion-free.
::: {.proof}
Poincaré duality gives $H_2(M)\cong H^2(M)$. The universal coefficient sequence
$$
0\to\operatorname{Ext}(H_1(M),\mathbb Z)\to H^2(M)\to\operatorname{Hom}(H_2(M),\mathbb Z)\to0
$$
has zero left term, so $H^2(M)$ is free abelian. Hence $H_2(M)$ is free abelian as well.
:::

<1>5. This contradicts $H_2(M)\cong\mathbb Z/2$. Therefore
$$
\boxed{\Sigma\mathbb{RP}^3\text{ is not homotopy equivalent to any compact }4\text{-manifold}.}
$$
::: {.proof}
Combine <1>2--<1>4.
:::
:::
