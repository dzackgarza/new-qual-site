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

Let $L(p)$ be a space whose integral homology groups are $\mathbb{Z}, \mathbb{Z}_p, 0, \mathbb{Z}$ in dimensions 0, 1, 2, 3, and zero otherwise.
Let $\Sigma$ denote the suspension of a space.
Compute the cohomology $H^*(\Sigma L(p) \times \Sigma L(q))$.

::: {.solution}
<1>1. Homology and cohomology of the suspension $\Sigma L(p)$:
<2>1. The reduced homology of the suspension satisfies $\widetilde{H}_{k+1}(\Sigma X) \cong \widetilde{H}_k(X)$.
Given $\widetilde{H}_*(L(p)) = (0, \mathbb{Z}_p, 0, \mathbb{Z})$, the homology of $X = \Sigma L(p)$ is:
\[
H_k(X) = \begin{cases}
\mathbb{Z} & k = 0, 4, \\
\mathbb{Z}_p & k = 2, \\
0 & k = 1, 3 \text{ or } k \ge 5.
\end{cases}
\]
::: {.proof}
suspension isomorphism for reduced homology.
:::
<2>2. By the Universal Coefficient Theorem for Cohomology, $H^k(X) \cong \operatorname{Hom}(H_k(X), \mathbb{Z}) \oplus \operatorname{Ext}(H_{k-1}(X), \mathbb{Z})$:
- $H^0(X) \cong \mathbb{Z}$,
- $H^1(X) \cong \operatorname{Hom}(0, \mathbb{Z}) \oplus \operatorname{Ext}(\mathbb{Z}, \mathbb{Z}) = 0$,
- $H^2(X) \cong \operatorname{Hom}(\mathbb{Z}_p, \mathbb{Z}) \oplus \operatorname{Ext}(0, \mathbb{Z}) = 0$,
- $H^3(X) \cong \operatorname{Hom}(0, \mathbb{Z}) \oplus \operatorname{Ext}(\mathbb{Z}_p, \mathbb{Z}) \cong \mathbb{Z}_p$,
- $H^4(X) \cong \operatorname{Hom}(\mathbb{Z}, \mathbb{Z}) \oplus \operatorname{Ext}(0, \mathbb{Z}) \cong \mathbb{Z}$,
- $H^k(X) = 0$ for $k \ge 5$.
Symmetrically for $Y = \Sigma L(q)$, $H^*(Y) = (\mathbb{Z}, 0, 0, \mathbb{Z}_q, \mathbb{Z}, 0, \ldots)$.
::: {.proof}
Universal Coefficient Theorem for Cohomology.
:::

<1>2. Cohomology of the product $\Sigma L(p) \times \Sigma L(q)$ via the Künneth Formula:
<2>1. The Künneth formula for cohomology splits as:
\[
H^k(X \times Y) \cong \left( \bigoplus_{i+j=k} H^i(X) \otimes H^j(Y) \right) \oplus \left( \bigoplus_{i+j=k+1} \operatorname{Tor}(H^i(X), H^j(Y)) \right).
\]
::: {.proof}
Künneth Theorem for cohomology with principal ideal domain coefficients $\mathbb{Z}$.
:::
<2>2. Evaluating each degree $k \in \{0, 1, \dots, 8\}$:
- **$k = 0$:** $H^0(X) \otimes H^0(Y) \cong \mathbb{Z} \otimes \mathbb{Z} \cong \mathbb{Z}$.
- **$k = 1$:** $0$.
- **$k = 2$:** $0$.
- **$k = 3$:** $(H^0(X) \otimes H^3(Y)) \oplus (H^3(X) \otimes H^0(Y)) \cong (\mathbb{Z} \otimes \mathbb{Z}_q) \oplus (\mathbb{Z}_p \otimes \mathbb{Z}) \cong \mathbb{Z}_p \oplus \mathbb{Z}_q$.
- **$k = 4$:** $(H^0(X) \otimes H^4(Y)) \oplus (H^4(X) \otimes H^0(Y)) \cong \mathbb{Z} \oplus \mathbb{Z}$.
- **$k = 5$:** The tensor terms vanish, and the Tor term from $i+j=6$ is $\operatorname{Tor}(H^3(X), H^3(Y)) = \operatorname{Tor}(\mathbb{Z}_p, \mathbb{Z}_q) \cong \mathbb{Z}_{\gcd(p, q)}$.
- **$k = 6$:** $H^3(X) \otimes H^3(Y) \cong \mathbb{Z}_p \otimes \mathbb{Z}_q \cong \mathbb{Z}_{\gcd(p, q)}$, with vanishing Tor.
- **$k = 7$:** $(H^3(X) \otimes H^4(Y)) \oplus (H^4(X) \otimes H^3(Y)) \cong \mathbb{Z}_p \oplus \mathbb{Z}_q$.
- **$k = 8$:** $H^4(X) \otimes H^4(Y) \cong \mathbb{Z} \otimes \mathbb{Z} \cong \mathbb{Z}$.
- **$k \ge 9$:** $H^k(X \times Y) = 0$.
::: {.proof}
direct calculation from the Künneth components.
:::

<1>3. Conclusion:
The integral cohomology groups $H^k(\Sigma L(p) \times \Sigma L(q))$ for $k = 0, 1, \dots, 8$ are:
\[
\mathbb{Z}, \quad 0, \quad 0, \quad \mathbb{Z}_p \oplus \mathbb{Z}_q, \quad \mathbb{Z} \oplus \mathbb{Z}, \quad \mathbb{Z}_{\gcd(p, q)}, \quad \mathbb{Z}_{\gcd(p, q)}, \quad \mathbb{Z}_p \oplus \mathbb{Z}_q, \quad \mathbb{Z},
\]
and $0$ for all $k \ge 9$. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
