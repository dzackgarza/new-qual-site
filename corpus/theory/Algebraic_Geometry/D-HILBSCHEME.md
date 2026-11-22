---
schema: qual/card@1
id: D-HILBSCHEME
kind: definition
title: The Hilbert functor and the Hilbert scheme
classification:
  areas:
  - algebraic-geometry
  topics:
  - Hilbert Schemes
  - Moduli
  - Flat Families
relations:
- kind: uses
  target: D-L6ERW
- kind: related-to
  target: T-COHFLATCHI
- kind: related-to
  target: D-CRVMOD
review: draft
prompts:
- What is the Hilbert scheme?
---

::: {.definition title="Hilbert functor"}
Let $S$ be a Noetherian scheme, $X \to S$ a projective morphism with a relatively very ample invertible sheaf $\OO_X(1)$, and $P \in \QQ[m]$.
The \dfn{Hilbert functor} $\operatorname{Hilb}^P_{X/S}$ sends a locally Noetherian $S$-scheme $T$ to the set of closed subschemes $Z \subseteq X \times_S T$ that are flat over $T$ and whose fibres $Z_t \subseteq X_t$, for $t \in T$, have Hilbert polynomial $m \mapsto \chi(Z_t, \OO_{Z_t}(m)) = P(m)$; it acts on morphisms $T' \to T$ by pullback of subschemes.
The Hilbert functor $\operatorname{Hilb}_{X/S}$ is the disjoint union of the $\operatorname{Hilb}^P_{X/S}$ over all $P$.
:::

::: {.theorem title="Representability"}
Let $f\colon X\to B$ be a morphism of algebraic spaces over a scheme $S$, of finite presentation and separated.
Then $\operatorname{Hilb}_{X/B}$ is an algebraic space, locally of finite presentation over $B$ (Stacks Project, Proposition 99.9.4, tag 0D01).
A representing object carries a universal family: the identity morphism of the representing object corresponds under Yoneda to a closed subspace $\mathcal{Z}\subseteq X\times_B\operatorname{Hilb}_{X/B}$, flat over the base, whose pullback along $T\to\operatorname{Hilb}_{X/B}$ is the family classified by that morphism.
:::

::: {.theorem title="Grothendieck, in the projective case"}
Let $S$ be a Noetherian scheme, $X\to S$ a projective morphism with a relatively very ample invertible sheaf $\OO_X(1)$, and $P\in\QQ[m]$.
Then $\operatorname{Hilb}^P_{X/S}$ is represented by a projective $S$-scheme, the \dfn{Hilbert scheme} $\operatorname{Hilb}^P(X/S)$, and $\operatorname{Hilb}_{X/S}$ by the disjoint union over $P$; the universal family is a closed subscheme $\mathcal{Z}\subseteq X\times_S\operatorname{Hilb}^P(X/S)$, flat over $\operatorname{Hilb}^P(X/S)$, pulling back to $Z$ along the unique morphism $T\to\operatorname{Hilb}^P(X/S)$ classifying $Z$.
This is Grothendieck's theorem; the proof goes by bounding the family and then applying the representability of quotients of a fixed sheaf, and it is not proved here.
:::

::: {.example}
Let $k$ be a field and $X = \PP^n_k$.

- For $P = 1$, a closed subscheme of $\PP^n_k$ with Hilbert polynomial $1$ is a $k$-point, and $\operatorname{Hilb}^1(\PP^n_k) \cong \PP^n_k$ with $\mathcal{Z}$ the diagonal.

- For $d \geq 1$ and $P(m) = \binom{m+n}{n} - \binom{m-d+n}{n}$, the Hilbert polynomial of a degree-$d$ hypersurface, from the sequence $0 \to \OO(m-d) \to \OO(m) \to \OO_H(m) \to 0$, every closed subscheme with Hilbert polynomial $P$ is a hypersurface $V(F)$ of degree $d$, and $\operatorname{Hilb}^P(\PP^n_k) \cong \PP(H^0(\PP^n_k, \OO(d))) \cong \PP^{N}_k$ with $N = \binom{n+d}{d} - 1$.
:::
