---
schema: qual/card@1
id: E-Y4GZM
kind: problem
title: Convolution of continuous compactly supported functions is continuous and compactly
  supported
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- Show that if $f, g$ are continuous and compactly supported, then so is $f\ast g$.
:::

::: {.solution}
<1>1. $f \ast g$ is uniformly continuous.

<2>1. $|f \ast g(x + h) - f \ast g(x)| \le \|g\|_1 \sup_{z}|f(z + h) - f(z)|$ for all $x, h$.

::: {.proof}
$|f\ast g(x+h) - f\ast g(x)| = \left|\int (f(x + h - y) - f(x - y))g(y)\,dy\right| \le \int |f(x+h-y) - f(x-y)|\,|g(y)|\,dy$, and the first factor of the integrand is at most $\sup_z|f(z+h) - f(z)|$.
:::

<2>2. $\sup_z|f(z + h) - f(z)| \to 0$ as $h \to 0$.

::: {.proof}
A continuous function with compact support is uniformly continuous.
:::

<2>3. Q.E.D.

::: {.proof}
Steps <2>1 and <2>2 give $\sup_x|f\ast g(x + h) - f\ast g(x)| \to 0$ as $h \to 0$.
:::

<1>2. $f \ast g$ is compactly supported.

<2>1. $\supp f + \supp g$ is compact.

::: {.proof}
It is the image of the compact set $\supp f \times \supp g$ under the continuous map $(a,b) \mapsto a + b$.
:::

<2>2. Q.E.D.

::: {.proof}
If $x \notin \supp f + \supp g$, then $(x - \supp g) \cap \supp f = \emptyset$, so $f(x - y)g(y) = 0$ for every $y$ and $f\ast g(x) = 0$. So $\theset{f\ast g \neq 0}$ lies in the closed set $\supp f + \supp g$, and so does its closure $\supp(f\ast g)$, which is compact by step <2>1.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2.
:::
:::
