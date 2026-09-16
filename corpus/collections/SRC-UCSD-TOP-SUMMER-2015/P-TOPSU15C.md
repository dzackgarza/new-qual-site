---
schema: qual/card@1
id: P-TOPSU15C
kind: problem
title: "Every map from RP^2 to the torus is null-homotopic"
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Projective Spaces
  - Surfaces
relations: []
review: draft
---

::: {.problem}
Prove that any map $\mathbb{RP}^2 \to T^2$ must be null-homotopic.
:::

::: {.solution}
<1>1. Let $f:\mathbb{RP}^2\to T^2$. The induced homomorphism
$$
f_*:\pi_1(\mathbb{RP}^2)\cong\mathbb Z/2\longrightarrow\pi_1(T^2)\cong\mathbb Z^2
$$
is trivial.
::: {.proof}
The torsion-free group $\mathbb Z^2$ has no nontrivial element of order dividing $2$.
:::

<1>2. Therefore $f$ lifts to the universal cover
$$
\widetilde f:\mathbb{RP}^2\to\mathbb R^2.
$$
::: {.proof}
The lifting criterion for the universal covering $\mathbb R^2\to T^2$ says that a lift exists exactly when $f_*(\pi_1(\mathbb{RP}^2))$ is trivial.
:::

<1>3. Since $\mathbb R^2$ is contractible, $\widetilde f$ is null-homotopic.
::: {.proof}
Any map into a contractible space is homotopic to a constant.
:::

<1>4. Projecting this homotopy to $T^2$ shows
$$
\boxed{f\simeq\mathrm{const}.}
$$
::: {.proof}
Compose the null-homotopy of $\widetilde f$ with the covering projection.
:::
:::
