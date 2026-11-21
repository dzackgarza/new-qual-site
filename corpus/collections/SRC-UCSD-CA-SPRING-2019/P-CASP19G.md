---
schema: qual/card@1
id: P-CASP19G
kind: problem
title: "Poisson integral converges to the boundary value at points of continuity"
classification:
  areas:
  - complex-analysis
  topics:
  - Poisson Kernel
  - Harmonic Functions
  - Boundary Values
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. Three things the prose left as assertions are now steps: the normalisation of the Poisson kernel together with its nonnegativity (which is what lets the first part be bounded by epsilon without a factor), the uniform vanishing of the kernel off the continuity interval, with 1 - 2r cos delta + r^2 -> 2 - 2 cos delta > 0 exhibited, and the splitting with the inequality |theta - t| >= delta derived from |theta - theta_0| < delta and |t - theta_0| >= 2 delta. The boundedness of f is used with M = sup |f| and the final bound is tracked. The initial "limsup <= epsilon" claim is replaced by the direct estimate, since the split already gives it. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair.
---

::: {.problem}
Let $f$ be a bounded, piecewise continuous function on $\partial \DD$, and consider the harmonic function
$$
u(z) = \frac{1}{2\pi} \int_{-\pi}^{\pi} P_r(\theta - t) f(e^{it}) \, dt, \quad z = re^{i\theta},
$$
where $P_r(t) := \operatorname{Re} \frac{1 + re^{it}}{1 - re^{it}}$ is the Poisson kernel in $\DD$.
Assume that $f$ is continuous at $a = e^{i\theta_0}$, and show that $\lim_{z \to a} u(z) = f(a)$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

Write $z=re^{i\theta}$ with $r<1$, $a=e^{i\theta_0}$, and $P_r(t)=\operatorname{Re}\frac{1+re^{it}}{1-re^{it}}=\frac{1-r^2}{1-2r\cos t+r^2}$.

::: pf

::: {.pf-step #mass}
$\dfrac1{2\pi}\displaystyle\int_{-\pi}^{\pi}P_r(t)\,dt=1$ and $P_r\ge0$.

::: pf-proof
$P_r$ is the real part of $\frac{1+re^{it}}{1-re^{it}}$, whose imaginary part is odd in $t$ and integrates to $0$; so $\frac1{2\pi}\int P_r=\operatorname{Re}\frac1{2\pi}\int\frac{1+re^{it}}{1-re^{it}}dt$. By the mean value property applied to the harmonic function $w\mapsto\frac{1+w}{1-w}$ at $0$, or by direct computation, this equals the value of that function at $0$, namely $1$. Finally $1-r^2>0$ and $1-2r\cos t+r^2=\abs{1-re^{it}}^2>0$ for $r<1$, so $P_r\ge0$.
:::

:::

::: {.pf-step #difference}
$u(re^{i\theta})-f(a)=\dfrac1{2\pi}\displaystyle\int_{-\pi}^{\pi}P_r(\theta-t)\bigl(f(e^{it})-f(a)\bigr)\,dt$.

::: pf-proof
Subtract $f(a)=\frac1{2\pi}\int_{-\pi}^{\pi}P_r(\theta-t)f(a)\,dt$ (which is step [](#mass){.pf-ref} after translating $t\mapsto\theta-t$, legitimate since $P_r$ and the interval are $2\pi$-periodic) from the definition of $u$.
:::

:::

::: {.pf-step #kernel}
For $0<\delta<\pi$, $\sup\{P_r(s):\delta\le\abs s\le\pi\}\to0$ as $r\to1^-$.

::: pf-proof
On $\delta\le\abs s\le\pi$ one has $\cos s\le\cos\delta<1$, so
$$
P_r(s)=\frac{1-r^2}{1-2r\cos s+r^2}\le\frac{1-r^2}{1-2r\cos\delta+r^2}\longrightarrow\frac{0}{2-2\cos\delta}=0,
$$
the denominator tending to $2-2\cos\delta>0$.
:::

:::

::: {.pf-step #estimate}
For every $\varepsilon>0$ there is $\rho<1$ such that $\abs{u(re^{i\theta})-f(a)}<\varepsilon(1+2M)$ whenever $r>\rho$ and $\abs{\theta-\theta_0}<\delta$, where $M=\sup_{\partial\DD}\abs f$.

::: pf-proof
Choose $\delta\in(0,\pi)$ with $\abs{f(e^{it})-f(a)}<\varepsilon$ for $\abs{t-\theta_0}<2\delta$, possible by continuity at $a$. Let $r$ be close enough to $1$ that $\sup_{\delta\le\abs s\le\pi}P_r(s)<\varepsilon/(2M+1)$, possible by step [](#kernel){.pf-ref}; and let $\abs{\theta-\theta_0}<\delta$.
Split the integral of step [](#difference){.pf-ref} over $E_1=\{\abs{t-\theta_0}<2\delta\}$ and $E_2$ its complement. On $E_1$ the integrand is bounded by $\varepsilon P_r(\theta-t)$, so that part is at most $\varepsilon\cdot\frac1{2\pi}\int P_r=\varepsilon$ by step [](#mass){.pf-ref}. On $E_2$ we have $\abs{\theta-t}\ge\abs{t-\theta_0}-\abs{\theta-\theta_0}>\delta$, and $\abs{f(e^{it})-f(a)}\le2M$, so that part is at most $2M\cdot\sup_{\delta\le\abs s\le\pi}P_r(s)<2M\varepsilon/(2M+1)<\varepsilon$.
:::

:::

::: {.pf-step}
$\lim_{z\to a}u(z)=f(a)$.

::: pf-proof
Let $\varepsilon>0$, take $\delta$ and $\rho$ from step [](#estimate){.pf-ref}, and let $\eta>0$ be small enough that $\abs{z-a}<\eta$, $\abs z<1$ imply $r>\rho$ and $\abs{\theta-\theta_0}<\delta$. Then $\abs{u(z)-f(a)}<\varepsilon(1+2M)$ there, so $u(z)\to f(a)$ as $z\to a$. Since $\varepsilon$ was arbitrary, the limit is $f(a)$.
:::

:::

:::
:::
