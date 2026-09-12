---
schema: qual/card@1
id: P-UCTOP-SU09-7
kind: problem
title: 1-connected CW complex with H_3 = Z^2 is S^3 ∨ S^3
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

Suppose $X$ is a 1-connected CW complex whose homology groups are $\mathbb{Z}$ in dimension 0, $\mathbb{Z}^2$ in dimension 3, and zero otherwise.
By constructing a map $S^3 \vee S^3 \to X$, show that $X$ is homotopy-equivalent to $S^3 \vee S^3$.

::: {.solution}
<1>1. Since $X$ is simply connected and $H_2(X)=0$, one has $\pi_2(X)=0$.
:::
::: {.proof}
For a simply connected space, the degree-$2$ Hurewicz map $\pi_2(X)\to H_2(X)$ is an isomorphism. The target is zero by hypothesis.
:::

<1>2. Hence $X$ is $2$-connected, and Hurewicz gives
$$
\pi_3(X)\xrightarrow{\sim}H_3(X)\cong\mathbb Z^2.
$$
:::
::: {.proof}
Apply the Hurewicz theorem in the first possible nonzero homotopy degree after <1>1.
:::

<1>3. Choose based maps $f_1,f_2:S^3\to X$ whose Hurewicz classes form a basis of $H_3(X)$, and let
$$
f=f_1\vee f_2:S^3\vee S^3\to X.
$$
:::
::: {.proof}
The isomorphism in <1>2 lets us represent any chosen basis of $H_3(X)$ by elements of $\pi_3(X)$. The common basepoint gives the wedge map.
:::

<1>4. The map $f$ is an isomorphism on integral homology in every degree.
:::
::: {.proof}
It is an isomorphism on $H_3$ by construction and on $H_0$ because both spaces are connected. The source and target have zero homology in every other degree by the hypothesis on $X$ and the homology of a wedge of two $3$-spheres.
:::

<1>5. Therefore
$$
\boxed{X\simeq S^3\vee S^3}.
$$
:::
::: {.proof}
Both spaces are simply connected CW complexes. The homological Whitehead theorem says that a homology equivalence between simply connected CW complexes is a homotopy equivalence. Apply it to <1>4.
:::
:::

