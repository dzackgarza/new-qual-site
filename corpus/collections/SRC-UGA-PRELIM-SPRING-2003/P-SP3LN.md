---
schema: qual/card@1
id: P-SP3LN
kind: problem
title: $x > \ln x$ for all $x > 0$
classification:
  areas:
  - prelim
  topics:
  - Inequalities
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card's first step had no proof and its claim was a definition
    ('Define f:(0,inf) -> R by f(x) = x - ln x'), and its last step asserted the conclusion with
    no justification beyond an inequality sign. It is now three proved steps: the derivative and
    the sign analysis giving monotonicity on each side of 1 (with the standard monotonicity
    criterion named); the global minimum value f(1) = 1 with both cases x < 1 and x > 1 handled;
    and the conclusion x - ln x >= 1 > 0. The claim is unchanged. Not claimed: a retained
    solution set; the collection's provenance is the examination paper only.
---

::: {.problem}
Prove that $x > \ln x$ for all $x > 0$.
:::

::: {.solution}
Throughout $\ln$ is the natural logarithm, $f\colon(0,\infty) \to \RR$ is $f(x) \coloneqq x - \ln x$, and the claim to be proved is $x > \ln x$ for every $x > 0$, that is $f(x) > 0$. The collection's `provenance` is the Spring 2003 examination paper, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #derivative}
$f'(x) = \frac{x-1}{x}$, so $f$ is decreasing on $(0,1]$ and increasing on $[1,\infty)$.

::: pf-proof
The derivative of $x$ is $1$ and that of $\ln x$ is $1/x$ on $(0,\infty)$, so $f'(x) = 1 - 1/x = (x-1)/x$. The denominator $x$ is positive on the domain, so the sign of $f'$ is the sign of $x - 1$: negative on $(0,1)$, zero at $x = 1$, positive on $(1,\infty)$. A differentiable function with non-positive derivative on an interval is non-increasing there, so $f$ decreases on $(0,1]$ and increases on $[1,\infty)$.

:::

:::

::: {.pf-step #minimum}
$f(x) \ge f(1) = 1$ for every $x > 0$, with equality only at $x = 1$.

::: pf-proof
Let $0 < x < 1$: since $f$ decreases on $(0,1]$, $f(x) \ge f(1)$. Let $x > 1$: since $f$ increases on $[1,\infty)$, $f(x) \ge f(1)$. And $f(1) = 1 - \ln 1 = 1 - 0 = 1$. So $1$ is a global minimum value of $f$.

:::

:::

::: pf-step
$x > \ln x$ for every $x > 0$.

::: pf-proof
By step [](#minimum){.pf-ref} $x - \ln x = f(x) \ge 1 > 0$ for every $x > 0$, so $x > \ln x$. The inequality is strict at $x = 1$ as well, where both sides are $1$ and $0$ respectively, so no case needs separate treatment.

:::

:::

:::
:::
