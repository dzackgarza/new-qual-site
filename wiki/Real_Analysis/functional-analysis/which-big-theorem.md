---
title: Which big theorem?
order: 0
problems:
  topics:
  - Functional Analysis
  - Banach Spaces
---

# Which big theorem?

Four theorems carry the subject, and each is triggered by a different hypothesis.

| You have | Use | You get |
| --- | --- | --- |
| a pointwise bound on a family of operators | uniform boundedness | a uniform bound |
| a bounded bijection | open mapping, or bounded inverse | the inverse is bounded |
| a closed graph | closed graph | the operator is bounded |
| a bounded functional on a subspace | Hahn--Banach | an extension of the same norm |

The first three all need completeness, and are all Baire category arguments; Hahn--Banach needs none and is a Zorn argument, which is why it works on normed spaces with no completeness at all.

## The tells

- **"$\sup_n \norm{T_n x} < \infty$ for each $x$"** is uniform boundedness, always.
  The standard consequence is that a pointwise limit of bounded operators is bounded.

- **"$T$ is a continuous bijection"** is the open mapping theorem, and the conclusion worth remembering is the bounded inverse theorem: a bounded bijection between Banach spaces has bounded inverse, with no separate proof.

- **"Whenever $x_n \to x$ and $Tx_n\to y$, then $y = Tx$"** is the closed graph theorem, which weakens what must be checked: convergence of $Tx_n$ is assumed rather than proved.

- **"Extend without increasing the norm"**, or "there exists a functional with $f(x) = \norm x$", is Hahn--Banach.
  Its most used corollary is that the dual separates points, which is what makes weak topologies useful.

## In Hilbert space, use the projection instead

None of the four is needed for most Hilbert space problems: orthogonal projection onto a closed subspace exists, the Riesz representation theorem identifies the dual, and Parseval turns a norm into a sum of coefficients.
Reach for the big four only when the space is Banach and not Hilbert, since the Hilbert tools are stronger and cheaper.
