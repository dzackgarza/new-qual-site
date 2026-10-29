---
schema: qual/card@1
id: T-CRVCAST
kind: theorem
title: Castelnuovo's bound for space curves
slogan: 'Castelnuovo is the balanced-quadric bound: maximal-genus nonplanar space curves lie on a quadric with bidegrees as equal as possible.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Space Curves
  - Genus
  - Quadric Surface
relations:
- kind: uses
  target: FE-CRVQUAD
review: draft
prompts:
- How large can the genus of a curve of degree $d$ in $\PP^3$ be?
- State Castelnuovo's bound.
---

::: {.theorem}
Let $k$ be an algebraically closed field and let $C \subseteq \PP^3_k$ be a smooth connected curve of degree $d$ and genus $g$ not contained in a plane.
Then $d \geq 3$ and
$$
g \leq
\begin{cases}
\tfrac{1}{4}d^2 - d + 1 , & d \text{ even} , \\[2pt]
\tfrac{1}{4}(d^2-1) - d + 1 , & d \text{ odd} .
\end{cases}
$$
The bound is attained for every $d \geq 3$, and a curve attaining it lies on a quadric surface.
:::

::: {.remark}
The bound may be written compactly as
$$
g\leq\left\lfloor\frac{(d-2)^2}{4}\right\rfloor.
$$
Balanced curves on a smooth quadric give equality examples. Under the identification
$$
Q\cong\PP^1\times\PP^1,
$$
a curve of type $(a,a)$ has $d=2a$ and $g=(a-1)^2$, while a curve of type $(a,a+1)$ has $d=2a+1$ and $g=a(a-1)$. These are exactly the two displayed numerical bounds.

An extremal curve lies on a quadric surface, but the quadric need not be smooth. The balanced bidegree calculation therefore supplies the equality numerics without asserting that every extremal curve is presented on a smooth quadric.

The nonplanarity hypothesis is necessary: a smooth plane curve of degree $d$ has genus $\binom{d-1}{2}$, which exceeds the bound for $d \geq 3$.
:::
