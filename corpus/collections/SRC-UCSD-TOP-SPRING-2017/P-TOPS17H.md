---
schema: qual/card@1
id: P-TOPS17H
kind: problem
title: 'Universal cover of a closed $3$-manifold with finite $\pi_1$ is homotopy equivalent to $S^3$'
classification:
  areas:
  - topology
  topics:
  - Universal Cover
  - Homotopy Type
  - Manifolds
  - Fundamental Group
relations: []
review: draft
---

::: problem
Let $M$ be a closed connected $3$-manifold with finite fundamental group.
Show that its universal cover is homotopy-equivalent to $S^3$.
:::

::: {.solution}
<1>1. Since $\pi_1(M)$ is finite, the universal cover
$$
p:\widetilde M\to M
$$
is a finite-sheeted covering of a closed $3$-manifold. Hence $\widetilde M$ is itself a closed connected $3$-manifold, and it is simply connected.
::: {.proof}
The universal cover of a manifold is a manifold, and finiteness of the deck group makes the covering finite, so compactness is preserved.
:::

<1>2. The manifold $\widetilde M$ is orientable and
$$
H_1(\widetilde M;\mathbb Z)=0.
$$
::: {.proof}
Simply connected manifolds are orientable, and $H_1$ is the abelianization of $\pi_1$.
:::

<1>3. Poincaré duality and the universal coefficient theorem give
$$
H_2(\widetilde M;\mathbb Z)=0,
$$
while
$$
H_0(\widetilde M)\cong H_3(\widetilde M)\cong\mathbb Z.
$$
::: {.proof}
For a closed oriented $3$-manifold,
$$
H_2\cong H^1\cong\operatorname{Hom}(H_1,\mathbb Z)=0.
$$
Connectedness gives $H_0=\mathbb Z$, and orientability gives the fundamental class in $H_3\cong\mathbb Z$.
:::

<1>4. Since $\widetilde M$ is simply connected and $H_2=0$, the Hurewicz theorem gives $\pi_2(\widetilde M)=0$, and then
$$
\pi_3(\widetilde M)\xrightarrow{\cong}H_3(\widetilde M)\cong\mathbb Z.
$$
::: {.proof}
The degree-$2$ Hurewicz theorem identifies $\pi_2$ with $H_2$ for simply connected spaces. Thus $\widetilde M$ is $2$-connected, and the degree-$3$ Hurewicz theorem applies.
:::

<1>5. Choose a map $f:S^3\to\widetilde M$ representing a generator of $\pi_3(\widetilde M)$. Then $f$ is an integral homology equivalence.
::: {.proof}
By <1>4 it maps the fundamental class to a generator of $H_3$. Both spaces have $H_0=H_3=\mathbb Z$ and zero homology in degrees $1,2$.
:::

<1>6. By the homological Whitehead theorem for simply connected CW complexes,
$$
\boxed{\widetilde M\simeq S^3.}
$$
::: {.proof}
Manifolds have CW type, and a homology equivalence between simply connected CW complexes is a homotopy equivalence.
:::
:::
