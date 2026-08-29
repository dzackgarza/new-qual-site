---
schema: qual/card@1
id: P-UCTOP-SU12-4
kind: problem
title: Homology of RP^2 × X where H_k(X;Z) = Z/kZ
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $X$ be a path-connected topological space whose integer homology groups in positive dimensions are:
$$H_0(X; \mathbb{Z}) \cong \mathbb{Z}, \qquad H_k(X; \mathbb{Z}) \cong \mathbb{Z}/k\mathbb{Z} \quad \text{for all } k \ge 1.$$
Compute the integer homology groups $H_n(\mathbb{RP}^2 \times X; \mathbb{Z})$ for all $n \ge 0$.
:::

::: solution
**Goal:** Compute the homology groups $H_n(\mathbb{RP}^2 \times X; \mathbb{Z})$ using the Künneth Formula for homology with integer coefficients.

<1>1. Homology of $\mathbb{RP}^2$:
    *Proof:*
    <2>1. The standard integer homology groups of the real projective plane $\mathbb{RP}^2$ are:
        $$H_0(\mathbb{RP}^2; \mathbb{Z}) \cong \mathbb{Z}, \quad H_1(\mathbb{RP}^2; \mathbb{Z}) \cong \mathbb{Z}/2\mathbb{Z}, \quad H_2(\mathbb{RP}^2; \mathbb{Z}) = 0, \quad H_i(\mathbb{RP}^2; \mathbb{Z}) = 0 \text{ for } i \ge 3.$$

<1>2. The Künneth Formula for $H_n(\mathbb{RP}^2 \times X; \mathbb{Z})$:
    *Proof:*
    <2>1. By the **Künneth Theorem in Homology**, for CW complexes:
        $$H_n(\mathbb{RP}^2 \times X; \mathbb{Z}) \cong \left( \bigoplus_{i+j=n} H_i(\mathbb{RP}^2) \otimes_\mathbb{Z} H_j(X) \right) \oplus \left( \bigoplus_{i+j=n-1} \operatorname{Tor}_1^\mathbb{Z}(H_i(\mathbb{RP}^2), H_j(X)) \right).$$
    <2>2. Since $H_i(\mathbb{RP}^2) = 0$ for $i \ge 2$ ($i \ne 0, 1$), the tensor sum simplifies to:
        $$\bigoplus_{i+j=n} H_i(\mathbb{RP}^2) \otimes H_j(X) = (H_0(\mathbb{RP}^2) \otimes H_n(X)) \oplus (H_1(\mathbb{RP}^2) \otimes H_{n-1}(X)) = (\mathbb{Z} \otimes H_n(X)) \oplus (\mathbb{Z}/2\mathbb{Z} \otimes H_{n-1}(X)).$$
    <2>3. Since $H_0(\mathbb{RP}^2) \cong \mathbb{Z}$ is free abelian, $\operatorname{Tor}(\mathbb{Z}, -) = 0$, so the Tor sum simplifies to:
        $$\bigoplus_{i+j=n-1} \operatorname{Tor}(H_i(\mathbb{RP}^2), H_j(X)) = \operatorname{Tor}(H_1(\mathbb{RP}^2), H_{n-2}(X)) = \operatorname{Tor}(\mathbb{Z}/2\mathbb{Z}, H_{n-2}(X)).$$
    <2>4. Thus, for any $n \ge 0$:
        $$H_n(\mathbb{RP}^2 \times X; \mathbb{Z}) \cong H_n(X) \oplus \left( \mathbb{Z}/2\mathbb{Z} \otimes_\mathbb{Z} H_{n-1}(X) \right) \oplus \operatorname{Tor}_1^\mathbb{Z}(\mathbb{Z}/2\mathbb{Z}, H_{n-2}(X)).$$

