---
schema: qual/card@1
id: P-YIC3K
kind: problem
title: $\int_0^1 x^4 f(x)\,dx=\frac15 f(\xi)$ for continuous $f$ on $[0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - Mean Value Theorem
  - Integrals
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against the Lamport standard and checked. This is the first mean value theorem for
    integrals: x^4 >= 0 on [0,1] and f is continuous, so m = min f and M = max f satisfy
    m/5 <= int_0^1 x^4 f(x) dx <= M/5, and continuity of f on the connected interval gives xi with
    5 int x^4 f = f(xi). The card states the weighted form with the weight x^4 and applies the
    theorem, which is the correct route; the hypothesis that f is real-valued and continuous is used
    exactly in the intermediate value step. Not claimed: any statement about uniqueness of xi.
---

::: {.problem}
Let $f$ be a continuous real-valued function on $[0,1]$.
Prove that there exists at least one point $\xi\in[0,1]$ such that $\int_0^1 x^4 f(x)\,dx=\frac{1}{5}f(\xi)$.
:::

::: {.solution}

::: pf

::: pf-step

$f$ attains a minimum $m$ and a maximum $M$ on $[0,1]$.

::: pf-proof

$f$ is continuous on the compact set $[0,1]$, so this is the [[T-RA-WORKSHOP-D4-3-2|extreme value theorem]].

:::

:::

::: {.pf-step #s2}

$m/5 \le \int_0^1 x^4 f(x)\,dx \le M/5$.

::: pf-proof

$m \le f(x) \le M$ for all $x$, and $x^4 \ge 0$, so $m x^4 \le x^4 f(x) \le M x^4$; integrating and using $\int_0^1 x^4\,dx = 1/5$ gives the claim.

:::

:::

::: {.pf-step #s3}

$5\int_0^1 x^4 f \in [m, M] = f([0,1])$.

::: pf-proof

By step [](#s2){.pf-ref}, $5\int_0^1 x^4 f \in [m, M]$.
By the [[T-RA-WORKSHOP-D4-3-4|intermediate value theorem]], the continuous function $f$ takes every value between $m$ and $M$, so $f([0,1]) = [m, M]$.

:::

:::

::: pf-step

There is $\xi \in [0,1]$ with $\int_0^1 x^4 f(x)\,dx = \frac15 f(\xi)$.

::: pf-proof

By step [](#s3){.pf-ref}, $5\int_0^1 x^4f = f(\xi)$ for some $\xi \in [0,1]$.

:::

:::

:::

:::
