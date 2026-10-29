---
schema: qual/card@1
id: P-2SV5S
kind: problem
title: Laurent expansions of $\frac{z+1}{z(z-1)^2}$ about $z=0$ and $z=1$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Poles
  - Principal Parts
relations: []
review: draft
---

::: {.problem}
Find the Laurent expansion of
$$
f(z) = {z+1 \over z(z-1)^2}
$$
about $z=0$ and $z=1$ respectively.
:::

::: {.hint}
Recall that power series can be differentiated.
:::

::: {.solution}

The expansions are given on each maximal annulus centered at the point, and $\zeta\coloneqq z-1$.

::: pf

::: {.pf-step #partial-fractions}
$f(z)=\dfrac1z-\dfrac1{z-1}+\dfrac2{(z-1)^2}$.

::: pf-proof
Clearing denominators, $z+1=(z-1)^2-z(z-1)+2z$, as expanding the right side shows.
:::

:::

::: {.pf-step #series}
For $\abs{w}<1$, $\dfrac1{1-w}=\sum_{n\geq0}w^n$ and $\dfrac1{(1-w)^2}=\sum_{n\geq0}(n+1)w^n$.

::: pf-proof
The first is the geometric series; the second is its term-by-term derivative.
:::

:::

::: pf-step
About $z=0$:
$$
f(z)=\boxed{\frac1z+\sum_{n=0}^\infty(2n+3)z^n} \quad (0<\abs{z}<1),
\qquad
f(z)=\boxed{\sum_{n=2}^\infty(2n-3)z^{-n}} \quad (\abs{z}>1).
$$

::: pf-proof
For $\abs{z}<1$, step [](#partial-fractions){.pf-ref} reads $f(z)=\frac1z+\frac1{1-z}+\frac2{(1-z)^2}$, and step [](#series){.pf-ref} with $w=z$ gives the coefficient $1+2(n+1)=2n+3$ of $z^n$.
For $\abs{z}>1$, step [](#series){.pf-ref} with $w=1/z$ gives $\frac1{z-1}=\sum_{n\geq1}z^{-n}$ and $\frac1{(z-1)^2}=\sum_{n\geq2}(n-1)z^{-n}$; the coefficient of $z^{-1}$ in $f$ is $1-1=0$ and that of $z^{-n}$ for $n\geq2$ is $-1+2(n-1)=2n-3$.
:::

:::

::: pf-step
About $z=1$:
$$
f(z)=\boxed{\frac2{\zeta^2}-\frac1\zeta+\sum_{n=0}^\infty(-1)^n\zeta^n} \quad (0<\abs{\zeta}<1),
\qquad
f(z)=\boxed{\frac1{\zeta^2}+\sum_{n=3}^\infty(-1)^{n+1}\zeta^{-n}} \quad (\abs{\zeta}>1).
$$

::: pf-proof
By step [](#partial-fractions){.pf-ref}, $f(z)=\frac1{1+\zeta}-\frac1\zeta+\frac2{\zeta^2}$.
For $\abs{\zeta}<1$, $\frac1{1+\zeta}=\sum_{n\geq0}(-1)^n\zeta^n$.
For $\abs{\zeta}>1$, $\frac1{1+\zeta}=\sum_{n\geq1}(-1)^{n+1}\zeta^{-n}$, whose $\zeta^{-1}$ term cancels $-\frac1\zeta$ and whose $\zeta^{-2}$ term $-\zeta^{-2}$ combines with $\frac2{\zeta^2}$.
:::

:::

:::

:::
