---
schema: qual/card@1
id: P-TRIV-DE03
kind: problem
title: First-order linear equation $(x+1)y'=2y+(x+1)^{5/2}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 3, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
${ \mathrm { S o l v e ~ } } ( x + 1 ) { \frac { d y } { d x } } = 2 y + ( x + 1 ) ^ { 5 / 2 } { \mathrm { ~ w i t h ~ } } y ( 0 ) = 3$
:::

::: {.solution}
Work on the interval
$$
x>-1,
$$
which contains the initial point $x=0$.

<1>1. Divide the equation by $x+1$:
$$
y'
-
\frac{2}{x+1}y
=
(x+1)^{3/2}.
$$

::: {.proof}
Since $x>-1$, one has $x+1\neq0$. Divide both sides of the differential equation by $x+1$.
:::

<1>2. An integrating factor is
$$
\mu(x)
=
\exp\left(
\int -\frac2{x+1}\,dx
\right)
=
(x+1)^{-2}.
$$

::: {.proof}
One has
$$
\int -\frac2{x+1}\,dx
=
-2\log(x+1)
$$
on $x>-1$. Exponentiating gives the stated factor.
:::

<1>3. Multiplying step <1>1 by $\mu(x)$ gives
$$
\frac d{dx}
\left[
(x+1)^{-2}y
\right]
=
(x+1)^{-1/2}.
$$

::: {.proof}
The left side becomes
$$
(x+1)^{-2}y'
-
2(x+1)^{-3}y,
$$
which is exactly the derivative of $(x+1)^{-2}y$. The right side is
$$
(x+1)^{-2}(x+1)^{3/2}
=
(x+1)^{-1/2}.
$$
:::

<1>4. Integrating gives
$$
(x+1)^{-2}y
=
2\sqrt{x+1}
+
C.
$$

::: {.proof}
An antiderivative of $(x+1)^{-1/2}$ is $2\sqrt{x+1}$.
:::

<1>5. Hence
$$
y(x)
=
2(x+1)^{5/2}
+
C(x+1)^2.
$$

::: {.proof}
Multiply step <1>4 by $(x+1)^2$.
:::

<1>6. The initial condition $y(0)=3$ gives
$$
C=1.
$$

::: {.proof}
Substitute $x=0$ into step <1>5:
$$
3
=
2
+
C.
$$
:::

<1>7. Therefore the solution is
$$
\boxed{
y(x)
=
(x+1)^2
+
2(x+1)^{5/2},
\qquad
x>-1.
}
$$

::: {.proof}
Substitute $C=1$ from step <1>6 into step <1>5.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 satisfies both the differential equation and the initial condition.
:::
:::
