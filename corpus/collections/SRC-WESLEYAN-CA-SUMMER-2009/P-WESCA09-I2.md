---
schema: qual/card@1
id: P-WESCA09-I2
kind: problem
title: 'Define free homotopy of closed paths'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Section I, item 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $U\subset\CC$ and let $\alpha_i:[0,1]\to U$ for $i=1,2$ be closed paths.
Define what it means for $\alpha_1$ to be freely homotopic to $\alpha_2$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The closed paths $\alpha_1$ and $\alpha_2$ are freely homotopic if there exists a continuous map
\[
\boxed{H:[0,1]\times[0,1]\to U}
\]
such that
\[
H(s,0)=\alpha_1(s),
\qquad
H(s,1)=\alpha_2(s)
\]
for every $s\in[0,1]$, and
\[
H(0,t)=H(1,t)
\]
for every $t\in[0,1]$.


::: pf-proof

For each fixed $t$, the path
\[
s\longmapsto H(s,t)
\]
is closed because its endpoint values agree. The first two identities say that
the family starts at $\alpha_1$ and ends at $\alpha_2$. No value of
$H(0,t)=H(1,t)$ is required to remain fixed as $t$ varies, which is precisely
the distinction between free homotopy of closed paths and based homotopy of
loops.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives the requested definition.

:::

:::

:::
