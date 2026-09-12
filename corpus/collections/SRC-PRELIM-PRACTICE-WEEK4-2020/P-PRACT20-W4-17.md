---
schema: qual/card@1
id: P-PRACT20-W4-17
kind: problem
title: "Week 4: Differential Equations & Linear Algebra, problem 17"
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
What is the dimension of the space of all polynomials p of degree at most 3 such that $p ( - 1 ) = p ( 0 ) = p ( 1 ) = 0 ?$
:::

::: {.solution}
As a general rule, each point you restrict will take away one degree of freedom.
Since order 3 polynomials have 4 degrees of freedom, the dimension of the set of polynomials p satisfying $p ( - 1 ) = p ( 0 ) = p ( 1 ) = 0$ is 1. More explicitly, any polynomial satistying the equations has the form

$$
p ( x ) = \alpha x ( x - 1 ) ( x + 1 ) , \alpha \in \mathbb { R } .
$$
:::
