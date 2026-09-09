---
schema: qual/card@1
id: P-F2YIN
kind: problem
title: Factorisation in $R[x_1,\ldots,x_n]$
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Polynomials
  - Irreducibility Criteria
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Talk about factorisation and primes in a polynomial ring.
What is irreducibility?
For what rings $R$ is it true that $R[x_1, \dots , x_n]$ is a unique factorisation domain?
What is wrong with unique factorisation if we don't have a domain?
Now, PIDs are Noetherian, but are there UFDs which are not?
:::

::: solution
Let $R$ be an integral domain. A nonzero nonunit $a\in R$ is **irreducible** if
\[
a=bc\implies b\in R^\times\text{ or }c\in R^\times,
\]
and **prime** if
\[
a\mid bc\implies a\mid b\text{ or }a\mid c.
\]
Every prime element is irreducible. In a UFD, every irreducible is prime.

Gauss's theorem says that if $R$ is a UFD, then $R[x]$ is a UFD. Iterating gives
\[
R\text{ UFD}\implies R[x_1,\dots,x_n]\text{ UFD}.
\]
Conversely, if $R[x_1,\dots,x_n]$ is a UFD, then every nonzero nonunit $a\in R$ factors uniquely there. Because the units of the polynomial ring are exactly the units of $R$, and a factorization of the constant polynomial $a$ can involve only constant factors, this is already a unique factorization in $R$. Hence
\[
R[x_1,\dots,x_n]\text{ is a UFD}\iff R\text{ is a UFD}.
\]

The usual definition of UFD is made for domains. With zero divisors, cancellation fails and factorizations need not behave in the UFD sense; for example, zero divisors and nontrivial idempotents can produce incompatible factorizations. One can study more general factorization theories for rings with zero divisors, but they are not UFDs in the standard sense.

A UFD need not be Noetherian. For example,
\[
k[x_1,x_2,x_3,\dots]
\]
is a UFD. Indeed, every nonzero nonunit belongs to some finite-variable UFD
\[
A_m=k[x_1,\dots,x_m]
\]
and factors there into irreducibles. Each such irreducible $p\in A_m$ is prime in $A_m$, and
\[
k[x_1,x_2,\dots]/(p)
\cong (A_m/(p))[x_{m+1},x_{m+2},\dots]
\]
is a domain, so $p$ remains prime in the full ring. Thus these factorizations are factorizations into primes in the full ring, and uniqueness follows. The ring is not Noetherian because
\[
(x_1)\subsetneq(x_1,x_2)\subsetneq(x_1,x_2,x_3)\subsetneq\cdots
\]
does not stabilize.
:::
