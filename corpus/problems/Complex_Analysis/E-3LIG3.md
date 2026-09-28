---
schema: qual/card@1
id: E-3LIG3
kind: problem
title: Entire functions satisfying $g(1-z)=1-g(z)$ are surjective
classification:
  areas:
  - complex-analysis
  topics:
  - Picard
  - Entire Functions
relations: []
review: draft
---

::: {.exercise}
Suppose that $g$ is entire and satisfies the functional equation $g(1-z) = 1-g(z)$.
Show that $g(\CC) = \CC$.
:::

::: {.solution}
Assume $g$ is nonconstant; the remark treats constant $g$.
Suppose $g$ omits a value $a$.
Setting $z=1/2$ in the functional equation gives $g(1/2)=1-g(1/2)$, so $g(1/2)=1/2$ and $a\neq 1/2$.
The value $1-a$ is also omitted: if $g(z)=1-a$, then $g(1-z)=1-g(z)=a$.
Since $a\ne1/2$, the values $a$ and $1-a$ are distinct, so the nonconstant entire function $g$ omits two values, contradicting Picard's little theorem.
:::

::: {.remark}
The only constant solution of $g(1-z)=1-g(z)$ is $g\equiv1/2$, which is not surjective. The conclusion holds for every nonconstant solution.
:::
