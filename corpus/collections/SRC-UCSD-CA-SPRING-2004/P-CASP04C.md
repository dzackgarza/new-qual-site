---
schema: qual/card@1
id: P-CASP04C
kind: problem
title: "Meromorphic functions satisfying |f + g| ≤ |g| are proportional"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $f$ and $g$ be meromorphic functions in $\mathbb{C}$.
Assume that $|f(z) + g(z)| \leq |g(z)|$ for every $z \in \mathbb{C}$ which is not a pole of either $f$ or $g$.
Show that there is a constant $c$ with $|c + 1| \leq 1$ such that $f(z) = cg(z)$.
:::

::: {.solution}
If $g\equiv0$, the inequality forces $f\equiv0$, and we may take $c=0$.
Assume $g\not\equiv0$ and consider the meromorphic quotient
\[
h=\frac fg.
\]
At every point where $f$ and $g$ are finite and $g\ne0$, the hypothesis gives
\[
|h+1|\le1.
\]
Thus $h$ is bounded on the complement of its isolated exceptional points.
No such point can be a pole of $h$, because a meromorphic function is
unbounded near a pole. Hence every exceptional point is removable, and $h$
extends to an entire function satisfying $|h+1|\le1$ everywhere.

By Liouville's theorem, $h$ is constant, say $h\equiv c$. Then
\[
f=cg,
\qquad |c+1|\le1,
\]
as required.
:::
