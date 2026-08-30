---
schema: qual/card@1
id: P-TOPF19C
kind: problem
title: "Integer homology of RP^2 x RP^2"
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
---

::: problem
Compute the integer homology $H_*(\mathbb{RP}^2 \times \mathbb{RP}^2; \mathbb{Z})$.
:::

::: {.solution}
<1>1. Homology of the factor space $\mathbb{RP}^2$:
<2>1. The integer homology of the real projective plane $\mathbb{RP}^2$ is:
\[
H_k(\mathbb{RP}^2; \mathbb{Z}) \cong \begin{cases}
\mathbb{Z} & k = 0, \\
\mathbb{Z}_2 & k = 1, \\
0 & k \ge 2.
\end{cases}
\]
Proof: standard cellular homology of $\mathbb{RP}^2$ ($C_2 \xrightarrow{2} C_1 \xrightarrow{0} C_0$).

<1>2. The Künneth Formula for homology:
<2>1. By the Künneth Theorem for product spaces over PID $\mathbb{Z}$, there is a split short exact sequence:
\[
0 \to \bigoplus_{i+j=n} H_i(\mathbb{RP}^2) \otimes_{\mathbb{Z}} H_j(\mathbb{RP}^2) \to H_n(\mathbb{RP}^2 \times \mathbb{RP}^2; \mathbb{Z}) \to \bigoplus_{i+j=n-1} \operatorname{Tor}_1^{\mathbb{Z}}(H_i(\mathbb{RP}^2), H_j(\mathbb{RP}^2)) \to 0.
\]
Proof: Künneth Theorem for topological spaces.

<1>3. Computation of each degree $n$:
<2>1. **Degree $n = 0$:**
\[
\bigoplus_{i+j=0} H_i \otimes H_j = H_0 \otimes H_0 \cong \mathbb{Z} \otimes \mathbb{Z} \cong \mathbb{Z}, \quad \text{Tor term} = 0.
\]
Thus $H_0(\mathbb{RP}^2 \times \mathbb{RP}^2) \cong \mathbb{Z}$.
Proof: connected space has $H_0 \cong \mathbb{Z}$.
<2>2. **Degree $n = 1$:**
\[
\bigoplus_{i+j=1} H_i \otimes H_j = (H_0 \otimes H_1) \oplus (H_1 \otimes H_0) \cong (\mathbb{Z} \otimes \mathbb{Z}_2) \oplus (\mathbb{Z}_2 \otimes \mathbb{Z}) \cong \mathbb{Z}_2 \oplus \mathbb{Z}_2.
\]
The Tor term is $\operatorname{Tor}(H_0, H_0) = \operatorname{Tor}(\mathbb{Z}, \mathbb{Z}) = 0$.
Thus $H_1(\mathbb{RP}^2 \times \mathbb{RP}^2) \cong \mathbb{Z}_2 \oplus \mathbb{Z}_2$.
Proof: tensor product with $\mathbb{Z}$.
<2>3. **Degree $n = 2$:**
\[
\bigoplus_{i+j=2} H_i \otimes H_j = (H_0 \otimes H_2) \oplus (H_1 \otimes H_1) \oplus (H_2 \otimes H_0) = 0 \oplus (\mathbb{Z}_2 \otimes \mathbb{Z}_2) \oplus 0 \cong \mathbb{Z}_2.
\]
The Tor term is $\operatorname{Tor}(H_0, H_1) \oplus \operatorname{Tor}(H_1, H_0) \cong \operatorname{Tor}(\mathbb{Z}, \mathbb{Z}_2) \oplus \operatorname{Tor}(\mathbb{Z}_2, \mathbb{Z}) = 0$.
Thus $H_2(\mathbb{RP}^2 \times \mathbb{RP}^2) \cong \mathbb{Z}_2$.
Proof: $\mathbb{Z}_2 \otimes \mathbb{Z}_2 \cong \mathbb{Z}_2$ and $\mathbb{Z}$ is torsion-free.
<2>4. **Degree $n = 3$:**
The tensor term is $\bigoplus_{i+j=3} H_i \otimes H_j = 0$ since $H_k = 0$ for all $k \ge 2$.
The Tor term is:
\[
\bigoplus_{i+j=2} \operatorname{Tor}_1^{\mathbb{Z}}(H_i, H_j) = \operatorname{Tor}_1^{\mathbb{Z}}(H_1, H_1) \cong \operatorname{Tor}_1^{\mathbb{Z}}(\mathbb{Z}_2, \mathbb{Z}_2) \cong \mathbb{Z}_2.
\]
Thus $H_3(\mathbb{RP}^2 \times \mathbb{RP}^2) \cong \mathbb{Z}_2$.
Proof: $\operatorname{Tor}_1^{\mathbb{Z}}(\mathbb{Z}_m, \mathbb{Z}_n) \cong \mathbb{Z}_{\gcd(m,n)}$.
<2>5. **Degree $n \ge 4$:**
Both tensor and Tor terms vanish because all higher homology groups vanish.
Thus $H_n(\mathbb{RP}^2 \times \mathbb{RP}^2) = 0$ for all $n \ge 4$.
Proof: dimension and Künneth vanishings.

<1>4. Conclusion:
\[
H_n(\mathbb{RP}^2 \times \mathbb{RP}^2; \mathbb{Z}) \cong \begin{cases}
\mathbb{Z} & n = 0, \\
\mathbb{Z}_2 \oplus \mathbb{Z}_2 & n = 1, \\
\mathbb{Z}_2 & n = 2, \\
\mathbb{Z}_2 & n = 3, \\
0 & n \ge 4.
\end{cases}
\]
Q.E.D.
Proof: <1>3.
:::
