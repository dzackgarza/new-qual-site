---
schema: qual/card@1
id: T-TZ3X7
kind: theorem
title: Kunneth
classification:
  areas:
  - topology
  topics:
  - Homology
  - Product Topology
  - Homological Algebra
relations: []
review: draft
---

:::{.theorem}
Let $X, Y$ be CW complexes and $R$ a PID. Then for each $k$ there is a natural short exact sequence
\[
0 \to \bigoplus_{i+j=k} H_{i}(X; R) \tensor_{R} H_{j}(Y; R) \to H_{k}(X\cross Y; R) \to \bigoplus_{i+j=k-1} \tor^R_1\qty{H_{i}(X; R), H_{j}(Y; R)} \to 0
,\]
and it splits, though not naturally:
\[
H_{k}(X\cross Y; R) \cong \qty{ \bigoplus_{i+j = k} H_{i}(X;R) \tensor_R H_{j}(Y;R) } \oplus \bigoplus_{i+j = k-1}\tor^R_1\qty{H_{i}(X;R), H_{j}(Y;R)}
.\]
:::

::: {.remark}
Hatcher, §3.B, Theorem 3B.6.

Three things were wrong as printed. The sums are direct sums, not products; the splitting is a tensor product of the homologies, not a direct sum of them, so the second display contradicted the first; and the sequence had no $\to 0$, so it was not exact at its right-hand end. The hypothesis "if $R$ is a free $R\dash$module, a PID, or a field" collapses to $R$ a PID, which is what Theorem 3B.6 assumes, together with $X$ and $Y$ being CW complexes.
:::
