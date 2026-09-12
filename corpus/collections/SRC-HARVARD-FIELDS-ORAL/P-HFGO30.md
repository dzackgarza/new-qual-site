---
schema: qual/card@1
id: P-HFGO30
kind: problem
title: A simple algebraic field extension is finite
classification:
  areas: [algebra]
  topics: [Field Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Fields and Galois Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
If $a$ is algebraic over $F$, prove that $[F(a):F]$ is finite.
:::

::: solution
Let $m_a(T)\in F[T]$ be the minimal polynomial of $a$ over $F$, and set
\[
d=\deg m_a.
\]

<1>1. Every element of $F(a)$ is represented by a polynomial in $a$ of degree
less than $d$.
::: proof
Because $m_a(a)=0$, Euclidean division gives, for every $f(T)\in F[T]$,
\[
f(T)=q(T)m_a(T)+r(T),
\qquad
\deg r<d.
\]
Evaluating at $a$ gives $f(a)=r(a)$.

Moreover, since $m_a$ is irreducible,
\[
F[a]\cong F[T]/(m_a)
\]
is a field. Hence $F(a)=F[a]$.
:::

<1>2. The elements
\[
1,a,\ldots,a^{d-1}
\]
form an $F$-basis of $F(a)$.
::: proof
They span by <1>1. If
\[
c_0+c_1a+\cdots+c_{d-1}a^{d-1}=0,
\]
then the polynomial $c_0+c_1T+\cdots+c_{d-1}T^{d-1}$ has $a$ as a root.
Minimality of $m_a$ forces this polynomial to be zero, so all coefficients
vanish.
:::

<1>3. Therefore
\[
[F(a):F]=d<\infty.
\]
::: proof
This is the dimension of the basis in <1>2.
:::
:::
