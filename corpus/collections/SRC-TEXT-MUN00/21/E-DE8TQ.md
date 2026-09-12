---
schema: qual/card@1
id: E-DE8TQ
kind: problem
title: Isometric imbeddings
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $X$ and $Y$ be metric spaces with metrics $d_X$ and $d_Y$, respectively.
Let $f: X \to Y$ have the property that for every pair of points $x_1, x_2$ of $X$,

$$
d_Y(f(x_1), f(x_2)) = d_X(x_1, x_2).
$$

Show that $f$ is an imbedding.
It is called an isometric imbedding of $X$ in $Y$.
:::

::: {.solution}
If $f(x_1)=f(x_2)$, then
\[
d_X(x_1,x_2)=d_Y(f(x_1),f(x_2))=0,
\]
so $x_1=x_2$. Thus $f$ is injective.

Moreover
\[
d_Y(f(x_1),f(x_2))=d_X(x_1,x_2)
\]
shows directly that $f$ is continuous: the inverse image of the radius-$r$ ball in $f(X)$ about $f(x)$ is the radius-$r$ ball in $X$ about $x$. The inverse map
\[
f^{-1}:f(X)\to X
\]
has the same property and is therefore continuous. Hence $f:X\to f(X)$ is a homeomorphism, so $f$ is an embedding.
:::
