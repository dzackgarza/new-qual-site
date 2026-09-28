---
schema: qual/card@1
id: P-BKS06-8B
kind: problem
title: A complex matrix with $\inner{x}{Ax}$ real for all $x$ is Hermitian
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $\langle ~ , ~ \rangle$ be the standard Hermitian inner product on $\mathbb { C } ^ { n }$.
Let A be an $n \times n$ matrix with complex entries.
Suppose $\langle x , A x \rangle$ is real for all $x \in \mathbb { C } ^ { n }$ . Prove that A is Hermitian.
:::

::: {.solution}
We have $\langle x , A x \rangle = x ^ { H } A x = { \overline { { x ^ { H } A x } } }$ (since $x ^ { H } A x$ is real) $= ( x ^ { H } A x ) ^ { H } = x ^ { H } A ^ { H } x$. Thus $x ^ { H } A x = x ^ { H } A ^ { H } x$ . So $x ^ { H } ( A - A ^ { H } ) x = 0$ for all $x \in \mathbb { C } ^ { n }$ . Let $B = A - A ^ { H }$ . We have

$$
x ^ { H } B x = 0\tag{∗}
$$

for all $x \in \mathbb { C } ^ { n }$ and $B ^ { H } = A ^ { H } - A = - B$ , so B is skew-Hermitian (hence normal).
Let x be an eigenvector of B with the eigenvalue λ, so $B x = \lambda x$. Then $0 = x ^ { H } B x$ (by (∗)) $= \lambda x ^ { H } x = \lambda \| x \| ^ { 2 }$. This gives $\lambda = 0$. Thus all eigenvalues of B are zero.
Being normal, B is diagonalizable, so $B = 0$ . By definition of B, we get $A = A ^ { H }$ . Thus A is Hermitian.
:::
