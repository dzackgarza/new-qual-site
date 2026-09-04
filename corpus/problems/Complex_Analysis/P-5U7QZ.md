---
schema: qual/card@1
id: P-5U7QZ
kind: problem
title: A sharp bound on $|f'(0)|$ for maps to the right half-plane with $f(0)=2$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
Let $\HH_R\da\{w\in\CC:\Re w>0\}$.
Suppose $f:\DD\to\HH_R$ is analytic and satisfies $f(0)=2$.
Find a sharp upper bound for $\abs{f'(0)}$, and prove it is sharp by example.
:::

::: {.solution}
Let
\[
r(w)=\frac{i}{2}w:\HH_R\to\HH,
\qquad
C(w)=\frac{w-i}{w+i}:\HH\to\DD.
\]
Then $r(2)=i$ and $C(i)=0$, so
\[
F\da C\circ r\circ f:\DD\to\DD
\]
satisfies $F(0)=0$. Schwarz's lemma gives $|F'(0)|\le1$.

By the chain rule,
\[
F'(0)=C'(i)\frac{i}{2}f'(0).
\]
Since
\[
C'(w)=\frac{2i}{(w+i)^2},
\qquad
|C'(i)|=\frac12,
\]
we obtain
\[
1\ge |F'(0)|=\frac14|f'(0)|,
\qquad
|f'(0)|\le4.
\]

The bound is sharp. For $|\lambda|=1$, take
\[
f(z)=2\frac{1+\lambda z}{1-\lambda z}.
\]
This maps $\DD$ biholomorphically onto $\HH_R$, satisfies $f(0)=2$, and has
\[
f'(0)=4\lambda.
\]
:::
