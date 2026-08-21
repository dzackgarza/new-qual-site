---
schema: qual/card@1
id: D-UEWPN
kind: definition
title: Long exact sequence
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Homology
relations: []
review: draft
---

::: {.definition title="Long exact sequence"}
An exact sequence that is unbounded in one or both directions.
The main source is a short exact sequence of chain complexes $0\to A_*\to B_*\to C_*\to 0$, which induces
\[
\cdots \to H_n(A) \to H_n(B) \to H_n(C) \mapsvia{\del} H_{n-1}(A) \to \cdots
,\]
where $\del$ is the connecting map.
For a pair $(X,A)$ this gives
\[
\cdots \to H_n(A)\to H_n(X) \to H_n(X, A) \mapsvia{\del} H_{n-1}(A) \to \cdots
.\]
:::

::: {.concept}
See Hatcher, §2.1, Theorem 2.16, p. 117.
:::
