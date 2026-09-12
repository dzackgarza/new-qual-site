---
schema: qual/card@1
id: P-BKS06-7A
kind: problem
title: UC Berkeley Spring 2006 prelim 7A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Recall that $\mathrm { S L } ( 2 , \mathbb { R } )$ denotes the group of real $2 \times 2$ matrices of determinant 1. Suppose that $A \in \mathrm { S L } ( 2 , \mathbb { R } )$ does not have a real eigenvalue.
Show that there exists $B \in \mathrm { S L } ( 2 , \mathbb { R } )$ such that $B A B ^ { - 1 }$ equals a rotation matrix $\left( \begin{array} { c c } { \cos \theta } & { - \sin \theta } \\ { \sin \theta } & { \cos \theta } \end{array} \right)$ for some $\theta \in \mathbb { R }$
:::

::: {.solution}
Since the eigenvalues of A are solutions to a real quadratic equation, they are complex conjugates of each other, call them λ and λ. Since det $( A ) = 1$ , it follows that $\lambda \overline { { \lambda } } = 1$ , i.e. λ and $\bar { \lambda }$ are on the unit circle.
Write $\lambda = \cos \theta + i$ sin θ. Pick a nonzero eigenvector $z \in \mathbb { C } ^ { 2 }$ with $A z = \lambda z$ . Write $z = v + i w$ with $v , w \in \mathbb { R } ^ { 2 }$ Taking the real and imaginary parts of the equation $A z = \lambda z \ \mathrm { g }$ ives the equations $A v = ( \cos \theta ) v - ( \sin \theta ) w$ , $A w = ( \sin \theta ) v + ( \cos \theta ) w$ Note also that $A ( v - i w ) = \overline { { { \lambda } } } ( v - i w )$ and $\lambda \neq { \overline { { \lambda } } } .$ , so $v + i w$ and $v - i w$ are linearly independent over C, so v and w are linearly independent over R. We can find $B \in \mathrm { S L } ( 2 , \mathbb { R } )$ taking the basis $\{ v , w \}$ to a real multiple of the standard basis for $\mathbb { R } ^ { 2 }$ Then $B A B ^ { - 1 } = \binom { \cos \theta } { - \sin \theta } \quad \sin \theta \quad$ . This is of the desired form, with θ in place of $- \theta .$
:::
