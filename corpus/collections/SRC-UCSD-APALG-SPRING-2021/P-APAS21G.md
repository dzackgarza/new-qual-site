---
schema: qual/card@1
id: P-APAS21G
kind: problem
title: Dimension of the $S_n$-fixed subspace of $S^\lambda \otimes S^\mu$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $\lambda, \mu \vdash n$ be partitions and let $S^\lambda$, $S^\mu$ be the corresponding irreducible $S_n$-modules.
Endow the tensor product $S^\lambda \otimes S^\mu$ with the structure of an $S_n$-module by the rule
\[
\sigma \cdot (v \otimes w) := (\sigma \cdot v) \otimes (\sigma \cdot w)
\]
for $\sigma \in S_n$, $v \in S^\lambda$, $w \in S^\mu$.
Find the vector space dimension of the $S_n$-fixed subspace
\[
(S^\lambda \otimes S^\mu)^{S_n}
\]
of $S^\lambda \otimes S^\mu$.
:::

::: {.solution}
**Goal.** Compute $\dim (S^\lambda \otimes S^\mu)^{S_n}$.

<1>1. $(S^\lambda \otimes S^\mu)^{S_n} \cong \operatorname{Hom}_{S_n}(\mathbf 1, S^\lambda \otimes S^\mu)$, where $\mathbf 1$ is the trivial representation.
Proof: the fixed subspace is the space of $S_n$-equivariant maps from the trivial representation.

<1>2. $\dim \operatorname{Hom}_{S_n}(\mathbf 1, S^\lambda \otimes S^\mu) = \langle \chi_{\mathbf 1}, \chi_\lambda \chi_\mu\rangle = \langle \chi_\lambda, \chi_\mu\rangle$.
Proof: the character of the tensor product is the product of characters, and $\chi_{\mathbf 1} = 1$; also $\chi_\lambda \chi_\mu$ is real-valued and $\langle 1, \chi_\lambda \chi_\mu\rangle = \langle \chi_\lambda, \overline{\chi_\mu}\rangle = \langle \chi_\lambda, \chi_\mu\rangle$ (characters of $S_n$ are real-valued).

<1>3. $\langle \chi_\lambda, \chi_\mu\rangle = \delta_{\lambda\mu}$ (the Kronecker delta).
Proof: the irreducible characters of $S_n$ are orthonormal.

<1>4. Hence $\dim (S^\lambda \otimes S^\mu)^{S_n} = \delta_{\lambda\mu}$.
Proof: <1>2 and <1>3.

<1>5. Q.E.D.
Proof: the dimension is $1$ if $\lambda = \mu$ and $0$ otherwise.
:::
