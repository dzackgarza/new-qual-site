---
schema: qual/card@1
id: D-UI3FE
kind: definition
title: Lens Space
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Covering Spaces
  - Group Actions
  - Homology
relations: []
review: draft
---

::: {.definition title="Lens Space"}
For $m \geq 1$ and integers $\ell_1, \cdots, \ell_n$ coprime to $m$, let $\ZZ/m$ act on the unit sphere $S^{2n-1}\subseteq \CC^n$ by
\[
(z_1, \cdots, z_n) \mapsto \qty{ e^{2\pi i \ell_1/m} z_1, \cdots, e^{2\pi i \ell_n /m} z_n }
.\]
The action is free, and the **lens space** is the orbit space
\[
L_m(\ell_1, \cdots, \ell_n) \da S^{2n-1}/\qty{\ZZ/m}
.\]
It is a closed orientable $(2n-1)\dash$manifold with universal cover $S^{2n-1}$ and $\pi_1 \cong \ZZ/m$.
:::

::: {.concept}
See Hatcher, §2.2, Example 2.43, p. 144.
:::
