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
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The source statement carried a nested bullet giving the answer, 'Known to be [ZZ, 0, ZZ^2, 0, ZZ, 0, 0, ...]'; the answer is removed from the statement and established in the solution."
---

::: {.problem}
Use the Künneth formula to compute $H^*(S^2\cross S^2; \ZZ)$.
:::

::: {.solution}

::: pf

::: {.pf-step #sphere}
$H^n(S^2;\ZZ)$ is $\ZZ$ for $n = 0, 2$ and $0$ otherwise.

::: pf-proof
This is the cohomology of the $2$-sphere; it follows from $H_n(S^2;\ZZ)$ by the universal coefficient theorem, since $H_*(S^2;\ZZ)$ is free.
:::

:::

::: {.pf-step #kunneth}
$H^n(S^2 \times S^2;\ZZ) \cong \bigoplus_{i+j=n} H^i(S^2;\ZZ) \otimes H^j(S^2;\ZZ)$.

::: pf-proof
The groups $H^i(S^2;\ZZ)$ are finitely generated and free by step [](#sphere){.pf-ref}, so the $\operatorname{Tor}$ terms of the Künneth formula vanish.
:::

:::

::: pf-step
$$
H^n(S^2 \times S^2;\ZZ) \cong \boxed{\begin{cases} \ZZ & n = 0, 4, \\ \ZZ^2 & n = 2, \\ 0 & \text{otherwise}. \end{cases}}
$$

::: pf-proof
By steps [](#sphere){.pf-ref} and [](#kunneth){.pf-ref}, the only nonzero summands are $H^0 \otimes H^0 = \ZZ$ in degree $0$, $H^2 \otimes H^0 \oplus H^0 \otimes H^2 = \ZZ^2$ in degree $2$, and $H^2 \otimes H^2 = \ZZ$ in degree $4$.
:::

:::

:::

:::
