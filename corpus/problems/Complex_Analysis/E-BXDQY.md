---
schema: qual/card@1
id: E-BXDQY
kind: problem
title: Rudin 10.3
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Removable Singularities
  - Entire Functions
relations: []
review: draft
---

::: {.exercise}
Suppose $f$ and $g$ are entire and $\abs{f(z)}\leq \abs{g(z)}$ for all $z\in\CC$.
What conclusion can you draw?
:::

::: {.solution}
If $g\equiv0$, then the inequality forces $f\equiv0$, so take $c=0$.

Assume $g\not\equiv0$ and set $h=f/g$ away from the zeros of $g$.
There $\abs{h}\leq1$.
If $a$ is a zero of $g$, then $h$ is bounded on a punctured neighborhood of $a$, so $a$ is a removable singularity of $h$.
Thus $h$ extends to an entire function on $\CC$ with $\abs h\leq1$ everywhere.
By Liouville's theorem, $h\equiv c$ for some $c\in\CC$ with $\abs c\leq1$.
Hence
\[
f=cg.
\]
:::
