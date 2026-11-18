---
schema: qual/card@1
id: P-TWH7U
kind: problem
title: Extrema of $xy$ on the ellipse $x^2+4y^2=8$
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Using the method of Lagrange Multipliers, find the maximum and minimum values of $f(x,y) = xy$ on the ellipse $x^2 + 4y^2 = 8$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own Lagrange multiplier computation follows, with the system, the elimination of the multiplier and the two cases as separate steps.

Let $f(x,y)=xy$ and $g(x,y)=x^{2}+4y^{2}$; the constraint set $g=8$ is an ellipse, hence compact, so $f$ attains a maximum and a minimum on it.

::: pf

::: {.pf-step #system}
At an extremum on $g=8$ there is $\lambda$ with $y=2\lambda x$ and $x=8\lambda y$.

::: pf-proof
$\nabla f=(y,x)$ and $\nabla g=(2x,8y)$, and $\nabla g\ne(0,0)$ on $g=8$ since $x=y=0$ does not satisfy the constraint; so Lagrange's condition $\nabla f=\lambda\nabla g$ gives $(y,x)=\lambda(2x,8y)$, that is the two displayed equations.
:::

:::

::: {.pf-step #multiplier}
At such a point $x\ne0$, $y\ne0$ and $\lambda=\pm\tfrac14$.

::: pf-proof
If $x=0$ then $y=2\lambda\cdot0=0$, contradicting $x^{2}+4y^{2}=8$; so $x\ne0$, and then $x=8\lambda y$ gives $y\ne0$. Substituting $y=2\lambda x$ into $x=8\lambda y$ gives $x=16\lambda^{2}x$, hence $16\lambda^{2}=1$ and $\lambda=\pm\tfrac14$.
:::

:::

::: {.pf-step #positive}
For $\lambda=\tfrac14$ the extremal points are $(\pm2,\pm1)$ with matching signs, and there $f=2$.

::: pf-proof
$\lambda=\tfrac14$ gives $y=\tfrac{x}{2}$, so the constraint reads $x^{2}+4\cdot\tfrac{x^{2}}{4}=2x^{2}=8$, that is $x=\pm2$ and then $y=\pm1$ with the same sign as $x$; at these points $xy=2$.
:::

:::

::: {.pf-step #negative}
For $\lambda=-\tfrac14$ the extremal points are $(2,-1)$ and $(-2,1)$, and there $f=-2$.

::: pf-proof
$\lambda=-\tfrac14$ gives $y=-\tfrac{x}{2}$, so again $2x^{2}=8$ and $x=\pm2$ with $y$ of the opposite sign; then $xy=-2$.
:::

:::

::: {.pf-qed}
The only candidate points are those of steps [](#positive){.pf-ref} and [](#negative){.pf-ref}, so the maximum of $f$ on the ellipse is $2$ and the minimum is $-2$.
:::

:::

:::
