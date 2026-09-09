---
schema: qual/card@1
id: P-JHUFA11ANE
kind: problem
title: 'An $L^2$-bounded sequence in $L^2$ of the line without convergent subsequences'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the JHU Analysis Qualifying Exam, September 2011, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Give a sequence $(f_j)$ in $L^2(\mathbb R)$ such that $\|f_j\|_2=1$ for every $j$, but $(f_j)$ has no norm-convergent subsequence.
:::

::: {.solution}
For $j\ge1$, let
\[
f_j=\mathbf1_{[j,j+1]}.
\]
Then
\[
\|f_j\|_2^2=\int_j^{j+1}1\,dx=1.
\]
If $j\ne k$, the supports are disjoint, so
\[
\|f_j-f_k\|_2^2
=\|f_j\|_2^2+\|f_k\|_2^2
=2.
\]
Thus distinct terms are always distance $\sqrt2$ apart. In particular, no subsequence can be Cauchy in $L^2(\mathbb R)$, and therefore no subsequence can converge in norm.
:::
