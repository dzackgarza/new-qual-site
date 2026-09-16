---
schema: qual/card@1
id: P-BKS17-4A
kind: problem
title: Legendre's relation for the Weierstrass zeta function
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the three-item property list (both quasi-periodicity relations and the pole condition as bullets) and inline-math spacing against Sp17_Exam_0.pdf page 5 problem 4A.
---

::: {.problem}
The Weierstrass zeta function $\zeta$ is a meromorphic function satisfying

- $\zeta(z + \omega_1) = \zeta(z) + \eta_1$
- $\zeta(z + \omega_2) = \zeta(z) + \eta_2$
- The singularities of $\zeta$ are poles of residue 1 at the points $m\omega_1 + n\omega_2$ for $m, n \in \mathbb{Z}$

Here $\omega_1, \omega_2, \eta_1, \eta_2$ are complex constants with $\omega_2 / \omega_1$ not real. Use Cauchy’s residue theorem to prove Legendre’s relation $\omega_2 \eta_1 - \omega_1 \eta_2 = \pm 2\pi i$ and express the sign in terms of $\omega_1$ and $\omega_2$.
:::
