---
schema: qual/card@1
id: P-TOPF02C
kind: problem
title: A Moore space $M(\ZZ_4,2)$ and the homology of $\RP^2\times M(\ZZ_4,2)$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
(a) Construct a space $Y$ with the following properties:
$$
H_k(Y; \ZZ) = \begin{cases} \ZZ_4 & \text{if } k = 2 \\ \ZZ & \text{if } k = 0 \\ 0 & \text{otherwise.} \end{cases}
$$

(b) Compute $H_*(\RP^2 \times Y; \ZZ_2)$, $H_*(\RP^2 \times Y; \ZZ)$, and $H^*(\RP^2 \times Y; \ZZ)$.
:::

::: {.solution}

::: pf

::: {.pf-step #moore-space-construction}
Part (a): Construction of Moore space $Y = M(\ZZ_4, 2)$:

::: pf-proof

::: pf-step
Define $Y = S^2 \cup_f e^3$, where the attaching map $f: \partial e^3 = S^2 \to S^2$ has topological degree $4$.

::: pf-proof
definition of Moore space.
:::

:::

::: pf-step
The cellular chain complex of $Y$ is:
\[
C_3 = \ZZ\langle e^3 \rangle, \quad C_2 = \ZZ\langle e^2 \rangle, \quad C_1 = 0, \quad C_0 = \ZZ\langle e^0 \rangle,
\]
with boundary maps $d_3(e^3) = 4 e^2$, $d_2 = 0$, and $d_1 = 0$.

::: pf-proof
degree of attaching map on 2-cells.
:::

:::

::: pf-step
The resulting integral homology groups are:
\[
H_0(Y; \ZZ) \cong \ZZ, \quad H_1(Y; \ZZ) = 0, \quad H_2(Y; \ZZ) = \ker(d_2)/\operatorname{im}(d_3) \cong \ZZ/4\ZZ = \ZZ_4, \quad H_k(Y; \ZZ) = 0 \ (k \ge 3).
\]

::: pf-proof
homology of cellular chain complex.
:::

:::

:::

:::

::: pf-step
Part (b)(i): Integer homology $H_*(\RP^2 \times Y; \ZZ)$:

::: pf-proof

::: pf-step
Recall $H_*(\RP^2; \ZZ) = (\ZZ, \ZZ_2, 0, \dots)$.

::: pf-proof
standard homology of real projective plane.
:::

:::

::: pf-step
Apply the Künneth Theorem $H_n(X \times Y) \cong \bigoplus_{i+j=n} (H_i \otimes H_j) \oplus \bigoplus_{i+j=n-1} \operatorname{Tor}_1^{\ZZ}(H_i, H_j)$:

- $n = 0$: $H_0 \otimes H_0 \cong \ZZ \otimes \ZZ \cong \ZZ$.

- $n = 1$: $H_1 \otimes H_0 \cong \ZZ_2 \otimes \ZZ \cong \ZZ_2$.

- $n = 2$: $H_0 \otimes H_2 \cong \ZZ \otimes \ZZ_4 \cong \ZZ_4$.

- $n = 3$: $(H_1 \otimes H_2) \oplus \operatorname{Tor}_1^{\ZZ}(H_1, H_2) \cong (\ZZ_2 \otimes \ZZ_4) \oplus \operatorname{Tor}(\ZZ_2, \ZZ_4) \cong \ZZ_2 \oplus \ZZ_2$.

- $n \ge 4$: $H_n = 0$.

::: pf-proof
Künneth Theorem for integral homology.
:::

:::

:::

:::

::: pf-step
Part (b)(ii): Mod 2 homology $H_*(\RP^2 \times Y; \ZZ_2)$:

::: pf-proof

::: pf-step
By the Universal Coefficient Theorem, $H_*(\RP^2; \ZZ_2) = (\ZZ_2, \ZZ_2, \ZZ_2, 0, \dots)$ and $H_*(Y; \ZZ_2) = (\ZZ_2, 0, \ZZ_2, \ZZ_2, 0, \dots)$.

::: pf-proof
UCT over $\ZZ_2$.
:::

:::

::: pf-step
By the Künneth Theorem over the field $\ZZ_2$, $H_n(\RP^2 \times Y; \ZZ_2) \cong \bigoplus_{i+j=n} H_i(\RP^2; \ZZ_2) \otimes_{\ZZ_2} H_j(Y; \ZZ_2)$:

- $n = 0$: $H_0 \otimes H_0 \cong \ZZ_2$.

- $n = 1$: $H_1 \otimes H_0 \cong \ZZ_2$.

- $n = 2$: $(H_0 \otimes H_2) \oplus (H_2 \otimes H_0) \cong \ZZ_2 \oplus \ZZ_2$.

- $n = 3$: $(H_0 \otimes H_3) \oplus (H_1 \otimes H_2) \cong \ZZ_2 \oplus \ZZ_2$.

- $n = 4$: $(H_1 \otimes H_3) \oplus (H_2 \otimes H_2) \cong \ZZ_2 \oplus \ZZ_2$.

- $n = 5$: $H_2 \otimes H_3 \cong \ZZ_2$.

- $n \ge 6$: $H_n = 0$.

::: pf-proof
field Künneth formula.
:::

:::

:::

:::

::: {.pf-step #integer-cohomology}
Part (b)(iii): Integer cohomology $H^*(\RP^2 \times Y; \ZZ)$:

::: pf-proof

::: pf-step
By the Universal Coefficient Theorem for cohomology, $H^n(X; \ZZ) \cong \operatorname{Free}(H_n(X)) \oplus \operatorname{Tors}(H_{n-1}(X))$:

- $n = 0$: $\operatorname{Free}(H_0) \cong \ZZ$.

- $n = 1$: $\operatorname{Free}(H_1) \oplus \operatorname{Tors}(H_0) = 0 \oplus 0 = 0$.

- $n = 2$: $\operatorname{Free}(H_2) \oplus \operatorname{Tors}(H_1) = 0 \oplus \ZZ_2 \cong \ZZ_2$.

- $n = 3$: $\operatorname{Free}(H_3) \oplus \operatorname{Tors}(H_2) = 0 \oplus \ZZ_4 \cong \ZZ_4$.

- $n = 4$: $\operatorname{Free}(H_4) \oplus \operatorname{Tors}(H_3) = 0 \oplus (\ZZ_2 \oplus \ZZ_2) \cong \ZZ_2 \oplus \ZZ_2$.

- $n \ge 5$: $H^n = 0$.

::: pf-proof
UCT for cohomology with coefficients in $\ZZ$.
:::

:::

:::

:::

::: pf-qed
Conclusion: $Y = S^2 \cup_4 e^3$, and all homology/cohomology groups are determined.

Steps [](#moore-space-construction){.pf-ref} through [](#integer-cohomology){.pf-ref}.
:::

:::

:::
