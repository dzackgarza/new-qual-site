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

::: {.theorem title="Grothendieck: representability in the projective case"}
Let $S$ be a Noetherian scheme, $\pi\colon X\to S$ a projective morphism, $L$ a relatively very ample invertible sheaf on $X$, $E$ a coherent $\OO_X$-module, and $\Phi\in\QQ[\lambda]$.
Then the functor $\operatorname{Quot}^{\Phi,L}_{E/X/S}$ is represented by a projective $S$-scheme $\operatorname{Quot}^{\Phi,L}_{E/X/S}$ (Nitsure, *Construction of Hilbert and Quot Schemes*, Theorem 5.1, which is Grothendieck's theorem; the functors and their families are defined in §1 of the same notes).
Setting $E=\OO_X$ identifies $\operatorname{Hilb}_{X/S}$ with $\operatorname{Quot}_{\OO_X/X/S}$: a closed subscheme $Z\subseteq X_T$ that is flat and proper over $T$ corresponds to the surjection $\OO_{X_T}\to\OO_Z$ of coherent sheaves on $X_T$, whose kernel is the ideal sheaf of $Z$ in $X_T$ and so recovers $Z$ (Nitsure, §1).
So for $L=\OO_X(1)$ and $\Phi=P$ the functor $\operatorname{Hilb}^P_{X/S}$ of the definition is represented by a projective $S$-scheme, the \dfn{Hilbert scheme} $\operatorname{Hilb}^P(X/S)$, and $\operatorname{Hilb}_{X/S}$ by the disjoint union over $P$; the universal family is a closed subscheme $\mathcal{Z}\subseteq X\times_S\operatorname{Hilb}^P(X/S)$, flat over $\operatorname{Hilb}^P(X/S)$, pulling back to $Z$ along the unique morphism $T\to\operatorname{Hilb}^P(X/S)$ classifying $Z$.
The hypotheses are those printed at Theorem 5.1, and the same notes record that the Hilbert and Quot functors are indeed represented by schemes for $X$ (quasi-)projective over $S$ with $L$ relatively very ample, but not in general.
The general Hilbert functor is defined by Stacks Project, Situation 99.9.1 (tag 0CZY), and Proposition 99.9.4 (tag 0D01) gives its algebraic-space representability when the morphism is separated and of finite presentation; these statements do not assert the projective-scheme conclusion of Grothendieck's theorem for the polynomial-graded subfunctor.
The functor represented is the functor of the definition, closed subschemes $Z\subseteq X\times_ST$ flat over $T$ whose fibres have Hilbert polynomial $P$, and $P$ is meaningful only because $\OO_X(1)$ is part of the data.
The Hilbert scheme represents the polynomial-graded projective Hilbert functor by a projective scheme, while the Stacks statement represents the general Hilbert functor by an algebraic space.
:::

::: {.theorem title="The Stacks Project's Hilbert functor"}
Let $S$ be a scheme and $f\colon X\to B$ a morphism of algebraic spaces over $S$ of finite presentation.
The functor $\operatorname{Hilb}_{X/B}$ of Stacks Project Situation 99.9.1 (tag 0CZY) sends $T$ to the closed subspaces $Z\subseteq X\times_BT$ such that $Z\to T$ is flat, proper and of finite presentation; its data contain no Hilbert polynomial and no relatively ample sheaf.
If $f$ is separated as well as of finite presentation, then this functor is an algebraic space locally of finite presentation over $B$ (Stacks Project, Proposition 99.9.4, tag 0D01).
A representing object carries a universal family: the identity morphism corresponds under Yoneda to a closed subspace $\mathcal{Z}\subseteq X\times_B\operatorname{Hilb}_{X/B}$, flat over the base, whose pullback along $T\to\operatorname{Hilb}_{X/B}$ is the family classified by that morphism.
For $X\to S$ projective with $\OO_X(1)$ fixed and $P\in\QQ[m]$, $\operatorname{Hilb}^P_{X/S}$ is the subfunctor of this one on which the fibres have polynomial $P$, and Grothendieck's theorem represents that subfunctor by a projective scheme; Proposition 99.9.4 does not supply projectivity and is not a substitute for it.
:::

::: {.example}
Let $k$ be a field and $X = \PP^n_k$.

- For $P = 1$, a closed subscheme of $\PP^n_k$ with Hilbert polynomial $1$ is a $k$-point, and $\operatorname{Hilb}^1(\PP^n_k) \cong \PP^n_k$ with $\mathcal{Z}$ the diagonal.

- For $d \geq 1$ and $P(m) = \binom{m+n}{n} - \binom{m-d+n}{n}$, the Hilbert polynomial of a degree-$d$ hypersurface, from the sequence $0 \to \OO(m-d) \to \OO(m) \to \OO_H(m) \to 0$, every closed subscheme with Hilbert polynomial $P$ is a hypersurface $V(F)$ of degree $d$, and $\operatorname{Hilb}^P(\PP^n_k) \cong \PP(H^0(\PP^n_k, \OO(d))) \cong \PP^{N}_k$ with $N = \binom{n+d}{d} - 1$.
:::
