---
schema: qual/card@1
id: P-TOPF02C
kind: problem
title: "Construct a space with prescribed homology and compute the homology of its product with RP^2"
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

::: problem
(a) Construct a space $Y$ with the following properties:
$$
H_k(Y; \mathbb{Z}) = \begin{cases} \mathbb{Z}_4 & \text{if } k = 2 \\ \mathbb{Z} & \text{if } k = 0 \\ 0 & \text{otherwise.} \end{cases}
$$

(b) Compute $H_*(\mathbb{RP}^2 \times Y; \mathbb{Z}_2)$, $H_*(\mathbb{RP}^2 \times Y; \mathbb{Z})$, and $H^*(\mathbb{RP}^2 \times Y; \mathbb{Z})$.
:::

::: {.solution}
<1>1. Part (a): Construction of Moore space $Y = M(\mathbb{Z}_4, 2)$:
<2>1. Define $Y = S^2 \cup_f e^3$, where the attaching map $f: \partial e^3 = S^2 \to S^2$ has topological degree $4$.
::: {.proof}
definition of Moore space.
:::
<2>2. The cellular chain complex of $Y$ is:
\[
C_3 = \mathbb{Z}\langle e^3 \rangle, \quad C_2 = \mathbb{Z}\langle e^2 \rangle, \quad C_1 = 0, \quad C_0 = \mathbb{Z}\langle e^0 \rangle,
\]
with boundary maps $d_3(e^3) = 4 e^2$, $d_2 = 0$, and $d_1 = 0$.
::: {.proof}
degree of attaching map on 2-cells.
:::
<2>3. The resulting integral homology groups are:
\[
H_0(Y; \mathbb{Z}) \cong \mathbb{Z}, \quad H_1(Y; \mathbb{Z}) = 0, \quad H_2(Y; \mathbb{Z}) = \ker(d_2)/\operatorname{im}(d_3) \cong \mathbb{Z}/4\mathbb{Z} = \mathbb{Z}_4, \quad H_k(Y; \mathbb{Z}) = 0 \ (k \ge 3).
\]
::: {.proof}
homology of cellular chain complex.
:::

<1>2. Part (b)(i): Integer homology $H_*(\mathbb{RP}^2 \times Y; \mathbb{Z})$:
<2>1. Recall $H_*(\mathbb{RP}^2; \mathbb{Z}) = (\mathbb{Z}, \mathbb{Z}_2, 0, \dots)$.
::: {.proof}
standard homology of real projective plane.
:::
<2>2. Apply the Künneth Theorem $H_n(X \times Y) \cong \bigoplus_{i+j=n} (H_i \otimes H_j) \oplus \bigoplus_{i+j=n-1} \operatorname{Tor}_1^{\mathbb{Z}}(H_i, H_j)$:
- $n = 0$: $H_0 \otimes H_0 \cong \mathbb{Z} \otimes \mathbb{Z} \cong \mathbb{Z}$.
- $n = 1$: $H_1 \otimes H_0 \cong \mathbb{Z}_2 \otimes \mathbb{Z} \cong \mathbb{Z}_2$.
- $n = 2$: $H_0 \otimes H_2 \cong \mathbb{Z} \otimes \mathbb{Z}_4 \cong \mathbb{Z}_4$.
- $n = 3$: $(H_1 \otimes H_2) \oplus \operatorname{Tor}_1^{\mathbb{Z}}(H_1, H_2) \cong (\mathbb{Z}_2 \otimes \mathbb{Z}_4) \oplus \operatorname{Tor}(\mathbb{Z}_2, \mathbb{Z}_4) \cong \mathbb{Z}_2 \oplus \mathbb{Z}_2$.
- $n \ge 4$: $H_n = 0$.
::: {.proof}
Künneth Theorem for integral homology.
:::

<1>3. Part (b)(ii): Mod 2 homology $H_*(\mathbb{RP}^2 \times Y; \mathbb{Z}_2)$:
<2>1. By the Universal Coefficient Theorem, $H_*(\mathbb{RP}^2; \mathbb{Z}_2) = (\mathbb{Z}_2, \mathbb{Z}_2, \mathbb{Z}_2, 0, \dots)$ and $H_*(Y; \mathbb{Z}_2) = (\mathbb{Z}_2, 0, \mathbb{Z}_2, \mathbb{Z}_2, 0, \dots)$.
::: {.proof}
UCT over $\mathbb{Z}_2$.
:::
<2>2. By the Künneth Theorem over the field $\mathbb{Z}_2$, $H_n(\mathbb{RP}^2 \times Y; \mathbb{Z}_2) \cong \bigoplus_{i+j=n} H_i(\mathbb{RP}^2; \mathbb{Z}_2) \otimes_{\mathbb{Z}_2} H_j(Y; \mathbb{Z}_2)$:
- $n = 0$: $H_0 \otimes H_0 \cong \mathbb{Z}_2$.
- $n = 1$: $H_1 \otimes H_0 \cong \mathbb{Z}_2$.
- $n = 2$: $(H_0 \otimes H_2) \oplus (H_2 \otimes H_0) \cong \mathbb{Z}_2 \oplus \mathbb{Z}_2$.
- $n = 3$: $(H_0 \otimes H_3) \oplus (H_1 \otimes H_2) \cong \mathbb{Z}_2 \oplus \mathbb{Z}_2$.
- $n = 4$: $(H_1 \otimes H_3) \oplus (H_2 \otimes H_2) \cong \mathbb{Z}_2 \oplus \mathbb{Z}_2$.
- $n = 5$: $H_2 \otimes H_3 \cong \mathbb{Z}_2$.
- $n \ge 6$: $H_n = 0$.
::: {.proof}
field Künneth formula.
:::

<1>4. Part (b)(iii): Integer cohomology $H^*(\mathbb{RP}^2 \times Y; \mathbb{Z})$:
<2>1. By the Universal Coefficient Theorem for cohomology, $H^n(X; \mathbb{Z}) \cong \operatorname{Free}(H_n(X)) \oplus \operatorname{Tors}(H_{n-1}(X))$:
- $n = 0$: $\operatorname{Free}(H_0) \cong \mathbb{Z}$.
- $n = 1$: $\operatorname{Free}(H_1) \oplus \operatorname{Tors}(H_0) = 0 \oplus 0 = 0$.
- $n = 2$: $\operatorname{Free}(H_2) \oplus \operatorname{Tors}(H_1) = 0 \oplus \mathbb{Z}_2 \cong \mathbb{Z}_2$.
- $n = 3$: $\operatorname{Free}(H_3) \oplus \operatorname{Tors}(H_2) = 0 \oplus \mathbb{Z}_4 \cong \mathbb{Z}_4$.
- $n = 4$: $\operatorname{Free}(H_4) \oplus \operatorname{Tors}(H_3) = 0 \oplus (\mathbb{Z}_2 \oplus \mathbb{Z}_2) \cong \mathbb{Z}_2 \oplus \mathbb{Z}_2$.
- $n \ge 5$: $H^n = 0$.
::: {.proof}
UCT for cohomology with coefficients in $\mathbb{Z}$.
:::

<1>5. Conclusion:
$Y = S^2 \cup_4 e^3$, and all homology/cohomology groups are determined. Q.E.D.
::: {.proof}
<1>1 through <1>4.
:::
:::
