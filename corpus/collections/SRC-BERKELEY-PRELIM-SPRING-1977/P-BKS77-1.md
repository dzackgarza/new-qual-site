---
schema: qual/card@1
id: P-BKS77-1
kind: problem
title: A differential inequality forces positivity to the right of a zero
classification: {areas: [prelim], topics: [Real Analysis]}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Applied the integrating factor e^{-x}; its derivative is strictly
    positive, so the transformed function is strictly increasing from zero.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained sheet `assets/attachments/Spring77.pdf`: the statement is its Problem 1, and the printed words
    are the card's. The exam, the problem number and the file are now named in the solution's
    opening sentence. Not checked in this pass: the solution, which the edit does not touch.
---

::: {.problem}
Let $f:\RR\to\RR$ be differentiable and suppose
$$
f'(x)>f(x)
$$
for every $x\in\RR$. If $f(x_0)=0$, prove that
$$
f(x)>0
$$
for every $x>x_0$.
:::

::: {.solution}
This is Problem 1 of the Preliminary Exam, Spring 1977, retained in this repository as `assets/attachments/Spring77.pdf`; the statement below is its wording.

::: pf

::: {.pf-step #s1}

Define
$$
g(x)=e^{-x}f(x).
$$
Then $g'(x)>0$ for every $x\in\RR$.

::: pf-proof

By the product rule,
$$
g'(x)
=
e^{-x}\bigl(f'(x)-f(x)\bigr).
$$
The factor $e^{-x}$ is positive, and the hypothesis gives
$f'(x)-f(x)>0$. Hence $g'(x)>0$.

:::

:::

::: {.pf-step #s2}

The function $g$ is strictly increasing on $\RR$.

::: pf-proof

If $a<b$, the mean value theorem gives some $c\in(a,b)$ such that
$$
g(b)-g(a)=g'(c)(b-a).
$$
By step [](#s1){.pf-ref}, both factors on the right are positive, so $g(b)>g(a)$.

:::

:::

::: {.pf-step #s3}

If $x>x_0$, then $f(x)>0$.

::: pf-proof

Since
$$
g(x_0)=e^{-x_0}f(x_0)=0,
$$
strict increase from step [](#s2){.pf-ref} gives $g(x)>0$ whenever $x>x_0$. Therefore
$$
f(x)=e^xg(x)>0.
$$

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required conclusion.

:::

:::

:::
