---
schema: qual/card@1
id: P-7VK5X
kind: problem
title: The set $\{(x,y):x-y\in A\}$ is Borel, and null if $A$ is
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Fubini-Tonelli
relations: []
review: draft
---

::: {.problem}
If $A$ is a Borel subset of the line.
Then $E=\{(x,y):x-y\in A\}$ is a Borel subset of the plane.
If $m(A)=0$, then $m\times m(E)=0$.
:::

::: {.solution}
$f:\mathbb{R}^2\to\mathbb{R}$ by $f(x,y)=x-y$ is continuous.
Thus, $E=f^{-1}(A)$ is Borel.
$E^y=\{x\in\mathbb{R}:(x,y)\in E\}=y+A$ which is a null set since $m(y+A)=m(A)=0$.
Thus $m\times m(E)=\int m(E^y)dm(y)=0$.
:::
