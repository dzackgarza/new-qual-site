---
schema: qual/card@1
id: D-DEFNOETH
kind: definition
title: Noetherian rings and modules
classification:
  areas:
  - algebraic-geometry
  topics:
  - Commutative Algebra
  - Noetherian Rings
relations: []
review: draft
prompts:
- What is a Noetherian ring, and what is the equivalent finiteness condition?
- Which operations preserve the Noetherian condition?
---

::: {.definition title="Noetherian ring"}
A ring $A$ is \dfn{Noetherian} if it satisfies the ascending chain condition on ideals: any increasing chain
\[
I_1 \subseteq I_2 \subseteq I_3 \subseteq \cdots
\]
of ideals of $A$ eventually stabilises.
Equivalently, every ideal of $A$ is finitely generated.
An $A$-module $M$ is Noetherian if its submodules satisfy the same condition.
:::

::: {.remark}
The Hilbert basis theorem is what makes the condition usable: $A$ Noetherian implies $A[x]$ Noetherian, hence every finitely generated algebra over a field or over $\ZZ$ is Noetherian.
Quotients and localisations of Noetherian rings are Noetherian; subrings need not be, and infinitely generated polynomial rings such as $k[x_1, x_2, \ldots]$ are not.

Over a Noetherian ring, finitely generated modules are Noetherian, submodules of finitely generated modules are finitely generated, and coherent and finitely generated agree for quasicoherent sheaves.
This is the hypothesis quietly supporting almost every finiteness statement on the exam: Krull dimension being finite on local rings, primary decomposition, and the finiteness of cohomology for coherent sheaves on a projective scheme.
:::
