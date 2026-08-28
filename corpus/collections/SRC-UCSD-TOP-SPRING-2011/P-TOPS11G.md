---
schema: qual/card@1
id: P-TOPS11G
kind: problem
title: "Cohomology of the product of suspensions of lens space homology spaces"
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Suspensions
  - Lens Spaces
  - Künneth Formula
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: problem
Let $L(p)$ be a space whose integral homology groups are $\mathbb{Z}$, $\mathbb{Z}_p$, $0$, $\mathbb{Z}$ in dimensions $0$, $1$, $2$, $3$, and zero otherwise.
Let $\Sigma$ denote the suspension of a space.
Compute the cohomology $H^*(\Sigma L(p) \times \Sigma L(q); \mathbb{Z})$, where $p$ and $q$ are coprime.
:::

::: solution
**Goal:** Compute the integral cohomology groups $H^k(\Sigma L(p) \times \Sigma L(q); \mathbb{Z})$ for all $k \ge 0$, where $\gcd(p, q) = 1$.

<1>1. Homology and cohomology of the suspension $\Sigma L(p)$:
    For $X = \Sigma L(p)$, the suspension isomorphism on reduced homology $\widetilde{H}_{n+1}(\Sigma Y) \cong \widetilde{H}_n(Y)$ yields:
    $$H_0(X) = \mathbb{Z}, \quad H_1(X) = 0, \quad H_2(X) = \mathbb{Z}_p, \quad H_3(X) = 0, \quad H_4(X) = \mathbb{Z}, \quad H_n(X) = 0 \text{ for } n \ge 5.$$
    By the Universal Coefficient Theorem for cohomology, $H^k(X; \mathbb{Z}) \cong \operatorname{Hom}(H_k(X), \mathbb{Z}) \oplus \operatorname{Ext}(H_{k-1}(X), \mathbb{Z})$:
    $$H^0(X) = \mathbb{Z}, \quad H^1(X) = 0, \quad H^2(X) = 0, \quad H^3(X) = \mathbb{Z}_p, \quad H^4(X) = \mathbb{Z}, \quad H^k(X) = 0 \text{ for } k \ge 5.$$
    Similarly, for $Y = \Sigma L(q)$:
    $$H^0(Y) = \mathbb{Z}, \quad H^1(Y) = 0, \quad H^2(Y) = 0, \quad H^3(Y) = \mathbb{Z}_q, \quad H^4(Y) = \mathbb{Z}, \quad H^k(Y) = 0 \text{ for } k \ge 5.$$

<1>2. Künneth formula for cohomology:
    Since $X$ and $Y$ have finitely generated cohomology in each dimension, the Künneth formula for cohomology with $\mathbb{Z}$-coefficients states:
    $$0 \to \bigoplus_{i+j=k} H^i(X) \otimes_\mathbb{Z} H^j(Y) \to H^k(X \times Y; \mathbb{Z}) \to \bigoplus_{i+j=k+1} \operatorname{Tor}_1^\mathbb{Z}(H^i(X), H^j(Y)) \to 0.$$

<1>3. Vanishing of all Tor terms:
    For all $k \ge 0$, $\bigoplus_{i+j=k+1} \operatorname{Tor}_1^\mathbb{Z}(H^i(X), H^j(Y)) = 0$.
    *Proof:*
    <2>1. $\operatorname{Tor}_1^\mathbb{Z}(\mathbb{Z}, G) = 0$ for any abelian group $G$.
    <2>2. The only non-free cohomology groups are $H^3(X) \cong \mathbb{Z}_p$ and $H^3(Y) \cong \mathbb{Z}_q$.
    <2>3. The only potential nonzero Tor term occurs at $i = j = 3$, giving $\operatorname{Tor}_1^\mathbb{Z}(\mathbb{Z}_p, \mathbb{Z}_q) \cong \mathbb{Z}_{\gcd(p, q)}$.
    <2>4. Since $p$ and $q$ are coprime, $\gcd(p, q) = 1$, so $\operatorname{Tor}_1^\mathbb{Z}(\mathbb{Z}_p, \mathbb{Z}_q) = 0$.
    <2>5. Thus all Tor terms vanish, giving an isomorphism $H^k(X \times Y; \mathbb{Z}) \cong \bigoplus_{i+j=k} H^i(X) \otimes_\mathbb{Z} H^j(Y)$.

<1>4. Computation of direct sum of tensor products by dimension:
    *Proof:*
    <2>1. $k = 0$: $H^0(X) \otimes H^0(Y) = \mathbb{Z} \otimes \mathbb{Z} \cong \mathbb{Z}$.
    <2>2. $k = 1$: No non-zero pairs $(i, j)$ with $i+j=1$, so $H^1 = 0$.
    <2>3. $k = 2$: No non-zero pairs with $i+j=2$, so $H^2 = 0$.
    <2>4. $k = 3$: $(H^0(X) \otimes H^3(Y)) \oplus (H^3(X) \otimes H^0(Y)) = (\mathbb{Z} \otimes \mathbb{Z}_q) \oplus (\mathbb{Z}_p \otimes \mathbb{Z}) \cong \mathbb{Z}_q \oplus \mathbb{Z}_p \cong \mathbb{Z}_{pq}$ (by Chinese Remainder Theorem).
    <2>5. $k = 4$: $(H^0(X) \otimes H^4(Y)) \oplus (H^4(X) \otimes H^0(Y)) = (\mathbb{Z} \otimes \mathbb{Z}) \oplus (\mathbb{Z} \otimes \mathbb{Z}) \cong \mathbb{Z} \oplus \mathbb{Z}$.
    <2>6. $k = 5$: No non-zero pairs with $i+j=5$, so $H^5 = 0$.
    <2>7. $k = 6$: $H^3(X) \otimes H^3(Y) = \mathbb{Z}_p \otimes \mathbb{Z}_q \cong \mathbb{Z}_{\gcd(p, q)} = 0$.
    <2>8. $k = 7$: $(H^3(X) \otimes H^4(Y)) \oplus (H^4(X) \otimes H^3(Y)) = (\mathbb{Z}_p \otimes \mathbb{Z}) \oplus (\mathbb{Z} \otimes \mathbb{Z}_q) \cong \mathbb{Z}_p \oplus \mathbb{Z}_q \cong \mathbb{Z}_{pq}$.
    <2>9. $k = 8$: $H^4(X) \otimes H^4(Y) = \mathbb{Z} \otimes \mathbb{Z} \cong \mathbb{Z}$.
    <2>10. $k \ge 9$: $H^k = 0$.

<1>5. Conclusion:
    $$H^k(\Sigma L(p) \times \Sigma L(q); \mathbb{Z}) \cong \begin{cases}
    \mathbb{Z} & k = 0, 8, \\
    \mathbb{Z} \oplus \mathbb{Z} & k = 4, \\
    \mathbb{Z}_{pq} & k = 3, 7, \\
    0 & k = 1, 2, 5, 6 \text{ or } k \ge 9.
    \end{cases}$$
    Q.E.D.
:::
