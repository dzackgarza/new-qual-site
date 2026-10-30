---
schema: qual/card@1
id: P-FPWLY
kind: problem
title: $f(0)=f(2)=0$ and $f(c)=1$ imply $\abs{f'}>1$ somewhere on $(0,2)$
classification:
  areas:
  - real-analysis
  topics:
  - Mean Value Theorem
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked directly against Problem 4 of the preserved UNL May 2016 qualifying-exam source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Suppose that $f \colon [0,2] \to \RR$ is continuous on $[0,2]$ , differentiable on $(0,2)$, and such that $f(0) = f(2) = 0$, $f(c) = 1$ for some $c \in (0,2)$.
Prove that there exists $x \in (0,2)$ such that $\abs{f'(x)} >1.$
:::

::: {.solution}

Throughout, MVT is the mean value theorem.

::: pf

::: {.pf-step #c-small}

If $c < 1$, some $x \in (0, c)$ has $f'(x) > 1$.

::: pf-proof

The MVT on $[0, c]$ gives $x \in (0,c)$ with $f'(x) = \frac{f(c) - f(0)}{c} = \frac{1}{c}$, and $1/c > 1$ because $0 < c < 1$.

:::

:::

::: {.pf-step #c-large}

If $c > 1$, some $y \in (c, 2)$ has $\abs{f'(y)} > 1$.

::: pf-proof

The MVT on $[c, 2]$ gives $y \in (c,2)$ with $f'(y) = \frac{f(2) - f(c)}{2 - c} = \frac{-1}{2-c}$, and $\frac{1}{2-c} > 1$ because $0 < 2 - c < 1$.

:::

:::

::: {.pf-step #c-one}

If $c = 1$, some point of $(0,2)$ has $\abs{f'} > 1$.

::: pf-proof

Suppose not, so $\abs{f'} \le 1$ on $(0,2)$.

::: {.pf-step #left}

$f(x) = x$ for all $x \in (0,1]$.

::: pf-proof

Let $x \in (0,1)$.
The MVT on $[0,x]$ gives $\abs{f(x)} = \abs{f(x) - f(0)} \le x$, and the MVT on $[x,1]$ gives $1 - f(x) = f(1) - f(x) \le 1 - x$, so $f(x) \ge x$.
Hence $f(x) = x$, and $f(1) = 1$ by hypothesis.

:::

:::

::: {.pf-step #right}

$f(x) = 2 - x$ for all $x \in [1,2)$.

::: pf-proof

Let $x \in (1,2)$.
The MVT on $[x,2]$ gives $\abs{f(x)} = \abs{f(2) - f(x)} \le 2 - x$, and the MVT on $[1,x]$ gives $1 - f(x) = f(1) - f(x) \le x - 1$, so $f(x) \ge 2 - x$.
Hence $f(x) = 2 - x$.

:::

:::

::: pf-step

This contradicts the differentiability of $f$ at $1$.

::: pf-proof

By steps [](#left){.pf-ref} and [](#right){.pf-ref}, the left derivative of $f$ at $1$ is $1$ and the right derivative is $-1$.

:::

:::

:::

:::

::: pf-qed

Steps [](#c-small){.pf-ref}, [](#c-large){.pf-ref} and [](#c-one){.pf-ref} cover every $c \in (0,2)$, so in every case some $x \in (0,2)$ has $\abs{f'(x)} > 1$.

:::

:::

:::
