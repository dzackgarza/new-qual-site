---
schema: qual/card@1
id: PR-QJZDT
kind: proposition
title: Product CW structure
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Product Topology
  - Homology
relations: []
review: draft
---

::: {.proposition}
Let $X$ and $Y$ be CW complexes such that $X\cross Y$ with the product topology is a CW complex with cells $e^i_\alpha\cross e^j_\beta$; this holds if $X$ or $Y$ is locally compact, or if both have countably many cells [@Hat02].
Then the cellular chain complexes satisfy
$$
C_n(X \cross Y) \cong \bigoplus_{i+j=n} C_i(X) \tensor_\ZZ C_j(Y), \qquad e^i\cross e^j\mapsto e^i\tensor e^j
,$$
with boundary
$$
d(e^i\cross e^j) = de^i\cross e^j + (-1)^{i} e^i\cross de^j
$$
[@Hat02].
In particular, if $X$ and $Y$ have finitely many cells in each dimension and $p_X(t) = \sum_n a_n t^n$, $p_Y(t)$ count their $n$-cells, then $p_{X\cross Y}(t) = p_X(t)\,p_Y(t)$.
:::
