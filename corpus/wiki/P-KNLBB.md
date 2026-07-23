---
schema: qual/card@1
id: P-KNLBB
kind: problem
title: "Show that $f(z) = z^2$ is uniformly continuous in any open disk $|z| <\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
> Tie, Fall 2009

:::{.problem title="?"}
Show that $f(z) = z^2$ is uniformly continuous in any open disk $|z| < R$, where $R>0$ is fixed, but it is not uniformly continuous on $\mathbb C$.
:::

:::{.solution}
A direct computation: fix $\eps>0$ and suppose $\abs{z-w} < R$. 
Then
\[
\abs{z^2-w^2} 
&= \abs{z-w}\abs{z+w} \\
&\leq \delta \qty{\abs z + \abs w} \\
&\leq \delta \cdot 2R
,\]
so choose $\delta < { \eps \over 2R}$ to get uniform continuity on $\DD_{R/2}(0)$.

To see $f$ can't be uniformly continuous on $\CC$, take $\eps \da c$ any constant and suppose the appropriate $\delta$ exists.
We'll look for a bad pair of $z, w$, so take $w = z + {1\over 2}\delta$.
This would imply
\[
\abs{z^2 - w^2}
&= \abs{z^2 - (z+\delta)^2} \\
&= \abs{-2z\delta - \delta^2} \\
&= \abs{2z\delta + \delta^2} \\
&= \delta \abs{2z + \delta} \\
&\convergesto{\abs{z}\to\infty}\infty
,\]
using the $\delta = \delta(\eps)$ can't depend on $z$ or $w$, and is thus constant in this expression.
This contradicts that $\abs{z^2-w^2} < \eps = c < \infty$.
:::


