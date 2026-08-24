---
schema: qual/card@1
id: P-WAI3F
kind: problem
title: The antipodal map on $S^n$ is homotopic to the identity when $n$ is odd
classification:
  areas:
  - topology
  topics:
  - Degree
  - Homotopy
relations: []
review: draft
---

::: problem
3. **Main Idea**: Linear homotopy fails continuity without the condition from (2), so use complex embedding to avoid the origin at $t=1/2$.

Suppose $n$ is odd and define $f:S^n \to S^n$ to be the antipodal map.
Since $n+1$ is even, we have $n+1 =2m$ for some $m\in \NN$, so identify $S^n = S^{2m-1} \subset \RR^{2m} \cong\CC^m$

Then $z\in S^n$ can be written as a vector $z \in \CC^m$ such that $\norm{z} = 1$.

Then define $P: \CC^m \to \CC^m$ by $P(z) = z/\abs{z}$, the projection onto the complex unit sphere, and define $H: \CC^m \cross I \to \CC^m$ by $H(z, t) = P(e^{i\pi t}z)$.

This is a homotopy, since $H(z, 0) = P(z) = z$ (since $\norm{z} = 1$), so this is the identity map.
We also have $H(z, 1) = P(-z) = -z$, the antipodal map.

This is well-defined, since $e^{i\pi t} > 0$ and $z \neq 0$, so the linear homotopy in ambient $\CC^m$ avoids the origin and thus the denominator when taking the projection is never zero.
:::
