---
schema: qual/card@1
id: T-2W5WN
kind: theorem
title: Universal coefficient theorems
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Homology
  - Cohomology
relations: []
review: draft
---

::: {.theorem}
Let $X$ be a topological space and $G$ an abelian group.
For each $i$ there are natural short exact sequences
$$
0 \to H_i(X;\ZZ)\tensor G \to H_i(X; G) \to \Tor(H_{i-1}(X;\ZZ), G) \to 0
$$
[@Hat02] and
$$
0 \to \Ext(H_{i-1}(X;\ZZ), G) \to H^i(X;G) \to \Hom(H_i(X;\ZZ), G) \to 0
$$
[@Hat02].
Both sequences split, though not naturally, so
$$
H_i(X;G) \cong \qty{H_i(X;\ZZ)\tensor G} \oplus \Tor(H_{i-1}(X;\ZZ), G), \qquad
H^i(X;G) \cong \Hom(H_i(X;\ZZ), G) \oplus \Ext(H_{i-1}(X;\ZZ), G)
.$$
:::

::: {.proposition}
If $H_i(X;\ZZ)$ and $H_{i-1}(X;\ZZ)$ are finitely generated with torsion subgroups $T_i$ and $T_{i-1}$, then
$$
H^i(X;\ZZ) \cong \qty{H_i(X;\ZZ)/T_i} \oplus T_{i-1}
$$
[@Hat02].
If $F$ is a field, then $H^i(X;F) \cong \Hom_F(H_i(X;F), F)$ [@Hat02].
:::
