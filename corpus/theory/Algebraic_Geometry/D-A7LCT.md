---
schema: qual/card@1
id: D-A7LCT
kind: definition
title: Kernel, image and cokernel sheaves, and which need sheafifying
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Sheafification
  - Exact Sequences
relations:
- kind: uses
  target: T-3VX80
review: draft
prompts:
- What is the kernel sheaf of a morphism of sheaves?
- What is the image sheaf, and why does it need sheafification?
- What is the cokernel sheaf?
---

::: {.definition}
Let $\varphi : \mcf \to \mcg$ be a morphism of sheaves.

- The \dfn{kernel} is $U \mapsto \ker \varphi(U)$, which is already a sheaf.

- The **image** is the sheafification of $U \mapsto \im \varphi(U)$.

- The **cokernel** is the sheafification of $U \mapsto \mcg(U)/\im \varphi(U)$.
:::

::: {.remark}
Which of the three needs correcting, and why, is the content.
The kernel is defined by a condition that is local — a section is in the kernel exactly when it is in the kernel near every point — so it satisfies both axioms already.
The image and cokernel are defined by an existential — a section is in the image when *some* preimage exists — and existence is not local: preimages may exist near every point without gluing.

The two failures are different, and it is worth saying which is which.
The image presheaf typically fails **gluing**, so sheafification adds sections.
The cokernel presheaf typically fails **identity**, so sheafification also kills sections that are locally zero.
:::
