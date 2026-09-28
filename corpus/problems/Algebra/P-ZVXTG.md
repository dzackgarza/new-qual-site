---
schema: qual/card@1
id: P-ZVXTG
kind: problem
title: Equality of the number of conjugacy classes and the number of irreducible representations
  of a finite group
classification:
  areas:
  - algebra
  topics:
  - Character Theory
  - Conjugacy
  - Representation Theory
relations: []
review: draft
---

::: {.problem}
What's the relation between the number of conjugacy classes in a finite group and the number of irreducible representations?
:::


::: {.solution}
Assume representations are finite-dimensional over $\CC$. Let $k(G)$ denote the number of conjugacy classes of the finite group $G$.

The space $\operatorname{Cl}(G)$ of complex-valued class functions on $G$ has dimension $k(G)$: a class function is determined independently by one value on each conjugacy class.

On the other hand, the irreducible characters of $G$ form an orthonormal basis of $\operatorname{Cl}(G)$ for the inner product
\[
\langle\chi,\psi\rangle
=\frac1{|G|}\sum_{g\in G}\chi(g)\overline{\psi(g)}.
\]
Orthogonality gives linear independence. Completeness follows from the regular representation, or equivalently from the standard character-theoretic fact that every class function is a linear combination of irreducible characters.

Therefore the number of irreducible complex characters, equivalently the number of isomorphism classes of irreducible complex representations, equals the dimension of $\operatorname{Cl}(G)$:
\[
\boxed{\#\operatorname{Irr}(G)=k(G).}
\]
Thus a finite group has exactly as many irreducible complex representations as conjugacy classes.
:::
