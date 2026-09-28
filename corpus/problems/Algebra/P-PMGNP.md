---
schema: qual/card@1
id: P-PMGNP
kind: problem
title: $\mathrm{Ext}$ of cyclic groups
classification:
  areas:
  - algebra
  topics:
  - Homological Algebra
  - Abelian Groups
  - Exact Sequences
relations: []
review: draft
---

::: {.problem}
Explain $\Ext^1_{\ZZ}$ for abelian groups, where it appears, and compute
\[
\Ext^1_{\ZZ}(\ZZ/m\ZZ,\ZZ/n\ZZ)
\quad\text{and}\quad
\Ext^1_{\ZZ}(\ZZ/m\ZZ,\ZZ).
\]
:::

::: {.solution}
For abelian groups, $\Ext^1_{\ZZ}(A,B)$ is the first right derived functor of $\Hom_{\ZZ}(A,-)$; equivalently, it classifies extensions
\[
0\to B\to E\to A\to0
\]
up to the usual equivalence.

Use the free resolution
\[
0\to\ZZ\xrightarrow{\times m}\ZZ\to\ZZ/m\ZZ\to0.
\]
Applying $\Hom_{\ZZ}(-,B)$ gives
\[
0\to\Hom(\ZZ/m\ZZ,B)\to B\xrightarrow{\times m}B\to
\Ext^1_{\ZZ}(\ZZ/m\ZZ,B)\to0.
\]
Hence
\[
\Ext^1_{\ZZ}(\ZZ/m\ZZ,B)\cong B/mB.
\]

Taking $B=\ZZ/n\ZZ$ gives
\[
\Ext^1_{\ZZ}(\ZZ/m\ZZ,\ZZ/n\ZZ)
\cong (\ZZ/n\ZZ)/m(\ZZ/n\ZZ)
\cong \ZZ/\gcd(m,n)\ZZ.
\]
Taking $B=\ZZ$ gives
\[
\Ext^1_{\ZZ}(\ZZ/m\ZZ,\ZZ)
\cong \ZZ/m\ZZ.
\]
:::
