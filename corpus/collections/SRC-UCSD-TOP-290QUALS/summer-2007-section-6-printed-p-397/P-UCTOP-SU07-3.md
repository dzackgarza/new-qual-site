---
schema: qual/card@1
id: P-UCTOP-SU07-3
kind: problem
title: Integral homology of RP^2 × RP^3
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Compute the integral homology $H_*(\RP^2 \times \RP^3; \ZZ)$.
:::

::: {.solution}

::: pf

::: {.pf-step #factor-homology-groups}
Homology groups of the factors:

::: pf-proof

::: pf-step
For $X = \RP^2$:
\[
H_0(X; \ZZ) \cong \ZZ, \quad H_1(X; \ZZ) \cong \ZZ_2, \quad H_k(X; \ZZ) = 0 \text{ for all } k \ge 2.
\]

::: pf-proof
cellular homology of $\RP^2$.
:::

:::

::: pf-step
For $Y = \RP^3$:
\[
H_0(Y; \ZZ) \cong \ZZ, \quad H_1(Y; \ZZ) \cong \ZZ_2, \quad H_2(Y; \ZZ) = 0, \quad H_3(Y; \ZZ) \cong \ZZ, \quad H_k(Y; \ZZ) = 0 \text{ for all } k \ge 4.
\]

::: pf-proof
cellular homology of the orientable 3-manifold $\RP^3$.
:::

:::

:::

:::

::: pf-step
The Künneth Formula:

::: pf-proof

::: pf-step
By the Künneth Theorem for singular homology with coefficients in a PID:
\[
H_n(X \times Y; \ZZ) \cong \bigoplus_{i+j=n} \big(H_i(X) \otimes_{\ZZ} H_j(Y)\big) \oplus \bigoplus_{i+j=n-1} \operatorname{Tor}_1^{\ZZ}(H_i(X), H_j(Y)).
\]

::: pf-proof
Künneth Theorem for product spaces over $\ZZ$.
:::

:::

:::

:::

::: {.pf-step #degree-by-degree-computation}
Degree-by-degree computation:

::: pf-proof

::: pf-step
**Degree $n = 0$:**
- Tensor ($i+j=0$): $H_0(X) \otimes H_0(Y) \cong \ZZ \otimes \ZZ \cong \ZZ$.
- Tor: $0$.
Thus $H_0(\RP^2 \times \RP^3) \cong \ZZ$.
:::

::: pf-step
**Degree $n = 1$:**
- Tensor ($i+j=1$): $(H_0(X) \otimes H_1(Y)) \oplus (H_1(X) \otimes H_0(Y)) \cong (\ZZ \otimes \ZZ_2) \oplus (\ZZ_2 \otimes \ZZ) \cong \ZZ_2 \oplus \ZZ_2$.
- Tor ($i+j=0$): $\operatorname{Tor}(\ZZ, \ZZ) = 0$.
Thus $H_1(\RP^2 \times \RP^3) \cong \ZZ_2 \oplus \ZZ_2$.
:::

::: pf-step
**Degree $n = 2$:**
- Tensor ($i+j=2$): $H_1(X) \otimes H_1(Y) \cong \ZZ_2 \otimes \ZZ_2 \cong \ZZ_2$ (all other pairs vanish).
- Tor ($i+j=1$): $\operatorname{Tor}(\ZZ, \ZZ_2) \oplus \operatorname{Tor}(\ZZ_2, \ZZ) = 0$.
Thus $H_2(\RP^2 \times \RP^3) \cong \ZZ_2$.
:::

::: pf-step
**Degree $n = 3$:**
- Tensor ($i+j=3$): $H_0(X) \otimes H_3(Y) \cong \ZZ \otimes \ZZ \cong \ZZ$.
- Tor ($i+j=2$): $\operatorname{Tor}(H_1(X), H_1(Y)) \cong \operatorname{Tor}(\ZZ_2, \ZZ_2) \cong \ZZ_2$.
Thus $H_3(\RP^2 \times \RP^3) \cong \ZZ \oplus \ZZ_2$.
:::

::: pf-step
**Degree $n = 4$:**
- Tensor ($i+j=4$): $H_1(X) \otimes H_3(Y) \cong \ZZ_2 \otimes \ZZ \cong \ZZ_2$.
- Tor ($i+j=3$): all Tor terms involve free or zero modules, so $\operatorname{Tor} = 0$.
Thus $H_4(\RP^2 \times \RP^3) \cong \ZZ_2$.
:::

::: pf-step
**Degrees $n \ge 5$:**
Both the tensor and Tor terms vanish, so $H_n(\RP^2 \times \RP^3) = 0$ for all $n \ge 5$.
:::

Step [](#factor-homology-groups){.pf-ref} and Künneth formula algebra.

:::

:::

::: pf-qed
Conclusion:
The integral homology groups $H_n(\RP^2 \times \RP^3; \ZZ)$ are:
\[
H_n(\RP^2 \times \RP^3; \ZZ) \cong \begin{cases}
\ZZ & n = 0, \\
\ZZ_2 \oplus \ZZ_2 & n = 1, \\
\ZZ_2 & n = 2, \\
\ZZ \oplus \ZZ_2 & n = 3, \\
\ZZ_2 & n = 4, \\
0 & n \ge 5.
\end{cases}
\]

Step [](#degree-by-degree-computation){.pf-ref}.
:::

:::

:::
