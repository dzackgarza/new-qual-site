---
schema: qual/card@1
id: P-4KRNC
kind: problem
title: "In both cases, we will need the characteristic polynomials $\\chi_A(x)$\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
In both cases, we will need the characteristic polynomials $\chi_A(x)$, since $RCF(A)$ will depend on the invariant factors of $A$.
We will also use the fact that over the algebraic closure $\overline \QQ$, the minimal and characteristic polnyomials must have the same roots.

## a
Suppose $m_A(x) = (x-1)(x^2+1)^2$, which is a degree 5 polynomial.
Since $\deg \chi_A$ must be 6 and $m_A$ must divide $\chi_A$ in $\QQ[x]$, the only possibility in this case is that
$$
\chi_A(x) = (x-1)^2 (x^2+2)^2.
$$

To determine the possible invariant factors $\theset{d_i}$, we can just note that $\prod d_i = \chi_A(x)$ and $d_n = m_A(x)$.
With these constraints, the only possibility is

\begin{align*}
d_1 &= (x-1) \\
d_2 &= (x-1)(x^2+1)^2.
,\end{align*}

from which we can immediately obtain the elementary divisors:

\begin{align*}
(x-1), (x-1), (x^2+1)^2
.\end{align*}

Then noting that 
$$
d_2 =d_2 =  (x-1)(x^2+1)^2 = x^5 -x^4 + 4x^3 -4x^2 + 4x - 4,
$$

there is thus only one possible Rational Canonical form:

\begin{align*}
RCF(A) &= 
\left[\begin{array}{c|ccccc}
1 & 0 & 0 & 0 & 0 & 0\\
\hline
0 & 0 & 0 & 0 & 0 & 4 \\
0 & 1 & 0 & 0 & 0 & -4 \\
0 & 0 & 1 & 0 & 0 & 4 \\
0 & 0 & 0 & 1 & 0 & -4 \\
0 & 0 & 0 & 0 & 1 & 1 \\
\end{array}\right]
.\end{align*}

## b 

The constraints $m_A(x) = (x^2+1)^2(x^3+1)$ with $\deg m_A(x) = 7$ and $\deg \chi_A(x) = 10$ forces
$$
\chi_A(x) = (x^2+1)^2 (x^3+1)^2.
$$

Furthermore, the invariant factors are similarly constrained, and so the only possibility is

\begin{align*}
d_1 &= (x_3 + 1) \\
d_2 &= (x^2+1)^2 (x^3+1)
\end{align*}

with corresponding elementary divisors

\begin{align*}
(x^3 + 1), (x^3 + 1), (x^2 + 1)^2
.\end{align*}

Noting that
$$
d_2 = (x^2+1)^2 (x^3+1) = x^5 + x^3 + x^2 + 1,
$$

we have

\begin{align*}
RCF(A) &= 
\left[\begin{array}{cc|ccccc}
0 & -1  & 0 & 0 & 0 & 0 & 0 \\
1 & 0   & 0 & 0 & 0 & 0 & 0 \\ \hline
0 & 0   & 0 & 0 & 0 & 0 & -1 \\
0 & 0   & 1 & 0 & 0 & 0 & 0 \\
0 & 0   & 0 & 1 & 0 & 0 & -1 \\
0 & 0   & 0 & 0 & 1 & 0 & -1 \\
0 & 0   & 0 & 0 & 0 & 1 & 0 \\
\end{array}\right]
.\end{align*}

