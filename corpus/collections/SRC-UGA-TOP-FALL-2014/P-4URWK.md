---
schema: qual/card@1
id: P-4URWK
kind: problem
title: 'Hausdorffness of arbitrary products'
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Checked the statement against problem 2 of the official UGA Fall 2014 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Verified that one coordinate separating two distinct product points suffices for arbitrary, including infinite, products.
---

::: {.problem}
Is every product (finite or infinite) of Hausdorff spaces Hausdorff?
If yes, prove it.
If no, give a counterexample.
:::

::: {.solution}

::: pf

::: pf-step

Yes.
Let
\[
X=\prod_{i\in I}X_i
\]
with the product topology, where every $X_i$ is Hausdorff.

::: pf-proof

We will verify the Hausdorff separation condition directly.
The argument does not require the index set $I$ to be finite.

:::

:::

::: {.pf-step #s2}

Let
\[
x=(x_i)_{i\in I},
\qquad
y=(y_i)_{i\in I}
\]
be distinct points of $X$.
Then there is an index $j\in I$ such that
\[
x_j\ne y_j.
\]

::: pf-proof

Two elements of a Cartesian product are equal exactly when all of their coordinates are equal.
Since $x\ne y$, at least one coordinate differs.

:::

:::

::: pf-step

There are disjoint open sets $U_j,V_j\subseteq X_j$ with
\[
x_j\in U_j,
\qquad
y_j\in V_j.
\]

::: pf-proof

The factor $X_j$ is Hausdorff and $x_j\ne y_j$ by step [](#s2){.pf-ref}. Hence the Hausdorff condition in $X_j$ supplies disjoint open neighborhoods $U_j$ and $V_j$.

:::

:::

::: {.pf-step #s4}

The sets
\[
U=\pi_j^{-1}(U_j),
\qquad
V=\pi_j^{-1}(V_j)
\]
are disjoint open neighborhoods of $x$ and $y$ in $X$.

::: pf-proof

The coordinate projection
\[
\pi_j:X\to X_j
\]
is continuous by the definition of the product topology.
Thus $U$ and $V$ are open.
Moreover,
\[
x\in U,
\qquad
y\in V.
\]
Finally,
\[
U\cap V
=
\pi_j^{-1}(U_j\cap V_j)
=
\pi_j^{-1}(\varnothing)
=
\varnothing.
\]

:::

:::

::: pf-step

Therefore every product of Hausdorff spaces is Hausdorff.

::: pf-proof

By step [](#s4){.pf-ref}, every pair of distinct points of $X$ has disjoint open neighborhoods.
This is precisely the Hausdorff property.
The proof uses only one coordinate, so it applies unchanged to arbitrary infinite products.
For the empty product, the product space is a singleton and hence Hausdorff as well.

:::

:::

:::

:::
