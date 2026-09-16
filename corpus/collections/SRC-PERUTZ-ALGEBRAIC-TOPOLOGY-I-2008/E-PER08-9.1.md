---
schema: qual/card@1
id: E-PER08-9.1
kind: problem
title: Euler characteristic of a chain complex and of an exact sequence
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Completed from the retained Perutz Algebraic Topology I source and checked against the stated hypotheses.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retyped the mathematics against Exercise 9.1 of the Perutz 2008 notes.
---

::: {.problem}
We consider chain complexes $(C_*,\delta)$ over a field $k$ such that $\dim_kH_*(C)<\infty$.
The Euler characteristic of $C_*$ is then defined as the alternating sum
\[
\chi(C_*)=\sum_p(-1)^p\dim_kH_p(C).
\]

(i) Show that when $\sum_p\dim_kC_p<\infty$, one has $\chi(C_*)=\sum_p(-1)^p\dim_kC_p$.

(ii) Show that if
\[
\cdots\to C_p\to C_{p-1}\to C_{p-2}\to\cdots
\]
is an exact sequence, and $\sum_p\dim C_p<\infty$, then $\sum_p(-1)^p\dim C_p=0$.
:::

::: {.solution}
Let $Z_p=\ker(d_p)$ and $B_p=\operatorname{im}(d_{p+1})$.

<1>1. Euler characteristic of a finite-dimensional chain complex equals the alternating sum of chain dimensions.
::: {.proof}
There are short exact sequences
\[
0\to Z_p\to C_p\to B_{p-1}\to0,
\qquad
0\to B_p\to Z_p\to H_p\to0.
\]
Hence
\[
\dim C_p=\dim H_p+\dim B_p+\dim B_{p-1}.
\]
Multiply by $(-1)^p$ and sum.
The two boundary sums cancel after shifting the index, giving
\[
\sum_p(-1)^p\dim C_p=\sum_p(-1)^p\dim H_p=\chi(C_*).
\]
:::

<1>2. The alternating sum of dimensions in a finite exact sequence is zero.
::: {.proof}
Regard the exact sequence as a chain complex.
Its homology vanishes in every degree, so <1>1 gives
\[
\sum_p(-1)^p\dim C_p=0.
\]
:::
:::
