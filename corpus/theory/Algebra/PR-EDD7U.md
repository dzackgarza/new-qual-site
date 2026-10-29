---
schema: qual/card@1
id: PR-EDD7U
kind: proposition
title: Characteristic polynomials via traces of exterior powers
slogan: 'Characteristic coefficients are traces of exterior powers, equivalently sums of principal minors.'
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Determinants
  - Trace
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a field, $A \in \Mat_{n\times n}(k)$, and $\chi_A(t) \coloneqq \det(tI - A)$.
Then
$$
\begin{aligned}
\chi_A(t) &= \sum_{j=0}^n (-1)^j \trace\qty{\Wedgepower^j A}\, t^{n-j} \\
&= t^n - \trace\qty{A} t^{n-1} + \trace\qty{\Wedgepower^2 A}\, t^{n-2} - \cdots + (-1)^{n-1} \trace\qty{\Wedgepower^{n-1} A}\, t + (-1)^n \det(A),
\end{aligned}
$$
where $\trace\qty{\Wedgepower^0 A} = 1$, $\Wedgepower^1 A = A$, and $\trace\qty{\Wedgepower^n A} = \det(A)$.
Moreover, for $0 \leq \ell \leq n$,
$$
\trace\qty{\Wedgepower^\ell A} = \sum_{\substack{S \subseteq \theset{1, \ldots, n} \\ \abs{S} = \ell}} \det\qty{A_{S,S}},
$$
the sum of the $\binom{n}{\ell}$ principal $\ell\times\ell$ minors of $A$, where $A_{S,S}$ is the submatrix of $A$ with rows and columns indexed by $S$, obtained by deleting the rows and columns indexed by the complement of $S$.
:::

::: {.example}
Let $M = (4i + j)_{0 \leq i, j \leq 3} \in \Mat_{4\times 4}(\QQ)$.
Its principal submatrices are as follows.
$$
M = \begin{bmatrix} 0 & 1 & 2 & 3 \\ 4 & 5 & 6 & 7 \\ 8 & 9 & 10 & 11 \\ 12 & 13 & 14 & 15 \end{bmatrix}
$$
For $\ell = 1$: $[0], [5], [10], [15]$.
For $\ell = 2$:
$$
\begin{bmatrix} 0 & 1 \\ 4 & 5 \end{bmatrix},\
\begin{bmatrix} 0 & 2 \\ 8 & 10 \end{bmatrix},\
\begin{bmatrix} 0 & 3 \\ 12 & 15 \end{bmatrix},\
\begin{bmatrix} 5 & 6 \\ 9 & 10 \end{bmatrix},\
\begin{bmatrix} 5 & 7 \\ 13 & 15 \end{bmatrix},\
\begin{bmatrix} 10 & 11 \\ 14 & 15 \end{bmatrix}.
$$
For $\ell = 3$:
$$
\begin{bmatrix} 0 & 1 & 2 \\ 4 & 5 & 6 \\ 8 & 9 & 10 \end{bmatrix},\
\begin{bmatrix} 0 & 1 & 3 \\ 4 & 5 & 7 \\ 12 & 13 & 15 \end{bmatrix},\
\begin{bmatrix} 0 & 2 & 3 \\ 8 & 10 & 11 \\ 12 & 14 & 15 \end{bmatrix},\
\begin{bmatrix} 5 & 6 & 7 \\ 9 & 10 & 11 \\ 13 & 14 & 15 \end{bmatrix}.
$$
For $\ell = 4$ the only principal submatrix is $M$ itself.

The $1\times 1$ minors sum to $\trace M = 0 + 5 + 10 + 15 = 30$, and the $2\times 2$ minors are $-4, -16, -36, -4, -16, -4$, with sum $-80$.
Every row of $M$ is a linear combination of $(1,1,1,1)$ and $(0,1,2,3)$, so $\rank M = 2$ and every $3\times 3$ and $4\times 4$ minor vanishes.
Therefore $\chi_M(t) = t^4 - 30t^3 - 80t^2$.
:::
