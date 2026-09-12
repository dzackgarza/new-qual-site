---
schema: qual/card@1
id: P-RAF10D
kind: problem
title: "Continuous functions in a closed subspace of L^2 are bounded in L^infinity"
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
  note: Checked against Problem 4 of the official UCSD Fall 2010 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $Y$ be a closed subspace of $L^2([0,1])$ each of whose elements may be represented by a continuous function on $[0,1]$.
Prove that there exists $C > 0$ so that
$$
\|f\|_{L^\infty([0,1])} \leq C \|f\|_{L^2([0,1])}
$$
for all $f \in Y$.
:::

::: solution
<1>1. The continuous representative is unique.
::: proof
If two continuous functions on $[0,1]$ agree almost everywhere, then their difference is continuous and vanishes almost everywhere. If it were nonzero at some point, continuity would make it nonzero on an interval of positive measure, a contradiction. Hence every element of $Y$ has a unique continuous representative.
:::

<1>2. Define the representative map and prove its graph is closed.
::: proof
Because $Y$ is a closed subspace of the Banach space $L^2([0,1])$, $Y$ is itself Banach. Define
\[
T:Y\to C([0,1]),
\]
where $T(f)$ is the unique continuous representative of the $L^2$ class $f$.

Suppose
\[
f_n\to f\quad\text{in }L^2
\]
and
\[
T(f_n)\to g\quad\text{uniformly on }[0,1].
\]
Uniform convergence implies convergence in $L^2$, so
\[
T(f_n)\to g\quad\text{in }L^2.
\]
But $T(f_n)$ represents the same $L^2$ class as $f_n$, and $f_n\to f$ in $L^2$. Uniqueness of limits in $L^2$ gives
\[
g=f\quad\text{a.e.}
\]
Since $g$ is continuous, it is exactly the continuous representative of $f$. Thus
\[
g=T(f).
\]
Therefore the graph of $T$ is closed.
:::

<1>3. Apply the Closed Graph Theorem.
::: proof
Both $Y$ and $C([0,1])$ are Banach spaces. By Step 2, the linear map
\[
T:Y\to C([0,1])
\]
has closed graph. Hence the Closed Graph Theorem gives a constant $C>0$ such that
\[
\|T(f)\|_\infty\le C\|f\|_2
\qquad(f\in Y).
\]
Since $T(f)$ is the continuous representative of $f$,
\[
\boxed{
\|f\|_{L^\infty([0,1])}
\le C\|f\|_{L^2([0,1])}.}
\]
:::
:::
