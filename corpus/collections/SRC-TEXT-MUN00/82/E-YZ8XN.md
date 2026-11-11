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
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. Corrected: the definition of semilocal simple connectedness is printed on p. 494, not p. 489 as the previous note said; p. 489 carries Corollaries 81.3 and 81.4. The proof now cites the Definition of simple connectedness (printed p. 333) and the Definition of semilocal simple connectedness (printed p. 494), and states the two points the argument needs: that $X$ is a neighbourhood of each of its points, because it is open in itself, and that the induced homomorphism of the inclusion $X\to X$ is the identity of the trivial group, not only a map into a trivial group. What the certificate does not cover: nothing; the exercise has no parts.
---

::: {.exercise}

Show that a simply connected space is semilocally simply connected.

:::

::: {.solution}

A space $X$ is simply connected when it is path connected and $\pi_1(X,x)$ is the trivial group for some, hence every, base point (Definition, printed p. 333). It is semilocally simply connected when for each $b\in X$ there is a neighbourhood $U$ of $b$ such that the homomorphism
$$
i_*:\pi_1(U,b)\longrightarrow\pi_1(X,b)
$$
induced by inclusion is trivial (Definition, printed p. 494).

Let $X$ be simply connected and let $x\in X$. Take $U=X$. This is a neighbourhood of $x$, because a set is open in itself. The inclusion $i:U\to X$ is the identity map, so $i_*$ is the identity homomorphism of $\pi_1(X,x)$, which is the trivial group by hypothesis; hence $i_*$ is trivial. This is the condition at $x$, and $x$ was arbitrary. Therefore $X$ is semilocally simply connected.

:::
