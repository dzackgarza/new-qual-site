---
schema: qual/card@1
id: E-E4H2J
kind: problem
title: Convolution of an $L^1$ function with a bounded function is bounded and uniformly
  continuous
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Uniform Continuity
  - L¹
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- Show that if $f\in L^1$ and $g$ is bounded, then  $f\ast g$ is bounded and uniformly continuous.
:::

::: {.solution}
Let $f \in L^1(\RR)$ and let $g$ be measurable with $|g| \leq M$ a.e., where $M > 0$.

<1>1. $f\ast g$ is bounded, with $|f\ast g(x)| \leq M\norm{f}_1$ for every $x$.

::: {.proof}
$|f\ast g(x)| = |\int f(x-y)g(y)\,dy| \leq \int |f(x-y)|\,|g(y)|\,dy \leq M \int |f(x-y)|\,dy = M\norm{f}_1$.
:::

<1>2. For $h \in \RR$ let $\tau_h f(y) \coloneqq f(y-h)$. For every $x, h \in \RR$, $|f\ast g(x+h) - f\ast g(x)| \leq M\, \norm{\tau_h f - f}_1$.

::: {.proof}
$f\ast g(x+h) = \int f(x+h-y)g(y)\,dy = \int f(x - (y-h))g(y)\,dy$, so $f\ast g(x+h) - f\ast g(x) = \int \big(f(x+h-y) - f(x-y)\big)g(y)\,dy$, and $|f\ast g(x+h) - f\ast g(x)| \leq M \int |f(x+h-y) - f(x-y)|\,dy = M\norm{\tau_h f - f}_1$, the equality by the change of variables $u = x - y + h$.
:::

<1>3. $\lim_{h \to 0} \norm{\tau_h f - f}_1 = 0$.

::: {.proof}
For a compactly supported continuous $\varphi$ the claim holds by uniform continuity of $\varphi$ and dominated convergence on a fixed compact set. Given $\eps > 0$, choose such $\varphi$ with $\norm{f - \varphi}_1 < \eps/3$, which exists by density of $C_c(\RR)$ in $L^1(\RR)$. Then $\norm{\tau_h f - f}_1 \leq \norm{\tau_h(f - \varphi)}_1 + \norm{\tau_h\varphi - \varphi}_1 + \norm{\varphi - f}_1 < \eps$ for $|h|$ small, since $\norm{\tau_h(f-\varphi)}_1 = \norm{f-\varphi}_1$.
:::

<1>4. $f\ast g$ is uniformly continuous.

::: {.proof}
Given $\eps > 0$, step <1>3 gives $\delta > 0$ with $\norm{\tau_h f - f}_1 < \eps/M$ for $|h| < \delta$. Then step <1>2 gives $|f\ast g(x+h) - f\ast g(x)| < \eps$ for all $x \in \RR$ and $|h| < \delta$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 gives boundedness and step <1>4 gives uniform continuity.
:::
:::
