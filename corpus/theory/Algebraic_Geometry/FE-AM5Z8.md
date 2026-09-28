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

::: {.example title="Bounded functions"}
Let $C$ be the sheaf of continuous real functions on $\RR$ and $B\subseteq C$ the presheaf of bounded continuous functions.
$B$ satisfies the identity axiom, being a subpresheaf of a sheaf, and fails gluing: the restrictions of $f(x)=x$ to the intervals $(n-1,n+1)$ are bounded and agree on overlaps, while $f$ is unbounded.
The presheaf quotient $U\mapsto C(U)/B(U)$ fails the identity axiom: the class of $f(x)=x$ on $\RR$ is nonzero, and its restriction to each interval $(n-1,n+1)$ is zero.
:::

::: {.example title="Tensor presheaf"}
On $X = \PP^1_k$ take $\mcf = \OO(1)$ and $\mcg = \OO(-1)$.
The presheaf $P(U) = \mcf(U) \tensor_{\OO_X(U)} \mcg(U)$ has $P(X) = k^2 \tensor_k 0 = 0$.
On each standard chart $U_i = D_+(x_i)$ both sheaves are trivial, so $P(U_i) \cong \OO(U_i)$, and the sections $x_0 \tensor x_0^{-1}$ on $U_0$ and $x_1 \tensor x_1^{-1}$ on $U_1$ agree on $U_0 \cap U_1$, since both equal the unit section there.
They do not glue to a section of $P(X) = 0$, so $P$ is not a sheaf; its sheafification is $\OO(1) \tensor \OO(-1) \cong \OO_X$, with $H^0 = k$.
:::

::: {.remark}
Given $\varphi : \mcf \to \mcg$ of sheaves, the presheaf $U \mapsto \mcg(U)/\varphi(\mcf(U))$ need not be a sheaf, and the sheaf cokernel is its sheafification ([[D-A7LCT]]); the presheaf $U \mapsto \ker \varphi_U$ is a sheaf.
A sequence of sheaves is exact if and only if it is exact on every stalk; a surjection of sheaves need not be surjective on sections over every open set, as $\exp\colon\OO\to\OO^\times$ on $\CC\sm\ts{0}$ shows.
:::
