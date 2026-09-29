---
schema: qual/card@1
id: E-K9POS
kind: problem
title: Continuous images of limit points
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Limit Points
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Suppose that $f: X \to Y$ is continuous.
If $x$ is a limit point of the subset $A$ of $X$, is it necessarily true that $f(x)$ is a limit point of $f(A)$?
:::

::: {.solution}

::: pf

::: {.pf-step #counterexample}
No: for the constant map $f\equiv0\colon\RR\to\RR$ and $A=\theset{1/n : n\in\NN}$, the point $0$ is a limit point of $A$, but $f(0)$ is not a limit point of $f(A)$.

::: pf-proof
A constant map is continuous.
Every interval about $0$ contains $1/n\ne0$ for large $n$, so $0$ is a limit point of $A$.
But $f(A)=\theset{0}$, and a limit point of $\theset{0}$ would need neighborhoods meeting $\theset{0}$ in a point other than itself, which is impossible for $f(0)=0$.
:::

:::

::: pf-step
For continuous $f$ and a limit point $x$ of $A$, $f(x)\in\overline{f(A)}$; if moreover $f(x)\notin f(A)$, then $f(x)$ is a limit point of $f(A)$.

::: pf-proof
Let $V$ be a neighborhood of $f(x)$.
Then $f^{-1}(V)$ is a neighborhood of $x$, so it contains a point $a\in A$ with $a\ne x$, and $f(a)\in V\cap f(A)$.
If $f(x)\notin f(A)$, the point $f(a)$ differs from $f(x)$.
:::

:::

::: pf-qed
Step [](#counterexample){.pf-ref} answers the question.
:::

:::

:::
