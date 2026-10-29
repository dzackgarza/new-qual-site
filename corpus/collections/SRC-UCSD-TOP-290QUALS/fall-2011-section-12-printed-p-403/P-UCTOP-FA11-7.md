---
schema: qual/card@1
id: P-UCTOP-FA11-7
kind: problem
title: Cohomology of suspension product of lens spaces
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $L(p)$ be a space whose integral homology groups are $\ZZ, \ZZ_p, 0, \ZZ$ in dimensions 0, 1, 2, 3, and zero otherwise.
Let $\Sigma$ denote the suspension of a space.
Compute the cohomology $H^*(\Sigma L(p) \times \Sigma L(q))$.
:::

::: {.solution}

::: pf

::: {.pf-step #suspension-homology-cohomology}
Homology and cohomology of the suspension $\Sigma L(p)$:

::: pf-proof

::: pf-step
The reduced homology of the suspension satisfies $\widetilde{H}_{k+1}(\Sigma X) \cong \widetilde{H}_k(X)$.
Given $\widetilde{H}_*(L(p)) = (0, \ZZ_p, 0, \ZZ)$, the homology of $X = \Sigma L(p)$ is:
\[
H_k(X) = \begin{cases}
\ZZ & k = 0, 4, \\
\ZZ_p & k = 2, \\
0 & k = 1, 3 \text{ or } k \ge 5.
\end{cases}
\]

::: pf-proof
suspension isomorphism for reduced homology.
:::

:::

::: pf-step
By the Universal Coefficient Theorem for Cohomology, $H^k(X) \cong \operatorname{Hom}(H_k(X), \ZZ) \oplus \operatorname{Ext}(H_{k-1}(X), \ZZ)$:
- $H^0(X) \cong \ZZ$,
- $H^1(X) \cong \operatorname{Hom}(0, \ZZ) \oplus \operatorname{Ext}(\ZZ, \ZZ) = 0$,
- $H^2(X) \cong \operatorname{Hom}(\ZZ_p, \ZZ) \oplus \operatorname{Ext}(0, \ZZ) = 0$,
- $H^3(X) \cong \operatorname{Hom}(0, \ZZ) \oplus \operatorname{Ext}(\ZZ_p, \ZZ) \cong \ZZ_p$,
- $H^4(X) \cong \operatorname{Hom}(\ZZ, \ZZ) \oplus \operatorname{Ext}(0, \ZZ) \cong \ZZ$,
- $H^k(X) = 0$ for $k \ge 5$.
Symmetrically for $Y = \Sigma L(q)$, $H^*(Y) = (\ZZ, 0, 0, \ZZ_q, \ZZ, 0, \ldots)$.

::: pf-proof
Universal Coefficient Theorem for Cohomology.
:::

:::

:::

:::

::: {.pf-step #product-cohomology-kunneth}
Cohomology of the product $\Sigma L(p) \times \Sigma L(q)$ via the Künneth Formula:

::: pf-proof

::: pf-step
The Künneth formula for cohomology splits as:
\[
H^k(X \times Y) \cong \left( \bigoplus_{i+j=k} H^i(X) \otimes H^j(Y) \right) \oplus \left( \bigoplus_{i+j=k+1} \operatorname{Tor}(H^i(X), H^j(Y)) \right).
\]

::: pf-proof
Künneth Theorem for cohomology with principal ideal domain coefficients $\ZZ$.
:::

:::

::: pf-step
Evaluating each degree $k \in \{0, 1, \dots, 8\}$:
- **$k = 0$:** $H^0(X) \otimes H^0(Y) \cong \ZZ \otimes \ZZ \cong \ZZ$.
- **$k = 1$:** $0$.
- **$k = 2$:** $0$.
- **$k = 3$:** $(H^0(X) \otimes H^3(Y)) \oplus (H^3(X) \otimes H^0(Y)) \cong (\ZZ \otimes \ZZ_q) \oplus (\ZZ_p \otimes \ZZ) \cong \ZZ_p \oplus \ZZ_q$.
- **$k = 4$:** $(H^0(X) \otimes H^4(Y)) \oplus (H^4(X) \otimes H^0(Y)) \cong \ZZ \oplus \ZZ$.
- **$k = 5$:** The tensor terms vanish, and the Tor term from $i+j=6$ is $\operatorname{Tor}(H^3(X), H^3(Y)) = \operatorname{Tor}(\ZZ_p, \ZZ_q) \cong \ZZ_{\gcd(p, q)}$.
- **$k = 6$:** $H^3(X) \otimes H^3(Y) \cong \ZZ_p \otimes \ZZ_q \cong \ZZ_{\gcd(p, q)}$, with vanishing Tor.
- **$k = 7$:** $(H^3(X) \otimes H^4(Y)) \oplus (H^4(X) \otimes H^3(Y)) \cong \ZZ_p \oplus \ZZ_q$.
- **$k = 8$:** $H^4(X) \otimes H^4(Y) \cong \ZZ \otimes \ZZ \cong \ZZ$.
- **$k \ge 9$:** $H^k(X \times Y) = 0$.

::: pf-proof
direct calculation from the Künneth components.
:::

:::

:::

:::

::: pf-qed
Conclusion:
The integral cohomology groups $H^k(\Sigma L(p) \times \Sigma L(q))$ for $k = 0, 1, \dots, 8$ are:
\[
\ZZ, \quad 0, \quad 0, \quad \ZZ_p \oplus \ZZ_q, \quad \ZZ \oplus \ZZ, \quad \ZZ_{\gcd(p, q)}, \quad \ZZ_{\gcd(p, q)}, \quad \ZZ_p \oplus \ZZ_q, \quad \ZZ,
\]
and $0$ for all $k \ge 9$.

Steps [](#suspension-homology-cohomology){.pf-ref} and [](#product-cohomology-kunneth){.pf-ref}.
:::

:::

:::
