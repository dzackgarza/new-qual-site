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
Prove Theorem 4.1.
:::

::: {.solution}
Let $a<b$, let $f:[a,b]\to\mathbb R$, and let $c\in(a,b)$ be a local extremum at which $f$ is differentiable, as in [[T-RA-WORKSHOP-D5-4-1|Theorem 4.1]].

<1>1. If $f$ has a local maximum at $c$, then $f'(c)\geq0$.

::: {.proof}
There is $\delta>0$ such that $[c-\delta,c+\delta]\subset(a,b)$ and $f(c+h)\leq f(c)$ whenever $|h|<\delta$. For $-\delta<h<0$,
\[
\frac{f(c+h)-f(c)}{h}\geq0.
\]
Since $f'(c)$ exists, taking the left-hand limit yields $f'(c)\geq0$.
:::

<1>2. If $f$ has a local maximum at $c$, then $f'(c)\leq0$.

::: {.proof}
With $\delta$ as in step <1>1, for $0<h<\delta$ one has
\[
\frac{f(c+h)-f(c)}{h}\leq0.
\]
Taking the right-hand limit yields $f'(c)\leq0$.
:::

<1>3. At a local maximum, $f'(c)=0$.

::: {.proof}
Steps <1>1 and <1>2 give $0\leq f'(c)\leq0$.
:::

<1>4. At a local minimum, $f'(c)=0$.

::: {.proof}
The function $-f$ is differentiable at $c$ with derivative $-f'(c)$ and has a local maximum there. Applying step <1>3 to $-f$ gives $-f'(c)=0$.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>3 and <1>4 establish the assertion for both kinds of local extrema.
:::
:::