<1>3. Evaluation for Small Degrees ($n = 0, 1, 2$):
    *Proof:*
    <2>1. **For $n = 0$:**
        $$H_0(\mathbb{RP}^2 \times X) \cong H_0(X) \cong \mathbb{Z}.$$
    <2>2. **For $n = 1$:**
        $$H_1(\mathbb{RP}^2 \times X) \cong H_1(X) \oplus (\mathbb{Z}/2\mathbb{Z} \otimes H_0(X)) = (\mathbb{Z}/1\mathbb{Z}) \oplus (\mathbb{Z}/2\mathbb{Z} \otimes \mathbb{Z}) \cong 0 \oplus \mathbb{Z}/2\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z}.$$
    <2>3. **For $n = 2$:**
        $$H_2(\mathbb{RP}^2 \times X) \cong H_2(X) \oplus (\mathbb{Z}/2\mathbb{Z} \otimes H_1(X)) \oplus \operatorname{Tor}(\mathbb{Z}/2\mathbb{Z}, H_0(X)).$$
        Since $H_2(X) \cong \mathbb{Z}/2\mathbb{Z}$, $H_1(X) \cong 0$, and $\operatorname{Tor}(\mathbb{Z}/2, \mathbb{Z}) = 0$:
        $$H_2(\mathbb{RP}^2 \times X) \cong (\mathbb{Z}/2\mathbb{Z}) \oplus (\mathbb{Z}/2\mathbb{Z} \otimes 0) \oplus 0 \cong \mathbb{Z}/2\mathbb{Z}.$$

<1>4. General Case for $n \ge 3$:
    *Proof:*
    <2>1. For $n \ge 3$, all indices $n, n-1, n-2 \ge 1$, so:
        - $H_n(X) \cong \mathbb{Z}/n\mathbb{Z}$.
        - $H_{n-1}(X) \cong \mathbb{Z}/(n-1)\mathbb{Z}$.
        - $H_{n-2}(X) \cong \mathbb{Z}/(n-2)\mathbb{Z}$.
    <2>2. **Tensor product term:**
        $$\mathbb{Z}/2\mathbb{Z} \otimes_\mathbb{Z} \mathbb{Z}/(n-1)\mathbb{Z} \cong \mathbb{Z}/\gcd(2, n-1)\mathbb{Z} = \begin{cases} \mathbb{Z}/2\mathbb{Z} & \text{if } n \text{ is even (so } n-1 \text{ is odd, } \gcd=1 \implies 0), \\ 0 & \text{if } n \text{ is even}, \\ \mathbb{Z}/2\mathbb{Z} & \text{if } n \text{ is odd (so } n-1 \text{ is even, } \gcd=2). \end{cases}$$
        Specifically:
        $$\mathbb{Z}/2\mathbb{Z} \otimes \mathbb{Z}/(n-1)\mathbb{Z} \cong \begin{cases} 0 & \text{if } n \text{ is even}, \\ \mathbb{Z}/2\mathbb{Z} & \text{if } n \text{ is odd}. \end{cases}$$
    <2>3. **Tor term:**
        $$\operatorname{Tor}_1^\mathbb{Z}(\mathbb{Z}/2\mathbb{Z}, \mathbb{Z}/(n-2)\mathbb{Z}) \cong \mathbb{Z}/\gcd(2, n-2)\mathbb{Z} = \begin{cases} \mathbb{Z}/2\mathbb{Z} & \text{if } n \text{ is even (since } 2 \mid (n-2)), \\ 0 & \text{if } n \text{ is odd (since } 2 \nmid (n-2)). \end{cases}$$
    <2>4. Summing the two $\mathbb{Z}/2$-terms: for any $n \ge 3$, exactly one of $(n-1)$ or $(n-2)$ is even, so:
        $$(\mathbb{Z}/2\mathbb{Z} \otimes H_{n-1}(X)) \oplus \operatorname{Tor}(\mathbb{Z}/2\mathbb{Z}, H_{n-2}(X)) \cong \mathbb{Z}/2\mathbb{Z}.$$
    <2>5. Therefore, for all $n \ge 3$:
        $$H_n(\mathbb{RP}^2 \times X; \mathbb{Z}) \cong (\mathbb{Z}/n\mathbb{Z}) \oplus (\mathbb{Z}/2\mathbb{Z}).$$

<1>5. Conclusion:
    - $H_0(\mathbb{RP}^2 \times X) \cong \mathbb{Z}$
    - $H_1(\mathbb{RP}^2 \times X) \cong \mathbb{Z}/2\mathbb{Z}$
    - $H_2(\mathbb{RP}^2 \times X) \cong \mathbb{Z}/2\mathbb{Z}$
    - $H_n(\mathbb{RP}^2 \times X) \cong \mathbb{Z}/n\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}$ for all $n \ge 3$. Q.E.D.
:::
