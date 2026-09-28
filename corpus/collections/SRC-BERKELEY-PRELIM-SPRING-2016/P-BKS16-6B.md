---
schema: qual/card@1
id: P-BKS16-6B
kind: problem
title: Optimality condition for nonnegative least squares
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $A$ be an $m\times n$ real matrix and $y\in\RR^m$.
Let $x\in\RR^n$ be a vector with nonnegative entries that minimizes the Euclidean distance $\norm{y-Ax}$ among all nonnegative vectors $x$.
Show that the vector
$$
v=A^T(y-Ax)
$$
has nonnegative entries.
:::

::: {.remark}
Erratum: the conclusion is false as printed in the source; the correct sign is nonpositive.
For $\varphi(x)\coloneqq\norm{y-Ax}^2$ one has $\partial\varphi/\partial x_i=-2v_i$.
Since $x+te_i$ is a nonnegative vector for every $t>0$, minimality of $x$ gives $\partial\varphi/\partial x_i\ge0$, that is, $v_i\le0$ for every $i$; if $x_i>0$, then $x+te_i$ is also admissible for small $t<0$, so $v_i=0$.
For $m=n=1$, $A=(1)$ and $y=-1$, the minimizer is $x=0$ and $v=-1<0$.
:::
