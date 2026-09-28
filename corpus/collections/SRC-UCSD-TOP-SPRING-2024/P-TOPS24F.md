---
schema: qual/card@1
id: P-TOPS24F
kind: problem
title: Nonvanishing of $\pi_5(S^3 \vee S^3)$ via a 6-cell
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
By considering ways to attach a 6-cell to $S^3 \vee S^3$, show that $\pi_5(S^3 \vee S^3) \neq 0$.
:::

::: {.solution}
<1>1. The product $S^3\times S^3$ has a CW structure with one $0$-cell, two $3$-cells, and one $6$-cell. Its $3$-skeleton is
$$S^3\vee S^3.$$
::: {.proof}
Take the product CW structure from the standard $0$- and $3$-cell structure on each factor. The cells are the products $e^0\times e^0$, $e^3\times e^0$, $e^0\times e^3$, and $e^3\times e^3$.
:::

<1>2. Thus
$$S^3\times S^3=(S^3\vee S^3)\cup_\alpha e^6$$
for some attaching map
$$\alpha:S^5\to S^3\vee S^3.$$
::: {.proof}
This is exactly the attaching map of the unique top-dimensional cell in the product CW structure.
:::

<1>3. The attaching map $\alpha$ is not null-homotopic.
::: {.proof}
If it were null-homotopic, the resulting space would be homotopy equivalent to
$$S^3\vee S^3\vee S^6.$$
In a wedge, the product of the two degree-$3$ cohomology generators is zero. But in $S^3\times S^3$, the cross product of the two factor generators is the nonzero fundamental class in $H^6(S^3\times S^3;\mathbb Z)$. Hence the two spaces cannot be homotopy equivalent.
:::

<1>4. Therefore
$$\boxed{0\ne[\alpha]\in\pi_5(S^3\vee S^3),}$$
so $\pi_5(S^3\vee S^3)\ne0$.
::: {.proof}
This is precisely the conclusion of <1>3. The attaching map is in fact the Whitehead product of the two wedge inclusions, up to sign.
:::
:::
