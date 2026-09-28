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
- Show that the presheaf tensor product of two sheaves of modules need not be a sheaf.
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

::: {.example title="Tensor presheaf"}
On $X = \PP^1_k$ take $\mcf = \OO(1)$ and $\mcg = \OO(-1)$.
The presheaf $P(U) = \mcf(U) \tensor_{\OO_X(U)} \mcg(U)$ has $P(X) = k^2 \tensor_k 0 = 0$.
On each standard chart $U_i = D_+(x_i)$ both sheaves are trivial, so $P(U_i) \cong \OO(U_i)$, and the sections $x_0 \tensor x_0^{-1}$ on $U_0$ and $x_1 \tensor x_1^{-1}$ on $U_1$ agree on $U_0 \cap U_1$, since both equal the unit section there.
They do not glue to a section of $P(X) = 0$, so $P$ is not a sheaf; its sheafification is $\OO(1) \tensor \OO(-1) \cong \OO_X$, with $H^0 = k$.
:::

::: {.remark}
The presheaf cokernel is where this matters in practice.
Given $\varphi : \mcf \to \mcg$ of sheaves, $U \mapsto \mcg(U)/\varphi(\mcf(U))$ is a presheaf that is usually not a sheaf, and the sheaf cokernel is its sheafification.
Kernels need no correction: $U \mapsto \ker \varphi_U$ is already a sheaf.
That asymmetry is the reason cokernels, images, and exactness of sheaves are stalk-local notions and not section-wise ones.
:::
