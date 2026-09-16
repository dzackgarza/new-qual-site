---
schema: qual/card@1
id: FE-SCHREPFUNCTORS
kind: example
title: The functors of points of $\AA^n$, $\AA^n \setminus \{0\}$ and $\PP^n$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Functor Of Points
  - Representable Functors
  - Projective Space
relations:
- kind: uses
  target: PR-SCHFOP
- kind: related-to
  target: D-OPENSUBFUNCTOR
review: draft
prompts:
- What is $\AA^n$ as a functor, and what represents it?
- What is $\PP^n$ as a functor, and what represents it?
- What is $\AA^n \setminus \{0\}$ as a functor?
---

Let $R$ be a ring and consider functors on the category of $R$-schemes.

::: {.example title="Affine space"}
The functor $X \mapsto \Gamma(X, \OO_X)^{n}$, sending a morphism $f \colon X' \to X$ to $(a_i) \mapsto (f^\sharp a_i)$, is represented by $\AA^n_R = \Spec R[x_1, \ldots, x_n]$, with universal element $(x_1, \ldots, x_n)$.

Indeed, for an $R$-scheme $X$, morphisms of $R$-schemes $X \to \Spec R[x_1, \ldots, x_n]$ correspond to $R$-algebra maps $R[x_1, \ldots, x_n] \to \Gamma(X, \OO_X)$, and such a map is determined by the images of $x_1, \ldots, x_n$, which are arbitrary.
Over $R = \ZZ$ this is the functor $X \mapsto \Gamma(X, \OO_X)^n$ on all schemes, represented by $\Spec \ZZ[x_1, \ldots, x_n]$: $n$ variables, not $n+1$.
:::

::: {.example title="Punctured affine space"}
$\AA^n_R \setminus \{0\}$ denotes the open complement of $V(x_1, \ldots, x_n)$.
It represents the functor sending $X$ to the set of $(a_1, \ldots, a_n) \in \Gamma(X, \OO_X)^n$ that are \dfn{unimodular}: the $a_i$ generate the unit ideal sheaf, that is, for every $x \in X$ some $a_i(x) \neq 0$ in $\kappa(x)$.

Indeed, a morphism $X \to \AA^n_R$ with coordinates $(a_i)$ factors through the open subscheme $\AA^n_R \setminus \{0\}$ exactly when its image avoids $V(x_1, \ldots, x_n)$, which says that no point of $X$ is a common zero of the $a_i$.
The condition is pointwise: on $X = \Spec k[t]$, the pair $(t, 0)$ is not the zero pair, but both entries vanish at $t = 0$, so it is not a point of $\AA^2_k \setminus \{0\}$.
When $X = \Spec A$ it says $(a_1, \ldots, a_n) = A$.
:::

::: {.example title="Projective space"}
$\PP^n_R$ represents the functor sending an $R$-scheme $X$ to the set of isomorphism classes of tuples $(\mathcal{L}, s_0, \ldots, s_n)$ with $\mathcal{L}$ an invertible sheaf on $X$ and $s_0, \ldots, s_n \in \Gamma(X, \mathcal{L})$ generating $\mathcal{L}$, where $(\mathcal{L}, s_i) \cong (\mathcal{L}', s'_i)$ if there is an isomorphism $\mathcal{L} \to \mathcal{L}'$ carrying each $s_i$ to $s'_i$.
The universal tuple is $(\OO(1), x_0, \ldots, x_n)$, and a tuple on $X$ corresponds to the morphism $f \colon X \to \PP^n_R$ with $f^* \OO(1) \cong \mathcal{L}$ and $f^* x_i = s_i$ [@Har10a, Theorem II.7.1]; the construction is the gluing in [[D-OPENSUBFUNCTOR]].

If every invertible sheaf on $X$ is trivial, for instance $X = \Spec A$ with $A$ local, a tuple is a unimodular $(a_0, \ldots, a_n) \in \Gamma(X, \OO_X)^{n+1}$ up to multiplication by a unit of $\Gamma(X, \OO_X)$.
So the map $\AA^{n+1}_R \setminus \{0\} \to \PP^n_R$ sends $(a_0, \ldots, a_n)$ to $(\OO_X, a_0, \ldots, a_n)$, and over a field $k$ its $k$-points are the classical description of $\PP^n(k)$ as nonzero $(n+1)$-tuples up to $k^\times$.
:::
