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

::: {.theorem title="Grothendieck"}
Each $\operatorname{Hilb}^P_{X/S}$ is represented by a projective $S$-scheme, the \dfn{Hilbert scheme} $\operatorname{Hilb}^P(X/S)$, and $\operatorname{Hilb}_{X/S}$ is represented by $\bigsqcup_P \operatorname{Hilb}^P(X/S)$.
The universal family is a closed subscheme $\mathcal{Z} \subseteq X \times_S \operatorname{Hilb}^P(X/S)$, flat over $\operatorname{Hilb}^P(X/S)$, such that every family $Z \subseteq X \times_S T$ as above is the pullback of $\mathcal{Z}$ along a unique morphism $T \to \operatorname{Hilb}^P(X/S)$.
:::

::: {.example}
Let $k$ be a field and $X = \PP^n_k$.

- For $P = 1$, a closed subscheme of $\PP^n_k$ with Hilbert polynomial $1$ is a $k$-point, and $\operatorname{Hilb}^1(\PP^n_k) \cong \PP^n_k$ with $\mathcal{Z}$ the diagonal.

- For $d \geq 1$ and $P(m) = \binom{m+n}{n} - \binom{m-d+n}{n}$, the Hilbert polynomial of a degree-$d$ hypersurface, from the sequence $0 \to \OO(m-d) \to \OO(m) \to \OO_H(m) \to 0$, every closed subscheme with Hilbert polynomial $P$ is a hypersurface $V(F)$ of degree $d$, and $\operatorname{Hilb}^P(\PP^n_k) \cong \PP(H^0(\PP^n_k, \OO(d))) \cong \PP^{N}_k$ with $N = \binom{n+d}{d} - 1$.
:::
