---
schema: qual/card@1
id: P-HXTMK
kind: problem
title: Rational canonical forms from specified minimal polynomials in dimensions $6$ and $10$
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

::: {.problem}
1. Let $A\in M_6(\QQ)$ have minimal polynomial
\[
m_A=(x-1)(x^2+1)^2.
\]
Determine all possible rational canonical forms of $A$.

2. Let $B\in M_{10}(\QQ)$ have minimal polynomial
\[
m_B=(x^2+1)^2(x^3+1).
\]
Determine all possible rational canonical forms of $B$.
:::

::: {.solution}
Recall that the invariant factors
\[
d_1\mid d_2\mid\cdots\mid d_t
\]
satisfy
\[
\chi_A=\prod_i d_i,
\qquad
m_A=d_t.
\]
Equivalently, one may list the elementary divisors and align the powers of each irreducible factor from the right.

<1>1. The $6\times6$ case is unique.
Write
\[
a=x-1,
\qquad
b=x^2+1.
\]
The minimal polynomial $ab^2$ already contributes degree
\[
1+4=5.
\]
Since the characteristic polynomial has degree $6$ and has the same irreducible factors as the minimal polynomial, the only possible additional elementary divisor has degree $1$, namely another copy of $a$.
Thus the elementary divisors are
\[
a,\ a,\ b^2.
\]
The invariant factors are therefore
\[
d_1=a,
\qquad
d_2=ab^2.
\]
Hence there is exactly one rational canonical form:
\[
\boxed{C(x-1)\oplus C\bigl((x-1)(x^2+1)^2\bigr)}.
\]

<1>2. The $10\times10$ case has three possibilities.
Factor
\[
x^3+1=(x+1)(x^2-x+1).
\]
Put
\[
b=x^2+1,
\qquad c=x+1,
\qquad d=x^2-x+1.
\]
Then
\[
m_B=b^2cd
\]
has degree $4+1+2=7$. We must add elementary divisors of total degree $3$, without introducing any new irreducible factor or increasing an exponent beyond those in the minimal polynomial.
The only possibilities are:

<2>1. Add $c$ and $d$.
The elementary divisors are
\[
b^2,\ c,\ c,\ d,\ d.
\]
Hence
\[
d_1=cd=x^3+1,
\qquad
d_2=b^2cd=m_B,
\]
and
\[
\boxed{C(x^3+1)\oplus C(m_B)}.
\]

<2>2. Add $c$ and $b$.
The elementary divisors are
\[
b,\ b^2,\ c,\ c,\ d.
\]
Hence
\[
d_1=bc=(x^2+1)(x+1),
\qquad
d_2=b^2cd=m_B,
\]
and
\[
\boxed{C\bigl((x^2+1)(x+1)\bigr)\oplus C(m_B)}.
\]

<2>3. Add three further copies of $c$.
The elementary divisors are
\[
b^2,\ c,\ c,\ c,\ c,\ d.
\]
The invariant factors are
\[
d_1=c,\qquad d_2=c,\qquad d_3=c,\qquad d_4=b^2cd=m_B.
\]
Thus
\[
\boxed{C(x+1)\oplus C(x+1)\oplus C(x+1)\oplus C(m_B)}.
\]

These three exhaust the degree-$3$ ways to augment the elementary divisors while preserving the given minimal polynomial.
:::
