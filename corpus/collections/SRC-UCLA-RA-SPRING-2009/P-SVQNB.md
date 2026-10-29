---
schema: qual/card@1
id: P-SVQNB
kind: problem
title: A nonconstant entire function with $f(1-z)=1-f(z)$ is surjective
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $f$ be an entire non-constant function that satisfies the functional equation $$f(1-z) = 1-f(z)$$ for all $z\in\CC$.
Show that $f(\CC)=\CC$.
:::

::: {.solution}

::: pf

::: {.pf-step #half}
$f(1/2)=1/2$.

::: pf-proof
Setting $z=1/2$ in the functional equation gives $f(1/2)=1-f(1/2)$.
:::

:::

::: {.pf-step #pair}
If $f$ omits a value $a$, then $f$ also omits $1-a$, and $a\ne1-a$.

::: pf-proof
If $f(z)=1-a$, then $f(1-z)=1-f(z)=a$, a contradiction.
By step [](#half){.pf-ref}, $a\ne1/2$, so $a\ne1-a$.
:::

:::

::: pf-step
$f(\CC)=\CC$.

::: pf-proof
If $f$ omitted a value, step [](#pair){.pf-ref} would give two distinct omitted values, contradicting Picard's little theorem for the nonconstant entire function $f$.
:::

:::

:::

:::
