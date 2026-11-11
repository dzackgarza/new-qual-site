---
schema: qual/card@1
id: E-SADP0
kind: problem
title: Continuous surjections from the interval onto cubes
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §44 Exercise 1 was located; the sets searched are listed in
    the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00, and Robert Gardner's ETSU notes on §44
    (faculty.etsu.edu/gardnerr/5357/notes/Munkres-44.pdf) prove only Theorem 44.1, which is the input
    here. The card follows the exercise's own hint. Checked line by line against the book: Theorem 44.1
    gives a continuous surjection p: I -> I^2; if q_k: I -> I^{2^k} is a continuous surjection then
    q_k x q_k: I x I -> I^{2^{k+1}} is one (Theorem 18.4 for continuity of a map into a product, and
    surjectivity coordinatewise), so q_{k+1} = (q_k x q_k) o p is a continuous surjection I -> I^{2^{k+1}},
    beginning at q_0 = id_I; for arbitrary n choose k with n <= 2^k and project onto the first n
    coordinates, which is continuous and surjective. Nothing on the card needed correction.
---

::: {.exercise}

Given $n$, show there is a continuous surjective map $g: I \to I^n$.
[Hint: Consider

$$
f \times f: I \times I \to I^2 \times I^2.]
$$
:::

::: {.solution}
Let $p:I\to I^2$ be a continuous surjection, such as the Peano space-filling curve.

We first obtain surjections onto powers whose dimensions are powers of $2$. Suppose $q_k:I\to I^{2^k}$ is continuous and surjective. Then
$$
q_k\times q_k:I^2\longrightarrow I^{2^{k+1}}
$$
is continuous and surjective, so
$$
q_{k+1}=(q_k\times q_k)\circ p:I\longrightarrow I^{2^{k+1}}
$$
is continuous and surjective. Starting with $q_0=\operatorname{id}_I$, induction gives such a map for every $2^k$.

Given arbitrary $n\ge1$, choose $k$ with $n\le2^k$ and compose $q_k$ with the projection
$$
I^{2^k}\longrightarrow I^n
$$
onto the first $n$ coordinates. The resulting map $I\to I^n$ is continuous and surjective.
:::
