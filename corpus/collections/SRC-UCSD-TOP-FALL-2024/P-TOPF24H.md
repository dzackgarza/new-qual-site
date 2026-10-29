---
schema: qual/card@1
id: P-TOPF24H
kind: problem
title: $\operatorname{Tor}(\ZZ\oplus\ZZ_4,\ZZ_6\oplus\ZZ_8)$
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
Compute $\operatorname{Tor}(\ZZ \oplus \ZZ_4, \ZZ_6 \oplus \ZZ_8)$.
:::

::: {.solution}
::: pf

::: pf-step
Tor of cyclic abelian groups via projective resolutions:

::: pf-proof

::: pf-step
For any abelian group $A$, since $\ZZ$ is a free (hence projective) $\ZZ$-module, $\operatorname{Tor}_1^\ZZ(\ZZ, A) = 0$.
:::

::: pf-step
For cyclic groups $\ZZ_n = \ZZ/n\ZZ$ and $\ZZ_m = \ZZ/m\ZZ$, consider the standard free resolution of $\ZZ_n$: $$0 \to \ZZ \xrightarrow{\times n} \ZZ \to \ZZ/n\ZZ \to 0.$$
:::

::: pf-step
Applying the functor $- \otimes_\ZZ \ZZ/m\ZZ$ yields the exact sequence $$0 \to \operatorname{Tor}_1^\ZZ(\ZZ_n, \ZZ_m) \to \ZZ \otimes \ZZ_m \xrightarrow{n \otimes \operatorname{id}} \ZZ \otimes \ZZ_m \to \ZZ_n \otimes \ZZ_m \to 0.$$
:::

::: pf-step
Identifying $\ZZ \otimes \ZZ_m \cong \ZZ_m$, the map is multiplication by $n$ on $\ZZ/m\ZZ$: $$\operatorname{Tor}_1^\ZZ(\ZZ_n, \ZZ_m) \cong \ker(\ZZ/m\ZZ \xrightarrow{\times n} \ZZ/m\ZZ) = \{x \in \ZZ/m\ZZ : nx \equiv 0 \pmod m\}.$$
:::

::: pf-step
The elements satisfying $nx \equiv 0 \pmod m$ form a cyclic subgroup of $\ZZ/m\ZZ$ of order $\gcd(n, m)$, so $$\operatorname{Tor}_1^\ZZ(\ZZ_n, \ZZ_m) \cong \ZZ/\gcd(n, m)\ZZ.$$
:::

:::

:::

::: pf-step
Additivity of Tor across direct sums:

::: pf-proof

::: pf-step
The Tor functor commutes with arbitrary direct sums in each variable: $$\operatorname{Tor}_1^\ZZ\left( \bigoplus_i A_i, \bigoplus_j B_j \right) \cong \bigoplus_{i, j} \operatorname{Tor}_1^\ZZ(A_i, B_j).$$
:::

::: pf-step
Expanding the given expression: $$\operatorname{Tor}_1^\ZZ(\ZZ \oplus \ZZ_4, \ZZ_6 \oplus \ZZ_8) \cong \operatorname{Tor}(\ZZ, \ZZ_6) \oplus \operatorname{Tor}(\ZZ, \ZZ_8) \oplus \operatorname{Tor}(\ZZ_4, \ZZ_6) \oplus \operatorname{Tor}(\ZZ_4, \ZZ_8).$$
:::

:::

:::

::: pf-step
Evaluation of components:

::: pf-proof

::: pf-step
$\operatorname{Tor}(\ZZ, \ZZ_6) = 0$ and $\operatorname{Tor}(\ZZ, \ZZ_8) = 0$.
:::

::: pf-step
$\operatorname{Tor}(\ZZ_4, \ZZ_6) \cong \ZZ_{\gcd(4, 6)} = \ZZ_2$.
:::

::: pf-step
$\operatorname{Tor}(\ZZ_4, \ZZ_8) \cong \ZZ_{\gcd(4, 8)} = \ZZ_4$.
:::

::: pf-step
Summing the components: $$\operatorname{Tor}_1^\ZZ(\ZZ \oplus \ZZ_4, \ZZ_6 \oplus \ZZ_8) \cong 0 \oplus 0 \oplus \ZZ_2 \oplus \ZZ_4 \cong \ZZ_2 \oplus \ZZ_4.$$
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
$\operatorname{Tor}(\ZZ \oplus \ZZ_4, \ZZ_6 \oplus \ZZ_8) \cong \ZZ_2 \oplus \ZZ_4 \cong \ZZ/2\ZZ \oplus \ZZ/4\ZZ$.
:::

:::

:::
:::
