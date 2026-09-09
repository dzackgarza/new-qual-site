---
schema: qual/card@1
id: E-AMD-DI5UYFIZ
kind: problem
title: $-1$ is the unique element of order $2$ in the quaternion group
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Group Presentations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that the Quaternion group has only one element of order 2, namely $-1$.
:::

::: solution
The quaternion group is
\[
Q_8=\{\pm1,\pm i,\pm j,\pm k\},
\]
with
\[
i^2=j^2=k^2=-1.
\]
Now
\[
(-1)^2=1,
\]
and \(-1\ne1\), so \(-1\) has order \(2\).

For each \(u\in\{i,j,k\}\),
\[
(\pm u)^2=u^2=-1\ne1,
\qquad
(\pm u)^4=1.
\]
Hence each of \(\pm i,\pm j,\pm k\) has order \(4\). The identity has order \(1\).

Therefore the only element of order \(2\) is
\[
\boxed{-1}.
\]
:::
