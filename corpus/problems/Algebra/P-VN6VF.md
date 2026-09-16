---
schema: qual/card@1
id: P-VN6VF
kind: problem
title: Example of a UFD that is not a Euclidean domain
classification:
  areas:
  - algebra
  topics:
  - Euclidean Domains
  - Factorization
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
Give an example of a UFD that is not a Euclidean domain.
:::

::: {.solution}
Let $k$ be a field. Then
\[
k[x,y]
\]
is a UFD but not a Euclidean domain.

First, $k[x]$ is a PID and hence a UFD. By Gauss's lemma, a polynomial ring over a UFD is again a UFD, so
\[
k[x,y]=k[x][y]
\]
is a UFD.

On the other hand, $k[x,y]$ is not a PID. The ideal
\[
(x,y)
\]
is not principal: if
\[
(x,y)=(f),
\]
then $f$ divides both $x$ and $y$. Since $x$ and $y$ have no common nonunit divisor, $f$ must be a unit, which would give
\[
(x,y)=k[x,y],
\]
contradicting $1\notin(x,y)$.

Every Euclidean domain is a PID. Since $k[x,y]$ is not a PID, it cannot be Euclidean.
:::
