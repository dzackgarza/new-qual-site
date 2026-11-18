---
schema: qual/card@1
id: P-F06PG
kind: problem
title: Product of continuous functions is continuous, by $\varepsilon$-$\delta$
classification:
  areas:
  - prelim
  topics:
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The two continuity thresholds are derived (with M = |f(a)| + 1 > 0 and |g(a)| + 1 > 0, so the divisions are legitimate), the add-and-subtract identity is displayed, and the final estimate separates into eps/2 + eps/2 using |g(a)|/(|g(a)|+1) < 1. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair.
---

::: {.problem}
Let $f, g: \RR \to \RR$ be continuous for all $x$.
Using an $\varepsilon$-$\delta$ argument, show that $f(x)g(x)$ is continuous for all $x$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #locallybounded}
For $a\in\RR$ there are $\delta_0>0$ and $M>0$ with $\abs{f(x)}\le M$ whenever $\abs{x-a}<\delta_0$.

::: pf-proof
$f$ is continuous at $a$, so with $\varepsilon=1$ there is $\delta_0>0$ such that $\abs{x-a}<\delta_0$ implies $\abs{f(x)-f(a)}<1$, hence $\abs{f(x)}<\abs{f(a)}+1$. Put $M=\abs{f(a)}+1>0$.
:::

:::

::: {.pf-step #deltas}
For $\varepsilon>0$ there are $\delta_1,\delta_2>0$ such that $\abs{x-a}<\delta_1$ implies $\abs{g(x)-g(a)}<\varepsilon/(2M)$ and $\abs{x-a}<\delta_2$ implies $\abs{f(x)-f(a)}<\varepsilon/(2(\abs{g(a)}+1))$.

::: pf-proof
$\varepsilon/(2M)>0$ because $M>0$, and $\varepsilon/(2(\abs{g(a)}+1))>0$ because $\abs{g(a)}+1>0$; the two continuity hypotheses give the corresponding $\delta$'s.
:::

:::

::: {.pf-step #product}
With $\delta=\min\{\delta_0,\delta_1,\delta_2\}>0$, $\abs{x-a}<\delta$ implies $\abs{f(x)g(x)-f(a)g(a)}<\varepsilon$.

::: pf-proof
Add and subtract $f(x)g(a)$:
$$
f(x)g(x)-f(a)g(a)=f(x)\bigl(g(x)-g(a)\bigr)+g(a)\bigl(f(x)-f(a)\bigr),
$$
so by the triangle inequality and the three bounds,
$$
\abs{f(x)g(x)-f(a)g(a)}<M\cdot\frac{\varepsilon}{2M}+\abs{g(a)}\cdot\frac{\varepsilon}{2(\abs{g(a)}+1)}<\frac\varepsilon2+\frac\varepsilon2=\varepsilon,
$$
using $\abs{g(a)}/(\abs{g(a)}+1)<1$.
:::

:::

::: {.pf-step}
$fg$ is continuous at every $a\in\RR$.

::: pf-proof
Given $a$ and $\varepsilon>0$, steps [](#locallybounded){.pf-ref}, [](#deltas){.pf-ref} and [](#product){.pf-ref} produce $\delta>0$ with the defining property; $a$ was arbitrary.
:::

:::

:::
:::
