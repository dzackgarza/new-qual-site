---
schema: qual/card@1
id: P-CASP09G
kind: problem
title: 'The Fourier transform of $(\sin x/x)^2$'
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
    Lamport structure, and the Fourier transform of sin x / x derived. The prose quoted "a standard contour integral gives" the transform of s; the card now computes it from sin x = (e^{ix} - e^{-ix})/2i and the Dirichlet integral of e^{iax}/x, obtaining (pi/2)(sgn(1+t) - sgn(t-1)) and reading off the three cases, including the endpoint value pi/2. The convolution formula, the description of the integrand's support as an intersection of intervals, and the length computation are steps, and the answer is stated for t >= 0 as asked with the two closed cases agreeing at t = 2. No retained solution set covers the exercise; the card says the argument is its own.
---

::: {.problem}
Evaluate $\int_{-\infty}^{\infty} \left(\frac{\sin x}{x}\right)^2 e^{itx}\,dx$ for all real $t \ge 0$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

Write $s(x)=\frac{\sin x}{x}$ for $x\ne0$ and $s(0)=1$, and $\widehat f(t)=\int_\RR f(x)e^{itx}dx$.

::: pf

::: {.pf-step #transform}
$\widehat s(t)=\pi$ for $\abs t<1$, $\widehat s(t)=0$ for $\abs t>1$, and $\widehat s(\pm1)=\frac\pi2$.

::: pf-proof
Since $\sin x=\frac{e^{ix}-e^{-ix}}{2i}$,
$$
s(x)e^{itx}=\frac{1}{2i}\cdot\frac{e^{i(1+t)x}-e^{i(t-1)x}}{x},
$$
and the improper integral $\int_{-\infty}^{\infty}\frac{e^{iax}}{x}dx$ converges for real $a$ (the Dirichlet test, the numerator being bounded and $1/x$ decreasing to $0$) with value $i\pi\operatorname{sgn}a$. Hence
$$
\widehat s(t)=\frac{1}{2i}\bigl(i\pi\operatorname{sgn}(1+t)-i\pi\operatorname{sgn}(t-1)\bigr)=\frac\pi2\bigl(\operatorname{sgn}(1+t)-\operatorname{sgn}(t-1)\bigr).
$$
For $\abs t<1$ the two signs are $1$ and $-1$, giving $\pi$; for $t>1$ they are both $1$, and for $t<-1$ both $-1$, giving $0$; for $t=1$ and $t=-1$ one sign vanishes, giving $\frac\pi2$.
:::

:::

::: {.pf-step #conv}
$\widehat{s^2}(t)=\dfrac1{2\pi}\displaystyle\int_\RR\widehat s(u)\widehat s(t-u)\,du$.

::: pf-proof
With the convention $\widehat f(t)=\int f(x)e^{itx}dx$, the product formula is $\widehat{fg}=\frac1{2\pi}\widehat f*\widehat g$: both sides are computed by writing $\widehat f(u)\widehat g(t-u)=\iint f(x)g(y)e^{iu x}e^{i(t-u)y}dx\,dy$, integrating in $u$ to get $2\pi\delta(x-y)$-type concentration, and collecting. So $\widehat{s^2}(t)=\frac1{2\pi}\int_\RR\widehat s(u)\widehat s(t-u)du$.
:::

:::

::: {.pf-step #integral}
$\displaystyle\int_\RR\widehat s(u)\widehat s(t-u)\,du=\pi^2\,\abs{[-1,1]\cap[t-1,t+1]}$.

::: pf-proof
By step [](#transform){.pf-ref} the integrand equals $\pi^2$ exactly when $\abs u\le1$ and $\abs{t-u}\le1$, that is $u\in[-1,1]\cap[t-1,t+1]$, and $0$ elsewhere. So the integral is $\pi^2$ times the length of that intersection.
:::

:::

::: {.pf-step #length}
For $t\ge0$ the intersection $[-1,1]\cap[t-1,t+1]$ has length $2-t$ when $t\le2$ and is empty when $t\ge2$.

::: pf-proof
The interval $[t-1,t+1]$ has length $2$ and moves right as $t$ grows. For $0\le t\le2$ its right end $t+1\ge1$ and its left end $t-1\le1$, so the intersection is $[\max(-1,t-1),1]=[t-1,1]$ of length $2-t$. For $t\ge2$ its left end $t-1\ge1$ meets $[-1,1]$ only at the point $1$ when $t=2$ and not at all when $t>2$, so the length is $0$.
:::

:::

::: {.pf-step}
$\displaystyle\int_{-\infty}^{\infty}\Bigl(\frac{\sin x}{x}\Bigr)^2e^{itx}dx=\pi\Bigl(1-\frac t2\Bigr)$ for $0\le t\le2$, and $0$ for $t\ge2$.

::: pf-proof
Combining steps [](#conv){.pf-ref}, [](#integral){.pf-ref} and [](#length){.pf-ref}: for $0\le t\le2$ the value is $\frac1{2\pi}\pi^2(2-t)=\pi(1-\frac t2)$, and for $t\ge2$ it is $0$; the two formulas agree at $t=2$, where both give $0$.
:::

:::

:::
:::
