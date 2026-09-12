---
schema: qual/card@1
id: P-BKF08-3A
kind: problem
title: Berkeley Fall 2008 prelim problem 3A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 3A of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf.
---

::: {.problem}
Find the eigenvalues of the $n\times n$ matrix $(a_{ij})$, where $n>2$, defined by
\[
a_{ij}=\begin{cases}
1,&j-i\equiv1\pmod n,\\
-1,&j-i\equiv-1\pmod n,\\
0,&\text{otherwise}.
\end{cases}
\]

*Hint.* Find sequences $(b_i)$ and complex numbers $z$ such that
\[
(z-z^{-1})b_i=b_{i+1}-b_{i-1},\qquad b_i=b_{i+n}
\]
for all integers $i$.
:::
