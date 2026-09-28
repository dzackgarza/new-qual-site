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

- The \dfn{image} is the sheafification of $U \mapsto \im \varphi(U)$.

- The \dfn{cokernel} is the sheafification of $U \mapsto \mcg(U)/\im \varphi(U)$.
:::

::: {.remark}
A section of $\mcf$ lies in $\ker\varphi(U)$ if and only if its restrictions to the members of an open cover of $U$ do, so the kernel presheaf satisfies both sheaf axioms.
A section $t\in\mcg(U)$ lies in $\im\varphi(U)$ when there exists $s\in\mcf(U)$ with $\varphi(s)=t$; local preimages on an open cover of $U$ need not agree on overlaps, so they need not glue to a preimage on $U$.

The image presheaf is a subpresheaf of the sheaf $\mcg$, so it satisfies the identity axiom; it can fail gluing, and sheafification adds the sections of $\mcg$ that lie in the image locally.
The cokernel presheaf can fail both axioms; sheafification sends to $0$ the sections that are locally zero.
:::

::: {.example title="The image presheaf of the exponential map"}
On $X=\CC\sm\ts{0}$, let $\varphi=\exp\colon\OO_X\to\OO_X^\times$.
The section $z\in\OO_X^\times(X)$ has a logarithm on every simply connected open subset of $X$ but none on $X$.
So $z$ is not in the image presheaf on $X$, and its class in the cokernel presheaf on $X$ is nonzero but locally zero.
The image sheaf is $\OO_X^\times$ and the cokernel sheaf is $0$.
:::
