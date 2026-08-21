---
schema: qual/card@1
id: P-4IWVY
kind: problem
title: Irreducible modules over a PID are $R/(p)$ and indecomposable modules are $R/(p^n)$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Semisimplicity
  - Principal Ideal Domains
relations: []
review: draft
solved: false
---

::: problem
**Irreducible:** Let $a\in M$ be arbitrary; we can then consider the cyclic submodule $aR \normal M$.
Since $M$ is irreducible, we must have $aR = 0$ or $aR = M$.
If $aR = 0$ then $a$ must be $0$.

Otherwise, $aR = M$ implies that $M$ itself is a cyclic module with generator $a$.
Since $R$ is a PID, we can find an element $p$ such that $\ann_R(M) = (p) \normal R$, in which case $M \cong R/(p)$.

It is also necessarily the case that $(p)$ is maximal, for if there were another ideal $(p) \subseteq J \normal R$, then $J/(p) \normal R/(p) \cong M$ is a submodule by the correspondence theorem for ideals.
But this necessarily forces $J/(p) = 0$ or $M$ by irreducibility of $M$, so $J = (p)$ or $R$.

Thus irreducible modules are exactly the cyclic modules, or equivalently those of the form $R/(p)$ where $(p)$ is a maximal ideal.

**Indecomposable:** We first note that by the structure theorem for modules over a PID, any module $M$ has a primary decomposition $M \cong \bigoplus_i R/(p_i^{k_i})$.

This means that if $M$ is indecomposable, we must have $M \cong R/(p^n)$ (with a single summand) for some prime $p \in R$; otherwise the primary decomposition would yield additional summands.
Moreover, by the Chinese Remainder Theorem, $M$ can not be decomposed further.

Thus all indecomposable module are of the form $R/(p^n)$ for some $n\geq 1$.
:::
