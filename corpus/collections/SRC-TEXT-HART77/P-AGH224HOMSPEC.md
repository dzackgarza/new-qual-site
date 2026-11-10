---
schema: qual/card@1
id: P-AGH224HOMSPEC
kind: problem
title: Morphisms to an affine scheme are ring maps into global sections
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Adjoint Functors
  - Global Sections
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.2.4 statement and source-order placement after II.2.3.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $A$ be a ring and let $(X, \OO_X)$ be a scheme.
Given a morphism $f: X \to \Spec A$, we have an associated map on sheaves $f^{\sharp}: \OO_{\Spec A} \to f_* \OO_X$.
Taking global sections we obtain a homomorphism $A \to \Gamma(X, \OO_X)$.
Thus there is a natural map
$$
\alpha: \Hom_{\Sch}(X, \Spec A) \to \Hom_{\Ring}\qty{A, \Gamma(X, \OO_X)}.
$$
Show that $\alpha$ is bijective.
:::

::: {.solution}
We use the affine case: for rings $A,B$ there is a natural bijection
$$
\Hom_{\Sch}(\Spec B,\Spec A)
\cong
\Hom_{\Ring}(A,B).
$$

::: pf

::: pf-step
Let
$$
\varphi:A\longrightarrow\Gamma(X,\OO_X)
$$
be a ring homomorphism.  Choose an affine open cover
$$
X=\bigcup_iU_i,
\qquad
U_i=\Spec B_i.
$$
Restriction gives ring homomorphisms
$$
\varphi_i:
A\xrightarrow{\varphi}
\Gamma(X,\OO_X)
\longrightarrow
\Gamma(U_i,\OO_X)
=B_i.
$$

::: pf-proof
The equality
$$
\Gamma(U_i,\OO_X)=B_i
$$
is the defining global-section property of the affine chart $U_i\cong\Spec B_i$.  Composition with restriction therefore gives the displayed maps.
:::

:::

::: pf-step
Each $\varphi_i$ determines a unique morphism of affine schemes
$$
f_i:U_i\longrightarrow\Spec A.
$$

::: pf-proof
Apply the affine anti-equivalence to the ring map
$$
\varphi_i:A\to B_i.
$$
:::

:::

