---
schema: qual/card@1
id: E-PBT3I
kind: problem
title: Products of closed sets are closed
classification:
  areas:
  - topology
  topics:
  - Closed Sets
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 3, printed p. 100, with the product
    topology of §15 and Theorem 17.1 on printed p. 95; the stored statement is the printed
    sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 17.3, PDF p. 6. The complement of A x B is the
    union of (X - A) x Y and X x (Y - B), which are product basis elements because A and B
    are closed. (tmp/sources/munkres-solutions-positron-ch2.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into STYLE-08: the complement identity, then closedness of $A\times B$. Re-checked that $X-A$ and $Y-B$ are open and that a product of open sets is a basis element of the product topology (printed p. 86). No statement change.
---

::: {.exercise}

Show that if $A$ is closed in $X$ and $B$ is closed in $Y$, then $A \times B$ is closed in $X \times Y$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 17.3, PDF p. 6** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the argument is theirs. Whitman's printed p. 159 has the same proof, with the identity below verified pointwise.

::: pf

::: {.pf-step #diff}

$X\times Y-A\times B=\big((X-A)\times Y\big)\cup\big(X\times(Y-B)\big)$.

::: pf-proof

A point $(x,y)\in X\times Y$ lies in $A\times B$ exactly when $x\in A$ and $y\in B$. Negating, $(x,y)$ lies outside $A\times B$ exactly when $x\notin A$ or $y\notin B$, that is exactly when $(x,y)\in(X-A)\times Y$ or $(x,y)\in X\times(Y-B)$.

:::

:::

::: pf-step

$A\times B$ is closed in $X\times Y$.

::: pf-proof

Since $A$ is closed in $X$, the set $X-A$ is open in $X$, so $(X-A)\times Y$ is a basis element of the product topology on $X\times Y$ and hence open; since $B$ is closed in $Y$, likewise $X\times(Y-B)$ is open. By step [](#diff){.pf-ref} the complement of $A\times B$ is the union of these two open sets, hence open, so $A\times B$ is closed in $X\times Y$.

:::

:::

:::
:::
