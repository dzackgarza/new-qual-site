---
schema: qual/card@1
id: P-CASP20D
kind: problem
title: "Fixed points of analytic self-maps and the role of the complement"
classification:
  areas:
  - complex-analysis
  topics:
  - Fixed Points
  - Conformal Maps
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $G \subset \mathbb{C}$ be a proper open connected subset.
Let $\mathbb{C}_\infty = \mathbb{C} \cup \{\infty\}$ denote the extended plane.

(i) Assume $\mathbb{C}_\infty \setminus G$ is connected.
Prove: Let $f$ be an analytic function from $G$ to $G$ which is not the identity map.
Then $f$ has at most one fixed point in $G$.

(ii) Is the statement still true if $\mathbb{C}_\infty \setminus G$ is not connected?
If true, give a proof.
If false, give a counterexample.
:::

::: {.solution}
For (i), connectedness of $\mathbb C_\infty\setminus G$ is equivalent to
simple connectedness of the proper plane domain $G$. Choose a Riemann map
$\phi:G\to\mathbb D$. If $f$ had two distinct fixed points, then
\[
F=\phi\circ f\circ\phi^{-1}
\]
would be a nonidentity disk self-map with two fixed points in $\mathbb D$.
Conjugating one fixed point to $0$ and applying Schwarz's lemma shows that a
disk self-map with two interior fixed points is the identity. Hence $f$ would
be the identity, a contradiction. Therefore a nonidentity self-map has at most
one fixed point.

For (ii), the statement is false. Take
\[
G=\{z:1/2<|z|<2\}
\]
and
\[
f(z)=\frac1z.
\]
Then $f$ maps $G$ biholomorphically to itself, is not the identity, and fixes
both $1$ and $-1$. The complement of $G$ in the sphere has two components.
:::
