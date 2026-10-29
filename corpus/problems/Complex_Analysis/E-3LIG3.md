---
schema: qual/card@1
id: E-3LIG3
kind: problem
title: Entire functions satisfying $g(1-z)=1-g(z)$ are surjective
classification:
  areas:
  - complex-analysis
  topics:
  - Picard
  - Entire Functions
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source reads "Suppose that g is entire"; the constant g = 1/2 satisfies the functional equation and is not surjective, so the statement adds the hypothesis that g is nonconstant.
---

::: {.exercise}
Suppose that $g$ is a nonconstant entire function and satisfies the functional equation $g(1-z) = 1-g(z)$.
Show that $g(\CC) = \CC$.
:::

::: {.solution}

::: pf

::: {.pf-step #half}
$g(1/2)=1/2$.

::: pf-proof
Setting $z=1/2$ in the functional equation gives $g(1/2)=1-g(1/2)$.
:::

:::

::: {.pf-step #pair}
If $g$ omits a value $a$, then $g$ also omits $1-a$, and $a\ne1-a$.

::: pf-proof
If $g(z)=1-a$, then $g(1-z)=1-g(z)=a$, a contradiction.
By step [](#half){.pf-ref}, $a\ne1/2$, so $a\ne1-a$.
:::

:::

::: pf-step
$g(\CC)=\CC$.

::: pf-proof
If $g$ omitted a value, step [](#pair){.pf-ref} would give two distinct omitted values, contradicting Picard's little theorem for the nonconstant entire function $g$.
:::

:::

:::

:::
