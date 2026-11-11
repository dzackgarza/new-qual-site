---
schema: qual/card@1
id: E-CEDQ9
kind: problem
title: Maps of higher spheres into the circle are nullhomotopic
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 79 Exercise 1, printed p. 483. The lifting criterion for S^n simply connected, then the contraction of R. Checked against Theorem 79.1 (the lifting criterion) and Theorem 59.3. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
---

::: {.exercise}

Show that if $n > 1$, every continuous map $f: S^n \to S^1$ is nullhomotopic.
[Hint: Use the lifting lemma.]
:::

::: {.solution}
Let $n>1$ and $f:S^n\to S^1$. Choose a basepoint $x_0\in S^n$, and let
$$
p:\RR\longrightarrow S^1,\qquad p(t)=e^{2\pi i t}
$$
be the universal covering map. Since $S^n$ is simply connected for $n>1$,
$$
f_*\pi_1(S^n,x_0)=0\subset p_*\pi_1(\RR,\tilde b_0)=0.
$$
The lifting criterion therefore gives a lift
$$
\tilde f:S^n\to\RR,\qquad p\tilde f=f.
$$
Because $\RR$ is contractible, $\tilde f$ is homotopic to a constant map. Composing this homotopy with $p$ gives a homotopy of $f$ to a constant map in $S^1$. Hence every map $S^n\to S^1$ is nullhomotopic.
:::
