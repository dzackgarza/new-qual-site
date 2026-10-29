---
schema: qual/card@1
id: P-8DY3N
kind: problem
title: '$f''\to0$ at infinity when $f\to0$ and $f''''$ is bounded'
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Taylor Series
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-30
  note: 'Split from P-4FH62, where it was part (b).'
---

::: {.problem}
Let $f : \RR \to \RR$ be an infinitely differentiable function.

1. Use Taylor's formula with remainder to show that, given $x$ and $h$, $f'(x) = (f(x+2h) - f(x))/2h - hf''(\xi)$ for some $\xi$.

2. Assume $f(x) \to 0$ as $x \to \infty$, and that $f''$ is bounded. Show that $f'(x) \to 0$ as $x \to \infty$.
:::

::: {.solution}

::: pf

::: pf-step

For $h \neq 0$, $f'(x) = \frac{f(x+2h)-f(x)}{2h} - hf''(\xi)$ for some $\xi$ between $x$ and $x+2h$; if $f(x) \to 0$ as $x \to \infty$ and $\abs{f''} \leq M$, then $f'(x) \to 0$.

::: pf-proof

Taylor's theorem with Lagrange remainder from $x$ to $x+2h$ gives
$$
f(x+2h)=f(x)+2hf'(x)+2h^2f''(\xi)
$$
for some $\xi$ between $x$ and $x+2h$; solving for $f'(x)$ gives part 1. For part 2, fix $\varepsilon>0$ and choose $h>0$ so that $Mh<\varepsilon/2$. For $x$ large, both $\abs{f(x)}$ and $\abs{f(x+2h)}$ are $<h\varepsilon/2$, so the first term has absolute value $<\varepsilon/2$. Thus $\abs{f'(x)}<\varepsilon$ for all large $x$, and $f'(x)\to0$.

:::

:::

:::

:::
