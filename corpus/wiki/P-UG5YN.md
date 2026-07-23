---
schema: qual/card@1
id: P-UG5YN
kind: problem
title: "Prove that, for $n \\geq 2$, every continuous map $f: \\RP^n \\to S^1$ is\u2026"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
Prove that, for $n \geq 2$, every continuous map $f: \RP^n \to S^1$ is null-homotopic.

:::{.solution}
\hfill
:::{.concept}
\hfill

:::
- Any continuous map $\RP^n \mapsvia{f} S^1$ induces a group morphism $\pi_1\RP^n \mapsvia{f_*} \pi_1S^1$
- Identify $\pi_1\RP^n = \ZZ/2\ZZ$ and $\pi_1S^1 = \ZZ$ to obtain a group morphism $f_*: \ZZ/2\ZZ \to \ZZ$.
- Claim: $f_* = 0$.
  - Recognizing this as a map of $\ZZ\dash$modules, we must have
  \[  
  0 = [2]_2 = 2\cdot [1]_2  \implies 0 = f_*(0) = 2\cdot f_*([1]_2)
  .\]
    since $\ZZ\dash$module maps send 0 to 0.

  - But no element of the image $\ZZ$ is annihilated by $2$, so $f_*$ can only be the zero map.

- But then $f$ is nullhomotopic.

- Lemma: $f_* = 0$ implies $f$ is nullhomotopic. 
:::{.remark}
Why?
:::

:::
