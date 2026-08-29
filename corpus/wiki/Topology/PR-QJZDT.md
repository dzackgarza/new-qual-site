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

:::{.proposition}
If $X, Y$ are CW complexes with $p_X(t), p_Y(t)$ the generating functions for the number of cells (so $[t^n] p_X(t) \da a_n$ is the number of $n\dash$cells in $X$), then the generating function for the product is 
\[
p_{X\cross Y}(t) = p_X(t)p_Y(t)
.\]
Categorified, this comes from a quasi-isomorphism 
\[
C_*^{\cell}(X\cross Y) \cong C_*^{\cell}(X) \tensor_\ZZ C_*^{\cell}(Y)
.\] 
so 
\[
C_n^{\cell}(X \cross Y ) \cong \bigoplus_{i+j=n} C_i^\cell(X) \cross C_j^{\cell}(Y)
.\]
The boundary maps are thus given by
\[
\bd(a, b) &\da \bd_X a \tensor b + (-1)^{\abs a} a \tensor \bd_Y b
.\]

:::
