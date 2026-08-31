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

Compute the integral homology $H_*(\mathbb{RP}^2 \times \mathbb{RP}^3; \mathbb{Z})$.

::: {.solution}
<1>1. Homology groups of the factors:
<2>1. For $X = \mathbb{RP}^2$:
\[
H_0(X; \mathbb{Z}) \cong \mathbb{Z}, \quad H_1(X; \mathbb{Z}) \cong \mathbb{Z}_2, \quad H_k(X; \mathbb{Z}) = 0 \text{ for all } k \ge 2.
\]
::: {.proof}
cellular homology of $\mathbb{RP}^2$.
:::
<2>2. For $Y = \mathbb{RP}^3$:
\[
H_0(Y; \mathbb{Z}) \cong \mathbb{Z}, \quad H_1(Y; \mathbb{Z}) \cong \mathbb{Z}_2, \quad H_2(Y; \mathbb{Z}) = 0, \quad H_3(Y; \mathbb{Z}) \cong \mathbb{Z}, \quad H_k(Y; \mathbb{Z}) = 0 \text{ for all } k \ge 4.
\]
::: {.proof}
cellular homology of the orientable 3-manifold $\mathbb{RP}^3$.
:::

<1>2. The Künneth Formula:
<2>1. By the Künneth Theorem for singular homology with coefficients in a PID:
\[
H_n(X \times Y; \mathbb{Z}) \cong \bigoplus_{i+j=n} \big(H_i(X) \otimes_{\mathbb{Z}} H_j(Y)\big) \oplus \bigoplus_{i+j=n-1} \operatorname{Tor}_1^{\mathbb{Z}}(H_i(X), H_j(Y)).
\]
::: {.proof}
Künneth Theorem for product spaces over $\mathbb{Z}$.
:::

<1>3. Degree-by-degree computation:
<2>1. **Degree $n = 0$:**
- Tensor ($i+j=0$): $H_0(X) \otimes H_0(Y) \cong \mathbb{Z} \otimes \mathbb{Z} \cong \mathbb{Z}$.
- Tor: $0$.
Thus $H_0(\mathbb{RP}^2 \times \mathbb{RP}^3) \cong \mathbb{Z}$.
<2>2. **Degree $n = 1$:**
- Tensor ($i+j=1$): $(H_0(X) \otimes H_1(Y)) \oplus (H_1(X) \otimes H_0(Y)) \cong (\mathbb{Z} \otimes \mathbb{Z}_2) \oplus (\mathbb{Z}_2 \otimes \mathbb{Z}) \cong \mathbb{Z}_2 \oplus \mathbb{Z}_2$.
- Tor ($i+j=0$): $\operatorname{Tor}(\mathbb{Z}, \mathbb{Z}) = 0$.
Thus $H_1(\mathbb{RP}^2 \times \mathbb{RP}^3) \cong \mathbb{Z}_2 \oplus \mathbb{Z}_2$.
<2>3. **Degree $n = 2$:**
- Tensor ($i+j=2$): $H_1(X) \otimes H_1(Y) \cong \mathbb{Z}_2 \otimes \mathbb{Z}_2 \cong \mathbb{Z}_2$ (all other pairs vanish).
- Tor ($i+j=1$): $\operatorname{Tor}(\mathbb{Z}, \mathbb{Z}_2) \oplus \operatorname{Tor}(\mathbb{Z}_2, \mathbb{Z}) = 0$.
Thus $H_2(\mathbb{RP}^2 \times \mathbb{RP}^3) \cong \mathbb{Z}_2$.
<2>4. **Degree $n = 3$:**
- Tensor ($i+j=3$): $H_0(X) \otimes H_3(Y) \cong \mathbb{Z} \otimes \mathbb{Z} \cong \mathbb{Z}$.
- Tor ($i+j=2$): $\operatorname{Tor}(H_1(X), H_1(Y)) \cong \operatorname{Tor}(\mathbb{Z}_2, \mathbb{Z}_2) \cong \mathbb{Z}_2$.
Thus $H_3(\mathbb{RP}^2 \times \mathbb{RP}^3) \cong \mathbb{Z} \oplus \mathbb{Z}_2$.
<2>5. **Degree $n = 4$:**
- Tensor ($i+j=4$): $H_1(X) \otimes H_3(Y) \cong \mathbb{Z}_2 \otimes \mathbb{Z} \cong \mathbb{Z}_2$.
- Tor ($i+j=3$): all Tor terms involve free or zero modules, so $\operatorname{Tor} = 0$.
Thus $H_4(\mathbb{RP}^2 \times \mathbb{RP}^3) \cong \mathbb{Z}_2$.
<2>6. **Degrees $n \ge 5$:**
Both the tensor and Tor terms vanish, so $H_n(\mathbb{RP}^2 \times \mathbb{RP}^3) = 0$ for all $n \ge 5$.
::: {.proof}
<1>1 and Künneth formula algebra.
:::

<1>4. Conclusion:
The integral homology groups $H_n(\mathbb{RP}^2 \times \mathbb{RP}^3; \mathbb{Z})$ are:
\[
H_n(\mathbb{RP}^2 \times \mathbb{RP}^3; \mathbb{Z}) \cong \begin{cases}
\mathbb{Z} & n = 0, \\
\mathbb{Z}_2 \oplus \mathbb{Z}_2 & n = 1, \\
\mathbb{Z}_2 & n = 2, \\
\mathbb{Z} \oplus \mathbb{Z}_2 & n = 3, \\
\mathbb{Z}_2 & n = 4, \\
0 & n \ge 5.
\end{cases}
\]
Q.E.D.
::: {.proof}
<1>3.
:::
:::
