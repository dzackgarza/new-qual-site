---
schema: qual/card@1
id: P-R9XZL
kind: problem
title: Every maximal ideal is prime, so $\MaxSpec R\subseteq\Spec R$
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Maximal Ideals
relations: []
review: draft
---

::: {.problem}
Show that $\operatorname{MaxSpec}R\subseteq\operatorname{Spec}R$, and give an example of strict containment and one of equality.
:::

::: {.solution}
Every maximal ideal is prime: a maximal ideal $I$ makes $R/I$ a field, and every field is a domain. Hence
\[
\operatorname{MaxSpec}R\subseteq\operatorname{Spec}R.
\]
For $R=\ZZ$ the containment is strict because $(0)$ is prime but not maximal. For a field $k$,
\[
\operatorname{Spec}k=\operatorname{MaxSpec}k=\{(0)\}.
\]
:::