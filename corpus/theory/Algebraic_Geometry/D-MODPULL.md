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

::: {.definition title="Direct and inverse image"}
For $f: X \to Y$ of ringed spaces, $f_*\mcf$ is the $\OO_Y$-module $U \mapsto \mcf(f\inv U)$.
For $\mcg \in \mods{\OO_Y}$, the **inverse image** is
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
$f^*$ is right exact: on quasicoherent sheaves over affines it corresponds to $\wait \tensor_A B$.
$f_*$ is left exact, and its right derived functors are the higher direct images $R^i f_*$. Its failure to preserve coherence is visible already in $f: \AA^1_k \to \Spec k$, where $f_*\OO_{\AA^1}$ has global sections $k[t]$, not finite over $k$.
For $f$ proper between Noetherian schemes and $\mcf$ coherent, every $R^i f_*\mcf$ is coherent.

On line bundles $f^*$ is a group homomorphism $\Pic(Y) \to \Pic(X)$. A very ample line bundle is obtained by pulling back $\OO(1)$ along an immersion into projective space.
:::
