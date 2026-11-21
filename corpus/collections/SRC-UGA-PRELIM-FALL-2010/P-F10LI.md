---
schema: qual/card@1
id: P-F10LI
kind: problem
title: A counterclockwise line integral $\int_C (x^3-y^3)\,dx+(x^3+y^3)\,dy$ is nonnegative
classification:
  areas:
  - prelim
  topics:
  - Line Integrals
  - Green's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Prove that $\int_C (x^3 - y^3)\,dx + (x^3 + y^3)\,dy \ge 0$ for every smooth, simple closed curve $C \subset \RR^2$, oriented counterclockwise.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own application of Green's theorem follows, with the integrand of the double integral as its own step.

::: pf

::: {.pf-step #green}
With $P=x^{3}-y^{3}$ and $Q=x^{3}+y^{3}$, for a smooth simple closed curve $C$ traversed counterclockwise bounding $D$,
$$\int_{C}P\,dx+Q\,dy=\iint_{D}\Big(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Big)dA.$$

::: pf-proof
$P$ and $Q$ have continuous partial derivatives on the plane, $C$ is smooth, simple and closed with the positive orientation, and $D$ is the bounded region it encloses; these are the hypotheses of Green's theorem.
:::

:::

::: {.pf-step #integrand}
$\dfrac{\partial Q}{\partial x}-\dfrac{\partial P}{\partial y}=3(x^{2}+y^{2})\ge0$ on $D$.

::: pf-proof
$\dfrac{\partial Q}{\partial x}=3x^{2}$ and $\dfrac{\partial P}{\partial y}=-3y^{2}$, so the difference is $3x^{2}+3y^{2}=3(x^{2}+y^{2})$, a sum of squares scaled by $3$.
:::

:::

::: {.pf-qed}
$\displaystyle\int_{C}(x^{3}-y^{3})\,dx+(x^{3}+y^{3})\,dy=3\iint_{D}(x^{2}+y^{2})\,dA\ge0$, since the integrand is nonnegative and $D$ has finite area by steps [](#green){.pf-ref} and [](#integrand){.pf-ref}.
:::

:::

:::
