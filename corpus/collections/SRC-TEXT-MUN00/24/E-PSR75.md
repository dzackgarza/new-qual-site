---
schema: qual/card@1
id: E-PSR75
kind: problem
title: Fixed points of continuous self-maps of the interval
classification:
  areas:
  - topology
  topics:
  - Connectedness
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

Let $f: X \to X$ be continuous.
Show that if $X = [0, 1]$, there is a point $x$ such that $f(x) = x$.
The point $x$ is called a fixed point of $f$.
What happens if $X$ equals $[0, 1)$ or $(0, 1)$?
:::

::: {.solution}
For $X=[0,1]$, define
\[
g(x)=f(x)-x.
\]
This is continuous. Since $f(0)\in[0,1]$ and $f(1)\in[0,1]$,
\[
g(0)=f(0)\ge0,\qquad g(1)=f(1)-1\le0.
\]
By the intermediate value theorem, $g(c)=0$ for some $c\in[0,1]$, hence $f(c)=c$.

The conclusion fails for $[0,1)$ and $(0,1)$. In either case the map
\[
f(x)=\frac{x+1}{2}
\]
maps the space into itself and satisfies $f(x)>x$ for every $x<1$, so it has no fixed point.
:::
