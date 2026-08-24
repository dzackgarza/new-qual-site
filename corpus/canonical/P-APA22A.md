---
schema: qual/card@1
id: P-APA22A
kind: problem
title: Jordan form of a map from two partially known matrix representations
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Jordan Canonical Form
relations: []
review: draft
---

::: problem
A linear map $\phi \colon \mathbb{C}^7 \to \mathbb{C}^7$ is given.
It has the following properties.

- There exist two different bases $B_1$ and $B_2$ for $\mathbb{C}^7$, such that the matrices of $\phi$ with respect to these bases are
  \[
  \mathcal{M}(\phi, B_1, B_1)
  =
  \begin{pmatrix}
  1 & 1 & 0 & * & * & * & * \\
  -1 & -1 & 0 & * & * & * & * \\
  0 & 0 & 0 & * & * & * & * \\
  0 & 0 & 0 & * & * & * & * \\
  0 & 0 & 0 & * & * & * & * \\
  0 & 0 & 0 & * & * & * & * \\
  0 & 0 & 0 & * & * & * & *
  \end{pmatrix},
  \qquad
  \mathcal{M}(\phi, B_2, B_2)
  =
  \begin{pmatrix}
  0 & * & * & * & * & * & * \\
  0 & 0 & * & * & * & * & * \\
  0 & 0 & 0 & * & * & * & * \\
  0 & 0 & 0 & 1 & * & * & * \\
  0 & 0 & 0 & 0 & 1 & * & * \\
  0 & 0 & 0 & 0 & 0 & 1 & * \\
  0 & 0 & 0 & 0 & 0 & 0 & 17
  \end{pmatrix},
  \]
  where $*$ denotes an unknown value.

- We have $\dim \ker(\phi - \operatorname{id}_{\mathbb{C}^7}) = 1$.

Determine, with proof, the Jordan Normal Form of $\phi$.
:::
