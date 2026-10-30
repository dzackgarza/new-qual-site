---
schema: qual/card@1
id: P-BKS06-7A
kind: problem
title: Elements of $\operatorname{SL}(2,\RR)$ without real eigenvalues are conjugate to rotations
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Recall that $\SL(2, \RR)$ denotes the group of real $2 \times 2$ matrices of determinant $1$. Suppose that $A \in \SL(2, \RR)$ does not have a real eigenvalue.
Show that there exists $B \in \SL(2, \RR)$ such that $B A B^{-1}$ equals a rotation matrix $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ for some $\theta \in \RR$.
:::

::: {.solution}
Since the eigenvalues of A are solutions to a real quadratic equation, they are complex conjugates of each other, call them $\lambda$ and $\bar\lambda$. Since $\det ( A ) = 1$ , it follows that $\lambda \overline { { \lambda } } = 1$ , i.e. λ and $\bar { \lambda }$ are on the unit circle.
Write $\lambda = \cos \theta + i \sin \theta$. Pick a nonzero eigenvector $z \in \CC ^ { 2 }$ with $A z = \lambda z$ . Write $z = v + i w$ with $v , w \in \RR ^ { 2 }$ Taking the real and imaginary parts of the equation $A z = \lambda z$ gives the equations $A v = ( \cos \theta ) v - ( \sin \theta ) w$ , $A w = ( \sin \theta ) v + ( \cos \theta ) w$ Note also that $A ( v - i w ) = \overline { { { \lambda } } } ( v - i w )$ and $\lambda \neq { \overline { { \lambda } } } .$ , so $v + i w$ and $v - i w$ are linearly independent over $\CC$, so $v$ and $w$ are linearly independent over $\RR$. Replacing $z$ by $\bar z$ and $\theta$ by $-\theta$ if necessary, which replaces $w$ by $-w$, we may assume that the matrix $(v \; w)$ with columns $v, w$ has $d = \det(v \; w) > 0$. Let $B = \sqrt{d}\,(v \; w)^{-1}$. Then $\det B = d \cdot d^{-1} = 1$, so $B \in \mathrm { S L } ( 2 , \RR )$, and $B v = \sqrt d\, e_1$, $B w = \sqrt d\, e_2$. Hence
$$
B A B ^ { - 1 } = \begin{pmatrix} \cos \theta & \sin \theta \\ - \sin \theta & \cos \theta \end{pmatrix} ,
$$
which is the rotation matrix for the angle $- \theta$.
:::
