---
schema: qual/card@1
id: P-6BKXI
kind: problem
title: Convolution with an approximate identity converges in $L^1$, almost everywhere,
  and uniformly
classification:
  areas:
  - real-analysis
  topics:
  - Approximations to the Identity
  - Convolution
  - L¹
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source did not define the approximate identity, put no hypothesis on f in the first part, and read "this converges is almost everywhere" and "Show that is f". The statement now defines phi_t from phi in L^1 with integral 1, assumes f in L^1(R^n) in (a), and corrects the two typos.'
---

::: {.problem}
Let $\phi \in L^1(\RR^n)$ with $\int \phi = 1$, and let $\phi_t(x) = t^{-n}\phi(x/t)$ be the corresponding approximate identity.

(a) Show that if $f \in L^1(\RR^n)$, then $$\norm{f\ast \phi_t - f}_1 \converges{t\to 0}\to 0.$$

(b) Show that if additionally $\abs{\phi(x)} \leq c(1 + \abs{x})^{-n-\eps}$ for some $c,\eps>0$, then this convergence is also almost everywhere.

(c) Show that if $f$ is bounded and uniformly continuous, then $f\ast \phi_t$ uniformly converges to $f$.
:::

::: {.solution}
For all three parts,
$$
f\ast\phi_t(x) - f(x) = \int\phi(y)\big(f(x - ty) - f(x)\big)\,dy
$$
by the substitution $u = ty$ in $\int f(x-u)\phi_t(u)\,du$ and $\int\phi = 1$.

::: pf

::: pf-step

For $f \in L^1$, $\norm{f \ast \phi_t - f}_1 \to 0$ as $t \to 0$.

::: pf-proof

By Tonelli's theorem, $\norm{f\ast\phi_t - f}_1 \le \int\abs{\phi(y)}\,\omega(ty)\,dy$ with $\omega(h) = \int\abs{f(x-h) - f(x)}\,dx$. Continuity of translation in $L^1$ gives $\omega(ty) \to 0$ for each $y$, and $\abs{\phi(y)}\,\omega(ty) \le 2\norm{f}_1\abs{\phi(y)}$, so dominated convergence applies. See [[E-QCYEM]].

:::

:::

::: pf-step

If also $\abs{\phi(x)} \le c(1 + \norm{x})^{-n-\eps}$, then $f \ast \phi_t \to f$ a.e. for $f \in L^1$.

::: pf-proof

::: {.pf-step #s2-1}

There is $A$ with $\sup_{t>0}\abs{f \ast \phi_t(x)} \le A\,Mf(x)$ for every $x$, where $Mf$ is the Hardy--Littlewood maximal function.

::: pf-proof

$\Psi(x) = c(1+\norm{x})^{-n-\eps}$ is a radial, radially decreasing, integrable majorant of $\abs{\phi}$. For such $\Psi$, $\sup_t (\abs{f} \ast \Psi_t)(x) \le \norm{\Psi}_1\,Mf(x)$, by writing $\Psi$ as an increasing limit of positive combinations of normalized indicators of balls centered at $0$. Take $A = \norm{\Psi}_1$.

:::

:::

::: pf-qed

Let $\Omega f(x) = \limsup_{t\to0}\abs{f\ast\phi_t(x) - f(x)}$. For $g \in C_c(\RR^n)$, $g\ast\phi_t \to g$ uniformly by step [](#s3){.pf-ref}, so $\Omega f \le \Omega(f - g) \le A\,M(f-g) + \abs{f - g}$ by step [](#s2-1){.pf-ref}. For $\alpha > 0$, the weak type $(1,1)$ bound $m\theset{Mh > \beta} \le 3^n\norm{h}_1/\beta$ and Chebyshev's inequality give $m\theset{\Omega f > 2\alpha} \le (3^nA + 1)\norm{f - g}_1/\alpha$. Since $C_c$ is dense in $L^1$, $m\theset{\Omega f > 2\alpha} = 0$ for every $\alpha > 0$. See [[E-KUOXT]].

:::

:::

:::

::: {.pf-step #s3}

If $f$ is bounded and uniformly continuous, then $f \ast \phi_t \to f$ uniformly.

::: pf-proof

Given $\eps > 0$, choose $M$ with $2\norm{f}_\infty\int_{\norm{y}>M}\abs{\phi} < \eps/2$, and by uniform continuity choose $t_0$ with $\abs{f(x - u) - f(x)} < \eps/(2\norm{\phi}_1)$ for all $x$ and $\norm{u} \le t_0M$. For $t < t_0$, splitting $\int\abs{\phi(y)}\,\abs{f(x-ty) - f(x)}\,dy$ at $\norm{y} = M$ bounds it by $\eps/2 + \eps/2$ for every $x$.

:::

:::

:::

:::
