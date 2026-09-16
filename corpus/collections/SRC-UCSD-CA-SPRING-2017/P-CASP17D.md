---
schema: qual/card@1
id: P-CASP17D
kind: problem
title: Entire and meromorphic functions with prescribed zeros, poles, and residues
classification:
  areas:
  - complex-analysis
  topics:
  - Weierstrass Theorem
  - Mittag-Leffler Theorem
  - Entire Functions
  - Meromorphic Functions
relations: []
review: draft
---

::: {.problem}
(i) Construct an entire function with simple zeros at $\left\{\sqrt{n} + \frac{1}{\sqrt{n}} : n = 1, 2, \ldots\right\}$ and no other zeroes.

(ii) Construct a meromorphic function with simple poles at $z = n\sqrt{n}$ and residues equal to $\sqrt{n}$ for $n = 1, 2, \ldots$.
:::

::: {.remark}
The local transcription previously altered both the pole locations and the
residues in part (ii). The official Spring 2017 UCSD exam has poles at
$n\sqrt n$ with residues $\sqrt n$.
:::

::: {.solution}
For (i), set
\[
a_n=\sqrt n+\frac1{\sqrt n}.
\]
Then $a_n\to\infty$ and $a_n\asymp\sqrt n$. Since
\[
\sum_n |a_n|^{-3}<\infty,
\]
the canonical product
\[
\boxed{F(z)=\prod_{n=1}^\infty E_2\!\left(\frac z{a_n}\right)},
\qquad
E_2(w)=(1-w)e^{w+w^2/2},
\]
converges normally on compact sets and has exactly the prescribed simple
zeros.

For (ii), the points
\[
b_n=n\sqrt n
\]
form a discrete set. By the Mittag--Leffler theorem there is a meromorphic
function on $\mathbb C$ whose principal part at $b_n$ is
\[
\frac{\sqrt n}{z-b_n}
\]
and which has no other poles. Such a function has the required simple poles
and residues.
:::
