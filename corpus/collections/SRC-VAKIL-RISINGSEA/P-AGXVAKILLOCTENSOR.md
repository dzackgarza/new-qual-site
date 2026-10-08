---
schema: qual/card@1
id: P-AGXVAKILLOCTENSOR
kind: problem
title: Localization of a module as a tensor product with $S^{-1}A$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Localization
  - Tensor Products
  - Universal Properties
relations: []
review: draft
---

::: {.problem}
If $S\subseteq A$ is multiplicative and $M\in \mods{A}$, describe a natural isomorphism
\[
\eta: (S^{-1}A)\tensor_A M \to S^{-1}M
\]
of both $S^{-1}A\dash$modules and $A\dash$modules.
:::

::: {.solution}
Let $A$ be a commutative ring, $S\subseteq A$ a multiplicative subset, and $M$ an $A$-module. Both $(S^{-1}A)\otimes_A M$ and $S^{-1}M$ carry their canonical $S^{-1}A$-module structures.

<1>1. There is an $S^{-1}A$-linear map
\[
\eta:(S^{-1}A)\otimes_A M\longrightarrow S^{-1}M,
\qquad \eta\left(\frac a s\otimes m\right)=\frac{am}{s}.
\]

::: {.proof}
For fixed $m$, the assignment $a/s\mapsto am/s$ is well-defined: if $a/s=a'/s'$, some $t\in S$ annihilates $s'a-sa'$, hence also $s'am-sa'm$. It is additive. The map
\[
(S^{-1}A)\times M\longrightarrow S^{-1}M,\qquad
\left(\frac a s,m\right)\longmapsto\frac{am}{s}
\]
is additive in $m$ and $A$-balanced since, for $r\in A$,
\[
\frac{(ra)m}{s}=\frac{a(rm)}{s}.
\]
It therefore factors uniquely through the tensor product. For $b/t\in S^{-1}A$, its value on an elementary tensor satisfies
\[
\eta\left(\frac bt\left(\frac as\otimes m\right)\right)
=\frac{bam}{ts}
=\frac bt\,\eta\left(\frac as\otimes m\right).
\]
Additivity proves $S^{-1}A$-linearity.
:::

<1>2. There is an $S^{-1}A$-linear map
\[
\theta:S^{-1}M\longrightarrow(S^{-1}A)\otimes_A M,
\qquad \theta\left(\frac ms\right)=\frac1s\otimes m.
\]

::: {.proof}
Suppose $m/s=m'/s'$. Then some $t\in S$ satisfies $t(s'm-sm')=0$. In the tensor product,
\[
\frac1s\otimes m-\frac1{s'}\otimes m'
=\frac1{ss'}\otimes(s'm-sm')=0,
\]
because multiplication by $t$ is invertible on the $S^{-1}A$-module and the displayed element becomes zero after multiplication by $t$. Thus $\theta$ is well-defined. The fraction identities and the tensor-product relations show that $\theta$ is additive. Finally, for $a/t\in S^{-1}A$,
\[
\theta\left(\frac at\cdot\frac ms\right)
=\frac1{ts}\otimes am
=\frac at\left(\frac1s\otimes m\right).
\]
Hence $\theta$ is $S^{-1}A$-linear.
:::

<1>3. The maps $\eta$ and $\theta$ are inverse isomorphisms, natural in $M$.

::: {.proof}
For $m/s\in S^{-1}M$ and an elementary tensor $(a/s)\otimes m$,
\[
\eta\theta\left(\frac ms\right)=\frac ms,
\qquad
\theta\eta\left(\frac as\otimes m\right)
=\frac1s\otimes am=\frac as\otimes m.
\]
Elementary tensors generate the tensor product, so both composites are identities. Given an $A$-linear morphism $f:M\to N$, the localization $S^{-1}f$ sends $m/s$ to $f(m)/s$, while $(\operatorname{id}_{S^{-1}A}\otimes f)$ sends $(a/s)\otimes m$ to $(a/s)\otimes f(m)$. Their composites with the corresponding $\eta$ agree on elementary tensors, proving naturality.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 proves the claimed natural isomorphism of $S^{-1}A$-modules. Restriction of scalars along $A\to S^{-1}A$ also makes it an isomorphism of $A$-modules.
:::
:::
