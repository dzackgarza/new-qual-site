---
schema: qual/card@1
id: E-LUR7G
kind: exercise
title: "Show"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
:::{.exercise title="?"}
Show 
\[
x^\ell - 1 \divides x^m-1 \iff \ell\divides m
.\]
:::

:::{.solution}
$\implies$

- Write $m = \ell q + r$ with $0\leq r < \ell$.
- Write 
\[
p(x) = {x^m-1 \over x^\ell - 1}
= {x^{lq+r} -1 \over x^\ell - 1}
= x^r{x^{lq} - 1 \over x^\ell - 1} + {x^r - 1 \over x^\ell - 1}
= q(x) + {x^r-1 \over x^\ell - 1}
,\]
where $p,q$ are polynomial by divisibility.
- So the remaining ratio must be polynomial, but since $r<\ell$ is strict this forces $r=0$.
  Thus $\ell \divides m$.

:::{.remark}
I don't like this proof!
:::

$\impliedby$:

- Write $m = \ell q + r$, then $r=0$ by divisibility.
- Then $x^m-1 = x^{\ell q} - 1 \da z^q-1$ where $z\da x^\ell$. 
- Use that $z-1 \divides z^q - 1$, so $x^{\ell}-1 \divides x{\lq} -1 = x^m-1$.

:::

