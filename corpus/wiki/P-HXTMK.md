---
schema: qual/card@1
id: P-HXTMK
kind: problem
title: Rational canonical forms for $m_A=(x-1)(x^2+1)^2$ and $m_A=(x^2+1)^2(x^3+1)$
classification:
  areas:
  - algebra
  topics:
  - rational-canonical-form
  - minimal-and-characteristic-polynomials
  - structure-theorem
relations: []
review: draft
solved: false
---

::: problem
In both cases, we will need the characteristic polynomials $\chi_A(x)$, since $RCF(A)$ will depend on the invariant factors of $A$.
We will also use the fact that over the algebraic closure $\overline \QQ$, the minimal and characteristic polnyomials must have the same roots.

Suppose $m_A(x) = (x-1)(x^2+1)^2$, which is a degree 5 polynomial.
Since $\deg \chi_A$ must be 6 and $m_A$ must divide $\chi_A$ in $\QQ[x]$, with the two sharing their irreducible factors, the only possibility in this case is that
$$
\chi_A(x) = (x-1)^2 (x^2+1)^2.
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
d_2 =  (x-1)(x^2+1)^2 = x^5 - x^4 + 2x^3 - 2x^2 + x - 1,
$$

the companion block $C(d_2)$ has last column $(1, -1, 2, -2, 1)^t$, and there is thus only one possible Rational Canonical form:

\begin{align*}
RCF(A) &= 
\left[\begin{array}{c|ccccc}
1 & 0 & 0 & 0 & 0 & 0\\
\hline
0 & 0 & 0 & 0 & 0 & 1 \\
0 & 1 & 0 & 0 & 0 & -1 \\
0 & 0 & 1 & 0 & 0 & 2 \\
0 & 0 & 0 & 1 & 0 & -2 \\
0 & 0 & 0 & 0 & 1 & 1 \\
\end{array}\right]
.\end{align*}

The constraints $m_A(x) = (x^2+1)^2(x^3+1)$ with $\deg m_A(x) = 7$ and $\deg \chi_A(x) = 10$ forces
$$
\chi_A(x) = (x^2+1)^2 (x^3+1)^2.
$$

Furthermore, the invariant factors are similarly constrained, and so the only possibility is

\begin{align*}
d_1 &= (x^3 + 1) \\
d_2 &= (x^2+1)^2 (x^3+1)
\end{align*}

with $\deg d_1 = 3$ and $\deg d_2 = 7$, summing to $\deg \chi_A = 10$.
Over $\QQ$ the factor $x^3+1 = (x+1)(x^2-x+1)$ splits further, so the elementary divisors, which must be powers of irreducibles, are

\begin{align*}
(x+1),\, (x+1),\, (x^2-x+1),\, (x^2-x+1),\, (x^2+1)^2
.\end{align*}

Noting that
$$
d_1 = x^3 + 1, \qquad d_2 = (x^2+1)^2 (x^3+1) = x^7 + 2x^5 + x^4 + x^3 + 2x^2 + 1,
$$

the two companion blocks are $3\times 3$ and $7\times 7$, with last columns $(-1, 0, 0)^t$ and $(-1, 0, -2, -1, -1, -2, 0)^t$ respectively, so

\begin{align*}
RCF(A) &= C(d_1) \oplus C(d_2), \\ \\
C(d_1) &=
\left[\begin{array}{ccc}
0 & 0 & -1 \\
1 & 0 & 0 \\
0 & 1 & 0 \\
\end{array}\right],
\qquad
C(d_2) =
\left[\begin{array}{ccccccc}
0 & 0 & 0 & 0 & 0 & 0 & -1 \\
1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & -2 \\
0 & 0 & 1 & 0 & 0 & 0 & -1 \\
0 & 0 & 0 & 1 & 0 & 0 & -1 \\
0 & 0 & 0 & 0 & 1 & 0 & -2 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 \\
\end{array}\right]
.\end{align*}
:::
