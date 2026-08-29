---
schema: qual/card@1
id: P-KPSXT
kind: problem
title: An example of a flat module
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Homological Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(1) What is the definition of a **flat module** over a ring $R$?
(2) Give standard examples of flat modules, including an example of a flat module that is not projective/free, and an example of a non-flat module.
:::

::: solution
**Goal:** Define flat $R$-modules, characterize them via the exactness of the tensor product functor $- \otimes_R M$, and provide examples and non-examples.

<1>1. Definition of a Flat Module:
    *Proof:*
    <2>1. Let $R$ be a ring. A right $R$-module $M$ is **flat** if the tensor product functor:
        $$T_M(-) \coloneqq - \otimes_R M$$
        is an **exact functor** from the category of left $R$-modules to the category of abelian groups.
    <2>2. Since $- \otimes_R M$ is always right-exact, $M$ is flat if and only if for every injective homomorphism of left $R$-modules $0 \to A \xrightarrow{i} B$, the induced map:
        $$0 \longrightarrow A \otimes_R M \xrightarrow{i \otimes \operatorname{id}_M} B \otimes_R M$$
        is also **injective**.
    <2>3. Equivalently, $M$ is flat if and only if $\operatorname{Tor}_1^R(N, M) = 0$ for all $R$-modules $N$.

<1>2. Free and Projective Modules are Flat:
    *Proof:*
    <2>1. Any **free module** $F = \bigoplus_{i \in I} R$ is flat, because tensor products commute with direct sums:
        $$A \otimes_R \left(\bigoplus_{i \in I} R\right) \cong \bigoplus_{i \in I} (A \otimes_R R) \cong \bigoplus_{i \in I} A,$$
        and direct sums of injective maps are injective.
    <2>2. Any **projective module** $P$ is a direct summand of a free module ($F \cong P \oplus Q$), hence $P$ is also flat.

<1>3. Flat Modules that are Not Free or Projective (Localization):
    *Proof:*
    <2>1. Let $R$ be a commutative ring and $S \subset R$ a multiplicative subset. The **localization** $S^{-1} R$ is always a flat $R$-module.
    <2>2. **Canonical Specimen:** Over $R = \mathbb{Z}$, the field of rational numbers $\mathbb{Q} = S^{-1} \mathbb{Z}$ (where $S = \mathbb{Z} \setminus \{0\}$) is a **flat $\mathbb{Z}$-module**.
    <2>3. *Why $\mathbb{Q}$ is flat over $\mathbb{Z}$:*
        - Over a PID/Dedekind domain, a module is flat if and only if it is **torsion-free**.
        - Since $\mathbb{Q}$ is torsion-free ($n \cdot q = 0 \implies q = 0$), $\mathbb{Q}$ is flat.
    <2>4. *Why $\mathbb{Q}$ is not projective/free over $\mathbb{Z}$:*
        - $\mathbb{Q}$ is not free because any two non-zero rationals are $\mathbb{Z}$-linearly dependent ($a \cdot (c/d) - c \cdot (a/d) = 0$), so $\operatorname{rank}(\mathbb{Q}) = 1$, but $\mathbb{Q} \not\cong \mathbb{Z}$.
        - $\mathbb{Q}$ is not projective because it is divisible: $\operatorname{Hom}_\mathbb{Z}(\mathbb{Q}, \mathbb{Z}) = 0$, so $\mathbb{Q}$ cannot be a direct summand of any free $\mathbb{Z}$-module.

<1>4. Non-Examples (Torsion Modules):
    *Proof:*
    <2>1. Over $R = \mathbb{Z}$, any non-trivial finite cyclic group $M = \mathbb{Z}/n\mathbb{Z}$ ($n \ge 2$) is **not flat**.
    <2>2. *Proof:* Consider the injective map $i: \mathbb{Z} \xrightarrow{\times n} \mathbb{Z}$.
        Tensoring with $\mathbb{Z}/n\mathbb{Z}$ gives:
        $$\mathbb{Z} \otimes_\mathbb{Z} (\mathbb{Z}/n\mathbb{Z}) \xrightarrow{\times n} \mathbb{Z} \otimes_\mathbb{Z} (\mathbb{Z}/n\mathbb{Z}) \iff \mathbb{Z}/n\mathbb{Z} \xrightarrow{\times n} \mathbb{Z}/n\mathbb{Z}.$$
        The multiplication-by-$n$ map on $\mathbb{Z}/n\mathbb{Z}$ is the **zero map**, which is not injective on the non-zero group $\mathbb{Z}/n\mathbb{Z}$.
        Thus $\mathbb{Z}/n\mathbb{Z}$ is not flat.

<1>5. Conclusion:
    Flat modules preserve monomorphisms under tensoring; $\mathbb{Q}$ is a classic flat non-projective $\mathbb{Z}$-module, while $\mathbb{Z}/n\mathbb{Z}$ is non-flat. Q.E.D.
:::
