---
schema: qual/card@1
id: FE-DNTT6
kind: example
title: The exponential sequence, and the logarithm that does not glue
classification:
  areas:
  - algebraic-geometry
  topics:
  - Exact Sequences
  - Sheafification
  - Cohomology
relations:
- kind: uses
  target: D-A7LCT
review: draft
prompts:
- Give an example showing the image presheaf is not a sheaf.
---

::: {.example}
On $X = \CC^*$ take the exponential sequence
\[
0 \to \ul{\ZZ} \xrightarrow{\ 2\pi i\ } \OO_X \xrightarrow{\ \exp\ } \OO_X^* \to 0 .
\]
It is exact as a sequence of sheaves, because it is exact on stalks: near any point a nonvanishing holomorphic function has a logarithm.

It is not exact as a sequence of presheaves.
Cover $\CC^*$ by contractible opens $U_i$, on each of which $\log$ exists, so $\id_{U_i} \in \OO^*(U_i)$ lies in the image presheaf.
These sections agree on overlaps and glue to $\id_{\CC^*}$, which is **not** in the image presheaf: a global logarithm on $\CC^*$ does not exist.

So the image presheaf fails the gluing axiom, and sheafifying it is exactly what supplies the missing section.
:::

::: {.remark}
The same sequence, taken in cohomology, is where the Picard group comes from:
\[
H^1(X, \OO) \to H^1(X, \OO^*) \to H^2(X, \ZZ) ,
\]
with $H^1(X,\OO^*) = \Pic(X)$ and the right-hand map the first Chern class.
The failure to glue here and the failure of surjectivity on global sections in [[PR-C9ZEK]] are the same phenomenon counted twice.
:::
