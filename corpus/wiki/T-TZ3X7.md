---
schema: qual/card@1
id: T-TZ3X7
kind: theorem
title: "Kunneth"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
:::{.theorem title="Kunneth"}
There exists a short exact sequence
\[
0 \to \prod_{i+j=k} H_{j}(X; R) \tensor_{R} H_{i}(Y; R) \to H_{k}(X\cross Y; R) \to \prod_{i+j=k-1} \tor_{R}^1(H_{i}(X; R), H_{j}(Y; R))
.\]
If $R$ is a free \(R\dash\)module, a PID, or a field, then there is a (non-canonical) splitting given by
\[
H_{k} (X\cross Y) \cong \left( \prod_{i+j = k} H_{i} X \oplus H_{j} Y\right) \cross \prod_{i+j = k-1}\tor(H_{i}X, H_{j} Y) \\
\]
:::
