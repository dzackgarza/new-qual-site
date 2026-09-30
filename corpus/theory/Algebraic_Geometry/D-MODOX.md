---
schema: qual/card@1
id: D-MODOX
kind: definition
title: Sheaves of modules, and the operations on them
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves Of Modules
  - Tensor Product
  - Sheaf Hom
relations:
- kind: related-to
  target: D-QNTZY
review: draft
prompts:
- What is an $\OO_X$-module?
- What is the tensor product of two $\OO_X$-modules?
- What is the sheaf hom, and why does it need no sheafification?
---

::: {.definition title="$\OO_X$-modules"}
An \dfn{$\OO_X$-module} is a sheaf $\mcf$ on $X$ with each $\mcf(U)$ an $\OO_X(U)$-module, compatibly with restriction: $\restrictionof{(rm)}{V} = \restrictionof{r}{V}\restrictionof{m}{V}$.
The \dfn{tensor product} $\mcf \tensor_{\OO_X} \mcg$ is the sheafification of $U \mapsto \mcf(U) \tensor_{\OO_X(U)} \mcg(U)$.
The \dfn{sheaf hom} $\sheafhom_{\OO_X}(\mcf, \mcg)$ is $U \mapsto \Hom_{\restrictionof{\OO_X}{U}}(\restrictionof{\mcf}{U}, \restrictionof{\mcg}{U})$.
A \dfn{sheaf of ideals} is a subsheaf $\mci \subseteq \OO_X$ of $\OO_X$-modules.
:::

::: {.remark}
The presheaf $U \mapsto \mcf(U) \tensor_{\OO_X(U)} \mcg(U)$ need not be a sheaf: on $X=\PP^1_k$, its value on $X$ for $\mcf=\OO(1)$ and $\mcg=\OO(-1)$ is $H^0(\OO(1))\tensor_kH^0(\OO(-1))=0$, while $\OO(1)\tensor\OO(-1)\cong\OO_X$ has the global section $1$.
Morphisms of sheaves defined on the members of an open cover and agreeing on overlaps glue uniquely, so $U\mapsto\Hom_{\restrictionof{\OO_X}{U}}(\restrictionof{\mcf}{U}, \restrictionof{\mcg}{U})$ is already a sheaf.

The functor $\wait\tensor_{\OO_X}\mcg$ is right exact, and $\sheafhom_{\OO_X}(\mcf,\wait)$ is left exact.
For every $x\in X$, $(\mcf \tensor \mcg)_x \cong \mcf_x \tensor_{\OO_{X,x}} \mcg_x$.
If $X$ is Noetherian and $\mcf$ is coherent, then $\sheafhom(\mcf,\mcg)_x \cong \Hom_{\OO_{X,x}}(\mcf_x, \mcg_x)$ [@Har10a, Proposition III.6.8].

$\mods{\OO_X}$ has enough injectives [@Har10a, Proposition III.2.2], but it need not have enough projectives.
On $\PP_k^1$ over an infinite field, no projective object surjects onto $\OO_X$, as proved in [[P-AGH362NOPROJECTIVES]].
In contrast, on a one-point ringed space with structure ring $A$, a sheaf of modules is just an $A$-module; free-module surjections show that this category has enough projectives.
:::
