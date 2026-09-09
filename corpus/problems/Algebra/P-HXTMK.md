---
schema: qual/card@1
id: P-HXTMK
kind: problem
title: Rational canonical forms for $m_A=(x-1)(x^2+1)^2$ and $m_A=(x^2+1)^2(x^3+1)$
classification:
  areas:
  - algebra
  topics:
  - Rational Canonical Form
  - Minimal and Characteristic Polynomials
  - Structure Theorem
relations: []
review: draft
---

::: problem
Let $A$ be a rational matrix.

1. Suppose $A$ is $6\times 6$ and
\[
m_A(x)=(x-1)(x^2+1)^2.
\]
Determine all possible rational canonical forms.

2. Suppose $A$ is $10\times 10$ and
\[
m_A(x)=(x^2+1)^2(x^3+1).
\]
Determine all possible rational canonical forms.
:::


::: {.solution}
The invariant factors satisfy
\[
d_1\mid d_2\mid\cdots\mid d_r,
\qquad d_r=m_A,
\qquad \sum_i\deg d_i=\dim A.
\]

<1>1. The $6\times6$ case.
Here $\deg m_A=5$. The characteristic polynomial has the same irreducible factors as the minimal polynomial and degree $6$, so the only extra degree available is one copy of $x-1$. Hence
\[
\chi_A=(x-1)^2(x^2+1)^2.
\]
The unique invariant-factor list is
\[
d_1=x-1,\qquad d_2=(x-1)(x^2+1)^2.
\]
Therefore
\[
\operatorname{RCF}(A)=C(x-1)\oplus C\bigl((x-1)(x^2+1)^2\bigr).
\]

<1>2. The $10\times10$ case.
Factor
\[
x^3+1=(x+1)(x^2-x+1)
\]
and set
\[
a=x^2+1,\qquad b=x+1,\qquad c=x^2-x+1.
\]
Then $m_A=a^2bc$, of degree $7$. Three additional dimensions must be distributed among elementary divisors while keeping the maximal exponents equal to those occurring in $m_A$. Exactly three distributions are possible.

<2>1. One additional $b$ and one additional $c$:
\[
\chi_A=a^2b^2c^2,\qquad
(d_1,d_2)=(bc,a^2bc).
\]
Thus
\[
\operatorname{RCF}(A)=C(x^3+1)\oplus C(m_A).
\]

<2>2. One additional $a$ with exponent $1$ and one additional $b$:
\[
\chi_A=a^3b^2c,\qquad
(d_1,d_2)=(ab,a^2bc).
\]
Thus
\[
\operatorname{RCF}(A)=C\bigl((x^2+1)(x+1)\bigr)\oplus C(m_A).
\]

<2>3. Three additional $b$ blocks:
\[
\chi_A=a^2b^4c,\qquad
(d_1,d_2,d_3,d_4)=(b,b,b,a^2bc).
\]
Thus
\[
\operatorname{RCF}(A)=C(b)\oplus C(b)\oplus C(b)\oplus C(m_A).
\]

These are all possibilities. In particular, the second minimal polynomial does not determine a unique rational canonical form.
:::
