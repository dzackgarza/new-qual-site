---
schema: qual/card@1
id: P-PRACT20-W4-04
kind: problem
title: The solution of $x\,dy+(y-xe^x)\,dx=0$ through $(1,0)$
classification:
  areas:
  - prelim
  topics:
  - Ordinary Differential Equations
relations: []
review: draft
audit:
  - event: solution-written
    by: claude
    date: 2026-11-19
    note: >-
      Lamport structure over the retained solution, which covers the problem: Week 4 solutions
      (assets/attachments/Week4_solns.pdf), Problem 4, pp. 1-2. Its argument is transcribed step
      by step and the citation is on the card in the solution section, as the project rule for
      exercise proofs requires; nothing is re-derived. Checked against the set: the rephrasing as
      a first-order equation, the perfect-derivative step, the antiderivative x e^x - e^x, and
      C = 0 from y(1) = 0. One thing added as a step that the set leaves implicit: the solution is
      only defined on an interval avoiding x = 0, and the one through x = 1 is (0, inf). No
      statement repair.
---

::: {.problem}
Find the solution of $x\, dy + (y - x e^{x})\, dx = 0$ which passes through the point $(1, 0)$.
:::

::: {.solution}
The argument is transcribed from the retained solution set for this collection, Week 4 solutions (`assets/attachments/Week4_solns.pdf`), Problem 4, pp. 1--2. The problem asks for the solution of
$$
x\,dy+(y-xe^x)\,dx=0
$$
passing through $(1,0)$.

::: pf

::: {.pf-step #rephrase}
On any interval not containing $0$ the equation is equivalent to $xy'(x)+y(x)=xe^x$.

::: pf-proof
Divide $x\,dy+(y-xe^x)dx=0$ by $dx$ and by the nonzero factor $x$: this is the rephrasing the set makes, $x\frac{dy}{dx}+y=xe^x$. The condition $x\ne0$ is what the division requires, so a solution is sought on an interval avoiding $0$; the point $(1,0)$ lies in $(0,\infty)$.
:::

:::

::: {.pf-step #perfect}
The left side is the derivative of $xy(x)$; hence $xy(x)=xe^x-e^x+C$.

::: pf-proof
By the product rule $\frac{d}{dx}\bigl[xy(x)\bigr]=xy'(x)+y(x)$, so the equation says $\frac{d}{dx}[xy]=xe^x$. An antiderivative of $xe^x$ is $xe^x-e^x$: differentiate it, getting $(e^x+xe^x)-e^x=xe^x$. Two functions with the same derivative on an interval differ by a constant, which gives the display.
:::

:::

::: {.pf-step #general}
$y(x)=e^x-\dfrac{e^x}{x}+\dfrac{C}{x}$ on an interval avoiding $0$.

::: pf-proof
Divide the display of step [](#perfect){.pf-ref} by $x\ne0$: $y(x)=\frac{xe^x-e^x+C}{x}$. This is the general solution on either of the two intervals $(-\infty,0)$ and $(0,\infty)$.
:::

:::

::: {.pf-step #initial}
$C=0$, so $y(x)=e^x-\dfrac{e^x}{x}$ on $(0,\infty)$.

::: pf-proof
Evaluate at $x=1$, which is allowed since $1\ne0$: $y(1)=e^1-\frac{e^1}{1}+C=e-e+C=C$. The condition $y(1)=0$ therefore forces $C=0$. The maximal interval of definition containing $1$ and avoiding the singularity of the coefficient at $0$ is $(0,\infty)$.
:::

:::

::: {.pf-step}
The solution through $(1,0)$ is $y(x)=e^x-\dfrac{e^x}{x}$ for $x>0$.

::: pf-proof
Step [](#general){.pf-ref} gives the general solution and step [](#initial){.pf-ref} fixes the constant, so this is the required solution. As a check, $y(1)=e-e=0$, and with $y=e^x-\frac{e^x}{x}$ one has $y'=e^x-\frac{e^x}{x}+\frac{e^x}{x^2}$, so
$$
xy'+y=\Bigl(xe^x-e^x+\frac{e^x}{x}\Bigr)+e^x-\frac{e^x}{x}=xe^x,
$$
which is the rephrased equation of step [](#rephrase){.pf-ref}, so the displayed function does satisfy it.
:::

:::

:::

:::
