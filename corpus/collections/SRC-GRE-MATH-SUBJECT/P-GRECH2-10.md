---
schema: qual/card@1
id: P-GRECH2-10
kind: problem
title: Differentiable gluing of a quadratic and a line at $x=1$
classification:
  areas: [prelim]
  topics:
  - Differentiability
  - Piecewise Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 10 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
For what values of $m$ and $b$ will the following function have a derivative for every $x$?

$$
f(x) = \begin{cases} x^2 + x - 3 & \text{if } x \le 1 \\ mx + b & \text{if } x > 1 \end{cases}
$$

(A) $m = 3, b = -2$
(B) $m = -2, b = -3$
(C) $m = 1, b = -4$
(D) $m = -2, b = 1$
(E) $m = 3, b = -4$
:::

::: {.solution}

Only the joining point $x=1$ can fail to be differentiable.

::: pf

::: {.pf-step #s1-1}

Differentiability at $x=1$ forces $m=3$.


::: pf-proof

For $x<1$, the derivative is
$$
2x+1,
$$
so the left derivative at $1$ is $3$. For $x>1$, the derivative is the constant $m$, so the right derivative at $1$ is $m$. Equality of the one-sided derivatives therefore requires $m=3$.

:::

:::

::: {.pf-step #s1-2}

Continuity at $x=1$ then forces $b=-4$.


::: pf-proof

Differentiability implies continuity. The left branch gives
$$
f(1)=1^2+1-3=-1.
$$
The right-hand limit is $m+b$, so continuity requires
$$
m+b=-1.
$$
Using $m=3$ from step [](#s1-1){.pf-ref} gives $b=-4$.

:::

:::

::: {.pf-step #s1-3}

The values $m=3$ and $b=-4$ are sufficient.


::: pf-proof

With these values, both one-sided limits at $1$ equal $-1$, so the function is continuous there, and both one-sided derivatives equal $3$ by step [](#s1-1){.pf-ref}. Hence the derivative exists at $1$. Each branch is a polynomial or linear function, so it is differentiable at every other point.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{m=3,\qquad b=-4},
$$
so the answer is (E).


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} show necessity, while step [](#s1-3){.pf-ref} shows sufficiency.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the unique pair for which $f$ is differentiable everywhere.

:::

:::

:::
