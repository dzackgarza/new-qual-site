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

::: {.problem}
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


::: {.solution}
The second displayed matrix is upper triangular, so the characteristic polynomial of $\phi$ is
\[
\chi_\phi(t)=t^3(t-1)^3(t-17).
\]
Hence the algebraic multiplicities of $0,1,17$ are respectively $3,3,1$.

Consider the $3$-dimensional subspace spanned by the first three vectors of $B_1$. It is $\phi$-stable, and the restriction of $\phi$ to it has matrix
\[
N=\begin{pmatrix}
1&1&0\\
-1&-1&0\\
0&0&0
\end{pmatrix}.
\]
Now $N\ne0$, $\operatorname{rank}N=1$, and a direct multiplication gives $N^2=0$. Therefore the Jordan form of this restriction is
\[
J_2(0)\oplus J_1(0).
\]
This already accounts for the full algebraic multiplicity $3$ of the eigenvalue $0$, so the $0$-primary part of the Jordan form of $\phi$ is exactly $J_2(0)\oplus J_1(0)$.

For the eigenvalue $1$, the hypothesis
\[
\dim\ker(\phi-I)=1
\]
says that there is exactly one Jordan block with eigenvalue $1$. Since the algebraic multiplicity of $1$ is $3$, that block must be $J_3(1)$.

Finally, $17$ has algebraic multiplicity $1$, so its Jordan block is $J_1(17)$.

Thus, up to permutation of Jordan blocks, the Jordan normal form is uniquely
\[
\boxed{J_2(0)\oplus J_1(0)\oplus J_3(1)\oplus J_1(17).}
\]
:::
