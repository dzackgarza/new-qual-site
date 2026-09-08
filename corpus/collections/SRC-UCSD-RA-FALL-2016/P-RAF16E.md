---
schema: qual/card@1
id: P-RAF16E
kind: problem
title: "Sequentially compact implies countably compact"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the official UCSD Fall 2016 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $X$ be a topological space.
Suppose it is sequentially compact (i.e., any sequence has a convergent subsequence).
Prove that it is countably compact (i.e., any countable open cover of $X$ has a finite subcover).
:::

::: solution
<1>1. Assume a countable open cover has no finite subcover.
::: proof
Let
\[
X=\bigcup_{n=1}^\infty U_n
\]
be a countable open cover. Suppose, for contradiction, that no finite subfamily covers $X$. Then for each $n$ choose
\[
x_n\in X\setminus\bigcup_{j=1}^n U_j.
\]
:::

<1>2. Use sequential compactness.
::: proof
By sequential compactness, some subsequence $(x_{n_k})$ converges to a point $x\in X$. Since the $U_j$ cover $X$, choose $m$ with
\[
x\in U_m.
\]
Because $U_m$ is open and $x_{n_k}\to x$, there exists $K$ such that
\[
x_{n_k}\in U_m
\]
for every $k\ge K$.

On the other hand, for all sufficiently large $k$ we have $n_k\ge m$, and by construction
\[
x_{n_k}\notin\bigcup_{j=1}^{n_k}U_j,
\]
so in particular $x_{n_k}\notin U_m$. This is a contradiction.

Therefore every countable open cover has a finite subcover, and
\[
\boxed{X\text{ is countably compact}.}
\]
:::
:::
