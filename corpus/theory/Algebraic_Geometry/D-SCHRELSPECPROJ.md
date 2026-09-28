---
schema: qual/card@1
id: D-SCHRELSPECPROJ
kind: definition
title: Relative Spec and relative Proj
classification:
  areas:
  - algebraic-geometry
  topics:
  - Relative Spec
  - Relative Proj
  - Affine Morphisms
relations:
- kind: uses
  target: D-QNTZY
- kind: related-to
  target: D-MORAFF
- kind: related-to
  target: D-MORPROJ
review: draft
prompts:
- What is the relative Spec of a quasicoherent sheaf of algebras, and what universal property does it have?
- How is the relative Proj of a graded quasicoherent sheaf of algebras constructed?
---

::: {.definition title="Relative Spec"}
Let $X$ be a scheme and $\mathcal{A}$ a quasicoherent sheaf of $\OO_X$-algebras.
The \dfn{relative Spec} of $\mathcal{A}$ is an $X$-scheme $\pi \colon \operatorname{\mathbf{Spec}}_X \mathcal{A} \to X$ representing the functor on $X$-schemes
$$(t \colon T \to X) \longmapsto \Hom_{\OO_X\text{-alg}}(\mathcal{A}, t_* \OO_T),$$
so that for every $X$-scheme $t \colon T \to X$ there is a bijection, natural in $T$,
$$\Hom_X(T, \operatorname{\mathbf{Spec}}_X \mathcal{A}) \cong \Hom_{\OO_X\text{-alg}}(\mathcal{A}, t_* \OO_T).$$
:::

::: {.proposition}
The relative Spec exists and is unique up to unique isomorphism.
For every affine open $V = \Spec B \subseteq X$ with $\mathcal{A}|_V \cong \widetilde{A}$ for a $B$-algebra $A$, $\pi^{-1}(V) \cong \Spec A$ over $V$.
In particular $\pi$ is affine, $\pi_* \OO_{\operatorname{\mathbf{Spec}}_X \mathcal{A}} \cong \mathcal{A}$, and $\mathcal{A} \mapsto \operatorname{\mathbf{Spec}}_X \mathcal{A}$ is an anti-equivalence from quasicoherent $\OO_X$-algebras to affine morphisms with target $X$ ([[P-AGH2517AFFMOR]]).
:::

::: {.definition title="Relative Proj"}
Let $X$ be a scheme and $\mathcal{S} = \bigoplus_{d \geq 0} \mathcal{S}_d$ a quasicoherent sheaf of graded $\OO_X$-algebras with $\mathcal{S}_0 = \OO_X$, generated in degree $1$: the map $\operatorname{Sym}^\bullet_{\OO_X} \mathcal{S}_1 \to \mathcal{S}$ is surjective.
The \dfn{relative Proj} $\operatorname{\mathbf{Proj}}_X \mathcal{S} \to X$ is the $X$-scheme obtained by gluing the schemes $\Proj \mathcal{S}(V) \to V$, for affine opens $V \subseteq X$, along the isomorphisms
$$\Proj \mathcal{S}(V) \times_V V' \cong \Proj \mathcal{S}(V')$$
for affine opens $V' \subseteq V$, which come from $\mathcal{S}(V') \cong \mathcal{S}(V) \otimes_{\OO_X(V)} \OO_X(V')$.
It carries the invertible sheaf $\OO(1)$ obtained by gluing the sheaves $\OO_{\Proj \mathcal{S}(V)}(1)$.
:::

::: {.remark}
For $X = \Spec A$ affine, $\operatorname{\mathbf{Proj}}_X \mathcal{S} = \Proj \mathcal{S}(X)$.
For $\mathcal{S} = \operatorname{Sym}^\bullet \OO_X^{\oplus(n+1)}$ it is $\PP^n_X$.
A morphism $Y \to X$ isomorphic over $X$ to $\operatorname{\mathbf{Proj}}_X \mathcal{S}$, for such an $\mathcal{S}$ with $\mathcal{S}_1$ of finite type, is projective in the sense of EGA; when $X$ is affine this agrees with the definition in [[D-MORPROJ]] by a closed immersion into $\PP^n_X$.
:::
