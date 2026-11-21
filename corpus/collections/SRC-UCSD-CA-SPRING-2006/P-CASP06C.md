---
schema: qual/card@1
id: P-CASP06C
kind: problem
title: "Periodic entire function with subexponential growth is constant"
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
    Lamport structure. The independence of the Fourier coefficient a_n from y is proved by Cauchy's theorem on the period rectangle, with the cancellation of the vertical sides coming from periodicity. The two limits are written with the right monotonicity: for n >= 1, |y| = -y and the coefficient 2 pi n - C is positive, so y -> -infinity sends the bound to 0; for n <= -1 the coefficient C + 2 pi n is negative, so y -> +infinity does. The passage from a_n = 0 to c_n(y) = 0 uses c_n(y) = a_n e^{2 pi n y}, which the prose did not write. No retained solution set covers the exercise; the card says the argument is its own. No statement repair.
---

::: {.problem}
$f$ is an entire function.
Assume that $f(z + 1) = f(z)$ and $\abs{f(z)} \leq e^{C\abs{z}}$ for some $C < 2\pi$.
Show that $f$ is a constant.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

For $n\in\ZZ$ and $y\in\RR$ put
$$
a_n(y)=\int_0^1f(x+iy)e^{-2\pi in(x+iy)}\,dx .
$$

::: pf

::: {.pf-step #independent}
For each $n$ the function $y\mapsto a_n(y)$ is constant.

::: pf-proof
Let $h(z)=f(z)e^{-2\pi inz}$, entire because $f$ is entire and the exponential is entire. For $y_1<y_2$ the boundary of the rectangle $[0,1]\times[y_1,y_2]$ is a closed contour, so by Cauchy's theorem
$$
0=\oint h(z)\,dz=\int_0^1h(x+iy_2)dx-\int_0^1h(x+iy_1)dx,
$$
the two vertical sides cancelling because $h$ is $1$-periodic (as $f$ is, and $e^{-2\pi in(z+1)}=e^{-2\pi inz}$). Hence $a_n(y_2)=a_n(y_1)$; write $a_n$ for the common value.
:::

:::

::: {.pf-step #growth}
For $0\le x\le1$ and all $y$, $\abs{f(x+iy)}\le e^{C(\abs y+1)}$, so $\abs{a_n}\le e^{C(\abs y+1)}e^{2\pi ny}$ for every $y$.

::: pf-proof
$\abs{x+iy}\le1+\abs y$, so the hypothesis gives $\abs{f(x+iy)}\le e^{C(1+\abs y)}$. Also $\abs{e^{-2\pi in(x+iy)}}=e^{2\pi ny}$, since $\abs{e^{-2\pi inx}}=1$ and $e^{-2\pi in(iy)}=e^{2\pi ny}$. Bounding the integrand in the definition of $a_n$ and using that the interval has length $1$ gives the estimate.
:::

:::

::: {.pf-step #positive}
$a_n=0$ for every $n\ge1$.

::: pf-proof
Let $y\to-\infty$ in the estimate of step [](#growth){.pf-ref}, writing $\abs y=-y$:
$$
\abs{a_n}\le e^{C}e^{(2\pi n-C)y}\longrightarrow0,
$$
because $2\pi n\ge2\pi>C$ makes the exponent's coefficient $2\pi n-C$ positive while $y\to-\infty$. So $\abs{a_n}=0$.
:::

:::

::: {.pf-step #negative}
$a_n=0$ for every $n\le-1$.

::: pf-proof
Let $y\to+\infty$: $\abs{a_n}\le e^{C}e^{(C+2\pi n)y}\to0$, because $C+2\pi n\le C-2\pi<0$.
:::

:::

::: {.pf-step #constant}
$f$ is constant.

::: pf-proof
Fix $y$. The function $x\mapsto f(x+iy)$ is continuous, $1$-periodic and piecewise $C^1$, so its Fourier series converges to it:
$$
f(x+iy)=\sum_{n\in\ZZ}c_n(y)e^{2\pi inx},\qquad c_n(y)=\int_0^1f(x+iy)e^{-2\pi inx}dx=a_n(y)e^{2\pi ny}.
$$
By steps [](#positive){.pf-ref} and [](#negative){.pf-ref}, $c_n(y)=0$ for every $n\ne0$, so $f(x+iy)=c_0(y)=a_0$ for every $x$; this holds for every $y$, with the same $a_0$ by step [](#independent){.pf-ref}. Hence $f\equiv a_0$ is constant.
:::

:::

:::
:::
