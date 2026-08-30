---
schema: qual/card@1
id: E-HAT-1.2-15
kind: exercise
title: Canonical map from loop complex $L(X)$ to $X$ induces isomorphism on $\pi_1$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - CW Complexes
  - van Kampen
relations: []
review: draft
---

Given a space $X$ with basepoint $x_0 \in X$, we may construct a CW complex $L(X)$ having a single 0 cell, a 1 cell $e^1_\gamma$ for each loop $\gamma$ in $X$ based at $x_0$, and a 2 cell $e^2_\tau$ for each map $\tau$ of a standard triangle $PQR$ into $X$ taking the three vertices $P$, $Q$, and $R$ of the triangle to $x_0$.
The 2 cell $e^2_\tau$ is attached to the three 1 cells that are the loops obtained by restricting $\tau$ to the three oriented edges $PQ$, $PR$, and $QR$.
Show that the natural map $L(X) \longrightarrow X$ induces an isomorphism $\pi_1\big(L(X)\big) \approx \pi_1(X, x_0)$.
