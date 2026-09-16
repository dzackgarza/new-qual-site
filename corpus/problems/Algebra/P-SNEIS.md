---
schema: qual/card@1
id: P-SNEIS
kind: problem
title: 'Fundamental theorem of cosets: $xH=yH\iff x^{-1}y\in H\iff y^{-1}x\in H$'
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
---

::: {.problem}
Let $H\le G$. Prove that
\[
xH=yH\iff x^{-1}y\in H\iff y^{-1}x\in H.
\]
:::

::: {.solution}
Suppose first that $xH=yH$. Since $y\in yH=xH$, there is some $h\in H$ with
\[
y=xh.
\]
Hence
\[
x^{-1}y=h\in H.
\]
Conversely, if $x^{-1}y=h\in H$, then $y=xh$, and therefore
\[
yH=xhH=xH.
\]
Thus
\[
xH=yH\iff x^{-1}y\in H.
\]

Finally,
\[
x^{-1}y\in H\iff (x^{-1}y)^{-1}=y^{-1}x\in H,
\]
because subgroups are closed under inverses. Hence all three conditions are equivalent.
:::
