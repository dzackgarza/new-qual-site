---
schema: qual/card@1
id: P-AG7QC
kind: problem
title: $z_1,z_2,z_3$ form an equilateral triangle iff $z_1^2+z_2^2+z_3^2=z_1z_2+z_2z_3+z_3z_1$
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
relations: []
review: draft
---

::: {.problem}
Prove that the distinct complex numbers $z_1, z_2, z_3$ are the vertices of an equilateral triangle if and only if
$$
z_{1}^{2}+z_{2}^{2}+z_{3}^{2}=z_{1} z_{2}+z_{2} z_{3}+z_{3} z_{1}
.$$
:::

::: {.solution}
Put $a=z_2-z_1$ and $b=z_3-z_1$. Since the points are distinct, $a\ne0$; put $t=b/a$.

::: pf

::: {.pf-step #reduce}

The displayed identity holds if and only if $t^2-t+1=0$, that is, $t = e^{\pm i\pi/3}$.

::: pf-proof

Both sides of the identity change by the same amount under $z_j \mapsto z_j + c$: the difference of the two sides is $\frac12\qty((z_1-z_2)^2+(z_2-z_3)^2+(z_3-z_1)^2)$, which depends only on differences. Taking $c = -z_1$ turns the identity into $a^2+b^2=ab$. Dividing by $a^2 \neq 0$ gives $t^2-t+1=0$, whose roots are $e^{\pm i\pi/3}$.

:::

:::

::: {.pf-step #equi}

The triangle is equilateral if and only if $t = e^{\pm i\pi/3}$.

::: pf-proof

The triangle with vertices $0, a, b$ is equilateral if and only if $b$ is obtained from $a$ by a rotation through $\pm\pi/3$ about $0$, that is, $b = e^{\pm i\pi/3}a$. Indeed, if $b = e^{\pm i\pi/3}a$, then $\abs{b} = \abs{a}$ and $\abs{a - b} = \abs{a}\,\abs{1 - e^{\pm i\pi/3}} = \abs{a}$; conversely, if $\abs{a} = \abs{b} = \abs{a-b}$, the angle at $0$ is $\pi/3$, so $t$ has modulus $1$ and argument $\pm\pi/3$.

:::

:::

::: pf-step

The points $z_1, z_2, z_3$ are the vertices of an equilateral triangle if and only if the displayed identity holds.

::: pf-proof

Translation by $-z_1$ preserves the shape of the triangle, so this follows from steps [](#reduce){.pf-ref} and [](#equi){.pf-ref}.

:::

:::

:::

:::
