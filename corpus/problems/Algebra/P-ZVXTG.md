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
Representations are finite-dimensional over $\CC$. Let $k(G)$ be the number of conjugacy classes of the finite group $G$, let $\operatorname{Cl}(G)$ be the space of complex-valued class functions on $G$, and give it the inner product
$$
\inner{\chi}{\psi}=\frac1{\abs{G}}\sum_{g\in G}\chi(g)\overline{\psi(g)}.
$$

::: pf

::: {.pf-step #dim}

$\dim\operatorname{Cl}(G)=k(G)$.

::: pf-proof

A class function is determined by its values on the conjugacy classes, and these values are arbitrary, so the indicator functions of the classes form a basis.

:::

:::

::: {.pf-step #basis}

The irreducible characters of $G$ form an orthonormal basis of $\operatorname{Cl}(G)$.

::: pf-proof

They are orthonormal by the row orthogonality relations, hence linearly independent, and they span $\operatorname{Cl}(G)$ by the standard completeness theorem of character theory.

:::

:::

::: pf-step

The number of isomorphism classes of irreducible complex representations of $G$ is $\boxed{k(G)}$.

::: pf-proof

Irreducible representations are determined up to isomorphism by their characters, so their number is the number of irreducible characters, which is $\dim\operatorname{Cl}(G)$ by step [](#basis){.pf-ref} and equals $k(G)$ by step [](#dim){.pf-ref}.

:::

:::

:::

:::
