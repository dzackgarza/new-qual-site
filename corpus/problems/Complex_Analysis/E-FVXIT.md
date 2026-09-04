---
schema: qual/card@1
id: E-FVXIT
kind: problem
title: Sharp bound on $|f'(0)|$ for $f:\mathbb{D}\to\mathbb{H}$ with $f(0)=2$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.problem}
Let $\HH_R\da\{w\in\CC:\Re w>0\}$.
Suppose $f:\DD\to\HH_R$ is analytic and satisfies $f(0)=2$.
Find a sharp upper bound for $|f'(0)|$, and prove sharpness by example.
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
satisfies $F(0)=0$.
Schwarz's lemma gives $|F'(0)|\le1$.

By the chain rule,
\[
F'(0)=C'(r(f(0)))\,r'(f(0))\,f'(0)
=C'(i)\frac{i}{2}f'(0).
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

The bound is sharp.
For $|\lambda|=1$, take $F(z)=\lambda z$ and unwind the conjugation:
\[
f(z)=r^{-1}\!\left(C^{-1}(\lambda z)\right)
=2\frac{1+\lambda z}{1-\lambda z}.
\]
This maps $\DD$ biholomorphically onto $\HH_R$, satisfies $f(0)=2$, and
\[
f'(0)=4\lambda,
\]
so $|f'(0)|=4$.
:::