::: {.pf-step #fi-agree-on-overlaps}
For every pair $i,j$, the morphisms $f_i$ and $f_j$ agree on the overlap
$$
U_i\cap U_j.
$$

::: pf-proof
Cover the open subscheme
$$
U_i\cap U_j
$$
by affine opens
$$
W=\Spec C.
$$

The restriction
$$
f_i\restrict_W:W\to\Spec A
$$
corresponds, in the affine anti-equivalence, to the composite
$$
A
\xrightarrow{\varphi}
\Gamma(X,\OO_X)
\longrightarrow
\Gamma(U_i,\OO_X)
\longrightarrow
\Gamma(W,\OO_X)=C.
$$
The restriction $f_j\restrict_W$ corresponds to the same composite, because both restriction chains are the restriction of the same global section to $W$.

Hence
$$
f_i\restrict_W=f_j\restrict_W
$$
for every affine $W$ in a cover of $U_i\cap U_j$.  Morphisms of schemes are local on the source, so
$$
f_i\restrict_{U_i\cap U_j}=f_j\restrict_{U_i\cap U_j}.
$$
:::

:::

::: pf-step
The local morphisms $f_i$ glue uniquely to a morphism
$$
\boxed{
f_\varphi:X\longrightarrow\Spec A.
}
$$

::: pf-proof
By step [](#fi-agree-on-overlaps){.pf-ref} the morphisms $f_i$ agree on every pairwise overlap.  Morphisms of locally ringed spaces glue over an open cover of the source: the underlying continuous maps glue because they agree on overlaps, and for every open subset $W$ of the target the maps
$$
\OO_{\Spec A}(W)
\longrightarrow
\OO_X(U_i\cap f_i^{-1}(W))
$$
glue, by the sheaf axiom for $\OO_X$, to the required map on
$$
f_\varphi^{-1}(W).
$$
The induced stalk maps are local because this can be checked on the open cover $\{U_i\}$, where they are the stalk maps of the scheme morphisms $f_i$.

Hence the $f_i$ glue to a scheme morphism $f_\varphi$.  Uniqueness follows because two morphisms agreeing on every $U_i$ agree globally.
:::

:::

::: {.pf-step #alpha-surjective}
The homomorphism on global sections induced by $f_\varphi$ is exactly the original map $\varphi$.

::: pf-proof
Let
$$
\alpha(f_\varphi):A\to\Gamma(X,\OO_X)
$$
be the pullback on global sections.

For every $i$, restricting $\alpha(f_\varphi)(a)$ to $U_i$ gives the global-section pullback of
$$
f_\varphi\restrict_{U_i}=f_i.
$$
By construction of $f_i$, this is
$$
\varphi_i(a)
=\varphi(a)\restrict_{U_i}.
$$
Thus the two global sections
$$
\alpha(f_\varphi)(a),
\qquad
\varphi(a)
$$
have equal restrictions to every member of the open cover $\{U_i\}$.  Since $\OO_X$ is a sheaf, they are equal.  This holds for every $a\in A$, so
$$
\alpha(f_\varphi)=\varphi.
$$
Hence $\alpha$ is surjective.
:::

:::

::: {.pf-step #alpha-injective}
The map $\alpha$ is injective.

::: pf-proof
Suppose
$$
f,g:X\longrightarrow\Spec A
$$
induce the same ring homomorphism
$$
\varphi:A\longrightarrow\Gamma(X,\OO_X).
$$

Choose an affine open cover
$$
X=\bigcup_iU_i,
\qquad
U_i=\Spec B_i.
$$
The restrictions
$$
f\restrict_{U_i},g\restrict_{U_i}:U_i\to\Spec A
$$
induce the same ring homomorphism
$$
A
\xrightarrow{\varphi}
\Gamma(X,\OO_X)
\longrightarrow
B_i,
$$
because pullback on global sections commutes with restriction to an open subset of the source.

By the affine anti-equivalence,
$$
f\restrict_{U_i}=g\restrict_{U_i}
$$
for every $i$.  Since the $U_i$ cover $X$, the two morphisms are equal globally:
$$
f=g.
$$
Thus $\alpha$ is injective.
:::

:::

::: {.pf-step #alpha-bijective}
Therefore
$$
\boxed{
\Hom_{\Sch}(X,\Spec A)
\cong
\Hom_{\Ring}
\bigl(A,\Gamma(X,\OO_X)\bigr).
}
$$

::: pf-proof
Step [](#alpha-surjective){.pf-ref} proves surjectivity and step [](#alpha-injective){.pf-ref} proves injectivity.  The constructions use only restriction and the affine anti-equivalence, so the bijection is natural in both $X$ and $A$.
:::

:::

::: pf-qed
Step [](#alpha-bijective){.pf-ref} is exactly the bijectivity of $\alpha$ required by the exercise.
:::

:::

:::

::: {.remark title="Published solution"}
Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Chapter II §2, Exercise 2.4, PDF p. 13, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`: he proves the affine case first, then observes that both sides are sheaves on the big Zariski site: over an affine cover $X=\bigcup\Spec A_i$ the left side is the equalizer of $\prod_i\Hom(\Spec A_i,\Spec A)\rightrightarrows\prod_{i,j,k}\Hom(\Spec A_{ijk},\Spec A)$, hence of $\prod_i\Hom(A,A_i)\rightrightarrows\prod_{i,j,k}\Hom(A,A_{ijk})$, and $\Gamma(X,\OO_X)$ is the equalizer of the same diagram.
The proof above is that equalizer argument written out as gluing without the site language: the restrictions $\varphi_i$ give $f_i$ by the affine anti-equivalence, the $f_i$ agree on overlaps because both are induced by restriction of the same global sections, they glue, and $\alpha$ is then shown to be bijective by comparing restrictions to an affine cover.
Agree in substance.
:::
