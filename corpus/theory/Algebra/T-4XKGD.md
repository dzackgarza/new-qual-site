---
schema: qual/card@1
id: T-4XKGD
kind: theorem
title: Frattini's argument
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Centralizers and Normalizers
  - Normal Subgroups
relations:
- kind: variant-of
  target: L-6QBOJ
review: draft
---

::: {.theorem}
Let $G$ be a finite group, $H\normal G$ a normal subgroup, $p$ a prime, and $P \in \Syl_p(H)$ a [[D-7TQ2M|Sylow $p$-subgroup]] of $H$.
Then $G=H\,N_G(P)$, and $[G: H]$ divides $\abs{N_G(P)}$.
:::

::: {.proof}
Let $g\in G$.
Since $H\normal G$, $gPg^{-1}\leq H$ is a Sylow $p$-subgroup of $H$, so by [[T-EF2MZ|Sylow's second theorem]] in $H$ there is $h\in H$ with $hgPg^{-1}h^{-1}=P$.
Then $hg\in N_G(P)$, so $g\in h^{-1}N_G(P)\subseteq H\,N_G(P)$.
Hence $G=H\,N_G(P)$, and by the second isomorphism theorem $G/H\cong N_G(P)/(N_G(P)\cap H)$, so $[G:H]$ divides $\abs{N_G(P)}$.
:::
