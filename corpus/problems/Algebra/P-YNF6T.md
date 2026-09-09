---
schema: qual/card@1
id: P-YNF6T
kind: problem
title: Proper subgroups of a group of order $pq$ are cyclic
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Cyclic Groups
  - Cosets and Lagrange
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
Suppose $|G| = pq$ with $p, q \geq 2$ prime, and let $H \le G$ be a proper subgroup.
Prove that $H$ must be cyclic.
:::

::: solution
By Lagrange's theorem,
\[
|H|\mid pq.
\]
Since $H$ is proper,
\[
|H|\in\{1,p,q\}.
\]
The trivial group is cyclic. If $|H|$ is prime, choose $h\in H$ with $h\neq e$. Then the order of $h$ divides $|H|$ and is greater than $1$, hence equals $|H|$. Therefore
\[
H=\langle h\rangle.
\]
Thus every proper subgroup of $G$ is cyclic.
:::
