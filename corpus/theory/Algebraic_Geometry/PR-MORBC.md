---
schema: qual/card@1
id: PR-MORBC
kind: proposition
title: Which properties are stable under base change and composition
slogan: 'The standard geometric properties of morphisms are universal: they survive composition and arbitrary base change.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Base Change
  - Fibre Products
  - Morphisms
relations:
- kind: uses
  target: D-MORFIB
review: draft
prompts:
- Name some properties of morphisms preserved by base change.
- Is properness stable under base change?
---

::: {.proposition}
Each of the following properties of morphisms of schemes is preserved by arbitrary base change and by composition:

- open immersion and closed immersion;
- affine, finite, and integral;
- quasicompact, locally of finite type, of finite type, and quasi-finite;
- flat and surjective;
- separated, proper, and projective;
- smooth, unramified, and étale.

[@Har77, Chapters II.3--4 and III.10]
:::

::: {.remark}
For an affine morphism induced by $A\to B$, base change along $A\to A'$ replaces the coordinate ring by $B\tensor_A A'$. Finiteness, integrality, finite type, and flatness are preserved by this operation. Open and closed immersions are preserved by the corresponding localization and quotient constructions. The geometric properties in the last two rows have base-change and composition stability as part of their standard theorems.

Being a closed map of underlying topological spaces is not stable under base change. The structure morphism $\AA^1_k\to\Spec k$ is closed, but after base change by $\AA^1_k\to\Spec k$ it becomes the projection
$$
\AA^2_k\longrightarrow\AA^1_k.
$$
The closed hyperbola $V(xy-1)\subseteq\AA^2_k$ has image $D(x)=\AA^1_k\sm V(x)$, which is not closed. Universal closedness is precisely closedness after every base change.

Dominance is also not stable under arbitrary base change. The morphism
$$
\Spec k(t)\longrightarrow\Spec k[t]
$$
is dominant, but its base change to the point $t=0$ is empty because
$$
k(t)\tensor_{k[t]}k=0.
$$

If a property in the proposition is stable under base change, every fibre inherits it from the original morphism. Thus a proper morphism has proper fibres, and a smooth morphism has smooth geometric fibres; after any field extension of the base, the corresponding base-changed morphism remains proper or smooth.
:::
