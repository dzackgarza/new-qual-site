---
schema: qual/card@1
id: P-UCTOP-SU07-3
kind: problem
title: 'Integral homology of $\RP^2\times\RP^3$'
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
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the three containers state why their subclaims suffice, and the 6
    degree computations that asserted their vanishing terms each carry a sentence naming which pairs are
    present and why the Tor terms vanish. The concluding answer was turned from a pf-qed, which ended
    with a bare reference to an earlier step, into an ordinary step with its own justification, and a
    stray sentence lying loose inside the degree container was removed. The homology of the factors is
    now derived from the cellular chain complexes rather than named, and the whole computation was
    re-checked: H_0 = Z, H_1 = Z/2 + Z/2, H_2 = Z/2, H_3 = Z + Z/2, H_4 = Z/2, H_n = 0 for n >= 5,
    which agrees with the Künneth formula over Z. Nothing in the statement was changed.
---

::: {.problem}
Compute the integral homology $H_*(\RP^2 \times \RP^3; \ZZ)$.
:::

::: {.solution}

::: pf

::: {.pf-step #factor-homology-groups}
Homology groups of the factors:

::: pf-proof
The first two subclaims record the homology of the two factors, which is all the Künneth formula needs.

::: pf-step
For $X = \RP^2$:
$$
H_0(X; \ZZ) \cong \ZZ, \quad H_1(X; \ZZ) \cong \ZZ_2, \quad H_k(X; \ZZ) = 0 \text{ for all } k \ge 2.
$$

::: pf-proof
The cellular chain complex of $\RP^2$ has one cell in dimensions $0$, $1$ and $2$, with the degree-$2$ map multiplying by $2$; hence $H_0=\ZZ$, $H_1=\ZZ/2$ and $H_2=0$.
:::

:::

::: pf-step
For $Y = \RP^3$:
$$
H_0(Y; \ZZ) \cong \ZZ, \quad H_1(Y; \ZZ) \cong \ZZ_2, \quad H_2(Y; \ZZ) = 0, \quad H_3(Y; \ZZ) \cong \ZZ, \quad H_k(Y; \ZZ) = 0 \text{ for all } k \ge 4.
$$

::: pf-proof
The cellular chain complex of $\RP^3$ has one cell in each dimension $0,1,2,3$, and the boundary maps alternate between multiplication by $2$ and $0$; hence $H_0=\ZZ$, $H_1=\ZZ/2$, $H_2=0$ and $H_3=\ZZ$, the last because $\RP^3$ is a closed orientable $3$-manifold.
:::

:::

:::

:::

::: pf-step
The Künneth Formula:

::: pf-proof
The single subclaim states the formula that the rest of the proof applies degree by degree.

::: pf-step
By the Künneth Theorem for singular homology with coefficients in a PID:
$$
H_n(X \times Y; \ZZ) \cong \bigoplus_{i+j=n} \big(H_i(X) \otimes_{\ZZ} H_j(Y)\big) \oplus \bigoplus_{i+j=n-1} \operatorname{Tor}_1^{\ZZ}(H_i(X), H_j(Y)).
$$

::: pf-proof
This is the Künneth theorem over the principal ideal domain $\ZZ$: for spaces whose homology is of finite type the short exact sequence splits, giving the displayed isomorphism with the Tor term one degree lower.
:::

:::

:::

:::

::: {.pf-step #degree-by-degree-computation}
Degree-by-degree computation:

::: pf-proof
The subclaims evaluate the formula in each degree, using that $\ZZ_2\otimes\ZZ_2\cong\ZZ_2$, $\ZZ\otimes A\cong A$, and that $\Tor$ vanishes against a free module.

::: pf-step
**Degree $n = 0$:**
- Tensor ($i+j=0$): $H_0(X) \otimes H_0(Y) \cong \ZZ \otimes \ZZ \cong \ZZ$.
- Tor: $0$.
Thus $H_0(\RP^2 \times \RP^3) \cong \ZZ$.

::: pf-proof
The only pair with $i+j=0$ is $(0,0)$, and $\ZZ\otimes\ZZ\cong\ZZ$; there is no pair with $i+j=-1$, so no Tor term occurs.
:::

:::

::: pf-step
**Degree $n = 1$:**
- Tensor ($i+j=1$): $(H_0(X) \otimes H_1(Y)) \oplus (H_1(X) \otimes H_0(Y)) \cong (\ZZ \otimes \ZZ_2) \oplus (\ZZ_2 \otimes \ZZ) \cong \ZZ_2 \oplus \ZZ_2$.
- Tor ($i+j=0$): $\operatorname{Tor}(\ZZ, \ZZ) = 0$.
Thus $H_1(\RP^2 \times \RP^3) \cong \ZZ_2 \oplus \ZZ_2$.

::: pf-proof
The pairs with $i+j=1$ are $(0,1)$ and $(1,0)$, each contributing $\ZZ_2$ because tensoring with $\ZZ$ changes nothing; the only pair with $i+j=0$ is $(0,0)$, and $\Tor$ of two free modules vanishes.
:::

:::

::: pf-step
**Degree $n = 2$:**
- Tensor ($i+j=2$): $H_1(X) \otimes H_1(Y) \cong \ZZ_2 \otimes \ZZ_2 \cong \ZZ_2$ (all other pairs vanish).
- Tor ($i+j=1$): $\operatorname{Tor}(\ZZ, \ZZ_2) \oplus \operatorname{Tor}(\ZZ_2, \ZZ) = 0$.
Thus $H_2(\RP^2 \times \RP^3) \cong \ZZ_2$.

::: pf-proof
Among the pairs with $i+j=2$, those involving $H_2$ vanish because $H_2$ of both factors is $0$, and $\ZZ_2\otimes\ZZ_2\cong\ZZ_2$. The pairs with $i+j=1$ are $(0,1)$ and $(1,0)$, and $\Tor$ vanishes because one argument is free.
:::

:::

::: pf-step
**Degree $n = 3$:**
- Tensor ($i+j=3$): $H_0(X) \otimes H_3(Y) \cong \ZZ \otimes \ZZ \cong \ZZ$.
- Tor ($i+j=2$): $\operatorname{Tor}(H_1(X), H_1(Y)) \cong \operatorname{Tor}(\ZZ_2, \ZZ_2) \cong \ZZ_2$.
Thus $H_3(\RP^2 \times \RP^3) \cong \ZZ \oplus \ZZ_2$.

::: pf-proof
$H_3(X)=0$ and $H_2(Y)=0$, so the only non-vanishing tensor term with $i+j=3$ is $H_0(X)\otimes H_3(Y)\cong\ZZ$. Among the pairs with $i+j=2$, the pairs involving $H_2$ vanish and $(1,1)$ gives $\Tor(\ZZ_2,\ZZ_2)\cong\ZZ_2$.
:::

:::

::: pf-step
**Degree $n = 4$:**
- Tensor ($i+j=4$): $H_1(X) \otimes H_3(Y) \cong \ZZ_2 \otimes \ZZ \cong \ZZ_2$.
- Tor ($i+j=3$): all Tor terms involve free or zero modules, so $\operatorname{Tor} = 0$.
Thus $H_4(\RP^2 \times \RP^3) \cong \ZZ_2$.

::: pf-proof
The only non-vanishing tensor term with $i+j=4$ is $H_1(X)\otimes H_3(Y)\cong\ZZ_2$, since $H_3(X)=0$ and $H_2$ of both factors vanishes. The pairs with $i+j=3$ are $(0,3)$, $(1,2)$, $(2,1)$ and $(3,0)$, and each has a free or a zero argument, so every Tor term is $0$.
:::

:::

::: pf-step
**Degrees $n \ge 5$:**
Both the tensor and Tor terms vanish, so $H_n(\RP^2 \times \RP^3) = 0$ for all $n \ge 5$.

::: pf-proof
The homology of $X$ vanishes above degree $2$ and that of $Y$ above degree $3$, so no pair with $i+j=n$ or $i+j=n-1$ survives once $n\ge5$; at $n=5$ the candidates $(2,3)$ and $(3,2)$ have a vanishing factor, and the Tor pairs with $i+j=4$ are $(1,3)$ and $(3,1)$, where one argument is free, and $(2,2)$, where one is zero.
:::

:::

:::

:::

::: pf-step
Conclusion:
The integral homology groups $H_n(\RP^2 \times \RP^3; \ZZ)$ are
$$
H_n(\RP^2 \times \RP^3; \ZZ) \cong \begin{cases}
\ZZ & n = 0, \\
\ZZ_2 \oplus \ZZ_2 & n = 1, \\
\ZZ_2 & n = 2, \\
\ZZ \oplus \ZZ_2 & n = 3, \\
\ZZ_2 & n = 4, \\
0 & n \ge 5.
\end{cases}
$$

::: pf-proof
Collecting the six degree computations of step [](#degree-by-degree-computation){.pf-ref} gives the displayed list, and the degrees not listed are those with $n\ge5$, where the group vanishes.
:::

:::

:::

:::
