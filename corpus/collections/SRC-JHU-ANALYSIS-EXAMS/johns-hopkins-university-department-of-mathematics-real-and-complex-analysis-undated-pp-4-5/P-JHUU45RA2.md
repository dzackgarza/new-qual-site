---
schema: qual/card@1
id: P-JHUU45RA2
kind: problem
title: 'Unit ball of $L^2$ is not compact'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against entry 2 of the undated JHU Real and Complex Analysis exam on pp. 4–5 of the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Prove that the unit ball of $L^2([0,1])$, with its norm topology, is not compact.
:::

::: {.solution}
For $n\ge1$, define
\[
e_n(x)=\sqrt2\sin(n\pi x),\qquad 0\le x\le1.
\]
The functions $(e_n)$ are orthonormal in $L^2([0,1])$, so
\[
\|e_n\|_2=1
\]
for every $n$. Thus every $e_n$ lies in the closed unit ball.

If $m\ne n$, orthogonality gives
\[
\|e_n-e_m\|_2^2
=\|e_n\|_2^2+\|e_m\|_2^2-2\operatorname{Re}\langle e_n,e_m\rangle
=2.
\]
Hence
\[
\|e_n-e_m\|_2=\sqrt2
\qquad(m\ne n).
\]
Therefore the sequence $(e_n)$ has no Cauchy subsequence, and hence no norm-convergent subsequence. A compact metric space is sequentially compact, so the closed unit ball of $L^2([0,1])$ is not compact.
:::
