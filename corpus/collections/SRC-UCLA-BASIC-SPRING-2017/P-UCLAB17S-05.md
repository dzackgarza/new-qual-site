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
Let $V$ be a finite-dimensional complex vector space, $T:V\to V$ linear, and $F(X)\in\CC[X]$. Show that $F(T)$ is invertible if and only if $F$ and the minimal polynomial of $T$ have no common factor.
:::

::: {.solution}

Let
$$
m_T(X)
$$
denote the minimal polynomial of $T$.

::: pf

::: {.pf-step #s1-1}

Suppose
$$
\gcd(F,m_T)=1.
$$
Then there exist polynomials
$$
A(X),B(X)\in\CC[X]
$$
such that
$$
\boxed{
A(X)F(X)+B(X)m_T(X)=1.
}
$$


::: pf-proof

The polynomial ring
$$
\CC[X]
$$
is a Euclidean domain.
Therefore Bézout's identity applies to relatively prime polynomials.

:::

:::

::: {.pf-step #s1-2}

Evaluating the identity from step [](#s1-1){.pf-ref} at $T$ gives
$$
\boxed{
A(T)F(T)=I.
}
$$


::: pf-proof

By definition of the minimal polynomial,
$$
m_T(T)=0.
$$
Thus
$$
A(T)F(T)+B(T)m_T(T)
=
A(T)F(T)
=
I.
$$

:::

:::

::: {.pf-step #s1-3}

The operators
$$
A(T)
\quad\text{and}\quad
F(T)
$$
commute.


::: pf-proof

Both are polynomials in the same operator $T$.
Any two polynomials in $T$ commute.

:::

:::

::: {.pf-step #s1-4}

Hence $F(T)$ is invertible.


::: pf-proof

Step [](#s1-2){.pf-ref} gives
$$
A(T)F(T)=I.
$$
By step [](#s1-3){.pf-ref},
$$
F(T)A(T)=A(T)F(T)=I.
$$
Thus
$$
\boxed{
F(T)^{-1}=A(T).
}
$$

:::

:::

::: {.pf-step #s1-5}

Conversely, suppose $F$ and $m_T$ have a nonconstant common factor.
Then they have a common root
$$
\lambda\in\CC.
$$


::: pf-proof

Over the algebraically closed field $\CC$, every nonconstant polynomial has a root.
Any nonconstant common divisor of $F$ and $m_T$ therefore has a root $\lambda$ that is simultaneously a root of both polynomials.

:::

:::

::: {.pf-step #s1-6}

The scalar $\lambda$ from step [](#s1-5){.pf-ref} is an eigenvalue of $T$.


::: pf-proof

Since
$$
m_T(\lambda)=0,
$$
the factor theorem gives
$$
m_T(X)
=
(X-\lambda)q(X)
$$
for some polynomial $q$.

Suppose
$$
T-\lambda I
$$
were invertible.
Then
$$
0
=
m_T(T)
=
(T-\lambda I)q(T)
$$
would imply
$$
q(T)=0.
$$
But
$$
\deg q<\deg m_T,
$$
contradicting the minimality of $m_T$.
Hence
$$
T-\lambda I
$$
is not invertible, so
$$
\lambda
$$
is an eigenvalue.

:::

:::

::: {.pf-step #s1-7}

Choose a nonzero eigenvector
$$
v
$$
with
$$
Tv=\lambda v.
$$
Then
$$
\boxed{F(T)v=0}.
$$


::: pf-proof

For every polynomial
$$
P(X)=\sum_j c_jX^j,
$$
the eigenvalue equation gives
$$
P(T)v
=
\sum_j c_jT^jv
=
\sum_j c_j\lambda^jv
=
P(\lambda)v.
$$
Apply this to $P=F$.
By step [](#s1-5){.pf-ref},
$$
F(\lambda)=0.
$$
Thus
$$
F(T)v=0.
$$

:::

:::

::: {.pf-step #s1-8}

Therefore $F(T)$ is not invertible.


::: pf-proof

Step [](#s1-7){.pf-ref} gives a nonzero vector
$$
v\in\ker F(T).
$$
Hence
$$
F(T)
$$
is not injective and therefore not invertible.

:::

:::

::: {.pf-step #s1-9}

Consequently,
$$
\boxed{
F(T)\text{ is invertible}
\iff
\gcd(F,m_T)=1.
}
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} prove the forward implication from coprimality to invertibility.
Steps [](#s1-5){.pf-ref} through [](#s1-8){.pf-ref} prove the contrapositive of the reverse implication.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the required equivalence.

:::

:::

:::
