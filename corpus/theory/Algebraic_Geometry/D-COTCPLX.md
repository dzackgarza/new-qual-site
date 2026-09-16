---
schema: qual/card@1
id: D-COTCPLX
kind: definition
title: The cotangent complex and its dual
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cotangent Complex
  - Deformation Theory
  - Derived Categories
relations:
- kind: uses
  target: D-4GCH6
review: draft
prompts:
- What is the cotangent complex?
- Why does dualizing the cotangent complex termwise not yield the tangent complex, and what is the correct dual?
---

::: {.definition title="Cotangent complex"}
For a morphism of schemes $f \colon X \to Y$, the \dfn{cotangent complex} $L_{X/Y}$ is an object of the derived category of $\OO_X$-modules, concentrated in nonpositive degrees, with $H^0(L_{X/Y}) = \Omega_{X/Y}$.
It is built from a simplicial resolution of $\OO_X$ by free $f^{-1}\OO_Y$-algebras, by applying $\Omega$ termwise.
:::

::: {.proposition}
1. If $f$ is smooth, $L_{X/Y} \simeq \Omega_{X/Y}[0]$.
2. If $X \hookrightarrow P$ is a closed immersion with ideal $\mathcal{I}$ into a smooth $Y$-scheme $P$ and $X \to Y$ is a local complete intersection, then $L_{X/Y} \simeq [\mathcal{I}/\mathcal{I}^2 \to \Omega_{P/Y}|_X]$ in degrees $-1$ and $0$.
3. A composition $X \to Y \to Z$ gives a distinguished triangle $f^* L_{Y/Z} \to L_{X/Z} \to L_{X/Y} \to$, extending the two exact sequences of differentials.
:::

::: {.definition title="Tangent complex"}
The \dfn{tangent complex} is the derived dual $T_{X/Y} = R\mathcal{H}om_{\OO_X}(L_{X/Y}, \OO_X)$.
:::

::: {.remark}
The derived dual is required because $L_{X/Y}$ is an object of the derived category, and a termwise dual of a chosen representative is not invariant under quasi-isomorphism unless the representative consists of locally free sheaves.
For the lci representative in part 2 the terms are locally free, and the termwise dual $[T_{P/Y}|_X \to \mathcal{N}_{X/P}]$ does compute $T_{X/Y}$.
For example, let $k$ have characteristic not $2$ and $A = k[x]/(x^2)$, a local complete intersection over $k$.
Its cotangent complex is $L_{A/k} \simeq [A \xrightarrow{\,2x\,} A]$ in degrees $-1, 0$, the lci complex $(x^2)/(x^4) \to A\, dx$ with $x^2 \mapsto 2x\, dx$.
So $\operatorname{Ext}^i_A(L_{A/k}, A)$ is $\ker(2x) = (x) \cong k$ for $i = 0$, $\operatorname{coker}(2x) = A/(x) \cong k$ for $i = 1$, and $0$ for $i \geq 2$: one infinitesimal automorphism, the first-order deformation $k[x, \varepsilon]/(x^2 - \varepsilon)$, and no obstructions.
The naive groups $\operatorname{Ext}^i_A(\Omega_{A/k}, A)$, with $\Omega_{A/k} = A\,dx/(2x\,dx) \cong k$, are $k$ for $i = 0$ and $0$ for $i \geq 1$, because $A$ is injective as a module over itself; the naive dual misses the first-order deformation.
:::
