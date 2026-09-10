---
schema: qual/card@1
id: P-SRI2S
kind: problem
title: Galois group of $x^2+1$ and the Gaussian integers
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Integral Extensions
  - Number Theory
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
What's the Galois group of $x^2 + 1$ over $\mathbb{Q}$? What's the integral closure of $\mathbb{Z}$ in $\mathbb{Q}(i)$?
:::

::: solution
The polynomial $x^2+1$ is irreducible over $\mathbb Q$, and its splitting field is
\[
\mathbb Q(i).
\]
Thus
\[
[\mathbb Q(i):\mathbb Q]=2,
\qquad
\operatorname{Gal}(\mathbb Q(i)/\mathbb Q)
=\{1,\text{complex conjugation}\}
\cong C_2.
\]

Now let $\alpha=a+bi\in\mathbb Q(i)$ be integral over $\mathbb Z$. Its trace and norm are integers:
\[
2a=\operatorname{Tr}(\alpha)\in\mathbb Z,
\qquad
a^2+b^2=N(\alpha)\in\mathbb Z.
\]
Put $m=2a\in\mathbb Z$. Then
\[
(2b)^2=4(a^2+b^2)-m^2\in\mathbb Z.
\]
Since $2b\in\mathbb Q$ and its square is an integer, $2b\in\mathbb Z$. Moreover
\[
m^2+(2b)^2=4(a^2+b^2)\equiv0\pmod4.
\]
Squares modulo $4$ are $0$ or $1$, so both $m$ and $2b$ are even. Hence $a,b\in\mathbb Z$.

Conversely, $i$ is integral because it satisfies $x^2+1=0$, so every element of $\mathbb Z[i]$ is integral. Therefore the integral closure of $\mathbb Z$ in $\mathbb Q(i)$ is
\[
\boxed{\mathbb Z[i]}.
\]
:::
