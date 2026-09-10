---
schema: qual/card@1
id: E-UB4PP
kind: problem
title: Extending cos(1/x) by enlarging the compactification
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Show that the bounded continuous function $g: (0, 1) \to \mathbb{R}$ defined by $g(x) = \cos(1/x)$ cannot be extended to the compactification of Example 3 of §38. Define an imbedding $h: (0, 1) \to [0, 1]^3$ such that the functions $x$, $\sin(1/x)$, and $\cos(1/x)$ are all extendable to the compactification induced by $h$.
:::

::: {.solution}
In Example 3 the compactification is the closure of
\[
e:(0,1)\longrightarrow [0,1]\times[-1,1],
\qquad e(x)=(x,\sin(1/x)).
\]
Suppose \(g(x)=\cos(1/x)\) extended continuously to this compactification. For
\[
x_n=\frac1{n\pi}
\]
we have
\[
e(x_n)=\left(\frac1{n\pi},0\right)\longrightarrow(0,0),
\]
but
\[
g(x_n)=\cos(n\pi)=(-1)^n
\]
has no limit. This contradicts continuity at \((0,0)\). Hence \(g\) does not extend.

Now define
\[
h:(0,1)\longrightarrow [0,1]\times[-1,1]\times[-1,1],
\qquad
h(x)=\bigl(x,\sin(1/x),\cos(1/x)\bigr).
\]
The first coordinate recovers \(x\), so \(h\) is injective; its inverse on \(h((0,1))\) is the restriction of the first-coordinate projection. Hence \(h\) is an embedding.

Let
\[
Y=\overline{h((0,1))}\subset [0,1]\times[-1,1]^2.
\]
The ambient cube is compact Hausdorff, so \(Y\) is a compactification of \((0,1)\). The three coordinate projections \(\pi_1,\pi_2,\pi_3\) are continuous on \(Y\), and on \(h((0,1))\) they restrict respectively to
\[
x,\qquad \sin(1/x),\qquad \cos(1/x).
\]
Thus all three functions extend continuously to the compactification induced by \(h\).
:::
