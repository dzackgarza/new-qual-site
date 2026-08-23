---
schema: qual/card@1
id: P-RASP22F
kind: problem
title: "A measure agreeing with an integral against itself on open sets has density one"
classification:
  areas:
  - real-analysis
  topics:
  - Radon Measures
  - Outer Regularity
relations: []
review: draft
solved: false
---

::: problem
Let $X$ be an LCH (a locally compact Hausdorff space). Let $\mu$ be a $\sigma$-finite measure on $X$ such that for any measurable set $E$, $\mu(E) = \inf\{\mu(U), E \subset U, U \text{ open}\}$. Let $f \geq 0$ be a bounded measurable function. Prove that if $\mu(U) = \int_U f \, d\mu$ whenever $U$ is open then $f = 1$ $\mu$-a.e.
:::