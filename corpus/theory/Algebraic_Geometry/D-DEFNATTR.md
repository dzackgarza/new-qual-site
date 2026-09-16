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
\[
\begin{matrix}
F(X) & \to & G(X) \\
\downarrow & & \downarrow \\
F(Y) & \to & G(Y)
\end{matrix}
\]
commutes.
For contravariant functors one asks the analogous square, with the vertical arrows reversed, to commute.
:::

::: {.definition title="natural isomorphism"}
A \dfn{natural isomorphism} $F \to G$ is a natural transformation such that $F(X) \to G(X)$ is an isomorphism for every object $X$.
:::

::: {.remark}
Natural transformations are the correct notion of morphism of functors, and they are the arrows in the functor category $\mcd^{\mcc}$; natural isomorphism is exactly isomorphism there, which is why the inverse maps $G(X) \to F(X)$ automatically assemble into a natural transformation again.

Naturality is what turns an accident into a statement.
A finite-dimensional vector space is isomorphic to its dual but not naturally so, while the map to its double dual is natural; the same distinction is what makes the Yoneda lemma, representability of $h_X$, and every adjunction on this exam say something.
:::
