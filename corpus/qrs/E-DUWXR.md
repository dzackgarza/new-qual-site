---
schema: qual/card@1
id: E-DUWXR
kind: exercise
title: $f,g\in L^1$ implies $f\ast g\in L^1$ and $\|f\ast g\|_1\leq\|f\|_1\|g\|_1$
classification:
  areas:
  - real-analysis
  topics:
  - convolution
  - l1
  - norms
relations: []
review: draft
solved: true
---

::: exercise
- $\star$: Show that $$f,g \in L^1 \implies f\ast g \in L^1 \qtext{and} \norm{f\ast g}_1 \leq \norm{f}_1 \norm{g}_1.$$
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** For $f,g \in L^1(\RR)$, show $f\ast g \in L^1(\RR)$ and $\norm{f\ast g}_1 \leq \norm{f}_1 \norm{g}_1$.

<1>1. $f \ast g$ is well defined and belongs to $L^1(\RR)$.
<2>1. $\int\!\int |f(x-y)g(y)|\,dy\,dx = \norm{f}_1 \norm{g}_1 < \infty$.
Proof: by Tonelli, $\int\!\int |f(x-y)g(y)|\,dy\,dx = \int |g(y)| \int |f(x-y)|\,dx\,dy = \int |g(y)| \norm{f}_1\,dy = \norm{f}_1 \norm{g}_1$, since $\int |f(x-y)|\,dx = \norm{f}_1$ for each fixed $y$ (translation invariance of Lebesgue measure).
<2>2. Q.E.D. Proof: by <2>1 the integrand is in $L^1(\RR^2)$, so the iterated integral $\int\!\int f(x-y)g(y)\,dy\,dx$ is finite for a.e. $x$, and the function $x \mapsto \int f(x-y)g(y)\,dy$ is measurable (Fubini) and integrable.
<1>2. $\norm{f\ast g}_1 \leq \norm{f}_1 \norm{g}_1$.
Proof: $\norm{f\ast g}_1 = \int |f\ast g(x)|\,dx \leq \int\!\int |f(x-y)g(y)|\,dy\,dx = \norm{f}_1 \norm{g}_1$, where the inequality is Tonelli/Fubini applied to the nonnegative integrand and <1>1 supplies finiteness.
<1>3. Q.E.D. Proof: <1>1 gives $f\ast g \in L^1$ and <1>2 gives the norm bound.
:::
