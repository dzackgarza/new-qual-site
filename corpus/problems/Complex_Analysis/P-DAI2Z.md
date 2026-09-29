---
schema: qual/card@1
id: P-DAI2Z
kind: problem
title: Number of solutions of $e^z=az^n$ in the unit disk
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let $n\in \ZZ^{\geq 0}$ and show that the equation
\[
e^z = az^n
\]
has $n$ solutions in the open unit disc if $\abs{a} > e$, and no solutions if $\abs{a} < {1\over e}$.
:::

::: {.solution}
**Goal:** Show that $e^z = az^n$ has exactly $n$ solutions in the open unit disk when $\abs a > e$, and no solutions when $\abs a < \frac{1}{e}$.

::: pf

::: {.pf-step #abs-ez-upper-bound}
On $\abs z = 1$: $\abs{e^z} = e^{\Re z} \leq e^{\abs z} = e$.

::: pf-proof
$\Re z \leq \abs z = 1$ on the unit circle.
:::

:::

::: {.pf-step #case-large-a}
Case $\abs a > e$: $e^z - az^n$ has exactly $n$ zeros in $\abs z < 1$.

::: pf-proof

::: {.pf-step #strict-ineq-large-a}
On $\abs z = 1$, $\abs{e^z} < \abs{az^n} = \abs a$.

::: pf-proof
Step [](#abs-ez-upper-bound){.pf-ref} and $\abs a > e$; also $\abs{z^n} = 1$.
:::

:::

::: {.pf-step #same-zero-count-large-a}
$e^z - az^n$ and $-az^n$ have the same number of zeros in $\abs z < 1$.

::: pf-proof
Rouch\'e's theorem with $f(z) = -az^n$ and $g(z) = e^z$, using step [](#strict-ineq-large-a){.pf-ref}.
:::

:::

::: {.pf-step #neg-az-n-zeros}
$-az^n$ has exactly $n$ zeros in $\abs z < 1$ (counting multiplicity).

::: pf-proof
Its only zero is $z = 0$, of multiplicity $n$ (for $n \geq 1$; for $n = 0$, $-a \neq 0$ has no zeros, and "$n = 0$ solutions" is consistent).
:::

:::

::: pf-step
Conclusion.

::: pf-proof
Steps [](#same-zero-count-large-a){.pf-ref} and [](#neg-az-n-zeros){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #abs-ez-lower-bound}
On $\abs z = 1$: $\abs{e^z} = e^{\Re z} \geq e^{-1} = \frac{1}{e}$.

::: pf-proof
$\Re z \geq -\abs z = -1$ on the unit circle.
:::

:::

::: {.pf-step #case-small-a}
Case $\abs a < \frac{1}{e}$: $e^z - az^n$ has no zeros in $\abs z < 1$.

::: pf-proof

::: {.pf-step #strict-ineq-small-a}
On $\abs z = 1$, $\abs{az^n} = \abs a < \frac{1}{e} \leq \abs{e^z}$.

::: pf-proof
Step [](#abs-ez-lower-bound){.pf-ref} and the hypothesis on $\abs a$.
:::

:::

::: {.pf-step #same-zero-count-small-a}
$e^z - az^n$ and $e^z$ have the same number of zeros in $\abs z < 1$.

::: pf-proof
Rouch\'e's theorem with $f(z) = e^z$ and $g(z) = -az^n$, using step [](#strict-ineq-small-a){.pf-ref}.
:::

:::

::: {.pf-step #ez-no-zeros}
$e^z$ has no zeros.

::: pf-proof
The exponential never vanishes.
:::

:::

::: pf-step
Conclusion.

::: pf-proof
Steps [](#same-zero-count-small-a){.pf-ref} and [](#ez-no-zeros){.pf-ref}.
:::

:::

:::

:::

::: pf-qed
Step [](#case-large-a){.pf-ref} gives exactly $n$ solutions in the disk when $\abs a > e$; step [](#case-small-a){.pf-ref} gives none when $\abs a < 1/e$.
:::

:::
