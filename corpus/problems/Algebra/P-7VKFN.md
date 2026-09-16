---
schema: qual/card@1
id: P-7VKFN
kind: problem
title: The quaternion group and the number of elements of each order
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Group Presentations
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
What is the quaternion group $Q_8$? Give its presentation and list the number of elements of each order.
:::

::: {.solution}
The quaternion group is
\[
Q_8=\{\pm1,\pm i,\pm j,\pm k\},
\]
with multiplication determined by
\[
i^2=j^2=k^2=ijk=-1.
\]
Equivalently,
\[
Q_8=\langle i,j\mid i^4=1,\ i^2=j^2,\ jij^{-1}=i^{-1}\rangle.
\]

The element orders are immediate from the relations:
\[
\operatorname{ord}(1)=1,\qquad \operatorname{ord}(-1)=2,
\]
and each of \(\pm i,\pm j,\pm k\) squares to \(-1\), so each has order \(4\). Thus the counts are
\[
\begin{array}{c|ccc}
\text{order}&1&2&4\\\hline
\text{number of elements}&1&1&6.
\end{array}
\]
In particular, \(-1\) is the unique involution of \(Q_8\).
:::
