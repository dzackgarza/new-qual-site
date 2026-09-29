---
schema: qual/card@1
id: P-AMD-T2WKOZFN
kind: problem
title: Antipodal map on $S^n$ is homotopic to the identity for $n$ odd
classification:
  areas:
  - topology
  topics:
  - Degree
  - Homotopy
relations: []
review: draft
---

::: {.problem}
Let $\alpha: S^n \to S^n,~ \alpha(p) = -p$ be the antipodal map on $S^n$.
Show that $n ~\text{odd} \implies f \simeq \text{id}$.
:::

::: {.solution}

::: pf

::: pf-step

The antipodal map $\alpha:S^n\to S^n$, $\alpha(x)=-x$, has degree
$$
\deg\alpha=(-1)^{n+1}.
$$

::: pf-proof

The antipodal map is the restriction to $S^n\subset\mathbb R^{n+1}$ of the linear map $-I_{n+1}$. The degree of the restriction of an invertible linear map to the unit sphere is the sign of its determinant, here
$$
\operatorname{sgn}\det(-I_{n+1})=(-1)^{n+1}.
$$

:::

:::

::: {.pf-step #s2}

If $n$ is odd, then $\deg\alpha=1=\deg\operatorname{id}_{S^n}$.

::: pf-proof

For odd $n$, the exponent $n+1$ is even.

:::

:::

::: pf-step

Therefore
$$
\boxed{\alpha\simeq\operatorname{id}_{S^n}}.
$$

::: pf-proof

For $n\ge1$, homotopy classes of maps $S^n\to S^n$ are classified by degree: two maps are homotopic iff they have the same degree. Apply step [](#s2){.pf-ref}. (For the only odd dimensions under consideration, $n\ge1$ automatically.)

:::

:::

:::

:::
