---
schema: qual/card@1
id: P-AMD-YAKYTEPB
kind: problem
title: The torsion elements of an abelian group form a subgroup
classification:
  areas:
  - algebra
  topics:
  - Torsion
  - Abelian Groups
  - Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked the card against the source-audited UCSD Math 200A Fall 2016 Homework 1 collection occurrence. The live provenance PDF endpoint timed out during this review, so no claim is made of a fresh PDF comparison. Independently corroborated the theorem in the Encyclopedia of Mathematics and standard algebra notes.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Verified the subgroup criterion directly: the identity has finite order, inverses preserve finite order, and if x^m=y^n=e then abelianness yields (xy)^(mn)=e.
---

::: {.problem}
Given: $G\in \mathbf{Ab}$

Show: $T(G) \leq G$ (where $T(G) = \{ g\in G : |g| < \infty\}$
:::

::: {.solution}
Let
\[
T(G)=\{g\in G:o(g)<\infty\}.
\]
We verify the subgroup conditions.

<1>1. The identity belongs to $T(G)$.
::: {.proof}
The identity has order $1$, hence finite order.
Therefore
\[
e\in T(G).
\]
:::

<1>2. If $x\in T(G)$, then $x^{-1}\in T(G)$.
::: {.proof}
Since $x$ has finite order, there is an integer $m\ge1$ such that
\[
x^m=e.
\]
Taking inverses gives
\[
(x^{-1})^m=(x^m)^{-1}=e.
\]
Thus $x^{-1}$ has finite order, so
\[
x^{-1}\in T(G).
\]
:::

<1>3. If $x,y\in T(G)$, then $xy\in T(G)$.
::: {.proof}
Choose positive integers $m,n$ such that
\[
x^m=e,
\qquad
y^n=e.
\]
Because $G$ is abelian,
\[
(xy)^{mn}=x^{mn}y^{mn}.
\]
But
\[
x^{mn}=(x^m)^n=e
\]
and
\[
y^{mn}=(y^n)^m=e.
\]
Hence
\[
(xy)^{mn}=e.
\]
Therefore $xy$ has finite order and belongs to $T(G)$.
:::

<1>4. Hence $T(G)$ is a subgroup of $G$.
::: {.proof}
By <1>1, $T(G)$ is nonempty; by <1>2 and <1>3, it is closed under inverses and products.
Therefore
\[
T(G)\le G.
\]
:::
:::
