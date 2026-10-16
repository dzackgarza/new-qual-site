---
schema: qual/card@1
id: P-B2YTD
kind: problem
title: Laurent series of $\frac{1}{1-z^2}+\frac{1}{z-3}$ on $\abs{z}<1$, $1<\abs{z}<3$, and $\abs{z}>3$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
relations: []
review: draft
---

::: {.problem}
Expand
\[
\frac1{1-z^2}+\frac1{z-3}
\]
as a Laurent series about $0$ on each of the regions $|z|<1$,
$1<|z|<3$, and $|z|>3$.
:::

::: {.solution}
For $|z|<1$,
\[
\frac1{1-z^2}+\frac1{z-3}
=\sum_{k=0}^\infty z^{2k}
-\sum_{k=0}^\infty\frac{z^k}{3^{k+1}}.
\]
For $1<|z|<3$,
\[
\frac1{1-z^2}+\frac1{z-3}
=-\sum_{k=1}^\infty z^{-2k}
-\sum_{k=0}^\infty\frac{z^k}{3^{k+1}}.
\]
For $|z|>3$,
\[
\frac1{1-z^2}+\frac1{z-3}
=-\sum_{k=1}^\infty z^{-2k}
+\sum_{k=0}^\infty 3^kz^{-k-1}.
\]
Each follows from the geometric series in the indicated region.
:::