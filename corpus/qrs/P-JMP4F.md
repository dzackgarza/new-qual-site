---
schema: qual/card@1
id: P-JMP4F
kind: problem
title: Number of roots of $z^7-4z^3-1$ in $|z|<1$
classification:
  areas:
  - complex-analysis
  topics:
  - rouche
  - zeros
  - polynomials
relations: []
review: draft
solved: true
---
How many roots does the following polynomial have in the open disc $\abs{z} < 1$?
\[
f(z) = z^7 - 4z^3 - 1
.\]

:::{.solution}
:::{.concept}

:::
- Set $h(z) = -4z^3$ and $g(z) = z^7 - 1$, then on $\abs{z} = 1$,
\begin{align*}
\abs{g(z)} = \abs{z^7 - 1} \leq 1 + 1 = 2 < 4 = \abs{-4z^3} = \abs{h(z)}
.\end{align*}

- So $h$ and $h+g$ have the same number of roots, but $h$ has three roots here.
:::


