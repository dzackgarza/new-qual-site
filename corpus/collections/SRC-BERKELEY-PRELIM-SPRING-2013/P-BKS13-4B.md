---
schema: qual/card@1
id: P-BKS13-4B
kind: problem
title: Cauchy estimate for derivatives on a compact subset
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $U$ be an open subset of $\mathbb C$.
Let $K$ be a closed bounded subset of $\mathbb C$ that is contained in $U$.
Put
\[
D=\min_{p\in K,\ q\notin U}|p-q|.
\]
That is, $D$ is the closest distance between $K$ and $\mathbb C\setminus U$.
(If $U=\mathbb C$, then we put $D=\infty$.)

Suppose that $f$ is an analytic function on $U$ so that for all $z\in U$, we have $|f(z)|\le M$.
Here $M$ is a fixed positive number.
Find an explicit number $C<\infty$, depending on $M$ and $D$, so that for all $z_0\in K$ we have $|f'(z_0)|\le C$.
Justify your answer.
:::
