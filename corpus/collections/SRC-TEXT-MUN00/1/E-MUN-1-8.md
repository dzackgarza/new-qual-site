---
schema: qual/card@1
id: E-MUN-1-8
kind: problem
title: Power set of a finite set
classification:
  areas:
  - topology
  topics:
  - Fundamental Concepts
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 1, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

If a set $A$ has two elements, show that $\mathcal{P}(A)$ has four elements.
How many elements does $\mathcal{P}(A)$ have if $A$ has one element?
Three elements?
No elements?
Why is $\mathcal{P}(A)$ called the power set of $A$ ?
:::

::: {.solution}
If \(A=\{a,b\}\), then its subsets are exactly
\[
\varnothing,\qquad \{a\},\qquad \{b\},\qquad \{a,b\},
\]
so \(|\mathcal P(A)|=4\).

In general, if \(|A|=n\), then each element of \(A\) has two independent choices when specifying a subset: include it or omit it. Hence
\[
|\mathcal P(A)|=2^n.
\]
Therefore:
\[
\begin{array}{c|c}
|A|&|\mathcal P(A)|\\ \hline
0&1\\
1&2\\
2&4\\
3&8
\end{array}
\]
The name *power set* reflects precisely this formula: its cardinality is the power \(2^{|A|}\) when \(A\) is finite.
:::
