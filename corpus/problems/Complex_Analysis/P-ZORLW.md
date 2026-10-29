---
schema: qual/card@1
id: P-ZORLW
kind: problem
title: Holomorphic functions vanishing on the boundary are constant or have an interior
  zero
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: statement-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'The card stated only "if |f| = 0 on the boundary of Omega", with no hypotheses on f or Omega; the hypotheses that the solution assumed (Omega a bounded region, f holomorphic on Omega and continuous on its closure) are now in the statement.'
---

::: {.problem}
Let $\Omega$ be a bounded region and let $f$ be holomorphic on $\Omega$ and continuous on $\bar\Omega$.
Show that if $\abs{f} = 0$ on $\bd \Omega$ then either $f$ is constant or $f$ has a zero in $\Omega$.
:::

::: {.solution}

::: pf

::: {.pf-step #zero}
$f\equiv0$ on $\bar\Omega$.

::: pf-proof
$\abs{f}$ is continuous on the compact set $\bar\Omega$, and by the maximum modulus principle $\max_{\bar\Omega}\abs{f}=\max_{\bd\Omega}\abs{f}=0$.
:::

:::

::: pf-step
$f$ is constant, and it has a zero in $\Omega$.

::: pf-proof
By step [](#zero){.pf-ref}, $f$ is the zero function, and $\Omega$ is nonempty.
:::

:::

:::

:::
