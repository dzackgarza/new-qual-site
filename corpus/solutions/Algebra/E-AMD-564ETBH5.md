---
schema: qual/card@1
id: E-AMD-564ETBH5
kind: exercise
title: $a+\nilrad{R}$ nilpotent implies $a\in\nilrad{R}$
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Ideals
  - Rings
relations: []
review: draft
---

::: {.exercise}
Let $R$ be a commutative ring.
Show that if $a + \nilrad{R}$ is nilpotent in $R/\nilrad{R}$, then $a \in \nilrad{R}$.
:::

::: {.solution}
\envlist
\[
a + \nilrad{R} \text{ nilpotent } &\implies (a+ \nilrad{R})^n \definedas a^n + \nilrad{R}= \nilrad{R} \\
&\implies a^n \in \nilrad{R} \\
&\implies \exists \ell \text{ such that } (a^n)^\ell = 0 \\
&\implies a\in \nilrad{R}
.
\]
:::
