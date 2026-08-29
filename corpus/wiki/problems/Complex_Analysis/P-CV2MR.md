---
schema: qual/card@1
id: P-CV2MR
kind: problem
title: $|z|^2$ is complex-differentiable only at $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Holomorphic Functions
  - Counterexamples
relations: []
review: draft
---

:::{.problem}
Prove that $f(z) = \abs{z}^2$ has a derivative at $z=0$ and nowhere else.
:::

:::{.solution}
The easy check: $f$ is differentiable iff $\delbar_z f = 0$, but
\[
\delbar_z \abs{z}^2 = \delbar_z z\bar{z} = z \neq 0
,\]
unless of course $z=0$.

A more explicit check: check the limits.
\[
{f(z) - f(0) \over z-0} = { \abs{z}^2 \over z } = {z\bar z \over z} = \bar{z} \converges{z\to 0}\too 0
,\]
so $f$ is differentiable at $w=0$.
Now taking $w = Re^{i\theta} \neq 0$,
\[
{f(z) -f(w) \over z-w} = {\abs{z}^2 - \abs{w}^2 \over z - w} 
= {\qty{\abs{z} + \abs{w} } \qty{\abs{z} - \abs{w}} \over z-w }
= {\abs z - \abs w \over z-w}\cdot \qty{\abs{z} + \abs{w}}
.\]
First let $z\to w$ along $\bd \DD_{R'}(0)$ where $R' \da \abs{w}$, so that the numerator vanishes and the limit is zero.
Then let $z\to w$ along the curve $\ts{tw\st t\in [0, 1]}$, then $\abs{z} = t \abs{w}$, so the ratio becomes
\[
{\abs z - \abs w \over z-w}\cdot \qty{\abs{z} + \abs{w}}
&= {t\abs{w}  - \abs w \over tw-w}\cdot \qty{t\abs{w} + \abs{w}} \\
&= {\abs{w}\qty{t-1 } \over w(t-1)} \cdot \abs{w}(t+1) \\
&= { \abs{w}^2(t+1) \over w} \\
&= \bar{w}(t+1) \\
&\converges{t\to 1}\to 2\bar{w}
,\]
which is nonzero is $w\neq 0$.
:::
