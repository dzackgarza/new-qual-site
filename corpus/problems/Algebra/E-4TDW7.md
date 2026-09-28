---
schema: qual/card@1
id: E-4TDW7
kind: problem
title: $K(a)=K(a^{2})$ when $a$ is algebraic of odd degree over $K$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Polynomials
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

::: {.problem}
Let $F/K$ be a field extension, and let $a \in F$ be algebraic over $K$ of odd degree $[K(a) : K] = 2m + 1$.
Prove that $a^2$ is algebraic over $K$, that $[K(a^2) : K]$ is odd, and that $K(a) = K(a^2)$.
:::

::: {.solution}
Since $a$ is algebraic over $K$, so is $a^2$, and
\[
K\subseteq K(a^2)\subseteq K(a).
\]
Hence the tower law gives
\[
[K(a):K]
=[K(a):K(a^2)]\,[K(a^2):K].
\]

Now $a$ is a root of
\[
x^2-a^2\in K(a^2)[x],
\]
so
\[
[K(a):K(a^2)]\le2.
\]
Therefore this degree is either $1$ or $2$. But it divides the odd integer
\[
[K(a):K]=2m+1,
\]
so it cannot be $2$. Thus
\[
[K(a):K(a^2)]=1,
\qquad
K(a)=K(a^2).
\]
Consequently
\[
[K(a^2):K]=[K(a):K]=2m+1,
\]
which is odd.
:::
