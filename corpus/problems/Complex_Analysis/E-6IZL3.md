---
schema: qual/card@1
id: E-6IZL3
kind: problem
title: Harmonic functions on $\DD$ with $u(1/2)=2$ and $\abs u\ge2$
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Maximum Modulus Principle
relations: []
review: draft
---

::: {.exercise}
Find all harmonic functions $u:\DD\to \CC$ such that $u(1/2) = 2$ and $\abs{u(z)}\geq 2$ for all $\abs{z} \leq 1$.
:::

::: {.solution}
Assume $u$ is real-valued; the remark treats complex-valued $u$.
Since $\DD$ is connected, $u$ is continuous and $\abs u\ge2$, either $u\ge2$ on $\DD$ or $u\le-2$ on $\DD$. As $u(1/2)=2$, $u\geq 2$ on $\DD$, so $u$ attains its minimum at the interior point $1/2$. By the minimum principle for harmonic functions, $u\equiv2$. The only such function is the constant $\boxed{u\equiv2}$.
:::

::: {.remark}
For complex-valued $u$ the conditions do not force $u$ to be constant: $u(x+iy)=2+iy$ is harmonic, satisfies $u(1/2)=2$, and has $\abs{u}^2=4+y^2\ge4$.
:::
