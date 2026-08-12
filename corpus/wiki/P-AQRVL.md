---
schema: qual/card@1
id: P-AQRVL
kind: problem
title: "Expand $\\frac{1}{1-z^{2}}+\\frac{1}{z-3}$ in a series of the form $\\sum_{-\\infty}^{\\infty} a_{n} z^{n}$ so it converges for $|z|<1$, $1<|z|<3$, $|z|>3$."
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Expand $\frac{1}{1-z^{2}}+\frac{1}{z-3}$ in a series of the form $\sum_{-\infty}^{\infty} a_{n} z^{n}$ so it converges for

- $|z|<1$,

- $1<|z|<3$,

- $|z|>3$.

:::

:::{.solution}
General strategy: each has two expansions, so just compute them all and pick appropriate ones for regions afterwards.

For $1\over z-3$:
\[
{1\over z-3} &= -{1\over 3}{1\over 1- {z\over 3}} = -{1\over 3}\sum_{k\geq 0}3^{-k}z^k 
&& \abs{z} < 3 \\
&= {1\over z} {1\over 1 - {3\over z}} = z\inv \sum_{k\geq 0} 3^k z^{-k}
&& \abs{z} > 3
.\]

For $1\over 1-z^2$:
\[
{1\over 1-z^2}
&= \sum_{k\geq 0} z^{2k} && \abs{z} < 1 \\
&= {1\over z^2} {-1\over 1- z^{-2}} = -z^{-2}\sum_{k\geq 0}z^{-2k} && \abs{z} > 1
.\]

So take
\[
0 < \abs{z} < 1 
&& f(z) &= \sum_{k\geq 0}z^{2k} - {1\over 3}\sum_{k\geq 0} 3^{-k}z^k \\
1 < \abs{z} < 3 
&& f(z) &= -z^{-2} \sum_{k\geq 0}z^{-2k} - {1\over 3}\sum_{k\geq 0} 3^{-k}z^k \\
3 < \abs{z} < \infty 
&& f(z) &= -z^{-2} \sum_{k\geq 0}z^{-2k} + z\inv \sum_{k\geq 0}3^k z^{-k} 
.\]

:::


