---
schema: qual/card@1
id: P-FD3UV
kind: problem
title: Every continuous map $\mathbb{RP}^2\to S^1\times S^1$ is null-homotopic
classification:
  areas:
  - topology
  topics:
  - homotopy
  - fundamental-group
  - covering-spaces
relations: []
review: draft
solved: true
---
Show that any continuous map $f : \RP^2 \to S^1 \times S^1$ is necessarily null-homotopic.

:::{.solution}
:::{.concept}
- Two techniques: 
  - Show $f_* = 0$ 
  - Lift to a contractible universal cover.
:::

- Any continuous map $\RP^2 \mapsvia{f} S^1\cross S^1$ induces a group morphism $\pi_1 \RP^2 \mapsvia{f_*} \pi_1(S^1\cross S^1)$
- Identify $\pi_1 \RP^2 = \ZZ/2\ZZ$ and $\pi_1(S^1\cross S^1) = \pi_1 S^1 \cross \pi_1 S^1 = \ZZ^2$.
- But as a $\ZZ\dash$module morphism, $f_*$ will preserve torsion submodules, and since $\ZZ^2$ is free we must have $f_* = 0$.

- Lemma: $f_* = 0$ implies $f$ is nullhomotopic. 
:::{.remark}
Why? What is the homotopy?
:::
  - Note that $\widetilde{S^1\cross S^1} = \RR^2$.
:::
