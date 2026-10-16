---
schema: qual/card@1
id: P-N8VZL
kind: problem
title: The Apollonius circle $\left|\frac{z-z_1}{z-z_2}\right|=c$ and its center and radius
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
relations: []
review: draft
---

::: {.problem}
(a) Prove that if $|w_1|=c|w_2|$, where $c>0$, then
\[
|w_1-c^2w_2|=c|w_1-w_2|.
\]
(b) If $c>0$, $c\ne1$, and $z_1\ne z_2$, prove that
\[
\left|\frac{z-z_1}{z-z_2}\right|=c
\]
is a circle, and find its center and radius.
:::

::: {.solution}
Squaring both sides of (a), and using
$|w_1|^2=c^2|w_2|^2$, gives
\[
|w_1-c^2w_2|^2
=c^2|w_1-w_2|^2,
\]
which proves (a). If $|z-z_1|=c|z-z_2|$, apply (a) to
$w_1=z-z_1$, $w_2=z-z_2$:
\[
|(1-c^2)z-(z_1-c^2z_2)|=c|z_1-z_2|.
\]
Since $c\ne1$, this is the circle with center and radius
\[
\frac{z_1-c^2z_2}{1-c^2},
\qquad
\frac{c|z_1-z_2|}{|1-c^2|}.
\]
:::