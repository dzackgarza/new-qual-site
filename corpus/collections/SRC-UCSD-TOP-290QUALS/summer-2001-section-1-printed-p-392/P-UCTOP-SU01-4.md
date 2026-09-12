---
schema: qual/card@1
id: P-UCTOP-SU01-4
kind: problem
title: Simply-connected CW-complex with H_2 = Z⊕Z is homotopy equivalent to S^2 ∨ S^2
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

Let $X$ be a (path-connected) simply-connected CW-complex with $H_2(X) \cong \mathbb{Z} \oplus \mathbb{Z}$ and $H_{\geq 3}(X) = 0$.
Prove that $X$ is homotopy-equivalent to the "bouquet of two spheres" $S^2 \vee S^2$.

::: {.solution}
<1>1. Since $X$ is simply connected, the Hurewicz map
$$
\pi_2(X)\longrightarrow H_2(X;\mathbb Z)
$$
is an isomorphism.
::: {.proof}
This is the Hurewicz theorem in the first nonzero homotopy degree: a path-connected simply connected space has $\pi_1=0$, and the degree-$2$ Hurewicz map is an isomorphism.
:::

<1>2. Choose maps $f_1,f_2:S^2\to X$ whose Hurewicz classes form a basis of
$$
H_2(X)\cong\mathbb Z\oplus\mathbb Z.
$$
::: {.proof}
By <1>1, every basis element of $H_2(X)$ is represented by an element of $\pi_2(X)$, hence by a based map $S^2\to X$.
:::

<1>3. The maps $f_1,f_2$ assemble to a based map
$$
f:S^2\vee S^2\longrightarrow X.
$$
::: {.proof}
Both sphere maps send the chosen basepoint to the same basepoint of $X$, so the universal property of the wedge gives $f$.
:::

<1>4. The map $f$ is an isomorphism on all integral homology groups.
::: {.proof}
It is an isomorphism on $H_0$ because both spaces are path-connected. By construction it is an isomorphism on $H_2$. Both spaces have $H_1=0$ because they are simply connected. The wedge has no homology above degree $2$, and $H_{\ge3}(X)=0$ by hypothesis. Thus $f_*$ is an isomorphism in every degree.
:::

<1>5. The map $f$ is a homotopy equivalence.
::: {.proof}
Both $S^2\vee S^2$ and $X$ are simply connected CW complexes. The homological Whitehead theorem states that a homology equivalence between simply connected CW complexes is a homotopy equivalence. Applying it to <1>4 gives the claim.
:::

<1>6. Therefore
$$
X\simeq S^2\vee S^2.
$$
::: {.proof}
This is the conclusion of <1>5.
:::
:::

