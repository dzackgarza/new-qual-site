---
schema: qual/card@1
id: E-DM2U0
kind: problem
title: The three-way split in the Tietze theorem proof
classification:
  areas:
  - topology
  topics:
  - Normal Spaces
relations: []
review: draft
---

::: {.exercise}

In the proof of the Tietze theorem, how essential was the clever decision in Step 1 to divide the interval $[-r, r]$ into three equal pieces?
Suppose instead that one divides this interval into the three intervals

$$
I_1 = [-r, -ar], \quad I_2 = [-ar, ar], \quad I_3 = [ar, r],
$$

for some $a$ with $0 < a < 1$.
For what values of $a$ other than $a = 1/3$ (if any) does the proof go through?
:::

::: {.solution}
Suppose \(f:A\to[-r,r]\), and replace the thirds in Step 1 by
\[
[-r,-ar],\qquad[-ar,ar],\qquad[ar,r],
\]
with \(0<a<1\). The same Urysohn construction produces a continuous \(g:X\to[-ar,ar]\) that equals \(-ar\) on \(f^{-1}([-r,-ar])\) and \(ar\) on \(f^{-1}([ar,r])\).

The error satisfies
\[
|f-g|\le q r,
\qquad
q=\max\{1-a,\,2a\}.
\]
Indeed, on the two outer pieces the worst error is \(r-ar=(1-a)r\), while on the middle piece both \(f\) and \(g\) lie in \([-ar,ar]\), so the worst error is \(2ar\).

The iterative Tietze proof works precisely when this error factor is a strict contraction:
\[
q<1.
\]
Since \(a>0\) already gives \(1-a<1\), the additional condition is
\[
2a<1.
\]
Thus the proof goes through for exactly
\[
\boxed{0<a<1/2.}
\]
For such \(a\), the residual norms decrease geometrically by \(q<1\), and the successive correction functions have uniformly summable sup norms. At \(a=1/2\) the estimate gives \(q=1\), so the iterative argument no longer forces convergence; for \(a>1/2\) it is even worse.
:::
