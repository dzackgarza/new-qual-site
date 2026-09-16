---
schema: qual/card@1
id: D-VARCHOW
kind: definition
title: Chow forms and the Chow variety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Chow Varieties
  - Grassmannians
  - Degree
relations:
- kind: uses
  target: D-VARDEG
review: draft
prompts:
- What is a Chow variety?
---

::: {.definition title="Chow form"}
Let $X \subseteq \PP^n$ be an irreducible projective variety of dimension $k$ and degree $d$ over an algebraically closed field.
The set of $(n-k-1)$-planes in $\PP^n$ that meet $X$ is an irreducible hypersurface
\[
Z(X) \subseteq \Gr(n-k-1, n),
\]
and it is the zero locus of a section of $\OO(d)$ in the Plücker embedding, unique up to a scalar.
This section is the \dfn{Chow form} of $X$.
For an effective $k$-cycle $\sum_i m_i X_i$, the Chow form is the product of the Chow forms of the $X_i$ raised to the powers $m_i$.
:::

::: {.definition title="Chow variety"}
The Chow form defines an injective map from the set of effective $k$-cycles of degree $d$ in $\PP^n$ to the projective space $\PP H^0(\Gr(n-k-1,n), \OO(d))$.
Its image is a closed algebraic subset, the \dfn{Chow variety} $\mathcal{C}_{k,d}(\PP^n)$, which parametrizes effective $k$-cycles of degree $d$ in $\PP^n$.
:::

::: {.example}
For $k = n-1$, a $(n-1)$-cycle of degree $d$ is a hypersurface counted with multiplicity, a $0$-plane meets it exactly when the point lies on it, and $\mathcal{C}_{n-1,d}(\PP^n) = \PP H^0(\PP^n, \OO(d))$ is the space of degree-$d$ hypersurfaces.
For $k = 0$, the $(n-1)$-planes meeting a point $p$ form a hyperplane in the dual projective space, and $\mathcal{C}_{0,d}(\PP^n) = \Sym^d \PP^n$.
:::
