---
schema: qual/card@1
id: P-DU7X7
kind: problem
title: Hilbert's theorem 90
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
What's Hilbert's theorem 90?
:::

::: {.solution}
Hilbert's Theorem 90 is the statement
\[
H^1(G,L^\times)=0
\]
for a finite Galois extension $L/K$ with Galois group $G$.

In the cyclic case, say $G=\langle\sigma\rangle$ of order $n$, this is equivalent to the familiar norm-one formulation:
\[
N_{L/K}(a)=1
\quad\Longleftrightarrow\quad
\exists\,b\in L^\times\text{ such that }
 a=\frac{b}{\sigma(b)}.
\]
Indeed, for a cyclic group the $1$-cocycle condition is determined by the value at $\sigma$, and the condition that this value define a cocycle is exactly that its norm be $1$; coboundaries have the form $b/\sigma(b)$ (up to the opposite convention).

There is also an additive analogue:
\[
H^1(G,L)=0.
\]
For a cyclic extension this says
\[
\operatorname{Tr}_{L/K}(a)=0
\quad\Longleftrightarrow\quad
 a=b-\sigma(b)
\]
for some $b\in L$ (again up to the sign convention for $1-\sigma$).
:::
