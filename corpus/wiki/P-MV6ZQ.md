---
schema: qual/card@1
id: P-MV6ZQ
kind: problem
title: "Mod by nilradical to kill nilpotents"
classification:
  areas:
  - algebra
  topics:
  - nilpotence
  - ideals
  - rings
relations: []
review: draft
solved: true
---

::: {.problem title="Mod by nilradical to kill nilpotents"}
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
