---
schema: qual/card@1
id: P-TOPS10G
kind: problem
title: '$\pi_2(\Sigma_g)=0$ for $g\ge1$; surface groups are not free'
classification:
  areas:
  - topology
  topics:
  - Homotopy Groups
  - Surfaces
  - Fundamental Group
relations: []
review: draft
---

::: {.problem}
Show that a closed orientable surface $\Sigma_g$ of genus $g \geq 1$ has $\pi_2(\Sigma_g) = 0$, and deduce that the fundamental group of $\Sigma_g$ is not a free group.
:::

::: {.solution}

::: pf

::: {.pf-step #genus-one-pi2-vanishes}
For $g=1$, $\Sigma_1=T^2$ has universal cover $\mathbb R^2$, hence $\pi_2(\Sigma_1)=0$.

::: pf-proof
Covering maps induce isomorphisms on homotopy groups in degrees at least $2$, and $\mathbb R^2$ is contractible.
:::

:::

::: {.pf-step #higher-genus-pi2-vanishes}
For $g\ge2$, the universal cover of $\Sigma_g$ is contractible, so again $\pi_2(\Sigma_g)=0$.

::: pf-proof
A closed orientable surface of genus at least two has universal cover homeomorphic to the plane (equivalently the disk), by the classification/uniformization of surfaces. Apply the same covering-space invariance of higher homotopy groups.
:::

:::

::: {.pf-step #sigma-g-aspherical}
In fact $\Sigma_g$ is aspherical for every $g\ge1$: all higher homotopy groups vanish.

::: pf-proof
Its universal cover is contractible in both cases above.
:::

:::

::: {.pf-step #free-pi1-implies-bouquet-equivalence}
Suppose $\pi_1(\Sigma_g)$ were a free group $F_S$. Then, since $\Sigma_g$ is a CW complex and aspherical, it would be homotopy equivalent to the bouquet $\bigvee_S S^1$.

::: pf-proof
Choose loops representing a free basis and obtain a map from the bouquet inducing an isomorphism on $\pi_1$. Both spaces have vanishing higher homotopy groups by step [](#sigma-g-aspherical){.pf-ref} and the asphericity of graphs. Whitehead's theorem then makes this map a homotopy equivalence.
:::

:::

::: {.pf-step #homology-mismatch}
This is impossible because
$$
H_2(\Sigma_g;\mathbb Z)\cong\mathbb Z,
\qquad
H_2\!\left(\bigvee_S S^1;\mathbb Z\right)=0.
$$

::: pf-proof
A closed orientable surface has an integral fundamental class, while a graph has no cells and hence no homology above degree $1$.
:::

:::

::: pf-step
Therefore
$$
\boxed{\pi_2(\Sigma_g)=0\text{ and }\pi_1(\Sigma_g)\text{ is not free for every }g\ge1.}
$$

::: pf-proof
Combine steps [](#genus-one-pi2-vanishes){.pf-ref}, [](#higher-genus-pi2-vanishes){.pf-ref}, [](#sigma-g-aspherical){.pf-ref}, [](#free-pi1-implies-bouquet-equivalence){.pf-ref} and [](#homology-mismatch){.pf-ref}.
:::

:::

:::

:::
