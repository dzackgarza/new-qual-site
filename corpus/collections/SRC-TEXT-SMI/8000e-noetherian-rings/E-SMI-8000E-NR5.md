---
schema: qual/card@1
id: E-SMI-8000E-NR5
kind: problem
title: Prime and maximal ideals detected in quotients
classification:
  areas:
  - algebra
  topics:
  - Noetherian Rings
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared both quotient criteria with the local 8000e PDF and extraction, Noetherian-rings problem 5."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Used zero divisors in R/I for the prime criterion and the ideal correspondence above I for the maximal/field criterion."
---

::: {.exercise}
If $R$ is any ring, and $I$ an ideal, $R/I$ is a domain if and only if $I$ is prime, and $R/I$ is a field if and only if $I$ is maximal.
:::


::: solution
<1>1. If $I$ is prime, then $R/I$ is a domain.
::: proof
Because $I$ is prime, it is proper, so $R/I$ is not the zero ring. Suppose
$$
(a+I)(b+I)=0+I.
$$
Then
$$
ab\in I.
$$
Primality gives
$$
a\in I\quad\text{or}\quad b\in I,
$$
so
$$
a+I=0+I\quad\text{or}\quad b+I=0+I.
$$
Thus $R/I$ has no nonzero zero divisors and is a domain.
:::

<1>2. If $R/I$ is a domain, then $I$ is prime.
::: proof
A domain is nonzero, so $I\ne R$. If
$$
ab\in I,
$$
then
$$
(a+I)(b+I)=0
$$
in the domain $R/I$. Hence one factor is zero, so
$$
a\in I\quad\text{or}\quad b\in I.
$$
Therefore $I$ is prime.
:::

<1>3. If $I$ is maximal, then $R/I$ is a field.
::: proof
Let $a+I$ be a nonzero element of $R/I$, so $a\notin I$. The ideal
$$
I+(a)
$$
strictly contains $I$. By maximality,
$$
I+(a)=R.
$$
Thus there are $i\in I$ and $r\in R$ with
$$
i+ra=1.
$$
Modulo $I$ this becomes
$$
(r+I)(a+I)=1+I.
$$
Hence every nonzero element of $R/I$ is invertible, so $R/I$ is a field.
:::

<1>4. If $R/I$ is a field, then $I$ is maximal.
::: proof
Let $J$ be an ideal with
$$
I\subseteq J\subseteq R.
$$
Then $J/I$ is an ideal of the field $R/I$. A field has only the ideals $0$
and itself, so
$$
J/I=0
\quad\text{or}\quad
J/I=R/I.
$$
Thus
$$
J=I
\quad\text{or}\quad
J=R.
$$
Hence $I$ is maximal.
:::

Combining the four steps,
$$
\boxed{R/I\text{ is a domain}\iff I\text{ is prime},}
$$
and
$$
\boxed{R/I\text{ is a field}\iff I\text{ is maximal}.}
$$
:::
