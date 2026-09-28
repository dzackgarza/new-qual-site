---
schema: qual/card@1
id: D-MODPIC
kind: definition
title: The Picard group
classification:
  areas:
  - algebraic-geometry
  topics:
  - Picard Group
  - Line Bundles
  - Tensor Product
relations:
- kind: uses
  target: T-MODVB
- kind: related-to
  target: D-CB9XS
review: draft
prompts:
- What is the Picard group?
- Why is the inverse of an invertible sheaf its dual?
- What is $\Pic$ of an affine scheme, of $\PP^n$, of a curve?
---

::: {.definition title="Picard group"}
Let $(X,\OO_X)$ be a ringed space with commutative structure sheaf.
Its \dfn{Picard group} $\Pic(X)$ is the group of isomorphism classes of invertible $\OO_X$-modules under tensor product, with identity $[\OO_X]$ and inverse $[\dualof{\mcl}]$, where $\dualof{\mcl}=\sheafhom_{\OO_X}(\mcl,\OO_X)$ [@Har10a, Chapter II, §6].
:::

::: {.proposition}
For $\mcl$ invertible, the evaluation map $\mcl\otimes_{\OO_X}\dualof{\mcl}\to\OO_X$ is an isomorphism: on every trivializing open it is the multiplication isomorphism $\OO_X\otimes\OO_X\cong\OO_X$.
There is a natural group isomorphism $\Pic(X)\cong H^1(X,\OO_X^\times)$, obtained by sending local frames to their transition-unit cocycle, as proved in [[P-AGH345PICH1]].
:::

::: {.remark title="Rank and tensor inverses"}
On a nonempty scheme, a locally free sheaf of constant rank $r\ge2$ has no tensor inverse.
At any point, an inverse would give $\kappa(x)^r\otimes_{\kappa(x)}V\cong\kappa(x)$ for a vector space $V$.
For $V=0$ the left side is zero; otherwise it contains at least $r$ independent vectors and cannot be one-dimensional.
:::

::: {.proposition title="Affine and projective examples"}
For a PID or a local ring $A$, one has $\Pic(\Spec A)=0$.
Under the affine sheaf-module correspondence, invertible sheaves correspond to finite projective modules of rank one; these are free over either such ring [@Har10a, Chapter II, §§5 and 6].
For a field $k$ and $n\ge1$, one has $\Pic(\PP_k^n)\cong\ZZ$, with generator $[\OO(1)]$ [@Har10a, Proposition II.6.4 and Corollary II.6.16].
For $n=0$, projective space is $\Spec k$ and its Picard group is zero.
:::

::: {.proposition title="Cartier--Weil comparison"}
For an integral noetherian separated locally factorial scheme $X$, the correspondence $D\mapsto\OO_X(D)$ identifies the [[D-5PQ5W|Weil divisor class group]] with $\Pic(X)$ [@Har10a, Corollary II.6.16].
In particular it applies to a smooth integral variety over a field, since its regular local rings are factorial [@Har10a, Remark II.6.11.1A].
:::
