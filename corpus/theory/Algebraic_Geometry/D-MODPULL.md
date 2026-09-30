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
The \dfn{inverse image sheaf} $\inverseof{f} \mcg$ is the sheafification of the presheaf
$$
U \mapsto \colim_{V \supseteq f(U)} \mcg(V) ,
$$
the colimit over open subsets $V \subseteq Y$ containing $f(U)$.
If $i: Z \injects X$ is the inclusion of a subspace, the \dfn{restriction} of a sheaf $\mcf$ on $X$ is $\restrictionof{\mcf}{Z} \definedas \inverseof{i} \mcf$.
:::

::: {.proposition}
$\inverseof{f}$ is left adjoint to $f_*$ on sheaves of abelian groups, and for $x \in X$ the stalk is $(\inverseof{f} \mcg)_x = \mcg_{f(x)}$; in particular $(\restrictionof{\mcf}{Z})_x = \mcf_x$ for $x \in Z$.
If $\mcg$ is an $\OO_Y$-module, then $\inverseof{f} \mcg$ is an $\inverseof{f} \OO_Y$-module, which need not be an $\OO_X$-module.
[@Har10a, §II.1, Exercise II.1.18]
:::

::: {.definition title="Direct and inverse image"}
For $f: X \to Y$ of ringed spaces, $f_*\mcf$ is the $\OO_Y$-module $U \mapsto \mcf(\inverseof{f} U)$.
For $\mcg \in \mods{\OO_Y}$, the \dfn{inverse image} is
$$
f^*\mcg \definedas \inverseof{f} \mcg \tensor_{\inverseof{f} \OO_Y} \OO_X ,
$$
the sheaf-theoretic inverse image, base changed along $\inverseof{f}\OO_Y \to \OO_X$.
:::

::: {.proposition}
$f^*$ is left adjoint to $f_*$: there is a natural isomorphism
$$
\Hom_{\OO_X}(f^*\mcg, \mcf) \cong \Hom_{\OO_Y}(\mcg, f_*\mcf) .
$$
$f^*$ preserves quasicoherence always, and coherence when $f$ is a morphism of Noetherian schemes; $f_*$ preserves quasicoherence for $f$ quasicompact and separated.
:::

::: {.remark}
For a morphism $\Spec B\to\Spec A$ of affine schemes, $f^*\tilde M\cong\widetilde{M\tensor_AB}$, so $f^*$ is right exact on quasicoherent sheaves.
The functor $f_*$ is left exact, and its right derived functors are the higher direct images $R^i f_*$.
For $f: \AA^1_k \to \Spec k$, $f_*\OO_{\AA^1}$ corresponds to the $k$-module $k[t]$, which is not finitely generated, so $f_*$ does not preserve coherence.
If $Y$ is Noetherian, $f$ is projective, and $\mcf$ is coherent, then every $R^i f_*\mcf$ is coherent [@Har10a, Theorem III.8.8]; the same holds for $f$ proper.

On line bundles $f^*$ is a group homomorphism $\Pic(Y) \to \Pic(X)$.
A very ample line bundle is obtained by pulling back $\OO(1)$ along an immersion into projective space.
:::
