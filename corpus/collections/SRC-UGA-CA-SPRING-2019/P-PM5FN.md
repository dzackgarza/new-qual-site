---
schema: qual/card@1
id: P-PM5FN
kind: problem
title: Bounds relating $\sup_{|z|\le R}|f|$ and $\sup_{|z|\le R}|f'|$ for holomorphic
  $f$ on $|z|<3R$
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Estimates
  - Maximum Modulus Principle
  - Cauchy Integral Formula
relations: []
review: draft
---

:::{.problem title="?"}
Let $R>0$. Suppose $f$ is holomorphic on $\ts{z\st \abs{z} < 3R}$. Let
$$
M_{R}:=\sup _{|z| \leq R}|f(z)|, \quad N_{R}:=\sup _{|z| \leq R}\left|f^{\prime}(z)\right|
$$

a.
Estimate $M_{R}$ in terms of $N_{R}$ from above.

b.
Estimate $N_{R}$ in terms of $M_{2 R}$ from above.

:::

:::{.solution}
First note that by the maximum modulus principal, it suffices to consider sups on the boundary, i.e.
\[
M_R = \sup_{\abs{z} = R}\abs{f(z)}, \qquad N_R = \sup_{\abs{z} = R} \abs{f'(z)}
.\]

The first estimate: **stuck!**


The second estimate:
suppose $z_0 \in \DD_R(0)$, then any $D_R(z_0)$ is contained in $D_{2R}(0)$, 
So for any such $z_0$, apply Cauchy's integral formula centered at $z_0$:
\[
f^{(1)}(z_0) &= {1\over 2\pi i }\oint_{\bd\DD_{R}(z_0)} {f(\xi)\over (\xi-z_0)^2 }\dxi \\
\implies 
\abs{ f^{(1)}(z_0)} 
&\leq {1\over 2\pi} \oint_{\bd\DD_{R}(z_0)} \abs{f(\xi)\over (\xi-z_0)^2 }\dxi \\
&= {1\over 2\pi} \oint_{\bd\DD_R(z_0)} { \abs{f(\xi)} \over \abs{\xi-z_0}^2 } \dxi \\
&= {1\over 2\pi} \oint_{\bd\DD_R(z_0)} { \abs{f(\xi)} \over R^2 } \dxi \\
&\leq {1\over 2\pi} R^{-2} \oint_{\bd\DD_R(z_0)} { \sup_{z\in \bd\DD_{R}(z_0) } \abs{f(z)} } \dxi \\
&= {1\over 2\pi} R^{-2} \sup_{\bd\DD_R(z_0) } \abs{f(z)} \cdot 2\pi R \\
&= R\inv \sup_{\bd\DD_R(z_0) } \abs{f(z)} \\
&\leq R\inv M_{2R}
,\]
where we've used in the last step that $\DD_R(z_0) \subseteq \DD_{2R}(0)$, and sups can only get larger when taken over larger sets.
Since this was an arbitrary $z_0\in \DD_R(0)$, this holds for all $z$ with $\abs{z} \leq R$.
Since taking sups preserves inequalities, we have
\[
\abs{f'(z_0)} 
\leq R\inv M_{2R}\,
\forall \abs{z} \leq R 
\implies 
N_R\da \sup_{\abs{z} \leq R}\abs{f'(z)}
\leq R\inv M_{2R}
.\]

:::


