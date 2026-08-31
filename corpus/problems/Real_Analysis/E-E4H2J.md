---
schema: qual/card@1
id: E-E4H2J
kind: exercise
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

::: exercise
- Show that if $f\in L^1$ and $g$ is bounded, then  $f\ast g$ is bounded and uniformly continuous.
:::

::: {.solution}
**Goal:** If $f \in L^1(\RR)$ and $g$ is bounded (say $|g| \leq M$ a.e.), then $f\ast g$ is bounded and uniformly continuous on $\RR$.

<1>1. $f\ast g$ is bounded, with $|f\ast g(x)| \leq M\norm{f}_1$ for every $x$.
::: {.proof}
$|f\ast g(x)| = |\int f(x-y)g(y)\,dy| \leq \int |f(x-y)|\,|g(y)|\,dy \leq M \int |f(x-y)|\,dy = M\norm{f}_1$.
:::
<1>2. For every $x, h \in \RR$: $|f\ast g(x+h) - f\ast g(x)| \leq M\, \norm{\tau_h f - f}_1$, where $\tau_h f(y) := f(y-h)$.
::: {.proof}
$f\ast g(x+h) = \int f(x+h-y)g(y)\,dy = \int f(x - (y-h))g(y)\,dy$, so $f\ast g(x+h) - f\ast g(x) = \int \big(f(x+h-y) - f(x-y)\big)g(y)\,dy$, and $|f\ast g(x+h) - f\ast g(x)| \leq M \int |f(x+h-y) - f(x-y)|\,dy = M\norm{\tau_h f - f}_1$, the equality by the change of variables $y \mapsto y+h$.
:::
<1>3. $\lim_{h \to 0} \norm{\tau_h f - f}_1 = 0$.
::: {.proof}
translation is continuous in $L^1$: the claim holds for compactly supported continuous $\varphi$ by uniform continuity, and extends to all of $L^1$ by density (an $\eps/3$ argument).
:::
<1>4. $f\ast g$ is uniformly continuous.
::: {.proof}
given $\eps > 0$, by <1>3 choose $\delta > 0$ with $\norm{\tau_h f - f}_1 < \eps/M$ for $|h| < \delta$; then <1>2 gives $|f\ast g(x+h) - f\ast g(x)| < \eps$ for all $x$, uniformly in $x$.
:::
<1>5. Q.E.D.
::: {.proof}
<1>1 gives boundedness and <1>4 gives uniform continuity.
:::
:::
