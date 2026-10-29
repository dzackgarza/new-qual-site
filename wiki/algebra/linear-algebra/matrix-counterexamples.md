---
title: Matrix counterexamples
order: 520
---

# Matrix counterexamples

::: {.example title="Diagonalizable over $\CC$ and not over $\RR$"}
The matrix
$$
M = \left(\begin{array}{rr}
0  & 1 \\
-1 & 0
\end{array}\right)
$$
has $\min_M(x) = \chi_M(x) = x^2 + 1$, which has no roots in $\RR$ and the distinct roots $\pm i$ in $\CC$.
So $M$ has no real eigenvalues and is not diagonalizable over $\RR$, and over $\CC$
$$
M \sim
\left(\begin{array}{rr}
-i & 0 \\
0 & i
\end{array}\right).
$$
:::

::: {.example title="Not diagonalizable over $\CC$"}
The matrix
$$
M = \left(\begin{array}{rr}
1 & 1 \\
0 & 1
\end{array}\right)
$$
has the repeated eigenvalue $1$ and $\min_M(x) = \chi_M(x) = (x-1)^2$, which does not have distinct roots, so $M$ is not diagonalizable over any field.
It is a Jordan block $J_2(1)$.
:::

::: {.example title="Equal characteristic polynomials, not similar"}
The matrices
$$
A = \left(\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right)
\quad\text{and}\quad
B = \left(\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right)
$$
satisfy $\chi_A(x) = \chi_B(x) = x^2$, and they are not similar: both are in Jordan form, with different Jordan blocks, and $\min_A(x)=x$ while $\min_B(x)=x^2$.
:::

::: {.example title="Invertible and not diagonalizable"}
The matrix
$$
\left(
\begin{array}{ccc}
1 & 1 & 0 \\
0 & 1 & 1 \\
0 & 0 & 1
\end{array}
\right)
$$
has determinant $1$, so it is invertible, and it is the Jordan block $J_3(1)$, so it is not diagonalizable.
:::

## Roots of matrices

[[FE-ISVDM]]
