---
schema: qual/card@1
id: P-PRACT20-W6-08
kind: problem
title: Continuous surjections and bijections between $(0,1)$ and $[0,1]$
classification:
  areas:
  - prelim
  topics:
  - Continuity
  - Compactness
  - Intermediate Value Theorem
relations: []
review: draft
---

::: {.problem}
Which of the following exist?

(A) A continuous function from $(0, 1)$ onto $[0, 1]$

(B) A continuous function from $[0, 1]$ onto $(0, 1)$

(C) A continuous bijection from $(0, 1)$ to $[0, 1]$
:::

::: {.solution}
(A) Such a function exists: $f(x)=\abs{\sin(2\pi x)}$ is continuous on $(0,1)$, takes values in $[0,1]$, and attains $0$ at $x=1/2$ and $1$ at $x=1/4$, so by the intermediate value theorem it maps $(0,1)$ onto $[0,1]$.

(B) No such function exists. The continuous image of a compact set is compact, and $[0,1]$ is compact while $(0,1)$ is not.

(C) No such function exists. If $f\colon(0,1)\to[0,1]$ is a continuous surjection, there are $a,b\in(0,1)$ with $f(a)=0$ and $f(b)=1$. By the intermediate value theorem, $f$ maps $I=[\min\{a,b\},\max\{a,b\}]$ onto $[0,1]$. Since $(0,1)\setminus I$ is nonempty, any $x$ in it has $f(x)=f(y)$ for some $y\in I$, so $f$ is not injective.
:::
