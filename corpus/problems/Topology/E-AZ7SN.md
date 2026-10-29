---
schema: qual/card@1
id: E-AZ7SN
kind: problem
title: A continuous real-valued function on a compact space attains its bounds
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: statement-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: Source printed "Show that if f:X -> R and X is compact then f is bounded and attains its min/max" without the continuity hypothesis, which the result needs; the statement adds "continuous".
---

::: {.exercise}
Show that if $f:X\to \RR$ is continuous and $X$ is compact then $f$ is bounded and attains its min/max.
:::

::: {.solution}

::: pf

::: pf-step
$f(X)$ is compact in $\RR$.

::: pf-proof
Continuous image of the compact space $X$.
:::

:::

::: {.pf-step #s2}
$f(X)$ is closed and bounded.

::: pf-proof
Compact subsets of $\RR$ are closed and bounded (Heine--Borel).
:::

:::

::: {.pf-step #s3}
$f$ is bounded.

::: pf-proof
$f(X)$ bounded (step [](#s2){.pf-ref}) means $f$ is bounded above and below.
:::

:::

::: {.pf-step #s4}
$f$ attains its supremum.

::: pf-proof

::: pf-step
$\sup f(X)$ is finite.

::: pf-proof
$f(X)$ is bounded above (step [](#s2){.pf-ref}).
:::

:::

::: pf-step
$\sup f(X) \in f(X)$.

::: pf-proof
$f(X)$ is closed (step [](#s2){.pf-ref}), and the supremum of a bounded set lies in its closure; since the set is closed, the supremum belongs to it.
:::

:::

::: pf-step
Some $x_{\max} \in X$ satisfies $f(x_{\max}) = \max f$.

::: pf-proof
$\sup f(X) \in f(X)$ means $\sup f(X) = f(x_{\max})$ for some $x_{\max} \in X$.
:::

:::

:::

:::

::: {.pf-step #s5}
$f$ attains its infimum.

::: pf-proof
Same argument as step [](#s4){.pf-ref} with $\inf$ in place of $\sup$ (or apply step [](#s4){.pf-ref} to $-f$).
:::

:::

::: pf-qed
Step [](#s3){.pf-ref} gives boundedness, and steps [](#s4){.pf-ref} and [](#s5){.pf-ref} show that $f$ attains its maximum and minimum.
:::

:::

:::
