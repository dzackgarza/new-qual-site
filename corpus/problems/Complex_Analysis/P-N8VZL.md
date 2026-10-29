---
schema: qual/card@1
id: P-N8VZL
kind: problem
title: The Apollonius circle $\left|\frac{z-z_1}{z-z_2}\right|=c$ and its center and radius
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
relations: []
review: draft
---

::: {.problem}
(a) Prove that if $\abs{w_1}=c\abs{w_2}$, where $c>0$, then
$$
\abs{w_1-c^2w_2}=c\abs{w_1-w_2}.
$$

(b) If $c>0$, $c\ne1$, and $z_1\ne z_2$, prove that
$$
\abs{\frac{z-z_1}{z-z_2}}=c
$$
is a circle, and find its center and radius.
:::

::: {.solution}
::: pf

::: {.pf-step #part-a}
(a) holds.

::: pf-proof
Using $\abs{w_1}^2=c^2\abs{w_2}^2$,
$$
\begin{aligned}
\abs{w_1-c^2w_2}^2&=\abs{w_1}^2-2c^2\Re(w_1\bar w_2)+c^4\abs{w_2}^2
=c^2\bigl(\abs{w_2}^2+\abs{w_1}^2\bigr)-2c^2\Re(w_1\bar w_2)\\
&=c^2\abs{w_1-w_2}^2.
\end{aligned}
$$
Both sides are nonnegative, so taking square roots gives (a).
:::

:::

::: pf-step
The set in (b) is the circle with center $\boxed{\frac{z_1-c^2z_2}{1-c^2}}$ and radius $\boxed{\frac{c\abs{z_1-z_2}}{\abs{1-c^2}}}$.

::: pf-proof
For $z\neq z_2$, the equation says $\abs{z-z_1}=c\abs{z-z_2}$, and $z=z_2$ does not satisfy it since $z_1\neq z_2$. By step [](#part-a){.pf-ref} with $w_1=z-z_1$, $w_2=z-z_2$, it implies $\abs{(1-c^2)z-(z_1-c^2z_2)}=c\abs{z_1-z_2}$. Conversely, the computation of step [](#part-a){.pf-ref} gives $\abs{w_1-c^2w_2}^2-c^2\abs{w_1-w_2}^2=(1-c^2)\bigl(\abs{w_1}^2-c^2\abs{w_2}^2\bigr)$, so since $c\neq1$ the two equations are equivalent. Dividing by $\abs{1-c^2}\neq0$ gives the stated circle, whose radius is positive since $z_1\ne z_2$.
:::

:::

:::
:::
