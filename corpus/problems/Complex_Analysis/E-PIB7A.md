---
schema: qual/card@1
id: E-PIB7A
kind: problem
title: Cancelling poles with Blaschke factors
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Poles
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source reads "Let f be meromorphic on D with no poles on the boundary of D"; f must be defined on the unit circle, and with infinitely many poles in D no finite Blaschke product cancels them, so the statement takes f meromorphic on a neighborhood of the closed disc.'
---

::: {.exercise}
Let $f$ be meromorphic on a neighborhood of $\overline{\DD}$ with no poles on $\bd\DD$.
Show that there exists a meromorphic $g$ with *no* poles in $\DD$ such that $\abs{f(z)} = \abs{g(z)}$ when $\abs{z} = 1$.
:::

::: {.solution}

For $a\in\DD$ let $\psi_a(z)\coloneqq\frac{z-a}{1-\bar a z}$.

::: pf

::: {.pf-step #finite}
$f$ has finitely many poles $a_1,\ldots,a_n$ in $\DD$, listed with multiplicity.

::: pf-proof
The poles of a meromorphic function are discrete, and $\overline\DD$ is compact.
:::

:::

::: {.pf-step #blaschke}
Each $\psi_a$ is holomorphic on a neighborhood of $\overline\DD$, has a simple zero at $a$ and no other zero, and satisfies $\abs{\psi_a(z)}=1$ for $\abs{z}=1$.

::: pf-proof
The only pole of $\psi_a$ is $1/\bar a$, outside $\overline\DD$.
For $\abs{z}=1$, $\abs{1-\bar az} = \abs{\bar z}\abs{1-\bar a z} = \abs{\bar z - \bar a} = \abs{z-a}$.
:::

:::

::: pf-step
$g\coloneqq f\prod_{k=1}^n\psi_{a_k}$ has no poles in $\DD$ and $\abs{g}=\abs{f}$ on $\abs{z}=1$.

::: pf-proof
By steps [](#finite){.pf-ref} and [](#blaschke){.pf-ref}, at each pole $a$ of $f$ in $\DD$ the product has a zero of order equal to the order of the pole, so $g$ has a removable singularity there, and $g$ has no other poles in $\DD$.
On $\abs{z}=1$, each $\abs{\psi_{a_k}(z)}=1$.
:::

:::

:::

:::
