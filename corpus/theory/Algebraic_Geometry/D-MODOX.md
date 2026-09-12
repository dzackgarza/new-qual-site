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
An **$\OO_X$-module** is a sheaf $\mcf$ on $X$ with each $\mcf(U)$ an $\OO_X(U)$-module, compatibly with restriction: $\ro{(rm)}{V} = \ro{r}{V}\ro{m}{V}$.
The **tensor product** $\mcf \tensor_{\OO_X} \mcg$ is the sheafification of $U \mapsto \mcf(U) \tensor_{\OO_X(U)} \mcg(U)$.
The **sheaf hom** $\sheafhom_{\OO_X}(\mcf, \mcg)$ is $U \mapsto \Hom_{\ro{\OO_X}{U}}(\ro{\mcf}{U}, \ro{\mcg}{U})$.
A **sheaf of ideals** is a subsheaf $\mci \subseteq \OO_X$ of $\OO_X$-modules.
:::

::: {.remark}
The sectionwise tensor-product presheaf need not satisfy the sheaf axioms. Morphisms of sheaves glue uniquely, so the sheaf-hom assignment already is a sheaf.
The functor $\tensor$ is right exact and $\sheafhom$ is left exact. The stalk formula $(\mcf \tensor \mcg)_x = \mcf_x \tensor \mcg_x$ holds while $\sheafhom(\mcf,\mcg)_x = \Hom(\mcf_x, \mcg_x)$ can fail without finiteness on $\mcf$.

$\mods{\OO_X}$ has enough injectives, so right derived functors define sheaf cohomology and $\Ext$; it need not have enough projectives.
:::
