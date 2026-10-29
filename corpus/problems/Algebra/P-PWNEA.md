---
schema: qual/card@1
id: P-PWNEA
kind: problem
title: Integral closure of $\ZZ$ in $\QQ(i)$
classification:
  areas:
  - algebra
  topics:
  - Integral Extensions
  - Number Theory
  - Commutative Algebra
relations: []
review: draft
---

::: {.problem}
Determine the integral closure of $\ZZ$ in $\QQ(i)$.
:::

::: {.solution}

::: pf

::: {.pf-step #contains}
$\ZZ[i]$ is contained in the integral closure.

::: pf-proof
For $a,b\in\ZZ$, the element $a+bi$ is a root of the monic polynomial $x^2-2ax+(a^2+b^2)\in\ZZ[x]$.
:::

:::

::: {.pf-step #trace-norm}
If $\alpha=a+bi$ with $a,b\in\QQ$ is integral over $\ZZ$, then $2a\in\ZZ$ and $a^2+b^2\in\ZZ$.

::: pf-proof
Complex conjugation is an automorphism of $\QQ(i)$ fixing $\ZZ$, so $\bar\alpha=a-bi$ is integral too. Sums and products of integral elements are integral, so $\alpha+\bar\alpha=2a$ and $\alpha\bar\alpha=a^2+b^2$ are rational numbers integral over $\ZZ$. Since $\ZZ$ is integrally closed in $\QQ$, both lie in $\ZZ$.
:::

:::

::: {.pf-step #reverse}
If $\alpha=a+bi$ with $a,b\in\QQ$ is integral over $\ZZ$, then $a,b\in\ZZ$.

::: pf-proof
By step [](#trace-norm){.pf-ref}, $m\coloneqq2a\in\ZZ$ and $(2b)^2=4(a^2+b^2)-m^2\in\ZZ$. A rational number whose square is an integer is an integer, so $k\coloneqq2b\in\ZZ$. Then $m^2+k^2=4(a^2+b^2)\equiv0\pmod4$. Squares are $0$ or $1$ modulo $4$, so $m^2\equiv k^2\equiv0\pmod 4$, and $m,k$ are even. Hence $a,b\in\ZZ$.
:::

:::

::: pf-step
The integral closure of $\ZZ$ in $\QQ(i)$ is $\boxed{\ZZ[i]}$.

::: pf-proof
Every element of $\QQ(i)$ is $a+bi$ with $a,b\in\QQ$, so steps [](#contains){.pf-ref} and [](#reverse){.pf-ref} give both inclusions.
:::

:::

:::

:::
