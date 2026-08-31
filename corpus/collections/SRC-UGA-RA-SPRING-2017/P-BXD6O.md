---
schema: qual/card@1
id: P-BXD6O
kind: problem
title: Convolution of two $L^2$ functions is uniformly continuous
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Uniform Continuity
  - L²
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Let $f, g \in L^2(\RR)$.
Prove that the formula
\[
h(x) \definedas \int _{-\infty}^{\infty} f(t) g(x-t) \, dt
\]
defines a uniformly continuous function $h$ on $\RR$.
:::
::: {.solution}
<1>1. $h$ is well-defined (a.e.) and bounded.
<2>1. For every $x$, $\int |f(t)|\,|g(x-t)|\,dt \le \|f\|_2\|g\|_2$.
::: {.proof}
Cauchy–Schwarz applied to $f(t)$ and $g(x-t)$; the second factor is $\|g\|_2$ by translation-invariance of the $L^2$ norm.
:::
<2>2. Hence $h(x)$ exists for every $x$ and $|h(x)| \le \|f\|_2\|g\|_2 < \infty$.
::: {.proof}
by <2>1 the defining integral converges absolutely.
:::

<1>2. Establish a continuity estimate.
<2>1. For any $x, y$: $|h(x) - h(y)| = \left|\int f(t)\,(g(x-t) - g(y-t))\,dt\right| \le \|f\|_2\left(\int |g(x-t) - g(y-t)|^2\,dt\right)^{1/2}$.
::: {.proof}
triangle inequality inside the integral, then Cauchy–Schwarz.
:::
<2>2. $\int |g(x-t) - g(y-t)|^2\,dt = \int |g(u) - g(u - (y-x))|^2\,du = \|g - \tau_{y-x} g\|_2^2$, where $\tau_a g(u) \definedas g(u - a)$.
::: {.proof}
substitute $u = x - t$; then $y - t = u - (y-x)$; Jacobian is $1$.
:::
<2>3. Hence $|h(x) - h(y)| \le \|f\|_2\,\|g - \tau_{y-x} g\|_2$.
::: {.proof}
combine <2>1 and <2>2.
:::

<1>3. Translation is strongly continuous on $L^2(\RR)$: $\|g - \tau_a g\|_2 \to 0$ as $a \to 0$.
<2>1. The claim holds for $g \in C_c^0(\RR)$.
::: {.proof}
$g$ uniformly continuous and compactly supported, so $|g(u) - g(u-a)| \to 0$ uniformly and lives in a fixed compact set for $|a| \le 1$; dominated convergence.
:::
<2>2. $C_c^0(\RR)$ is dense in $L^2(\RR)$.
::: {.proof}
standard density theorem.
:::
<2>3. Given $\eps > 0$, choose $q \in C_c^0$ with $\|g - q\|_2 < \eps/3$; then $\|g - \tau_a g\|_2 \le \|g - q\|_2 + \|q - \tau_a q\|_2 + \|\tau_a q - \tau_a g\|_2 \le 2\eps/3 + \|q - \tau_a q\|_2$.
::: {.proof}
triangle inequality; the last term is $\|q - g\|_2$ by translation-invariance of the norm.
:::
<2>4. For $|a|$ small, $\|q - \tau_a q\|_2 < \eps/3$, so $\|g - \tau_a g\|_2 < \eps$.
::: {.proof}
<2>1 applied to $q$, then <2>3.
:::

<1>4. Q.E.D.
::: {.proof}
<1>2<2>3 and <1>3 show $|h(x) - h(y)| \le \|f\|_2\|g - \tau_{y-x} g\|_2 \to 0$ as $y \to x$, uniformly in $x, y$ (the bound depends only on $y - x$); hence $h$ is uniformly continuous.
:::
:::
