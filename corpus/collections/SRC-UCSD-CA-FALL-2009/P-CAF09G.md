---
schema: qual/card@1
id: P-CAF09G
kind: problem
title: "Zeros of a sum of sin functions at cube roots of unity"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The trigonometric identity the prose quoted ("for any x+y+w = 0, sin x + sin y + sin w = -4 sin(x/2) sin(y/2) sin(w/2)") is now derived from the sum-to-product formulas, which also settles that it holds for complex arguments rather than only real ones; the card says that, since the whole point is to evaluate the identity at complex z. The vanishing of 1 + rho + rho^2 for a third root of unity other than 1 is proved from (rho^3-1)/(rho-1), the factorization is applied, and 2 pi is checked to be a zero and nonzero. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair.
---

::: {.problem}
Suppose $\rho$ is a third root of 1 (other than 1). Let $f(z) = \sin(z) + \sin(\rho z) + \sin(\rho^2 z)$.
Prove that $f(z)$ has a zero other than $z = 0$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

Let $\rho\ne1$ with $\rho^3=1$, so that $\rho^2+\rho+1=0$, and let $f(z)=\sin z+\sin(\rho z)+\sin(\rho^2z)$.

::: pf

::: {.pf-step #identity}
For all $x,y\in\CC$, with $w=-(x+y)$,
$$
\sin x+\sin y+\sin w=-4\sin\frac x2\,\sin\frac y2\,\sin\frac w2 .
$$

::: pf-proof
The addition and subtraction formulas for $\sin$ and $\cos$ are identities between entire functions, so they hold for complex arguments. Using $\sin u+\sin v=2\sin\frac{u+v}2\cos\frac{u-v}2$, and $w=-(x+y)$,
$$
\sin x+\sin y+\sin w=2\sin\frac{x+y}2\cos\frac{x-y}2-\sin(x+y).
$$
Now $\sin(x+y)=2\sin\frac{x+y}2\cos\frac{x+y}2$, so the display equals
$$
2\sin\frac{x+y}2\left[\cos\frac{x-y}2-\cos\frac{x+y}2\right]
=2\sin\frac{x+y}2\cdot2\sin\frac x2\,\sin\frac y2,
$$
by $\cos A-\cos B=-2\sin\frac{A+B}2\sin\frac{A-B}2$ with $A=\frac{x-y}2$, $B=\frac{x+y}2$, which gives $-\sin\frac x2\sin\left(-\frac y2\right)=\sin\frac x2\sin\frac y2$. Finally $\sin\frac w2=\sin\left(-\frac{x+y}2\right)=-\sin\frac{x+y}2$, so the last display is $-4\sin\frac x2\sin\frac y2\sin\frac w2$.
:::

:::

::: {.pf-step #factorization}
$f(z)=-4\sin\dfrac z2\,\sin\dfrac{\rho z}2\,\sin\dfrac{\rho^2z}2$ for all $z\in\CC$.

::: pf-proof
$z+\rho z+\rho^2z=z(1+\rho+\rho^2)=0$, since $\rho\ne1$ and $\rho^3=1$ give $\rho^2+\rho+1=(\rho^3-1)/(\rho-1)=0$. So step [](#identity){.pf-ref} applies with $x=z$, $y=\rho z$ and $w=\rho^2z$.
:::

:::

::: {.pf-step #zeros}
Every integral multiple of $2\pi$ is a zero of $f$.

::: pf-proof
If $z=2\pi k$ with $k\in\ZZ$ then $\frac z2=\pi k$, and $\sin(\pi k)=0$, so by step [](#factorization){.pf-ref} $f(z)=0$.
:::

:::

::: {.pf-step}
$f$ has a zero other than $0$.

::: pf-proof
$2\pi\ne0$ and step [](#zeros){.pf-ref} gives $f(2\pi)=0$. (The same factorization gives the zeros $\frac{2\pi k}{\rho}$ and $\frac{2\pi k}{\rho^2}$ as well.)
:::

:::

:::
:::
