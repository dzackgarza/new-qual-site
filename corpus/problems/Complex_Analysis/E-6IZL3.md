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
For complex-valued $u$ the conditions cut out no family simpler than the conditions themselves, which is why the solution treats real-valued $u$. For every real harmonic $h$ on $\DD$ with $h(1/2)=0$, $u=2+ih$ satisfies both, since $\abs{u}^2=4+h^2$. The real part need not be constant either: for $0<\eps\le1$ and $K^2\ge4\eps$, the harmonic function $u=2+\eps\qty{(x-\tfrac12)^2-y^2}+iKy$ has $u(1/2)=2$ and $\Re u\ge2-\eps y^2\ge1$ on $\overline\DD$, so $\abs{u}^2\ge(2-\eps y^2)^2+K^2y^2\ge4+(K^2-4\eps)y^2\ge4$.
:::
