---
schema: qual/card@1
id: D-CHOWRING
kind: definition
title: Chow groups, the Chow ring and the cycle class map
classification:
  areas:
  - algebraic-geometry
  topics:
  - Chow Ring
  - Cycles
  - Intersection Theory
relations:
- kind: uses
  target: T-MOVLEM
review: draft
prompts:
- What is the Chow ring?
- What is the cycle class map?
---

::: {.definition title="Chow groups"}
Let $X$ be a variety.
The group $Z_k(X)$ of $k$-cycles is the free abelian group on $k$-dimensional subvarieties.
For a $(k+1)$-dimensional subvariety $W$ and $f \in k(W)^\times$, the cycle $\div(f) \in Z_k(X)$ is \dfn{rationally equivalent to zero}.
The \dfn{Chow group} $A_k(X)$ is $Z_k(X)$ modulo these cycles, and for $X$ of pure dimension $n$ one writes $A^k(X) = A_{n-k}(X)$.
:::

::: {.definition title="Chow ring"}
For $X$ smooth and quasiprojective, the \dfn{Chow ring} is $A^\bullet(X) = \bigoplus_k A^k(X)$ with the intersection product: for subvarieties $V, W$ meeting properly, $[V] \cdot [W] = \sum_i m_i [Z_i]$ over the components $Z_i$ of $V \cap W$ with intersection multiplicities $m_i$.
The moving lemma makes this well defined on classes.
:::

::: {.definition title="Cycle class map"}
For $X$ smooth projective over $\CC$, the \dfn{cycle class map} $\operatorname{cl} \colon A^k(X) \to H^{2k}(X, \ZZ)$ sends a subvariety $V$ of codimension $k$ to the Poincaré dual of its fundamental class.
It is a ring homomorphism and lands in the Hodge classes $H^{2k}(X, \ZZ) \cap H^{k,k}(X)$.
:::

::: {.example}
$A^\bullet(\PP^n) = \ZZ[H]/(H^{n+1})$, where $H$ is the class of a hyperplane, a subvariety of degree $d$ and codimension $k$ has class $d H^k$, and the product formula recovers Bézout's theorem.
Here $\operatorname{cl}$ is an isomorphism onto $H^{\mathrm{even}}(\PP^n, \ZZ)$.
For an elliptic curve $E$, $A^1(E) = \Pic(E)$ is uncountable while $H^2(E, \ZZ) = \ZZ$, so $\operatorname{cl}$ is far from injective: it records only the degree.
:::
