---
schema: qual/card@1
id: P-BKS84-8
kind: problem
title: A linear system with a trajectory decaying forward and diverging backward
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

:::{.problem}
Show that the system
\[
\frac d{dt}\begin{pmatrix}x\\y\\z\end{pmatrix}
=
\begin{pmatrix}
0&1&0\\
2&0&0\\
0&0&3
\end{pmatrix}
\begin{pmatrix}x\\y\\z\end{pmatrix}
\]
has a solution whose norm tends to $\infty$ as $t\to-\infty$ and tends to $0$ as $t\to+\infty$.
:::
