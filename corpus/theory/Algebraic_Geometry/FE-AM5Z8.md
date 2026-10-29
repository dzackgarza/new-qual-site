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
For a fixed abelian group $A$, the constant presheaf with $P(U)=A$ for $U\ne\emptyset$, $P(\emptyset)=0$, and identity restrictions between nonempty open sets fails the gluing axiom.
On a disconnected $U = U_1 \sqcup U_2$ the sections $a \in A$ on $U_1$ and $b \neq a$ on $U_2$ agree on the empty overlap, and no element of $P(U)=A$ restricts to both.
Its sheafification is the sheaf of locally constant $A$-valued functions.
:::

::: {.example title="Identity fails"}
Let $\mathcal C(U)$ be the continuous real-valued functions on $U\subseteq\RR$, and let $\mathcal B(U)\subseteq\mathcal C(U)$ be the bounded continuous functions.
The presheaf quotient
$$
\mathcal Q(U)
\coloneqq
\mathcal C(U)/\mathcal B(U)
$$
fails the identity axiom.
The class of $x\mapsto x$ is nonzero in $\mathcal Q(\RR)$ because it is unbounded, but it restricts to zero on every bounded open interval because there it is bounded.
Thus a nonzero global section can be locally zero.
Separately, the presheaf $\mathcal B$ itself fails gluing: bounded local functions on an unbounded cover can glue to an unbounded global continuous function.
:::

::: {.example title="Tensor presheaf"}
On $X = \PP^1_k$ take $\mcf = \OO(1)$ and $\mcg = \OO(-1)$.
The presheaf $P(U) = \mcf(U) \tensor_{\OO_X(U)} \mcg(U)$ has $P(X) = k^2 \tensor_k 0 = 0$.
On each standard chart $U_i = D_+(x_i)$ both sheaves are trivial, so $P(U_i) \cong \OO(U_i)$, and the sections
$x_0 \tensor_{\OO_X(U_0)} x_0^{-1}$ on $U_0$ and
$x_1 \tensor_{\OO_X(U_1)} x_1^{-1}$ on $U_1$
agree on $U_0 \cap U_1$, since both equal the unit section there.
They do not glue to a section of $P(X) = 0$, so $P$ is not a sheaf; its sheafification is
$\OO(1) \tensor_{\OO_X} \OO(-1) \cong \OO_X$, with $H^0 = k$.
:::

::: {.remark}
Given $\varphi \colon \mcf \to \mcg$ of sheaves, the presheaf $U \mapsto \mcg(U)/\varphi(\mcf(U))$ need not be a sheaf, and the sheaf cokernel is its sheafification ([[D-A7LCT]]); the presheaf $U \mapsto \ker \varphi_U$ is a sheaf.
A sequence of sheaves is exact if and only if it is exact on every stalk; a surjection of sheaves need not be surjective on sections over every open set, as $\exp\colon\OO\to\OO^\times$ on $\CC\sm\theset{0}$ shows.
:::
