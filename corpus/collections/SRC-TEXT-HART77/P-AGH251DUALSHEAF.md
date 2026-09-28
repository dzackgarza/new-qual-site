---
schema: qual/card@1
id: P-AGH251DUALSHEAF
kind: problem
title: Duals of locally free sheaves and the projection formula
classification:
  areas:
  - algebraic-geometry
  topics:
  - Locally Free Sheaves
  - Sheaf Hom
  - Projection Formula
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the four parts with the retained MinerU transcription Hartshorne_Solutions_extracted.md, section 2.5, solution 5.1(a)-(d). Restored the missing dual-tensor identity and the quantifier for G, and distinguished global Hom from sheaf Hom.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $(X,\OO_X)$ be a ringed space, and let $\mce$ be a locally free $\OO_X$-module of finite rank.
We define the \dfn{dual} of $\mce$, denoted $\dualof{\mce}$, to be the sheaf $\sheafhom_{\OO_X}(\mce,\OO_X)$.

(a) Show that $\dualof{(\dualof{\mce})}\cong\mce$.

(b) For any $\OO_X$-module $\mcf$, show that there is a natural isomorphism $$ \dualof{\mce}\otimes_{\OO_X}\mcf \cong\sheafhom_{\OO_X}(\mce,\mcf).
$$

(c) For any $\OO_X$-modules $\mcf$ and $\mcg$, show that there is a natural isomorphism $$ \Hom_{\OO_X}(\mce\otimes_{\OO_X}\mcf,\mcg) \cong\Hom_{\OO_X}\bigl(\mcf,\sheafhom_{\OO_X}(\mce,\mcg)\bigr).
$$

(d) (Projection formula.)
    If $f:(X,\OO_X)\to(Y,\OO_Y)$ is a morphism of ringed spaces, if $\mcf$ is an $\OO_X$-module, and if $\mce$ is a locally free $\OO_Y$-module of finite rank, then there is a natural isomorphism $$ f_*\bigl(\mcf\otimes_{\OO_X}f^*\mce\bigr) \cong f_*\mcf\otimes_{\OO_Y}\mce.
$$
:::

::: {.solution}
For sheaves of modules $\mathcal A,\mathcal B$ on $X$, the sections of $\sheafhom_{\OO_X}(\mathcal A,\mathcal B)$ on an open set $U$ are the $\OO_U$-linear sheaf morphisms $\mathcal A|_U\to\mathcal B|_U$.
Here $\OO_U=\OO_X|_U$; in particular $\Hom_{\OO_X}(\mathcal A,\mathcal B)$ is the module of global sections of this sheaf [@Har10a, Chapter II, §5].
Tensor products in parts (a)-(c) are over $\OO_X$.

<1>1. For part (a), the evaluation morphism $\delta:\mce\dualof{\to(\dualof{\mce})}$ is an isomorphism.

::: {.proof}
For an open set $U$ and $e\in\mce(U)$, define $\delta_U(e)$ by the compatible maps
$$
\dualof{\mce}(V)\longrightarrow\OO_X(V),
\qquad\lambda\longmapsto\lambda_V(e|_V),
\qquad V\subseteq U.
$$
These maps are linear and compatible with restriction, so they define the morphism $\delta$.

On a trivializing open set $U$, choose a frame $e_1,\ldots,e_r$ for $\mce|_U$ and its coordinate functionals $\dualof{e_1},\ldots,\dualof{e_r}$.
These functionals form a frame for $\dualof{\mce}|_U$: a sheaf morphism $\mce|_V\to\OO_V$ is determined uniquely by its values on the restricted $e_j$ for every $V\subseteq U$.
For $h\dualof{\in(\dualof{\mce})}(V)$, the formula
$$
h\longmapsto\sum_{j=1}^r h_V(\dualof{e_j}|_V)e_j|_V
$$
is inverse to $\delta_V$.
Thus $\delta$ is locally, and hence globally, an isomorphism.
The defining evaluation formula commutes with morphisms of locally free sheaves, so it is natural and does not depend on the frames used to verify it.
:::

<1>2. For part (b), the morphism $\beta:\dualof{\mce}\otimes\mcf\to\sheafhom_{\OO_X}(\mce,\mcf)$ defined by evaluation and scalar multiplication is an isomorphism.

