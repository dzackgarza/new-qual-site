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
- Show that a scheme is locally Noetherian if and only if $R$ is Noetherian for every affine open $\Spec R \subseteq X$.
- If $(f_1, \ldots, f_n) = (1)$ in $A$ and every $A_{f_i}$ is Noetherian, show that $A$ is Noetherian.
- Give a scheme whose underlying space is Noetherian but which is not a Noetherian scheme.
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

::: {.definition title="Noetherian scheme"}
A scheme $X$ is \dfn{locally Noetherian} if it can be covered by open affine subsets $\Spec A_i$ with each $A_i$ a Noetherian ring.
It is **Noetherian** if it is locally Noetherian and quasicompact, equivalently if it has a finite such cover.
A scheme is locally Noetherian if and only if $R$ is Noetherian for every open affine $\Spec R \subseteq X$.
[@Har10a, §II.3, Proposition II.3.2]
:::

::: {.remark}
The Hilbert basis theorem is what makes the condition usable: $A$ Noetherian implies $A[x]$ Noetherian, hence every finitely generated algebra over a field or over $\ZZ$ is Noetherian.
Quotients and localisations of Noetherian rings are Noetherian; subrings need not be, and infinitely generated polynomial rings such as $k[x_1, x_2, \ldots]$ are not.

Over a Noetherian ring, finitely generated modules are Noetherian, submodules of finitely generated modules are finitely generated, and coherent and finitely generated agree for quasicoherent sheaves.
This is the hypothesis quietly supporting almost every finiteness statement on the exam: Krull dimension being finite on local rings, primary decomposition, and the finiteness of cohomology for coherent sheaves on a projective scheme.
:::
