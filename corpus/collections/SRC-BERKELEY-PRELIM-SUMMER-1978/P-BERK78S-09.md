---
schema: qual/card@1
id: P-BERK78S-09
kind: problem
title: Attainment of distance between subsets of a metric space
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained PDF was checked directly. Parts 1 and 2 are false as printed for an arbitrary metric space; closed subsets need not contain nearest points. The card preserves the source statement rather than silently adding a properness or compactness hypothesis.
---

:::{.problem}
Let $X,Y$ be nonempty subsets of a metric space $M$, and define
\[
d(X,Y)=\inf\{d(x,y):x\in X,\ y\in Y\}.
\]

1. Suppose $X=\{x\}$ consists of one point and $Y$ is closed. Prove that
   \[
   d(X,Y)=d(x,y)
   \]
   for some $y\in Y$.
2. Suppose $X$ is compact and $Y$ is closed. Prove that
   \[
   d(X,Y)=d(x,y)
   \]
   for some $x\in X$ and $y\in Y$.
3. Give an example showing that the conclusion of part 2 can fail if $X$ and $Y$ are closed but not compact.
:::
