---
schema: qual/card@1
id: P-3OH6H
kind: problem
title: $\lim_{x\to 2}(x+1/x)=5/2$
classification:
  areas:
  - prelim
  topics:
  - Limits
  - Continuity
relations: []
review: draft
---

::: problem
Use the $\varepsilon$-$\delta$ definition to prove that
\[
\lim_{x\to2}\left(x+\frac1x\right)=\frac52.
\]
:::

::: solution
Let $\varepsilon>0$ and choose
\[
\delta=\min\left\{1,\frac{2\varepsilon}{5}\right\}.
\]
If $0<|x-2|<\delta$, then $1<x<3$.
Hence $|x|>1$ and $|2x-1|<5$.
Therefore
\[
\left|x+\frac1x-\frac52\right|
=\frac{|2x-1|\,|x-2|}{2|x|}
<\frac52|x-2|
<\frac52\delta
\leq\varepsilon.
\]
:::
