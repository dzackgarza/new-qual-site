---
schema: qual/card@1
id: FE-AM5Z8
kind: example
title: Presheaves that are not sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Presheaves
  - Sheaves
  - Counterexamples
relations:
- kind: uses
  target: D-RCCFY
review: draft
prompts:
- Give a presheaf that is not a sheaf, and say which axiom fails.
---

::: {.example title="Gluing fails"}
The **constant presheaf** $U \mapsto A$ for a fixed abelian group $A$, with identity restrictions.
On a disconnected $U = U_1 \sqcup U_2$ the sections $a \in A$ on $U_1$ and $b \neq a$ on $U_2$ agree on the empty overlap but glue to nothing.
Its sheafification is the sheaf of locally constant $A$-valued functions.
:::

::: {.example title="Identity fails"}
The presheaf of **bounded** real functions on $\RR$, or of functions with bounded support.
Boundedness is not a local condition: every function is locally bounded, so the presheaf of bounded functions is not even closed under gluing, and the presheaf quotient of functions by bounded functions has nonzero sections that are locally zero.
:::

::: {.remark}
The presheaf cokernel is where this matters in practice.
Given $\varphi : \mathcal{F} \to \mathcal{G}$ of sheaves, $U \mapsto \mathcal{G}(U)/\varphi(\mathcal{F}(U))$ is a presheaf that is usually not a sheaf, and the sheaf cokernel is its sheafification.
Kernels need no correction: $U \mapsto \ker \varphi_U$ is already a sheaf.
That asymmetry is the reason cokernels, images, and exactness of sheaves are stalk-local notions and not section-wise ones.
:::
