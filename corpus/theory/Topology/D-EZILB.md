---
schema: qual/card@1
id: D-EZILB
kind: proposition
title: Eilenberg--Zilber theorem for CW complexes
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
---

::: {.proposition}
For CW complexes $X$ and $Y$, the cellular chain complex of $X\cross Y$ is the tensor product chain complex
$$
C_n(X\cross Y) \cong \bigoplus_{i+j=n} C_i(X)\tensor_\ZZ C_j(Y),
\qquad
d(e^i\tensor e^j) = de^i\tensor e^j + (-1)^i e^i\tensor de^j,
$$
with the boundary formula of [@Hat02, Proposition 3B.1].
Its homology is therefore computed from the homology of $X$ and $Y$ by the algebraic Künneth theorem [@Hat02, Theorem 3B.5].
:::
