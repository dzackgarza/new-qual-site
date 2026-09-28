---
schema: qual/card@1
id: D-DEFNATTR
kind: definition
title: Natural transformations and natural isomorphisms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Category Theory
  - Functors
relations: []
review: draft
prompts:
- What is a natural transformation between two functors?
- What is a natural isomorphism, and in what category is it the notion of isomorphism?
---

::: {.definition title="natural transformation"}
Let $F, G: \mcc \to \mcd$ be covariant functors.
A \dfn{natural transformation} $F \to G$ is the data of maps $F(X) \to G(X)$ in $\mcd$ for all $X \in \mcc$, such that for every $f: X \to Y$ in $\mcc$ the square
$$
\begin{matrix}
F(X) & \to & G(X) \\
\downarrow & & \downarrow \\
F(Y) & \to & G(Y)
\end{matrix}
$$
commutes.
For contravariant functors one asks the analogous square, with the vertical arrows reversed, to commute.
:::

::: {.definition title="natural isomorphism"}
A \dfn{natural isomorphism} $F \to G$ is a natural transformation such that $F(X) \to G(X)$ is an isomorphism for every object $X$.
:::

::: {.remark}
Natural transformations are the morphisms of the functor category $\mcd^{\mcc}$, and the natural isomorphisms are its isomorphisms: if each component $F(X)\to G(X)$ is an isomorphism, the inverse maps $G(X) \to F(X)$ form a natural transformation.

On finite-dimensional vector spaces over a field $k$, the evaluation maps $V\to V^{\vee\vee}$ form a natural isomorphism from the identity functor to the double-dual functor.
An isomorphism $V\cong V^\vee$ exists for each $V$ but depends on a choice, such as a basis; the dual is contravariant, so the identity functor and $V\mapsto V^\vee$ are not functors of the same variance.
:::
