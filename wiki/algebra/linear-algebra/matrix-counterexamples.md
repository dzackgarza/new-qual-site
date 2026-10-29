---
title: Matrix counterexamples
order: 520
---

# Matrix counterexamples

::: {.example title="A basis of $\mathfrak{su}(2)$ from the Pauli matrices"}
The Lie algebra $\mathfrak{su}(2) = \theset{X \in \Mat_{2\times 2}(\CC) \suchthat X^* = -X,\ \trace X = 0}$ is a real vector space of dimension $3$ with basis
$$
\sigma_1 \coloneqq \frac{1}{\sqrt 2}\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix},\qquad
\sigma_2 \coloneqq \frac{1}{\sqrt 2}\begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix},\qquad
\sigma_3 \coloneqq \frac{1}{\sqrt 2}\begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}.
$$
With the Pauli matrices $\tau_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $\tau_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$, $\tau_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$, these are $\sigma_1 = \frac{1}{\sqrt 2}\, i\tau_y$, $\sigma_2 = \frac{1}{\sqrt 2}\, i\tau_x$, and $\sigma_3 = \frac{1}{\sqrt 2}\, i\tau_z$.
Each Pauli matrix is Hermitian and traceless, so $i$ times it is skew-Hermitian and traceless, and lies in $\mathfrak{su}(2)$.
:::

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

::: {.example title="Distinct square roots of $-I$"}
The matrices
$$
M_1
\definedas
\matt 0 {-1} 1 0, \qquad
M_2
\definedas
\matt 0 1 {-1} 0
$$
are distinct and satisfy $M_1^2 = M_2^2 = -I$.
Hence $A^n = B^n$ does not imply $A=B$ for real $2\times 2$ matrices, and $M_1$ and $M_2$ are the images of $i$ and $-i$ under the ring embedding $\CC\to\Mat(2\times 2;\RR)$, $a+bi\mapsto\matt a{-b}ba$.
:::

[[FE-ISVDM]]
