---
schema: qual/card@1
id: E-DUWXR
kind: problem
title: $f,g\in L^1$ implies $f\ast g\in L^1$ and $\|f\ast g\|_1\leq\|f\|_1\|g\|_1$
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - L¹
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- $\star$: Show that $$f,g \in L^1 \implies f\ast g \in L^1 \qtext{and} \norm{f\ast g}_1 \leq \norm{f}_1 \norm{g}_1.$$
:::

::: {.solution}
Let $f,g \in L^1(\RR)$.

<1>1. $f \ast g$ is defined almost everywhere and belongs to $L^1(\RR)$.

<2>1. $\int\!\int |f(x-y)g(y)|\,dy\,dx = \norm{f}_1 \norm{g}_1 < \infty$.

::: {.proof}
The function $(x,y)\mapsto f(x-y)g(y)$ is measurable on $\RR^2$. By Tonelli's theorem, $\int\!\int |f(x-y)g(y)|\,dy\,dx = \int |g(y)| \int |f(x-y)|\,dx\,dy = \int |g(y)| \norm{f}_1\,dy = \norm{f}_1 \norm{g}_1$, since $\int |f(x-y)|\,dx = \norm{f}_1$ for each fixed $y$ by translation invariance of Lebesgue measure.
:::

<2>2. Q.E.D.

::: {.proof}
By step <2>1, $(x,y)\mapsto f(x-y)g(y)$ is in $L^1(\RR^2)$. By Fubini's theorem, $\int f(x-y)g(y)\,dy$ converges absolutely for a.e. $x$, and $x \mapsto \int f(x-y)g(y)\,dy$ is measurable and integrable.
:::

<1>2. $\norm{f\ast g}_1 \leq \norm{f}_1 \norm{g}_1$.

::: {.proof}
$\norm{f\ast g}_1 = \int |f\ast g(x)|\,dx \leq \int\!\int |f(x-y)g(y)|\,dy\,dx = \norm{f}_1 \norm{g}_1$, where the last equality is step <2>1.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>1 gives $f\ast g \in L^1$ and step <1>2 gives the norm bound.
:::
:::
