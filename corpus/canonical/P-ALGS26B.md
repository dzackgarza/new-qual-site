---
schema: qual/card@1
id: P-ALGS26B
kind: problem
title: "Normal p-subgroup and Sylow subgroups of subgroups"
classification:
  areas:
  - algebra
  topics:
  - Algebra
relations: []
review: draft
solved: false
---

::: problem
Suppose $G$ is a finite group and $p$ is a prime divisor of $|G|$. Let $\operatorname{Syl}_p(G)$ denote the set of all Sylow $p$-subgroups of $G$, and
$$
O_p(G) := \bigcap_{P \in \operatorname{Syl}_p(G)} P.
$$

(a) Prove that $O_p(G)$ is the largest normal $p$-subgroup of $G$.

(b) Suppose $H$ is a subgroup of $G$. Prove that there exists a function $f : \operatorname{Syl}_p(H) \to \operatorname{Syl}_p(G)$ such that $f(P) \cap H = P$.

(c) Prove that if $|\operatorname{Syl}_p(H)| = |\operatorname{Syl}_p(G)|$, then $O_p(H) = O_p(G) \cap H$.

Hint: Show that the function $f$ given in the previous part is a bijection.

(d) Prove that if $O_p(G) = 1$ and $\bar{P}$ is a non-trivial $p$-subgroup of $G$, then $|\operatorname{Syl}_p(N_G(\bar{P}))| < |\operatorname{Syl}_p(G)|$.
:::
