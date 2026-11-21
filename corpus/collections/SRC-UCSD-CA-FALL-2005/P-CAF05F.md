---
schema: qual/card@1
id: P-CAF05F
kind: problem
title: "Statement and proof of Harnack's inequality for harmonic functions"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the exam paper retained at assets/attachments/FA05_220_Complex_Analysis_Qual.pdf,
    "MATH 220. Complex Analysis, Qualifying exam. September 8, 2005", Problem 6: "State and prove
    Harnack's inequality for non-negative functions that are continuous in the closure of the disc
    and harmonic in the disc. (You may use without proof the Poisson integral formula.)" The card's
    statement is that problem verbatim.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked the kernel estimate by
    completing the square, 1 - 2r cos(theta) + r^2 = (1-r)^2 + 2r(1 - cos(theta)), which gives
    both bounds in one line; checked that the mean-value property identifies the average of the
    boundary values with u(0) and that the hypothesis of continuity on the closed disc is what lets
    the Poisson formula be applied to the boundary values. No retained published solution covers
    this problem, so the argument is the card's own, and the card now says so.
---

::: {.problem}
State and prove Harnack's inequality for non-negative functions that are continuous in $\overline{\DD}$ and harmonic in $\DD$.
(You may use without proof the Poisson integral formula.)
:::

::: {.solution}
This is Problem 6 of the UCSD complex-analysis qualifying exam of 8 September 2005 (`assets/attachments/FA05_220_Complex_Analysis_Qual.pdf`). No published solution set is transcribed: the argument below is the card's own, and it is the standard Poisson-kernel proof that the exam's permission to use the Poisson integral formula invites.

::: pf

::: {.pf-step #statement}
For $u$ harmonic in $\DD$, continuous and nonnegative on $\overline{\DD}$, and $z\in\DD$,
$$\frac{1-\abs{z}}{1+\abs{z}}\,u(0)\leq u(z)\leq\frac{1+\abs{z}}{1-\abs{z}}\,u(0).$$

::: pf-proof
This is the inequality to be proved; it is the statement of Harnack's inequality for the disc in the form the exam asks for. Write $z=re^{i\phi}$ with $0\leq r<1$; for $r=0$ both quotients are $1$ and the inequality is an equality.
:::
:::

::: {.pf-step #kernel}
For $0\leq r<1$ and every $\theta$ the Poisson kernel satisfies $\frac{1-r}{1+r}\leq P_{r}(\theta)\leq\frac{1+r}{1-r}$.

::: pf-proof
$P_{r}(\theta)=\frac{1-r^{2}}{1-2r\cos\theta+r^{2}}$ and
$1-2r\cos\theta+r^{2}=(1-r)^{2}+2r(1-\cos\theta)$, so $(1-r)^{2}\leq1-2r\cos\theta+r^{2}\leq(1+r)^{2}$. Dividing $1-r^{2}=(1-r)(1+r)$ by these bounds gives the two inequalities.
:::
:::

::: {.pf-step #integrate}
$\frac{1-r}{1+r}\cdot\frac{1}{2\pi}\int_{0}^{2\pi}u(e^{it})\,dt\leq u(re^{i\phi})\leq\frac{1+r}{1-r}\cdot\frac{1}{2\pi}\int_{0}^{2\pi}u(e^{it})\,dt$.

::: pf-proof
The Poisson integral formula, which the exam allows, gives $u(re^{i\phi})=\frac{1}{2\pi}\int_{0}^{2\pi}P_{r}(\phi-t)u(e^{it})\,dt$; it applies because $u$ is continuous on $\overline{\DD}$ and harmonic in $\DD$. The boundary values $u(e^{it})$ are nonnegative, so multiplying the bounds of step [](#kernel){.pf-ref} by them preserves the inequalities pointwise, and integrating against the nonnegative weight $\frac{dt}{2\pi}$ preserves them too.
:::
:::

::: {.pf-step #meanvalue}
$\frac{1}{2\pi}\int_{0}^{2\pi}u(e^{it})\,dt=u(0)$, and therefore the boxed inequality holds.

::: pf-proof
$u$ is harmonic in a neighbourhood of $\overline{\DD}$, so the mean-value property at the centre gives $u(0)=\frac{1}{2\pi}\int_{0}^{2\pi}u(e^{it})\,dt$; substituting this value in step [](#integrate){.pf-ref} gives the statement of step [](#statement){.pf-ref} for every $z\in\DD$.
:::
:::
:::

:::
