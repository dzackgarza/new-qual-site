---
schema: qual/card@1
id: P-YHXGO
kind: problem
title: Multiplicative linear functionals on $A(\DD)$ are point evaluations
classification:
  areas:
  - real-analysis
  topics:
  - Holomorphic Functions
  - Functional Analysis
relations: []
review: draft
---

::: {.problem}
Let $A(\DD)$ be the $\CC$-vector space of all holomorphic functions on $\DD$ and suppose that $L:A(\DD)\to\CC$ is a multiplicative linear functional.
If $L$ is not identically zero, show that there is a $z_0\in\DD$ so that $L(f)=f(z_0)$ for all $f\in A(\DD)$.
:::

::: {.solution}
Write $z$ for the identity function on $\DD$ and set $z_0:=L(z)$.
Since $L$ is not identically zero, choose $f$ with $L(f)\ne0$.
Multiplicativity gives $L(f)=L(f\cdot1)=L(f)L(1)$, so $L(1)=1$.

First, $z_0\in\DD$.
Otherwise $z-z_0$ has no zero in $\DD$, so $1/(z-z_0)\in A(\DD)$ and $$1=L(1)=L\bigl((z-z_0)\cdot\tfrac1{z-z_0}\bigr)=\bigl(L(z)-z_0L(1)\bigr)\,L\bigl(\tfrac1{z-z_0}\bigr)=0,$$ a contradiction.

Now let $f\in A(\DD)$.
Since $z_0\in\DD$, the function $g(z)=\dfrac{f(z)-f(z_0)}{z-z_0}$ has a removable singularity at $z_0$, so $g\in A(\DD)$ and $f-f(z_0)\cdot1=(z-z_0)g$.
Therefore $$L(f)-f(z_0) = L\bigl((z-z_0)g\bigr) = \bigl(L(z)-z_0\bigr)L(g) = 0,$$ so $L(f)=f(z_0)$.
:::
