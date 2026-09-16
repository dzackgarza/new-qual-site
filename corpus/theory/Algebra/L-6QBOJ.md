---
schema: qual/card@1
id: L-6QBOJ
kind: lemma
title: Frattini's argument
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Centralizers and Normalizers
  - Normal Subgroups
relations: []
review: draft
---

::: {.lemma}
Let $G$ be a finite group, let $N$ be a [[D-EKE4Q|normal subgroup]] of $G$, let $p$ be a prime, and let $P$ be a [[D-7TQ2M|Sylow $p$-subgroup]] of $N$.
Then $G=N_G(P)N$, where $N_G(P)$ is the [[D-OZ2RR|normalizer]] of $P$ in $G$.
:::

::: {.proof}
Let $g\in G$.
Since $N$ is normal, $gPg^{-1}\subseteq N$, and it is a Sylow $p$-subgroup of $N$.
By [[FT-ZENUU|Sylow's second theorem]] in $N$, there is $n\in N$ with $ngPg^{-1}n^{-1}=P$, so $ng\in N_G(P)$.
Hence $g=n^{-1}(ng)\in NN_G(P)=N_G(P)N$, the last equality because $N$ is normal.
:::
