---
schema: qual/card@1
id: E-HAT-3.1-12
kind: exercise
title: Hatcher Section 3.1 Exercise 12
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

# E-HAT-3.1-12


Show $H^k(X, X^n; G) = 0$ if $X$ is a CW complex and $k \leq n$, by using the cohomology version of the second proof of the corresponding result for homology in Lemma 2.34.

::: solution
**Goal:** Prove vanishing of relative cohomology in low degrees by cellular cochains.

<1> Use cellular cohomology for the pair $(X,X^n;G)$.
    The cellular cochain groups are
    $$
    C^k(X,X^n;G)\cong C^k(X;G)/C^k(X^n;G).
    $$

<1> For $k\le n$, the $k$-skeleta agree, so $C^k(X^n;G)=C^k(X;G)$.
    Hence
    $$
    C^k(X,X^n;G)=0 \qquad (k\le n).
    $$
    Therefore all coboundaries and cocycles vanish in these degrees, so
    $$
    H^k(X,X^n;G)=0\quad (k\le n).
    $$

Authored by **Codex 5.3 Spark Extra High**.
:::
