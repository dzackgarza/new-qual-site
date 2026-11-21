---
schema: qual/card@1
id: P-TOPF19C
kind: problem
title: 'Integral homology of $\RP^2\times\RP^2$'
classification:
  areas:
  - topology
  topics:
  - Homology
  - Projective Spaces
  - Künneth Formula
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained exam assets/attachments/MATH-290A-Exam-Fall-2019.pdf,
    problem 3: "Compute the integer homology H_*(RP^2 x RP^2; Z)." The card
    agrees.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    The computation is correct. The factor has H_0 = Z, H_1 = Z/2 and H_k = 0
    above, and the Kunneth sequence over Z splits into the tensor summands in
    degree n and the Tor summands in degree n-1. Degree 0 is Z; degree 1 is
    (Z tensor Z/2) + (Z/2 tensor Z) = (Z/2)^2 with the Tor term trivial; degree
    2 is Z/2 tensor Z/2 = Z/2 with both Tor terms trivial because one factor is
    Z; degree 3 has no tensor term and Tor(Z/2, Z/2) = Z/2; above that
    everything vanishes. The Euler characteristic checks: only H_0 has a free
    part, giving 1, which is chi(RP^2)^2. Nothing was changed.
---

::: {.problem}
Compute the integer homology $H_*(\RP^2 \times \RP^2; \ZZ)$.
:::

::: {.solution}

::: pf

::: pf-step

Homology of the factor space $\RP^2$:

::: pf-proof

::: pf-step

The integer homology of the real projective plane $\RP^2$ is:
$$
H_k(\RP^2; \ZZ) \cong \begin{cases}
\ZZ & k = 0, \\
\ZZ_2 & k = 1, \\
0 & k \ge 2.
\end{cases}
$$

::: pf-proof

standard cellular homology of $\RP^2$ ($C_2 \xrightarrow{2} C_1 \xrightarrow{0} C_0$).

:::

:::

:::

:::

::: pf-step

The Künneth Formula for homology:

::: pf-proof

::: pf-step

By the Künneth Theorem for product spaces over PID $\ZZ$, there is a split short exact sequence:
$$
0 \to \bigoplus_{i+j=n} H_i(\RP^2) \otimes_{\ZZ} H_j(\RP^2) \to H_n(\RP^2 \times \RP^2; \ZZ) \to \bigoplus_{i+j=n-1} \operatorname{Tor}_1^{\ZZ}(H_i(\RP^2), H_j(\RP^2)) \to 0.
$$

::: pf-proof

Künneth Theorem for topological spaces.

:::

:::

:::

:::

::: {.pf-step #s3}

Computation of each degree $n$:

::: pf-proof

::: pf-step

**Degree $n = 0$:**
$$
\bigoplus_{i+j=0} H_i \otimes H_j = H_0 \otimes H_0 \cong \ZZ \otimes \ZZ \cong \ZZ, \quad \text{Tor term} = 0.
$$
Thus $H_0(\RP^2 \times \RP^2) \cong \ZZ$.

::: pf-proof

connected space has $H_0 \cong \ZZ$.

:::

:::

::: pf-step

**Degree $n = 1$:**
$$
\bigoplus_{i+j=1} H_i \otimes H_j = (H_0 \otimes H_1) \oplus (H_1 \otimes H_0) \cong (\ZZ \otimes \ZZ_2) \oplus (\ZZ_2 \otimes \ZZ) \cong \ZZ_2 \oplus \ZZ_2.
$$
The Tor term is $\operatorname{Tor}(H_0, H_0) = \operatorname{Tor}(\ZZ, \ZZ) = 0$.
Thus $H_1(\RP^2 \times \RP^2) \cong \ZZ_2 \oplus \ZZ_2$.

::: pf-proof

tensor product with $\ZZ$.

:::

:::

::: pf-step

**Degree $n = 2$:**
$$
\bigoplus_{i+j=2} H_i \otimes H_j = (H_0 \otimes H_2) \oplus (H_1 \otimes H_1) \oplus (H_2 \otimes H_0) = 0 \oplus (\ZZ_2 \otimes \ZZ_2) \oplus 0 \cong \ZZ_2.
$$
The Tor term is $\operatorname{Tor}(H_0, H_1) \oplus \operatorname{Tor}(H_1, H_0) \cong \operatorname{Tor}(\ZZ, \ZZ_2) \oplus \operatorname{Tor}(\ZZ_2, \ZZ) = 0$.
Thus $H_2(\RP^2 \times \RP^2) \cong \ZZ_2$.

::: pf-proof

$\ZZ_2 \otimes \ZZ_2 \cong \ZZ_2$ and $\ZZ$ is torsion-free.

:::

:::

::: pf-step

**Degree $n = 3$:**
The tensor term is $\bigoplus_{i+j=3} H_i \otimes H_j = 0$ since $H_k = 0$ for all $k \ge 2$.
The Tor term is:
$$
\bigoplus_{i+j=2} \operatorname{Tor}_1^{\ZZ}(H_i, H_j) = \operatorname{Tor}_1^{\ZZ}(H_1, H_1) \cong \operatorname{Tor}_1^{\ZZ}(\ZZ_2, \ZZ_2) \cong \ZZ_2.
$$
Thus $H_3(\RP^2 \times \RP^2) \cong \ZZ_2$.

::: pf-proof

$\operatorname{Tor}_1^{\ZZ}(\ZZ_m, \ZZ_n) \cong \ZZ_{\gcd(m,n)}$.

:::

:::

::: pf-step

**Degree $n \ge 4$:**
Both tensor and Tor terms vanish because all higher homology groups vanish.
Thus $H_n(\RP^2 \times \RP^2) = 0$ for all $n \ge 4$.

::: pf-proof

dimension and Künneth vanishings.

:::

:::

:::

:::

::: pf-step

Conclusion:
$$
H_n(\RP^2 \times \RP^2; \ZZ) \cong \begin{cases}
\ZZ & n = 0, \\
\ZZ_2 \oplus \ZZ_2 & n = 1, \\
\ZZ_2 & n = 2, \\
\ZZ_2 & n = 3, \\
0 & n \ge 4.
\end{cases}
$$
Q.E.D.

::: pf-proof

Step [](#s3){.pf-ref}.

:::

:::

:::

:::

::: {.remark title="Variations"}
The Fall 2020 exam asks for $H_k$ for all $k \geq 0$ and requires the computation of $H_k(\RP^2;\ZZ)$ to be shown.
:::
