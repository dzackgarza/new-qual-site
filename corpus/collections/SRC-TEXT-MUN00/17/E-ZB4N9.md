---
schema: qual/card@1
id: E-ZB4N9
kind: problem
title: Boundaries and interiors of plane regions
classification:
  areas:
  - topology
  topics:
  - Boundary
  - Interior
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

Find the boundary and the interior of each of the following subsets of $\mathbb{R}^2$.

(a) $A = \ts{x \times y \mid y = 0}$

(b) $B = \ts{x \times y \mid x > 0 \text{ and } y \neq 0}$

(c) $C = A \cup B$

(d) $D = \ts{x \times y \mid x \text{ is rational}}$

(e) $E = \ts{x \times y \mid 0 < x^2 + y^2 \leq 1}$

(f) $F = \ts{x \times y \mid x \neq 0 \text{ and } y \leq 1/x}$
:::

::: {.solution}
All interiors and boundaries are taken in $\mathbb R^2$.

(a) For the $x$-axis
\[
A=\{(x,y):y=0\},
\]
we have
\[
\operatorname{Int}A=\varnothing,\qquad \operatorname{Bd}A=A.
\]

(b) For
\[
B=\{(x,y):x>0,\ y\ne0\},
\]
the set itself is open, so $\operatorname{Int}B=B$. Its closure is the closed right half-plane $\{x\ge0\}$, since deleting the $x$-axis does not affect density in $x>0$. Therefore
\[
\operatorname{Bd}B=\{x=0\}\cup\{(x,0):x>0\}.
\]

(c) Since
\[
C=A\cup B=\{x>0\}\cup\{y=0\},
\]
we have
\[
\operatorname{Int}C=\{x>0\},
\]
and
\[
\overline C=\{x\ge0\}\cup\{y=0\}.
\]
Hence
\[
\operatorname{Bd}C=\{x=0\}\cup\{(x,0):x\le0\}.
\]

(d) The set
\[
D=\mathbb Q\times\mathbb R
\]
is dense in $\mathbb R^2$ because every open rectangle contains a rational first coordinate. Its interior is empty because every open rectangle also contains irrational first coordinates. Thus
\[
\operatorname{Int}D=\varnothing,\qquad \operatorname{Bd}D=\mathbb R^2.
\]

(e) For the corrected source region
\[
E=\{(x,y):0<x^2+y^2\le1\},
\]
we have
\[
\operatorname{Int}E=\{0<x^2+y^2<1\},
\]
while
\[
\overline E=\{x^2+y^2\le1\}.
\]
Therefore
\[
\operatorname{Bd}E=\{(0,0)\}\cup\{x^2+y^2=1\}.
\]

(f) Let
\[
F=\{(x,y):x\ne0,\ y\le1/x\}.
\]
On each of the open half-planes $x>0$ and $x<0$, the graph $y=1/x$ is continuous and separates the strict and non-strict inequalities. Hence
\[
\operatorname{Int}F=\{x\ne0,\ y<1/x\}.
\]
Every point $(0,y_0)$ is a limit of points of $F$ approached from $x>0$, since $1/x\to+\infty$ as $x\to0^+$. No other new closure points occur. Thus
\[
\overline F=F\cup(\{0\}\times\mathbb R),
\]
and
\[
\operatorname{Bd}F=\{(x,1/x):x\ne0\}\cup(\{0\}\times\mathbb R).
\]
:::
