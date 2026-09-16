---
schema: qual/card@1
id: T-TZ3X7
kind: theorem
title: Künneth formula for homology
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

::: {.theorem}
Let $X, Y$ be CW complexes and $R$ a principal ideal domain.
For each $k$ there is a natural short exact sequence
$$
0 \to \bigoplus_{i+j=k} H_{i}(X; R) \tensor_{R} H_{j}(Y; R) \to H_{k}(X\cross Y; R) \to \bigoplus_{i+j=k-1} \Tor^R_1\qty{H_{i}(X; R), H_{j}(Y; R)} \to 0
,$$
and it splits, though not naturally:
$$
H_{k}(X\cross Y; R) \cong \qty{ \bigoplus_{i+j = k} H_{i}(X;R) \tensor_R H_{j}(Y;R) } \oplus \bigoplus_{i+j = k-1}\Tor^R_1\qty{H_{i}(X;R), H_{j}(Y;R)}
$$
[@Hat02, Theorem 3B.6, p. 275].
:::
