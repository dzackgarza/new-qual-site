---
schema: qual/card@1
id: E-5CCAN
kind: problem
title: $\RR$ is not homeomorphic to $[0,\infty)$
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Connectedness
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that $\RR$ is not homeomorphic to $[0, \infty)$.
:::

::: {.solution}
Suppose, for a contradiction, that $f:[0,\infty)\to\RR$ is a homeomorphism, and set $y=f(0)$.

::: pf

::: {.pf-step #restrict}

$f$ restricts to a homeomorphism $(0,\infty)\to\RR\setminus\{y\}$.

::: pf-proof

A bijection that is a homeomorphism restricts to a homeomorphism from any subspace onto its image, and $f\big([0,\infty)\setminus\{0\}\big)=\RR\setminus\{y\}$.

:::

:::

::: pf-qed

The space $(0,\infty)$ is connected, whereas $\RR\setminus\{y\}=(-\infty,y)\sqcup(y,\infty)$ is a union of two disjoint nonempty open sets, hence disconnected. Connectedness is preserved by homeomorphisms, so step [](#restrict){.pf-ref} is impossible. Therefore $\RR$ is not homeomorphic to $[0,\infty)$.

:::

:::

:::
