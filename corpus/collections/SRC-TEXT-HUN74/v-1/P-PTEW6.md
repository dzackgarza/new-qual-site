---
schema: qual/card@1
id: P-PTEW6
kind: problem
title: Hungerford 5.1.14
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Bases
  - Roots of Unity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
\envlist

1. If $F = \mathbb{Q}(\sqrt 2, \sqrt 3)$, compute $[F: \mathbb{Q}]$ and find a basis of $F/\mathbb{Q}$.

2. Do the same for $\mathbb{Q}(i, \sqrt 3, \zeta_3)$ where $\zeta_3$ is a complex third root of 1.
:::

::: {.solution}
**Part 1.**

<1>1. $[\mathbb{Q}(\sqrt 2) : \mathbb{Q}] = 2$ and $[\mathbb{Q}(\sqrt 2, \sqrt 3) : \mathbb{Q}(\sqrt 2)] = 2$ (since $\sqrt 3 \notin \mathbb{Q}(\sqrt 2)$).
Proof: $\sqrt 2$ and $\sqrt 3$ are irrational, and $\sqrt 3 \notin \mathbb{Q}(\sqrt 2)$ (otherwise $\sqrt 3 = a + b\sqrt 2$ with $a, b \in \mathbb{Q}$, which is impossible).

<1>2. Hence $[F : \mathbb{Q}] = 2 \cdot 2 = 4$.
Proof: <1>1 and the tower law.

<1>3. A basis is $\{1, \sqrt 2, \sqrt 3, \sqrt 6\}$.
Proof: <1>1 (the basis is the product of the bases $\{1, \sqrt 2\}$ and $\{1, \sqrt 3\}$).

**Part 2.**

<1>1. $\zeta_3 = \frac{-1 + i\sqrt 3}{2}$, so $\zeta_3 \in \mathbb{Q}(i, \sqrt 3)$.
Proof: $\zeta_3 = \frac{-1 + i\sqrt 3}{2}$.

<1>2. Hence $\mathbb{Q}(i, \sqrt 3, \zeta_3) = \mathbb{Q}(i, \sqrt 3)$.
Proof: <1>1.

<1>3. $[\mathbb{Q}(i) : \mathbb{Q}] = 2$ and $[\mathbb{Q}(i, \sqrt 3) : \mathbb{Q}(i)] = 2$ (since $\sqrt 3 \notin \mathbb{Q}(i)$).
Proof: $i$ is a root of $x^2 + 1$, and $\sqrt 3 \notin \mathbb{Q}(i)$ (since $\mathbb{Q}(i)$ contains no real irrationals).

<1>4. Hence $[\mathbb{Q}(i, \sqrt 3, \zeta_3) : \mathbb{Q}] = 2 \cdot 2 = 4$.
Proof: <1>2 and <1>3.

<1>5. A basis is $\{1, i, \sqrt 3, i\sqrt 3\}$.
Proof: <1>3 (the product of the bases $\{1, i\}$ and $\{1, \sqrt 3\}$).

<1>6. Q.E.D.
Proof: <1>2, <1>3 (part 1) and <1>4, <1>5 (part 2).
:::
