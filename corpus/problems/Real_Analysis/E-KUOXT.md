---
schema: qual/card@1
id: E-KUOXT
kind: problem
title: Almost everywhere and uniform convergence of approximations to the identity
classification:
  areas:
  - real-analysis
  topics:
  - Approximations to the Identity
  - Convolution
  - Uniform Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- Show that if additionally $\abs{\phi(x)} \leq c(1 + \abs{x})^{-n-\eps}$ for some $c,\eps>0$, then this converges is almost everywhere.

- Show that is $f$ is bounded and uniformly continuous and $\phi_t$ is an approximation to the identity, then $f\ast \phi_t$ uniformly converges to $f$.
:::

::: {.solution}
Let $\phi \in L^1(\RR^n)$ with $\int \phi = 1$, and put $\phi_t(x) \coloneqq t^{-n}\phi(x/t)$ for $t > 0$, so that $\int \phi_t = 1$ and $\norm{\phi_t}_1 = \norm{\phi}_1$. Part (a) concerns $f \in L^1(\RR^n)$ and the convergence $f \ast \phi_t \to f$ as $t \to 0$. Let $Mf$ denote the Hardy--Littlewood maximal function of $f$.

(a)

::: pf

::: {.pf-step #p1-1}
There is a constant $A$ with $\sup_{t>0}\abs{f \ast \phi_t(x)} \leq A\, Mf(x)$ for every $x$ and every $f \in L^1$.

::: pf-proof
$\Psi(x) \coloneqq c(1+\abs x)^{-n-\eps}$ is radial, radially decreasing, and integrable, and $\abs\phi \leq \Psi$. For a radial, radially decreasing, integrable $\Psi$, $\sup_{t>0}\abs{f\ast\Psi_t(x)} \leq \norm{\Psi}_1\, Mf(x)$; this is the standard maximal inequality for such kernels, proved by writing $\Psi$ as an increasing limit of positive combinations of normalized indicators of balls centered at $0$. Since $\abs{f\ast\phi_t} \leq \abs f \ast \Psi_t$, take $A = \norm\Psi_1$.
:::

:::

::: {.pf-step #p1-2}
For $g \in C_c(\RR^n)$, $g \ast \phi_t \to g$ uniformly as $t \to 0$.

::: pf-proof
$g$ is bounded and uniformly continuous, so this is part (b) below.
:::

:::

::: {.pf-step #p1-3}
For $f \in L^1$ let $\Omega f(x) \coloneqq \limsup_{t \to 0}\abs{f\ast\phi_t(x) - f(x)}$. Then $\Omega f \leq A\, M(f-g) + \abs{f - g}$ for every $g \in C_c(\RR^n)$.

::: pf-proof
$f\ast\phi_t - f = (f-g)\ast\phi_t - (f-g) + (g\ast\phi_t - g)$. The last term tends to $0$ by step [](#p1-2){.pf-ref}, and the first two are bounded by $A\,M(f-g)$ and $\abs{f-g}$ by step [](#p1-1){.pf-ref}.
:::

:::

::: {.pf-step #p1-4}
$\Omega f = 0$ a.e.

::: pf-proof
Fix $\alpha > 0$ and $\eta > 0$, and choose $g \in C_c(\RR^n)$ with $\norm{f-g}_1 < \eta$. By step [](#p1-3){.pf-ref}, the weak type $(1,1)$ bound $m\theset{M h > \beta} \leq \frac{3^n}{\beta}\norm h_1$, and Chebyshev's inequality,
$$
m\theset{\Omega f > 2\alpha} \leq m\theset{A\,M(f-g) > \alpha} + m\theset{\abs{f-g} > \alpha} \leq \frac{3^n A + 1}{\alpha}\,\eta.
$$
Since $\eta$ is arbitrary, $m\theset{\Omega f > 2\alpha} = 0$ for every $\alpha > 0$.
:::

:::

::: pf-qed
Step [](#p1-4){.pf-ref} says $f\ast\phi_t(x) \to f(x)$ for a.e. $x$.
:::

:::

(b) Let $f$ be bounded and uniformly continuous.

::: pf

::: {.pf-step #p2-1}
$f\ast\phi_t(x) - f(x) = \int \phi_t(y)\big(f(x-y) - f(x)\big)\,dy$.

::: pf-proof
This uses $\int \phi_t = 1$.
:::

:::

::: {.pf-step #p2-2}
Given $\eps > 0$, there is $\delta > 0$ with $\int_{\abs y<\delta} \abs{\phi_t(y)}\,\abs{f(x-y)-f(x)}\,dy \leq \eps/2$ for every $x$ and $t$.

::: pf-proof
By uniform continuity choose $\delta$ with $\abs{f(x-y) - f(x)} < \eps/(2\norm\phi_1)$ for $\abs y < \delta$, and use $\int \abs{\phi_t} = \norm\phi_1$.
:::

:::

::: {.pf-step #p2-3}
For this $\delta$, $\int_{\abs y\geq\delta} \abs{\phi_t(y)}\,\abs{f(x-y) - f(x)}\,dy \leq 2\norm f_\infty \int_{\abs z \geq \delta/t} \abs{\phi(z)}\,dz$, which tends to $0$ as $t \to 0$ uniformly in $x$.

::: pf-proof
Bound $\abs{f(x-y) - f(x)}$ by $2\norm f_\infty$ and substitute $y = tz$. The tail integral of $\abs\phi \in L^1$ tends to $0$ by dominated convergence.
:::

:::

::: pf-qed
By steps [](#p2-1){.pf-ref} through [](#p2-3){.pf-ref}, $\abs{f\ast\phi_t(x) - f(x)} < \eps$ for every $x$ once $t$ is small.
:::

:::

:::
