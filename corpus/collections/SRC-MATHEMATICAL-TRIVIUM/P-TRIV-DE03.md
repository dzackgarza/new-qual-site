---
schema: qual/card@1
id: P-TRIV-DE03
kind: problem
title: First-order linear equation $(x+1)y'=2y+(x+1)^{5/2}$
classification:
  areas: [prelim]
  topics:
  - First-Order Linear ODEs
  - Integrating Factors
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 3, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve $(x + 1)\frac{dy}{dx} = 2y + (x + 1)^{5/2}$ with $y(0) = 3$.
:::

::: {.solution}

Work on the interval
$$
x>-1,
$$
which contains the initial point $x=0$.

::: pf

::: {.pf-step #s1-1}

Divide the equation by $x+1$:
$$
y'
-
\frac{2}{x+1}y
=
(x+1)^{3/2}.
$$


::: pf-proof

Since $x>-1$, one has $x+1\neq0$. Divide both sides of the differential equation by $x+1$.

:::

:::

::: pf-step

An integrating factor is
$$
\mu(x)
=
\exp\left(
\int -\frac2{x+1}\,dx
\right)
=
(x+1)^{-2}.
$$


::: pf-proof

One has
$$
\int -\frac2{x+1}\,dx
=
-2\log(x+1)
$$
on $x>-1$. Exponentiating gives the stated factor.

:::

:::

::: pf-step

Multiplying step [](#s1-1){.pf-ref} by $\mu(x)$ gives
$$
\frac d{dx}
\left[
(x+1)^{-2}y
\right]
=
(x+1)^{-1/2}.
$$


::: pf-proof

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

:::

::: {.pf-step #s1-4}

Integrating gives
$$
(x+1)^{-2}y
=
2\sqrt{x+1}
+
C.
$$


::: pf-proof

An antiderivative of $(x+1)^{-1/2}$ is $2\sqrt{x+1}$.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
y(x)
=
2(x+1)^{5/2}
+
C(x+1)^2.
$$


::: pf-proof

Multiply step [](#s1-4){.pf-ref} by $(x+1)^2$.

:::

:::

::: {.pf-step #s1-6}

The initial condition $y(0)=3$ gives
$$
C=1.
$$


::: pf-proof

Substitute $x=0$ into step [](#s1-5){.pf-ref}:
$$
3
=
2
+
C.
$$

:::

:::

::: {.pf-step #s1-7}

Therefore the solution is
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


::: pf-proof

Substitute $C=1$ from step [](#s1-6){.pf-ref} into step [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} satisfies both the differential equation and the initial condition.

:::

:::

:::
