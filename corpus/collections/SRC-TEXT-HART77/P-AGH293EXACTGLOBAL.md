---
schema: qual/card@1
id: P-AGH293EXACTGLOBAL
kind: problem
title: Global sections on an affine formal scheme are exact
classification:
  areas:
  - algebraic-geometry
  topics:
  - Formal Schemes
  - Coherent Sheaves
  - Inverse Limits
relations: []
review: draft
---

::: problem
Prove the analogue for formal schemes of the exactness of global sections on affine schemes: if $\mathfrak{X}$ is an affine formal scheme, and if
\[
0 \to \mcf' \to \mcf \to \mcf'' \to 0
\]
is an exact sequence of $\OO_\mathfrak{X}\dash$modules, and if $\mcf'$ is coherent, then the sequence of global sections
\[
0 \to \Gamma(\mathfrak{X}, \mcf') \to \Gamma(\mathfrak{X}, \mcf) \to \Gamma(\mathfrak{X}, \mcf'') \to 0
\]
is exact.
Proceed in the following steps.

a. Let $\mci$ be an ideal of definition for $\mathfrak{X}$, and for each $n > 0$ consider the exact sequence
\[
0 \to \mcf'/\mci^n \mcf' \to \mcf/\mci^n \mcf' \to \mcf'' \to 0
.\]
   Use the affine case, slightly modified, to show that for every open affine subset $\mcu \subseteq \mathfrak{X}$ the sequence
\[
0 \to \Gamma(\mcu, \mcf'/\mci^n \mcf') \to \Gamma(\mcu, \mcf/\mci^n \mcf') \to \Gamma(\mcu, \mcf'') \to 0
\]
   is exact.

b. Now pass to the limit.
   Conclude that $\mcf \cong \inverselim_n \mcf/\mci^n \mcf'$ and that the sequence of global sections above is exact.
:::
