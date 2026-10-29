---
schema: qual/card@1
id: P-RA-WORKSHOP-D5-13
kind: problem
title: Fermat's stationary-point theorem
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
relations:
- kind: uses
  target: T-RA-WORKSHOP-D5-4-1
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Let $a<b$, let $f\colon[a,b]\to\RR$, and let $c\in(a,b)$.
Prove that if $f$ has a local maximum or a local minimum at $c$ and $f$ is differentiable at $c$, then $f'(c)=0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $f$ has a local maximum at $c$, then $f'(c)\geq0$.

::: pf-proof

There is $\delta>0$ such that $[c-\delta,c+\delta]\subset(a,b)$ and $f(c+h)\leq f(c)$ whenever $\abs{h}<\delta$. For $-\delta<h<0$,
$$
\frac{f(c+h)-f(c)}{h}\geq0.
$$
Since $f'(c)$ exists, taking the left-hand limit yields $f'(c)\geq0$.

:::

:::

::: {.pf-step #s2}

If $f$ has a local maximum at $c$, then $f'(c)\leq0$.

::: pf-proof

With $\delta$ as in step [](#s1){.pf-ref}, for $0<h<\delta$ one has
$$
\frac{f(c+h)-f(c)}{h}\leq0.
$$
Taking the right-hand limit yields $f'(c)\leq0$.

:::

:::

::: pf-step

$f'(c)=0$.

::: pf-proof

At a local maximum, steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give $0\leq f'(c)\leq0$. At a local minimum, the function $-f$ is differentiable at $c$ with derivative $-f'(c)$ and has a local maximum there, so the same steps applied to $-f$ give $-f'(c)=0$.

:::

:::

:::

:::
