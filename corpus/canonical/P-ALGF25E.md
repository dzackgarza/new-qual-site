---
schema: qual/card@1
id: P-ALGF25E
kind: problem
title: Submodules isomorphic to $A/\mathfrak{P}$ and existence when $A$ is Noetherian
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Ideals
relations: []
review: draft
---

::: problem
Let $A$ be a unital commutative ring, $\operatorname{Spec}(A)$ denote the set of its prime ideals, and let $M$ be an $A$-module.

(a) Suppose $N_1$ and $N_2$ are two submodules of $M$ such that
\[
N_1 \simeq A/P_1 \qquad \text{and} \qquad N_2 \simeq A/P_2
\]
as $A$-modules for some $P_1, P_2 \in \operatorname{Spec}(A)$.
Prove that if $P_1 \neq P_2$, then $N_1 \cap N_2 = \{0\}$.
(Hint.
Consider $\operatorname{ann}(x)$ for $x \in N_i$.)

(b) Suppose $A$ is Noetherian.
Prove that there exist a submodule $N$ of $M$ and $P \in \operatorname{Spec}(A)$ such that $N \simeq A/P$.
(Hint.
Consider $\Sigma := \{\operatorname{ann}(x) \mid x \in M \setminus \{0\}\}$.)
:::
