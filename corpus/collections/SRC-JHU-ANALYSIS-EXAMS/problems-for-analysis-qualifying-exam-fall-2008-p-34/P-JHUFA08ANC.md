---
schema: qual/card@1
id: P-JHUFA08ANC
kind: problem
title: "Separability of the Banach space l-infinity"
classification:
  areas:
  - real-analysis
  topics:
  - Banach Spaces
  - Separability
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the JHU Analysis Qualifying Exam, Fall 2008, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Is the Banach space $\ell^\infty$ of bounded complex sequences, with the supremum norm, separable? Prove your answer.
:::

::: {.solution}
No. The space $\ell^\infty$ is not separable.

For each subset $A\subset\mathbb N$, let $x^A\in\ell^\infty$ be its characteristic sequence:
\[
x^A_n=\begin{cases}1,&n\in A,\\0,&n\notin A.\end{cases}
\]
If $A\ne B$, then for some $n$ exactly one of $A,B$ contains $n$, so
\[
\|x^A-x^B\|_\infty=1.
\]
Thus
\[
\{x^A:A\subset\mathbb N\}
\]
is an uncountable subset of $\ell^\infty$ whose distinct points are pairwise distance $1$.

If $\ell^\infty$ were separable, let $D$ be a countable dense subset. The open balls
\[
B(x^A,1/3)
\]
are pairwise disjoint, and density would require each such ball to contain a point of $D$. This would inject the uncountable power set $\mathcal P(\mathbb N)$ into the countable set $D$, a contradiction. Therefore $\ell^\infty$ is not separable.
:::
