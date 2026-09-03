---
schema: qual/card@1
id: E-LXPI7
kind: problem
title: Constructing functions with specified singularities
classification:
  areas:
  - complex-analysis
  topics:
  - Singularities
  - Essential Singularities
  - Poles
  - Removable Singularities
relations: []
review: draft
---

:::{.exercise}
Determine a function with

- An essential singularity at $z=1$
- An essential singularity at $z=0$
- A pole of order 1 at $z=1-i$
- A pole of order 2 at $z=1+i$
- A removable singularity at $z=7$

:::

:::{.solution}
Note that writing a single function for each singularity and taking a product *might* work, except that there may be unforeseen cancellation of zeros of one with poles of another, or some might become removable.
A surefire way is to take a sum, e.g. 
\[
f(z) = e^{1\over z-1} + e^{1\over z} + {1\over z - (1-i)} + {1\over (z - (1+i) )^2 } + { z-7 \over \sin(z-7) }
.\]

:::
