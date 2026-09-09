---
schema: qual/card@1
id: P-JWPJ5
kind: problem
title: Number of irreducible representations of $S_n$
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Partitions
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
(1) How many non-isomorphic irreducible complex representations does the symmetric group $S_n$ have?
(2) What classical function in mathematics does this number equal, and how are the irreducible representations explicitly indexed?
:::

::: solution
For a finite group over $\mathbb C$, the number of isomorphism classes of irreducible representations equals the number of conjugacy classes. In $S_n$, two permutations are conjugate exactly when they have the same cycle type.

A cycle type is precisely a partition
\[
\lambda=(\lambda_1\ge\cdots\ge\lambda_r)\vdash n.
\]
Hence the conjugacy classes of $S_n$ are indexed by partitions of $n$, so
\[
|\operatorname{Irr}(S_n)|=p(n),
\]
where $p(n)$ is the integer partition function.

More precisely, the irreducible complex representations are the Specht modules
\[
S^\lambda,\qquad \lambda\vdash n.
\]
Their dimensions are given by the hook-length formula
\[
\dim S^\lambda=\frac{n!}{\prod_{u\in\lambda} h(u)}.
\]
Thus the partitions of $n$ simultaneously index the conjugacy classes and the irreducible complex representations of $S_n$.
:::
