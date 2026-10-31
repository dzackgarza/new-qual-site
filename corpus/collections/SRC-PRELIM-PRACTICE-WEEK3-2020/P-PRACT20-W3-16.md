---
schema: qual/card@1
id: P-PRACT20-W3-16
kind: problem
title: Recovering $f(x,y)$ from its partial derivatives $2x+y$ and $x+2y$
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Partial Derivatives
relations: []
review: draft
---

::: {.problem}
Find all functions $f(x, y)$ satisfying $\frac{\partial f}{\partial x}(x, y) = 2x + y$, $\frac{\partial f}{\partial y}(x, y) = x + 2y$.
:::

::: {.solution}
Integrating the first equation in $x$, we find $f(x,y)=x^2+xy+g(y)$ for some function $g$. Differentiating in $y$ shows that $x+g'(y)=x+2y$, so $g'(y)=2y$ and $g(y)=y^2+C$. Thus $f(x,y)=x^2+xy+y^2+C$, where $C$ is a constant, and every such function satisfies both equations.
:::
