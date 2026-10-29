---
schema: qual/card@1
id: T-4XKGD
kind: theorem
title: Frattini's argument
slogan: 'A normal subgroup together with the normalizer of one of its Sylow subgroups generates the whole group.'
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

::: {.theorem}
Let $G$ be a finite group, let $N$ be a [[D-EKE4Q|normal subgroup]] of $G$, let $p$ be a prime, and let $P \in \Syl_p(N)$ be a [[D-7TQ2M|Sylow $p$-subgroup]] of $N$.
Then $G=N\,N_G(P)=N_G(P)\,N$, where $N_G(P)$ is the [[D-OZ2RR|normalizer]] of $P$ in $G$, and $[G:N]$ divides $\abs{N_G(P)}$.
:::

::: {.proof}
Let $g\in G$.
Since $N\normal G$, $gPg^{-1}\leq N$ is a Sylow $p$-subgroup of $N$, so by [[T-EF2MZ|Sylow's second theorem]] in $N$ there is $n\in N$ with $ngPg^{-1}n^{-1}=P$.
Then $ng\in N_G(P)$, so $g=n^{-1}(ng)\in N\,N_G(P)$.
Hence $G=N\,N_G(P)$, which equals $N_G(P)\,N$ because $N$ is normal.
By the second isomorphism theorem $G/N\cong N_G(P)/(N_G(P)\cap N)$, so $[G:N]$ divides $\abs{N_G(P)}$.
:::
