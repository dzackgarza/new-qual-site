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
$$
H^1(G,L^\times)=0
$$
for a finite Galois extension $L/K$ with Galois group $G$.

In the cyclic case, say $G=\langle\sigma\rangle$ of order $n$, this is equivalent to the norm-one formulation:
$$
N_{L/K}(a)=1
\quad\Longleftrightarrow\quad
\exists\,b\in L^\times\text{ such that }
 a=\frac{b}{\sigma(b)}.
$$
Indeed, for a cyclic group the $1$-cocycle condition is determined by the value at $\sigma$, and the condition that this value define a cocycle is exactly that its norm be $1$; the coboundaries take the values $\sigma(b)/b$ at $\sigma$, and replacing $b$ by $b^{-1}$ writes these as $b/\sigma(b)$.

There is also an additive analogue:
$$
H^1(G,L)=0.
$$
For a cyclic extension this says
$$
\Tr_{L/K}(a)=0
\quad\Longleftrightarrow\quad
 a=b-\sigma(b)
$$
for some $b\in L$.
:::
