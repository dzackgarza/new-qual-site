---
schema: qual/card@1
id: FD-ONITX
kind: definition
title: Local homeomorphism
prompts:
- 'When is a map $f: X \to Y$ a local homeomorphism?'
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Covering Spaces
relations: []
review: draft
---

::: {.definition}
A map $f:X\to Y$ is a local homeomorphism iff for every $x\in X$ there exists a neighborhood $U_x$ such that $f(U_x)$ is open in $Y$ and $f\mid_{U_x}: U_x \to f(U_x)$ is a homeomorphism.

Examples: etale spaces, covering spaces.
:::
