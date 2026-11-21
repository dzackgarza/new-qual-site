---
schema: qual/card@1
id: P-BKF04-8A
kind: problem
title: A complex linear map with $\langle Tv,v\rangle=0$ for all $v$ is zero
classification:
  areas: [prelim]
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the polarization identity, the rotated identity
    from substituting $ix$, the consequence that the form vanishes, and the conclusion. No retained
    solution set covers this exercise (the collection retains the examination, not solutions), so the
    argument is the card's own; it was re-read for this pass and agrees with the convention stated on
    the card, linearity in the first variable.
---

::: {.problem}
Let $\langle\ ,\ \rangle$ be a positive-definite Hermitian inner product on a finite-dimensional complex vector space $V$. Suppose $T\colon V\to V$ is a $\CC$-linear map such that $\langle Tv,v\rangle=0$ for all $v\in V$. Prove that $T=0$.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own. The inner product is taken linear in the first variable and conjugate-linear in the second, and it is positive definite, so $\langle v,v\rangle=0$ forces $v=0$.

::: pf

::: {.pf-step #polarization}
$\langle Tx,y\rangle+\langle Ty,x\rangle=0$ for all $x,y\in V$.

::: pf-proof
Expand $\langle T(x+y),x+y\rangle$ using additivity of $T$ and linearity in the first variable, conjugate-linearity in the second:
$$
\langle T(x+y),x+y\rangle=\langle Tx+T y,x+y\rangle=\langle Tx,x\rangle+\langle Tx,y\rangle+\langle Ty,x\rangle+\langle Ty,y\rangle .
$$
The hypothesis gives $\langle T(x+y),x+y\rangle=0$, $\langle Tx,x\rangle=0$ and $\langle Ty,y\rangle=0$, so subtracting leaves $\langle Tx,y\rangle+\langle Ty,x\rangle=0$.
:::

:::

::: {.pf-step #rotate}
$i\langle Tx,y\rangle-i\langle Ty,x\rangle=0$ for all $x,y\in V$.

::: pf-proof
Apply the identity of step [](#polarization){.pf-ref} with $ix$ in place of $x$ and the same $y$. Using $\langle T(ix),y\rangle=i\langle Tx,y\rangle$ and $\langle Ty,ix\rangle=\bar{i}\langle Ty,x\rangle=-i\langle Ty,x\rangle$, the identity reads $i\langle Tx,y\rangle-i\langle Ty,x\rangle=0$.
:::

:::

::: {.pf-step #vanishes}
$\langle Tx,y\rangle=0$ for all $x,y\in V$.

::: pf-proof
Multiplying the identity of step [](#rotate){.pf-ref} by $-i$ gives $\langle Tx,y\rangle-\langle Ty,x\rangle=0$. Adding this to the identity of step [](#polarization){.pf-ref} gives $2\langle Tx,y\rangle=0$, hence $\langle Tx,y\rangle=0$ for every $x$ and $y$.
:::

:::

::: {.pf-step}
$T=0$.

::: pf-proof
Fix $x\in V$ and take $y=Tx$ in step [](#vanishes){.pf-ref}: then $\langle Tx,Tx\rangle=0$, and positive definiteness gives $Tx=0$. As $x$ was arbitrary, $T$ is the zero map. The argument uses no finite-dimensionality, only the inner product axioms and additivity of $T$.
:::

:::

:::

:::

::: {.remark}
The argument does not use $\dim V<\infty$, so the conclusion holds for every complex inner product space $V$.
:::
