---
schema: qual/card@1
id: E-AHBVF
kind: problem
title: Taylor expansion of $z^2\cos(z/3)$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Trigonometry
relations: []
review: draft
---

::: {.exercise}
Expand $f(z) = z^2\cos\qty{z\over 3}$ about $z=0$.
:::

::: {.solution}
\[
\cos\qty{z\over3}
=\sum_{k=0}^\infty(-1)^k{(z/3)^{2k}\over(2k)!},
\]
so
\[
z^2\cos\qty{z\over3}
=\sum_{k=0}^\infty(-1)^k{z^{2k+2}\over 3^{2k}(2k)!}
=z^2-{z^4\over 2!\,3^2}+{z^6\over 4!\,3^4}-\cdots.
\]
This is an ordinary Taylor series; there are no negative powers.
:::