::: {.proof}
For $\lambda\in\dualof{\mce}(U)$ and $s\in\mcf(U)$, define $\beta_U(\lambda\otimes s)$ on each $V\subseteq U$ by
$$
e\longmapsto\lambda_V(e)s|_V,
\qquad e\in\mce(V).
$$
This construction is balanced over $\OO_X(U)$ and compatible with restrictions.
It therefore induces $\beta$ by the universal property of the sheaf tensor product.

On an open set $U$ with frame $e_1,\ldots,e_r$ and dual frame $\dualof{e_1},\ldots,\dualof{e_r}$, the inverse sends a sheaf morphism $\theta:\mce|_V\to\mcf|_V$, for $V\subseteq U$, to
$$
\sum_{j=1}^r \dualof{e_j}|_V\otimes\theta_V(e_j|_V).
$$
Evaluation on the frame proves that applying $\beta$ to this section recovers $\theta$.
Conversely, the identity $\lambda=\sum_j\lambda(e_j)\dualof{e_j}$ proves that the reverse composite fixes every local elementary tensor, and these tensors locally generate the tensor product sheaf.
Thus $\beta$ is an isomorphism.
Its evaluation formula commutes with precomposition in $\mce$ and postcomposition in $\mcf$, giving naturality.
:::

<1>3. For part (c), currying gives the natural tensor–Hom adjunction.

::: {.proof}
Given an $\OO_X$-linear morphism $\varphi:\mce\otimes\mcf\to\mcg$, define
$$
C(\varphi):\mcf\longrightarrow\sheafhom_{\OO_X}(\mce,\mcg)
$$
as follows.
For $s\in\mcf(U)$, its image is the sheaf morphism whose component on $V\subseteq U$ sends $e\in\mce(V)$ to $\varphi_V(e\otimes s|_V)$.
Linearity and compatibility with restrictions follow from the corresponding properties of $\varphi$.

Conversely, for an $\OO_X$-linear morphism $\psi:\mcf\to\sheafhom_{\OO_X}(\mce,\mcg)$, the maps
$$
\mce(U)\times\mcf(U)\longrightarrow\mcg(U),
\qquad (e,s)\longmapsto\bigl(\psi_U(s)\bigr)_U(e)
$$
are bilinear and compatible with restrictions.
They induce a unique morphism $D(\psi):\mce\otimes\mcf\to\mcg$.

The definitions give $D(C(\varphi))=\varphi$ on local elementary tensors, hence on the tensor product sheaf, and $C(D(\psi))=\psi$ on every open set.
Thus $C$ and $D$ are inverse module homomorphisms.
They commute with precomposition in $\mce,\mcf$ and postcomposition in $\mcg$, proving naturality.
The same constructions on each open subspace commute with restriction, so they also prove
$$
\sheafhom_{\OO_X}(\mce\otimes\mcf,\mcg)
\cong\sheafhom_{\OO_X}\bigl(\mcf,\sheafhom_{\OO_X}(\mce,\mcg)\bigr).
$$
:::

<1>4. For part (d), the canonical projection morphism
$$
\pi:f_*\mcf\otimes_{\OO_Y}\mce
\longrightarrow f_*\bigl(\mcf\otimes_{\OO_X}f^*\mce\bigr)
$$
is an isomorphism.

::: {.proof}
For an open set $U\subseteq Y$, a section $s\in\mcf(f^{-1}U)$, and a section $e\in\mce(U)$, let $f^*e\in(f^*\mce)(f^{-1}U)$ denote its pullback.
The rule $s\otimes e\mapsto s\otimes f^*e$ is balanced over $\OO_Y(U)$ and compatible with restriction.
Sheafification therefore gives $\pi$.

Take an open cover of $Y$ by sets $U$ on which $\mce|_U\cong\OO_U^{\oplus r}$.
Then $(f^*\mce)|_{f^{-1}U}\cong\OO_{f^{-1}U}^{\oplus r}$.
Tensoring with either finite free sheaf takes the corresponding finite direct sum, and direct image commutes with finite direct sums because its sections are computed on inverse images of open sets.
Thus both the source and target of $\pi|_U$ identify with $(f_*\mcf|_U)^{\oplus r}$.
On these identifications $\pi|_U$ is the identity, since each frame section pulls back to the corresponding frame section.
It follows that $\pi$ is an isomorphism on $Y$, and its inverse gives the displayed direction in part (d). The defining formula commutes with morphisms of $\mcf$ and $\mce$, so the isomorphism is natural.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1, <1>2, <1>3, and <1>4 prove parts (a), (b), (c), and (d), respectively.
:::
:::
