---
schema: qual/card@1
id: P-LF4NL
kind: problem
title: $\lim_{x\to 1}\frac{x^2+1}{x}=2$
classification:
  areas:
  - prelim
  topics:
  - Limits
  - Continuity
relations: []
review: draft
---

::: {.problem}
Use the $\varepsilon$-$\delta$ definition of the limit to prove that
$$
\lim_{x\to1}\frac{x^2+1}{x}=2.
$$
:::

::: {.solution}
Let $\varepsilon>0$ and choose
$$
\delta=\min\left\{\frac12,\sqrt{\frac\varepsilon2}\right\}.
$$
If $\abs{x-1}<\delta$, then $\abs{x}>1/2$.
Hence
$$
\abs{\frac{x^2+1}{x}-2}
=\frac{\abs{x-1}^2}{\abs{x}}
<2\abs{x-1}^2
<2\delta^2
\leq\varepsilon.
$$
:::
