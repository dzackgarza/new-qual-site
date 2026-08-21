---
schema: qual/card@1
id: P-GRL4N
kind: problem
title: Jordan and rational canonical forms for $\chi_A=(x-1)^2(x+1)^2$ and $p_A=(x-1)(x+1)^2$
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Rational Canonical Form
  - Minimal and Characteristic Polynomials
relations: []
review: draft
solved: false
---

::: problem
The standard computation of $\det(xI - A) = 0$ shows that $\chi_A(x) = \det(xI - A) = (x-1)^2 (x+1)^2$, and so the eigenvalues of $A$ are $1, -1$.
We want the minimal polynomial of $A$, which is given by $\prod(x-\lambda_i)^{\alpha_i}$ where $\alpha_i$ is the size of the **largest** Jordan block for $\lambda_i$.
That exponent is not the geometric multiplicity $\dim E_{\lambda_i}$, which instead counts how **many** Jordan blocks $\lambda_i$ has.

Another standard computation shows that 
$$
\lambda = 1 \implies \rank(A - 1I) = 2 \implies \dim \ker (A-1I) = 4-2 = 2
$$
and similarly
$$
\lambda = -1 \implies \rank(A + I) = 3 \implies \dim \ker(A + I) = 4 - 3 = 1.
$$

We thus have
\begin{align*}
p_A(x) &= (x-1) (x+1)^2\\
\chi_A(x) &= (x-1)^2 (x+1)^2
.\end{align*}

To compute $JCF(A)$, we use the following facts:

- For $\lambda = 1$,
  - Since $(x-1)^1$ occurs in $p_A(x)$, the largest Jordan block for $\lambda = 1$ is size 1.
  - Since $(x-1)^2$ occurs in $\chi_A(x)$, the sum of sizes of all such Jordan blocks is 2.
  - Since $\dim E_1 = 2$, there are 2 such Jordan blocks.
- For $\lambda = -1$,
  - Since $(x+1)^2$ occurs in $p_A(x)$, the largest Jordan block for $\lambda = -1$ is size 2.
  - Since $(x+1)^2$ occurs in $\chi_A(x)$, the sum of sizes of all such Jordan blocks is 2.
  - Since $\dim E_{-1} = 1$, there is 1 such Jordan block.


We can thus immediately write

\begin{align*}
JCF(A) = J_{-1}^2 \oplus 2 J_{1}^1 
=
\left[\begin{array}{cccc}
-1 & 1 & 0 & 0 \\
0 & -1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{array}\right]
.\end{align*}


The largest invariant factor is always the minimal polynomial, so $d_2 = p_A(x) = (x-1)(x+1)^2$, and $d_1$ is then forced by $d_1 d_2 = \chi_A(x)$:

\begin{align*}
d_1 &= (x-1) \\
d_2 &= (x-1) (x+1)^2
\end{align*}

which satisfies the required divisibility $d_1 \divides d_2$.
Expanding $d_2 = x^3 + x^2 - x - 1$, the companion block has last column $(1, 1, -1)^t$, and thus

\begin{align*}
RCF(A) &= C(d_1) \oplus C(d_2) =
\left[\begin{array}{c|ccc}
1 & 0 & 0 & 0 \\ \hline
0  & 0 & 0 & 1 \\
0  & 1 & 0 & 1 \\
0  & 0 & 1 & -1 \\
\end{array}\right]
.\end{align*}
:::
