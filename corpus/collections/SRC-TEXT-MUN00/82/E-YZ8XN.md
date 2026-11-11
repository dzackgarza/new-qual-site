---
schema: qual/card@1
id: E-YZ8XN
kind: problem
title: Simple connectedness implies semilocal simple connectedness
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
    Checked against Munkres, Topology (2000), Section 82 Exercise 1, printed p. 499. A simply connected space is semilocally simply connected, by taking the neighbourhood itself. Checked against the definition of semilocally simply connected, printed p. 489. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
---

::: {.exercise}

Show that a simply connected space is semilocally simply connected.
:::

::: {.solution}
If $X$ is simply connected, then $X$ is path connected and
$$
\pi_1(X,x)=0
$$
for every basepoint $x\in X$. Let $x\in X$. Taking $U=X$ itself (or any path-connected neighborhood of $x$), the inclusion-induced homomorphism
$$
\pi_1(U,x)\longrightarrow\pi_1(X,x)
$$
has trivial target and hence is trivial. This is precisely the semilocal simple-connectedness condition. Therefore every simply connected space is semilocally simply connected.
:::
