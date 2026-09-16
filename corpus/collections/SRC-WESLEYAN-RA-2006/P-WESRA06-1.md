---
schema: qual/card@1
id: P-WESRA06-1
kind: problem
title: Cauchy sequences, completeness, and Baire category
classification:
  areas: [real-analysis]
  topics: [Metric Spaces, Baire Category]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis Problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $(X,d)$ be a metric space.

1. Define a Cauchy sequence in $(X,d)$.

2. Prove that every convergent sequence in $(X,d)$ is Cauchy.

3. Define completeness of $(X,d)$.

4. State one form of Baire's category theorem.
:::

::: {.solution}
<1>1. Cauchy sequences.
::: {.proof}
A sequence $(x_n)$ in $X$ is Cauchy if for every $\varepsilon>0$ there exists $N$ such that
\[
m,n\ge N\quad\Longrightarrow\quad d(x_m,x_n)<\varepsilon.
\]
:::

<1>2. Every convergent sequence is Cauchy.
::: {.proof}
Suppose $x_n\to x\in X$.
Given $\varepsilon>0$, choose $N$ such that
\[
n\ge N\quad\Longrightarrow\quad d(x_n,x)<\frac\varepsilon2.
\]
Then for $m,n\ge N$, the triangle inequality gives
\[
d(x_m,x_n)\le d(x_m,x)+d(x,x_n)<\varepsilon.
\]
Hence $(x_n)$ is Cauchy.
:::

<1>3. Completeness.
::: {.proof}
The metric space $(X,d)$ is complete if every Cauchy sequence in $X$ converges to a point of $X$.
:::

<1>4. Baire category theorem.
::: {.proof}
One standard form is: if $(X,d)$ is a nonempty complete metric space and $U_1,U_2,\ldots$ are open dense subsets of $X$, then
\[
\bigcap_{n=1}^\infty U_n
\]
is dense in $X$.

Equivalently, a nonempty complete metric space cannot be written as a countable union of closed sets with empty interior.
:::
:::
