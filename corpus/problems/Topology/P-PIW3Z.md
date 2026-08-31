---
schema: qual/card@1
id: P-PIW3Z
kind: problem
title: $H^*(S^2\times S^2;\ZZ)$ via Künneth
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Product Topology
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
- Use the Kunneth formula to compute $H^*(S^2\cross S^2; \ZZ)$.

  - Known to be $[\ZZ, 0, \ZZ^2, 0, \ZZ, 0, 0, \cdots]$.
:::

::: {.solution}
<1>1. $H^*(S^2;\ZZ) = \ZZ$ in degree $0$, $\ZZ$ in degree $2$, and $0$ otherwise.
::: {.proof}
standard computation of the cohomology of $S^2$.
:::

<1>2. By the Künneth formula (with $\ZZ$ coefficients, and all the relevant groups free so the Tor terms vanish),
$$H^n(S^2 \times S^2;\ZZ) \cong \bigoplus_{i+j=n} H^i(S^2;\ZZ) \otimes H^j(S^2;\ZZ).$$
::: {.proof}
Künneth theorem; since $H^*(S^2;\ZZ)$ is free, $\operatorname{Tor}$ vanishes.
:::

<1>3. The nonzero tensor products are:
- $n=0$: $H^0 \otimes H^0 = \ZZ$;
- $n=2$: $H^2 \otimes H^0 \oplus H^0 \otimes H^2 = \ZZ \oplus \ZZ = \ZZ^2$;
- $n=4$: $H^2 \otimes H^2 = \ZZ$.
::: {.proof}
<1>1 and <1>2.
:::

<1>4. Hence
$$H^n(S^2 \times S^2;\ZZ) = \begin{cases} \ZZ & n = 0, 4 \\ \ZZ^2 & n = 2 \\ 0 & \text{otherwise}. \end{cases}$$
::: {.proof}
<1>3.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4, matching the known answer $[\ZZ, 0, \ZZ^2, 0, \ZZ, 0, \ldots]$.
:::
:::
