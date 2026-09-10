---
schema: qual/card@1
id: E-ZPC0X
kind: problem
title: Interchanging limits under uniform convergence
classification:
  areas:
  - topology
  topics:
  - Uniform Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $X$ be a topological space and let $Y$ be a metric space.
Let $f_n: X \to Y$ be a sequence of continuous functions.
Let $x_n$ be a sequence of points of $X$ converging to $x$.
Show that if the sequence $(f_n)$ converges uniformly to $f$, then $(f_n(x_n))$ converges to $f(x)$.
:::

::: {.solution}
Uniform convergence of continuous maps into a metric space implies that the limit map $f$ is continuous. Let $d$ be the metric on $Y$. Then
\[
d(f_n(x_n),f(x))
\le d(f_n(x_n),f(x_n))+d(f(x_n),f(x)).
\]
The first term tends to $0$ because
\[
\sup_{z\in X}d(f_n(z),f(z))\to0.
\]
The second tends to $0$ because $x_n\to x$ and $f$ is continuous. Hence
\[
f_n(x_n)\longrightarrow f(x).
\]
:::
