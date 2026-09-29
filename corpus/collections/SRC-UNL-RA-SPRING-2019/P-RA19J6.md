---
schema: qual/card@1
id: P-RA19J6
kind: problem
title: A positive continuous function on $[a,b]$ is bounded away from zero, via Heine-Borel
classification:
  areas:
  - real-analysis
  topics:
  - Compactness
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked directly against Problem 6 in the preserved UNL January 2019 qualifying-exam PDF/extraction.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Use the Heine--Borel Theorem to prove that if $f$ is continuous on $[a,b]$ and $f(x)>0$ for every $x\in[a,b]$, then there exists $\varepsilon>0$ such that $f(x)\ge\varepsilon$ for every $x\in[a,b]$.
:::

::: {.solution}
**Goal:** Use the Heine–Borel theorem to prove: $f$ continuous on $[a,b]$ with $f(x) > 0$ for all $x$ implies $f(x) \ge \varepsilon$ for some $\varepsilon > 0$ and all $x$.

::: pf

::: {.pf-step #s1}
Cover $[a,b]$ by neighborhoods where $f$ is bounded below by a positive constant.

::: pf-proof

::: pf-step
For each $x_0 \in [a,b]$: since $f(x_0) > 0$ and $f$ is continuous at $x_0$, choose $\delta_{x_0} > 0$ with $|f(x) - f(x_0)| < f(x_0)/2$ for $|x - x_0| < \delta_{x_0}$; then $f(x) > f(x_0)/2 > 0$ on $(x_0 - \delta_{x_0}, x_0 + \delta_{x_0}) \cap [a,b]$.

::: pf-proof
$\varepsilon$-$\delta$ definition of continuity with $\varepsilon = f(x_0)/2$.
:::

:::

::: pf-step
The intervals $\{B(x_0, \delta_{x_0})\}$ form an open cover of $[a,b]$.

::: pf-proof
each $x_0$ lies in its own ball.
:::

:::

:::

:::

::: {.pf-step #s2}
Extract a finite subcover $B(x_1, \delta_{x_1}), \ldots, B(x_n, \delta_{x_n})$.

::: pf-proof
Heine–Borel: $[a,b]$ is compact, so every open cover has a finite subcover.
:::

:::

::: {.pf-step #s3}
Set $\varepsilon := \min_i \frac{f(x_i)}{2} > 0$; then $f(x) \ge \varepsilon$ for all $x \in [a,b]$.

::: pf-proof
every $x \in [a,b]$ lies in some $B(x_i, \delta_{x_i})$ by step [](#s2){.pf-ref}, where $f(x) > f(x_i)/2 \ge \varepsilon$ by step [](#s1){.pf-ref} and the definition of $\varepsilon$; $\varepsilon > 0$ since each $f(x_i) > 0$ and the minimum is over finitely many positive numbers.
:::

:::

::: pf-qed
step [](#s3){.pf-ref} is the claim.
:::

:::

:::
