---
schema: qual/card@1
id: P-ALGF25B
kind: problem
title: Minimal Sylow intersections and the normalizer of $N$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Centralizers and Normalizers
relations: []
review: draft
solved: false
---

::: problem
Suppose $G$ is a finite group.
Let $\operatorname{Syl}_p(G)$ be the set of all Sylow $p$-subgroups of $G$.
Suppose $P_1, P_2 \in \operatorname{Syl}_p(G)$ are distinct and $P_1 \cap P_2$ is minimal among all the subgroups that are the intersection of two distinct Sylow $p$-subgroups.
Suppose $N$ is a subgroup of $P_1 \cap P_2$ and $N \trianglelefteq P_i$ for $i = 1, 2$, and let $H := N_G(N)$.

(a) Prove that for every $P \in \operatorname{Syl}_p(G)$, there exists $h \in H$ such that $hPh^{-1} \cap H \subseteq P_1$.

(b) Prove that for every $P \in \operatorname{Syl}_p(G)$, there exists $h \in H$ such that $hPh^{-1} \cap P_2 = P_1 \cap P_2$.

(c) Prove that for every $P \in \operatorname{Syl}_p(G)$, $N \subseteq P$.

(d) Suppose $P_1$ is abelian.
Prove that
\[
P_1 \cap P_2 = \bigcap_{P \in \operatorname{Syl}_p(G)} P.
\]
:::
