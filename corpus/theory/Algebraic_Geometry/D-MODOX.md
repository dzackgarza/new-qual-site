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
Tensor product and sheaf Hom differ in how locality enters their construction.
Tensor needs sheafifying because a tensor product of sections is not determined locally; sheaf hom does not, because a morphism of sheaves is already a local object and the assignment is a sheaf on the nose.
The functor $\tensor_{\OO_X}$ is right exact and $\sheafhom_{\OO_X}$ is left exact.
Since sheafification preserves stalks, the stalk formula
$$
(\mcf\tensor_{\OO_X}\mcg)_x
\cong
\mcf_x\tensor_{\OO_{X,x}}\mcg_x
$$
holds, while
$$
\sheafhom_{\OO_X}(\mcf,\mcg)_x
\longrightarrow
\Hom_{\OO_{X,x}}(\mcf_x,\mcg_x)
$$
need not be an isomorphism without a finite-presentation hypothesis on $\mcf$.

$\mods{\OO_X}$ has enough injectives [@Har77, Proposition III.2.2], but it need not have enough projectives.
On $\PP_k^1$ over an infinite field, no projective object surjects onto $\OO_X$, as proved in [[P-AGH362NOPROJECTIVES]].
In contrast, on a one-point ringed space with structure ring $A$, a sheaf of modules is just an $A$-module; free-module surjections show that this category has enough projectives.
:::
