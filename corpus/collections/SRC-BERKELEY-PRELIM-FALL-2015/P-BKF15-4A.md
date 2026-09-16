---
schema: qual/card@1
id: P-BKF15-4A
kind: problem
title: The orthogonal-complement involution of the Riemann sphere is antiholomorphic
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
  note: Statement checked against F15_Exam.pdf problem 4A; restored the arrows of phi and tau and the broken equation in (a).
---

::: {.problem}
Let $S = \mathbb{C} \cup \{\infty\}$ be the Riemann sphere.
Let $\phi \colon \mathbb{C}^2 \setminus \{(0,0)\} \to S$ be the map defined by $\phi(w, z) = w/z$ for $z \neq 0$ and $\phi(w, 0) = \infty$.

(a) Prove that there is a unique map $\tau \colon S \to S$ with the following property: $\tau(\phi(w, z)) = \phi(w', z')$ if and only if the one-dimensional subspaces $\mathbb{C} \cdot (w, z)$ and $\mathbb{C} \cdot (w', z')$ are orthogonal under the standard Hermitian inner product on $\mathbb{C}^2$ in which the unit vectors $(1, 0)$ and $(0, 1)$ are orthonormal.

(b) Prove that $\tau$ is continuous and bijective.

(c) Determine, with proof, whether $\tau$ is holomorphic or not.
:::
