---
schema: qual/card@1
id: D-MODPULL
kind: definition
title: Pullback and pushforward of sheaves of modules
classification:
  areas:
  - algebraic-geometry
  topics:
  - Pullback
  - Pushforward
  - Adjunction
relations:
- kind: uses
  target: D-MODOX
- kind: uses
  target: D-QNTZY
review: draft
prompts:
- Define $f^*$ and $f_*$ for $\OO_X$-modules.
- What is the adjunction between them?
- Does $f_*$ preserve quasicoherence? Coherence?
---

::: {.definition title="Topological inverse image"}
Let $f: X \to Y$ be a continuous map and $\mcg$ a sheaf on $Y$.
The \dfn{inverse image sheaf} $f\inv \mcg$ is the sheafification of the presheaf
\[
U \mapsto \colim_{V \supseteq f(U)} \mcg(V) ,
\]
the colimit over open subsets $V \subseteq Y$ containing $f(U)$.
If $i: Z \injects X$ is the inclusion of a subspace, the **restriction** of a sheaf $\mcf$ on $X$ is $\ro{\mcf}{Z} \da i\inv \mcf$.
:::

::: {.proposition}
$f\inv$ is left adjoint to $f_*$ on sheaves of abelian groups, and for $x \in X$ the stalk is $(f\inv \mcg)_x = \mcg_{f(x)}$; in particular $(\ro{\mcf}{Z})_x = \mcf_x$ for $x \in Z$.
If $\mcg$ is an $\OO_Y$-module, then $f\inv \mcg$ is an $f\inv \OO_Y$-module, which need not be an $\OO_X$-module.
[@Har10a, §II.1, Exercise II.1.18]
:::

::: {.definition title="Direct and inverse image"}
For $f: X \to Y$ of ringed spaces, $f_*\mcf$ is the $\OO_Y$-module $U \mapsto \mcf(f\inv U)$.
For $\mcg \in \mods{\OO_Y}$, the \dfn{inverse image} is
\[
f^*\mcg \da f\inv \mcg \tensor_{f\inv \OO_Y} \OO_X ,
\]
the sheaf-theoretic inverse image, base changed along $f\inv\OO_Y \to \OO_X$.
:::

::: {.proposition}
$f^*$ is left adjoint to $f_*$: there is a natural isomorphism
\[
\Hom_{\OO_X}(f^*\mcg, \mcf) \cong \Hom_{\OO_Y}(\mcg, f_*\mcf) .
\]
$f^*$ preserves quasicoherence always, and coherence when $f$ is a morphism of Noetherian schemes; $f_*$ preserves quasicoherence for $f$ quasicompact and separated.
:::

::: {.remark}
The two halves behave differently and the difference is the exam question.
$f^*$ is right exact and easy: on affines it is $\wait \tensor_A B$, so it is the algebraic base change and inherits every good property of a tensor product.
$f_*$ is only left exact, and its failure to be exact is the definition of higher direct images $R^i f_*$; its failure to preserve coherence is visible already in $f: \AA^1_k \to \Spec k$, where $f_*\OO_{\AA^1}$ has global sections $k[t]$, not finite over $k$.
Properness is what repairs this: for $f$ proper and $\mcf$ coherent, every $R^i f_*\mcf$ is coherent.

On line bundles $f^*$ is a group homomorphism $\Pic(Y) \to \Pic(X)$, which is how $\OO(1)$ is transported to any scheme with a map to projective space, and hence how very ampleness is defined at all.
:::
