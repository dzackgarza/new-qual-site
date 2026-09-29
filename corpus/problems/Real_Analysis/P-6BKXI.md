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
---

::: {.problem}
- Show that if $\phi$ is an approximate identity, then $$\norm{f\ast \phi_t - f}_1 \converges{t\to 0}\to 0.$$

  - Show that if additionally $\abs{\phi(x)} \leq c(1 + \abs{x})^{-n-\eps}$ for some $c,\eps>0$, then this converges is almost everywhere.

- Show that is $f$ is bounded and uniformly continuous and $\phi_t$ is an approximation to the identity, then $f\ast \phi_t$ uniformly converges to $f$.
:::

::: {.solution}
Let $\phi \in L^1(\RR^n)$ with $\int\phi = 1$ and $\phi_t(x) = t^{-n}\phi(x/t)$. Then
$$
f\ast\phi_t(x) - f(x) = \int\phi(y)\big(f(x - ty) - f(x)\big)\,dy
$$
by the substitution $u = ty$ in $\int f(x-u)\phi_t(u)\,du$ and $\int\phi = 1$.

::: pf

::: pf-step

For $f \in L^1$, $\|f \ast \phi_t - f\|_1 \to 0$ as $t \to 0$.

::: pf-proof

By Tonelli's theorem, $\|f\ast\phi_t - f\|_1 \le \int|\phi(y)|\,\omega(ty)\,dy$ with $\omega(h) = \int|f(x-h) - f(x)|\,dx$. Continuity of translation in $L^1$ gives $\omega(ty) \to 0$ for each $y$, and $|\phi(y)|\,\omega(ty) \le 2\|f\|_1|\phi(y)|$, so dominated convergence applies. See [[E-QCYEM]].

:::

:::

::: pf-step

If also $|\phi(x)| \le c(1 + |x|)^{-n-\eps}$, then $f \ast \phi_t \to f$ a.e. for $f \in L^1$.

::: pf-proof

::: {.pf-step #s2-1}

There is $A$ with $\sup_{t>0}|f \ast \phi_t(x)| \le A\,Mf(x)$ for every $x$, where $Mf$ is the Hardy--Littlewood maximal function.

::: pf-proof

$\Psi(x) = c(1+|x|)^{-n-\eps}$ is a radial, radially decreasing, integrable majorant of $|\phi|$. For such $\Psi$, $\sup_t (|f| \ast \Psi_t)(x) \le \|\Psi\|_1\,Mf(x)$, by writing $\Psi$ as an increasing limit of positive combinations of normalized indicators of balls centered at $0$. Take $A = \|\Psi\|_1$.

:::

:::

::: pf-qed

Let $\Omega f(x) = \limsup_{t\to0}|f\ast\phi_t(x) - f(x)|$. For $g \in C_c(\RR^n)$, $g\ast\phi_t \to g$ uniformly by step [](#s3){.pf-ref}, so $\Omega f \le \Omega(f - g) \le A\,M(f-g) + |f - g|$ by step [](#s2-1){.pf-ref}. For $\alpha > 0$, the weak type $(1,1)$ bound $m\theset{Mh > \beta} \le 3^n\|h\|_1/\beta$ and Chebyshev's inequality give $m\theset{\Omega f > 2\alpha} \le (3^nA + 1)\|f - g\|_1/\alpha$. Since $C_c$ is dense in $L^1$, $m\theset{\Omega f > 2\alpha} = 0$ for every $\alpha > 0$. See [[E-KUOXT]].

:::

:::

:::

::: {.pf-step #s3}

If $f$ is bounded and uniformly continuous, then $f \ast \phi_t \to f$ uniformly.

::: pf-proof

Given $\eps > 0$, choose $M$ with $2\|f\|_\infty\int_{|y|>M}|\phi| < \eps/2$, and by uniform continuity choose $t_0$ with $|f(x - u) - f(x)| < \eps/(2\|\phi\|_1)$ for all $x$ and $|u| \le t_0M$. For $t < t_0$, splitting $\int|\phi(y)|\,|f(x-ty) - f(x)|\,dy$ at $|y| = M$ bounds it by $\eps/2 + \eps/2$ for every $x$.

:::

:::

:::

:::
