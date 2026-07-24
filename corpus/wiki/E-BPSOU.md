---
schema: qual/card@1
id: E-BPSOU
kind: exercise
title: "Show that if $f$ is entire and $\\abs{f(z)} \\in \\bigo(\\abs{z}^p)$ for $\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="?"} 
Show that if $f$ is entire and $\abs{f(z)} \in \bigo(\abs{z}^p)$ for $\abs{z}$ sufficiently large, then $f$ is a polynomial of degree at most $\floor{p}$.

:::

:::{.solution}
The basic idea:
\[
\abs{c_k} 
&\leq {k!\over 2\pi}\int_{\abs{z} = R} \abs{f(\xi) \over (\xi - 0)^{k+1}}\dxi\\
&\leq {k! \over 2\pi}\int_{\abs z = R}{ \abs{\xi}^{p} \over \abs{\xi}^{k+1} }\dxi \\
&= {k! \over 2\pi}\int_{\abs z = R} {1\over \abs{R}^{k+1-p}} \dxi\\
&= {k! \over 2\pi} {1\over \abs{R}^{k+1-p}} \cdot 2\pi R \\
&= \bigo(1/R^{k-p})
,\]
which converges to $0$ as $R\to \infty$ provided that $k-p>0$, so $k>p$.
So any coefficient $c_k$ for $k\geq \floor{p}$ vanishes.
:::
