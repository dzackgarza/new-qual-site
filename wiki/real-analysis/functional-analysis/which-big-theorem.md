---
title: Which big theorem?
order: 0
problems:
  topics:
  - Functional Analysis
  - Banach Spaces
---

# Which big theorem?

Choose by hypothesis:

| You have | Use | You get |
| --- | --- | --- |
| a pointwise bound on a family of operators | uniform boundedness | a uniform bound |
| a bounded bijection | open mapping, or bounded inverse | the inverse is bounded |
| a closed graph | closed graph | the operator is bounded |
| a bounded functional on a subspace | Hahn--Banach | an extension of the same norm |

The first three require completeness and come from Baire category.
Hahn--Banach is a Zorn argument and holds on normed spaces without a completeness hypothesis.

## The tells

- **"$\sup_n \norm{T_n x} < \infty$ for each $x$"** is uniform boundedness, always.
  The standard consequence is that a pointwise limit of bounded operators is bounded.

- **"$T$ is a continuous bijection"** is the open mapping theorem.
  The bounded inverse theorem is the immediate consequence: a bounded bijection between Banach spaces has bounded inverse.

- **"Whenever $x_n \to x$ and $Tx_n\to y$, then $y = Tx$"** is the closed graph theorem, which weakens what must be checked: convergence of $Tx_n$ is assumed rather than proved.

- **"Extend without increasing the norm"**, or "there exists a functional with $f(x) = \norm x$", is Hahn--Banach.
  Its most used corollary is that the dual separates points; in particular, the weak topology is Hausdorff.

## In Hilbert space, use the projection instead

None of the four is needed for most Hilbert space problems: orthogonal projection onto a closed subspace exists, the Riesz representation theorem identifies the dual, and Parseval turns a norm into a sum of coefficients.
Reach for the big four only when the space is Banach and not Hilbert, since the Hilbert tools are stronger and cheaper.
