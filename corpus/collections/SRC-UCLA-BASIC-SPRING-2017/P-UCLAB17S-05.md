---
schema: qual/card@1
id: P-UCLAB17S-05
kind: problem
title: Invertibility of a polynomial in an operator
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2017, `assets/attachments/basic-17S.pdf`.
---

::: {.problem}
Let $V$ be a finite-dimensional complex vector space, $T:V\to V$ linear, and $F(X)\in\mathbb C[X]$. Show that $F(T)$ is invertible if and only if $F$ and the minimal polynomial of $T$ have no common factor.
:::

Let
\[
m_T(X)
\]
denote the minimal polynomial of $T$.

::: pf

::: pf-step

Suppose
\[
\gcd(F,m_T)=1.
\]
Then there exist polynomials
\[
A(X),B(X)\in\mathbb C[X]
\]
such that
\[
\boxed{
A(X)F(X)+B(X)m_T(X)=1.
}
\]


::: pf-proof

The polynomial ring
\[
\mathbb C[X]
\]
is a Euclidean domain.
Therefore Bézout's identity applies to relatively prime polynomials.

:::

:::

::: pf-step

Evaluating the identity from step <1>1 at $T$ gives
\[
\boxed{
A(T)F(T)=I.
}
\]


::: pf-proof

By definition of the minimal polynomial,
\[
m_T(T)=0.
\]
Thus
\[
A(T)F(T)+B(T)m_T(T)
=
A(T)F(T)
=
I.
\]

:::

:::

::: pf-step

The operators
\[
A(T)
\quad\text{and}\quad
F(T)
\]
commute.


::: pf-proof

Both are polynomials in the same operator $T$.
Any two polynomials in $T$ commute.

:::

:::

::: pf-step

Hence $F(T)$ is invertible.


::: pf-proof

Step <1>2 gives
\[
A(T)F(T)=I.
\]
By step <1>3,
\[
F(T)A(T)=A(T)F(T)=I.
\]
Thus
\[
\boxed{
F(T)^{-1}=A(T).
}
\]

:::

:::

::: pf-step

Conversely, suppose $F$ and $m_T$ have a nonconstant common factor.
Then they have a common root
\[
\lambda\in\mathbb C.
\]


::: pf-proof

Over the algebraically closed field $\mathbb C$, every nonconstant polynomial has a root.
Any nonconstant common divisor of $F$ and $m_T$ therefore has a root $\lambda$ that is simultaneously a root of both polynomials.

:::

:::

::: pf-step

The scalar $\lambda$ from step <1>5 is an eigenvalue of $T$.


::: pf-proof

Since
\[
m_T(\lambda)=0,
\]
the factor theorem gives
\[
m_T(X)
=
(X-\lambda)q(X)
\]
for some polynomial $q$.

Suppose
\[
T-\lambda I
\]
were invertible.
Then
\[
0
=
m_T(T)
=
(T-\lambda I)q(T)
\]
would imply
\[
q(T)=0.
\]
But
\[
\deg q<\deg m_T,
\]
contradicting the minimality of $m_T$.
Hence
\[
T-\lambda I
\]
is not invertible, so
\[
\lambda
\]
is an eigenvalue.

:::

:::

::: pf-step

Choose a nonzero eigenvector
\[
v
\]
with
\[
Tv=\lambda v.
\]
Then
\[
\boxed{F(T)v=0}.
\]


::: pf-proof

For every polynomial
\[
P(X)=\sum_j c_jX^j,
\]
the eigenvalue equation gives
\[
P(T)v
=
\sum_j c_jT^jv
=
\sum_j c_j\lambda^jv
=
P(\lambda)v.
\]
Apply this to $P=F$.
By step <1>5,
\[
F(\lambda)=0.
\]
Thus
\[
F(T)v=0.
\]

:::

:::

::: pf-step

Therefore $F(T)$ is not invertible.


::: pf-proof

Step <1>7 gives a nonzero vector
\[
v\in\ker F(T).
\]
Hence
\[
F(T)
\]
is not injective and therefore not invertible.

:::

:::

::: pf-step

Consequently,
\[
\boxed{
F(T)\text{ is invertible}
\iff
\gcd(F,m_T)=1.
}
\]


::: pf-proof

Steps <1>1--<1>4 prove the forward implication from coprimality to invertibility.
Steps <1>5--<1>8 prove the contrapositive of the reverse implication.

:::

:::

::: pf-qed

Step <1>9 is the required equivalence.

:::

:::
