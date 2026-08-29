---
schema: qual/card@1
id: P-MV6ZQ
kind: problem
title: Mod by nilradical to kill nilpotents
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

::: {.problem}
$R/ \nilrad{R}$ has no nonzero nilpotent elements.
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
