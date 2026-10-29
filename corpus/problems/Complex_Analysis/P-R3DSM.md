---
schema: qual/card@1
id: P-R3DSM
kind: problem
title: Reverse triangle inequality $|z-w|\ge\bigl||z|-|w|\bigr|$ and equality cases
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
relations: []
review: draft
---

::: {.problem}
Prove the following inequality, and explain when equality holds:
$$
\abs{z-w} \geq \abs{ \abs{z} - \abs{w} }
.$$
:::

::: {.solution}

::: pf

::: {.pf-step #expand}

$\abs{z-w}^2-\bigl(\abs z-\abs w\bigr)^2=2\bigl(\abs z\abs w-\Re(z\bar w)\bigr)$.

::: pf-proof

$$
\begin{aligned}
\abs{z-w}^2&=(z-w)(\bar z-\bar w)=\abs z^2+\abs w^2-z\bar w-\bar zw\\
&=\abs z^2+\abs w^2-2\Re(z\bar w),
\end{aligned}
$$
and $\bigl(\abs z-\abs w\bigr)^2=\abs z^2+\abs w^2-2\abs z\abs w$.

:::

:::

::: pf-step

$\abs{z-w}\ge\abs{\abs z-\abs w}$.

::: pf-proof

Since $\Re(z\bar w)\le\abs{z\bar w}=\abs z\abs w$, step [](#expand){.pf-ref} gives $\abs{z-w}^2\ge\bigl(\abs z-\abs w\bigr)^2$. Both sides of the claim are nonnegative, so taking square roots gives it.

:::

:::

::: pf-step

Equality holds if and only if $z\bar w\ge0$, that is, if and only if $z$ and $w$ lie on a common ray from $0$ (one of them may be $0$).

::: pf-proof

By step [](#expand){.pf-ref}, equality holds exactly when $\Re(z\bar w)=\abs{z\bar w}$, which means $z\bar w$ is a nonnegative real number. If $w\ne0$ this says $z=(z\bar w/\abs w^2)\,w$ is a nonnegative multiple of $w$; if $w=0$ it always holds.

:::

:::

:::

:::
