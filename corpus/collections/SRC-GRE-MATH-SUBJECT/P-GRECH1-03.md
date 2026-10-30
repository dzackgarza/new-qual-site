---
schema: qual/card@1
id: P-GRECH1-03
kind: problem
title: Solve an equation with absolute values
classification:
  areas:
  - algebra
  topics:
  - Absolute Value Equations
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 1 review Question 3 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription.
---

::: {.problem}
Solve for $x: \abs{x+1} - \abs{x} + 2\abs{x-1} = 2x-1$

(A) $x = -\frac{1}{2}, 1$
(B) $x = -\frac{1}{2}, 2$
(C) $x = 1, 2$
(D) $x = -\frac{1}{2}, 1, 2$
(E) $x \ge 1$
:::

::: {.solution}

The absolute-value breakpoints are $-1$, $0$, and $1$.

::: pf

::: {.pf-step #s1-1}

There is no solution with $x\leq-1$.


::: pf-proof

On this interval,
$$
\abs{x+1}=-(x+1),\qquad \abs{x}=-x,\qquad \abs{x-1}=1-x.
$$
The equation becomes
$$
1-2x=2x-1,
$$
whose only solution is $x=1/2$, outside the interval.

:::

:::

::: {.pf-step #s1-2}

There is no solution with $-1<x\leq0$.


::: pf-proof

Here
$$
\abs{x+1}=x+1,\qquad \abs{x}=-x,\qquad \abs{x-1}=1-x,
$$
so the equation becomes
$$
3=2x-1.
$$
Its only solution is $x=2$, outside the interval.

:::

:::

::: {.pf-step #s1-3}

There is no solution with $0<x<1$.


::: pf-proof

Here
$$
\abs{x+1}=x+1,\qquad \abs{x}=x,\qquad \abs{x-1}=1-x,
$$
so
$$
3-2x=2x-1.
$$
The only solution is $x=1$, which is not in the open interval $(0,1)$.

:::

:::

::: {.pf-step #s1-4}

Every $x\geq1$ is a solution.


::: pf-proof

For $x\geq1$,
$$
\abs{x+1}=x+1,\qquad \abs{x}=x,\qquad \abs{x-1}=x-1.
$$
Hence the left-hand side is
$$
(x+1)-x+2(x-1)=2x-1,
$$
identically equal to the right-hand side.

:::

:::

::: {.pf-step #s1-5}

The solution set is
$$
\boxed{[1,\infty)},
$$
so the answer is (E).


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} exhaust the real line and leave exactly $x\geq1$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the complete solution set and choice.

:::

:::

:::
