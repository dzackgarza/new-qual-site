---
schema: qual/card@1
id: P-FHW1-11
kind: problem
title: $K(\alpha)=K(\alpha^2)$ for an extension of odd degree
classification:
  areas: [algebra]
  topics: [Field Extensions]
relations: []
review: draft
audit:
- event: source-checked
  by: Claude Opus 5.5
  date: 2026-10-30
  note: Transcribed from the MinerU Flash extraction of assets/attachments/fields-homework-1.pdf and checked against the page image.
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Let $F=K(\alpha)$ and suppose that $[F:K]$ is odd. Show that $F=K(\alpha^2)$.
:::

::: {.solution}
The field $K(\alpha^2)$ is an intermediate field of $K\subseteq K(\alpha^2)\subseteq K(\alpha)=F$.

::: pf

::: {.pf-step #degree-two}
$[K(\alpha):K(\alpha^2)]\le2$.

::: pf-proof
The element $\alpha$ is a root of $x^2-\alpha^2\in K(\alpha^2)[x]$, so its minimal polynomial over $K(\alpha^2)$ has degree at most $2$.
:::

:::

::: {.pf-step #equality}
$F=K(\alpha^2)$.

::: pf-proof
The tower law gives $[F:K]=[K(\alpha):K(\alpha^2)]\,[K(\alpha^2):K]$.
The left side is odd by hypothesis, and by step [](#degree-two){.pf-ref} the first factor is $1$ or $2$; an odd number cannot be divisible by $2$, so the first factor is $1$.
Hence $[K(\alpha):K(\alpha^2)]=1$, which means $K(\alpha)=K(\alpha^2)$.
:::

:::

:::

:::
