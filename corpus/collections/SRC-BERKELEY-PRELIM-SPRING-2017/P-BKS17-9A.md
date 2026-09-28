---
schema: qual/card@1
id: P-BKS17-9A
kind: problem
title: Bell numbers grow slower than $n!$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in P_n/n! -> 0 and inline-math spacing against Sp17_Exam_0.pdf page 10 problem 9A.
---

::: {.problem}
The Bell number $P_n$ is the number of partitions of a set of $n$ elements into disjoint nonempty subsets, so for example $\{1, 2, 3\} = \{1\} \cup \{2\} \cup \{3\} = \{1, 2\} \cup \{3\} = \{2, 3\} \cup \{1\} = \{1, 3\} \cup \{2\}$ and $P_3 = 5$. Show that

$$
\frac{P_n}{n!} \to 0
$$

as $n \to \infty$.
:::
