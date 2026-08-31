---
schema: qual/card@1
id: P-P5TFA
kind: problem
title: $\lim_{x\to\infty}f(x)\le 1+\frac\pi 4$ when $f(1)=1$ and $f'=1/(x^2+f^2)$
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Limits
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Let $f: [1, \infty) \to \RR$ such that $f(1) = 1$ and
\[
f^{\prime}(x)= \frac{1} {x^{2}+f(x)^{2}}
\]

Show that the following limit exists and satisfies the equality
\[
\lim _{x \rightarrow \infty} f(x) \leq 1 + \frac \pi 4
\]
:::

::: {.solution}
<1>1. $f$ is strictly increasing on $[1,\infty)$.
::: {.proof}
$f'(x) = 1/(x^2 + f(x)^2) > 0$ for every $x \ge 1$.
:::
<1>2. Hence $f(x) \ge f(1) = 1$ for all $x \ge 1$.
::: {.proof}
<1>1 and $f(1) = 1$.
:::
<1>3. $f'(x) \le 1/(x^2+1)$ for all $x \ge 1$.
::: {.proof}
$f(x)^2 \ge 1$ by <1>2, so $x^2 + f(x)^2 \ge x^2 + 1$; inverting gives $f'(x) = 1/(x^2+f(x)^2) \le 1/(x^2+1)$.
:::
<1>4. $f(x) \le 1 + \pi/4$ for all $x \ge 1$.
::: {.proof}
integrate <1>3 from $1$ to $x$: \[ f(x) - f(1) = \int_1^x f'(t)\,dt \le \int_1^x \frac{dt}{1+t^2} = \arctan x - \frac{\pi}{4} < \frac{\pi}{2} - \frac{\pi}{4} = \frac{\pi}{4}. \] Adding $f(1) = 1$ gives the claim.
:::
<1>5. $\lim_{x\to\infty} f(x)$ exists and is $\le 1 + \pi/4$.
::: {.proof}
$f$ is increasing (<1>1) and bounded above by $1+\pi/4$ (<1>4), so the monotone convergence theorem for functions of a real variable applies: the limit exists and is at most the bound.
:::
<1>6. Q.E.D.
:::
