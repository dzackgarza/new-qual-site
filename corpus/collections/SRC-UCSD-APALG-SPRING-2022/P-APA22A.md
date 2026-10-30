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
A linear map $\phi \colon \CC^7 \to \CC^7$ is given.
It has the following properties.

- There exist two different bases $B_1$ and $B_2$ for $\CC^7$, such that the matrices of $\phi$ with respect to these bases are
  $$
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
  $$
  where $*$ denotes an unknown value.

- We have $\dim \ker(\phi - \operatorname{id}_{\CC^7}) = 1$.

Determine, with proof, the Jordan Normal Form of $\phi$.
:::


::: {.solution}
Write $J_m(\lambda)$ for the Jordan block of size $m$ with eigenvalue $\lambda$.

::: pf

::: {.pf-step #charpoly}

$\chi_\phi(t)=t^3(t-1)^3(t-17)$.

::: pf-proof

The matrix $\mathcal M(\phi,B_2,B_2)$ is upper triangular with diagonal $0,0,0,1,1,1,17$.

:::

:::

::: {.pf-step #zero-part}

The Jordan blocks of $\phi$ with eigenvalue $0$ are $J_2(0)$ and $J_1(0)$.

::: pf-proof

The first three columns of $\mathcal M(\phi,B_1,B_1)$ vanish below row $3$, so the span $U$ of the first three vectors of $B_1$ is $\phi$-stable, and $\phi\restrict_U$ has matrix $N=\begin{pmatrix}1&1&0\\-1&-1&0\\0&0&0\end{pmatrix}$. Direct multiplication gives $N^2=0$, and $\operatorname{rank}N=1$, so $\phi\restrict_U$ is nilpotent with Jordan form $J_2(0)\oplus J_1(0)$. Thus $U$ lies in the generalized $0$-eigenspace of $\phi$, which has dimension $3$ by step [](#charpoly){.pf-ref}, so the two are equal.

:::

:::

::: {.pf-step #one-part}

The only Jordan block of $\phi$ with eigenvalue $1$ is $J_3(1)$.

::: pf-proof

The number of Jordan blocks for the eigenvalue $1$ is $\dim\ker(\phi-\operatorname{id})=1$, and their sizes add up to the algebraic multiplicity $3$ of step [](#charpoly){.pf-ref}.

:::

:::

::: pf-step

The Jordan normal form of $\phi$ is $\boxed{J_2(0)\oplus J_1(0)\oplus J_3(1)\oplus J_1(17)}$, up to the order of the blocks.

::: pf-proof

The eigenvalue $17$ is simple by step [](#charpoly){.pf-ref}, so it contributes $J_1(17)$; steps [](#zero-part){.pf-ref} and [](#one-part){.pf-ref} give the other blocks.

:::

:::

:::
:::
