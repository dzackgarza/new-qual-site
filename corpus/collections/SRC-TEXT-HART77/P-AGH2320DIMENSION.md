---
schema: qual/card@1
id: P-AGH2320DIMENSION
kind: problem
title: Dimension of an integral scheme of finite type over a field
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dimension Theory
  - Function Fields
  - Codimension
relations: []
review: draft
---

::: problem
Let $X$ be an integral scheme of finite type over a field $k$, not necessarily algebraically closed.
Prove the following, where for rings $\krulldim$ always means the Krull dimension.

a. For any closed point $P \in X$, $\krulldim X = \krulldim \OO_P$.

b. Let $K(X)$ be the function field of $X$.
Then
\[
\krulldim X = \trdeg\qty{K(X)/k}.
\]

c. If $Y$ is a closed subset of $X$, then
\[
\codim(Y, X) = \inf \ts{\krulldim \OO_{P, X} \st P \in Y}.
\]

d. If $Y$ is a closed subset of $X$, then
\[
\krulldim Y + \codim(Y, X) = \krulldim X.
\]

e. If $U$ is a nonempty open subset of $X$, then $\krulldim U = \krulldim X$.

f. If $k \subseteq k'$ is a field extension, then every irreducible component of $X' = \fiberprod{X}{k}{k'}$ has dimension equal to $\krulldim X$.
:::
