---
schema: qual/card@1
id: P-YFBBW
kind: problem
title: A continuous $f:\RR\to\RR$ vanishing at $\pm\infty$ is uniformly continuous
classification:
  areas:
  - complex-analysis
  topics:
  - uniform-continuity
  - continuity
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Suppose $f:\RR\to\RR$ is continuous and $\lim_{x\to \pm \infty} f(x) = 0$.
Prove that $f$ is uniformly continuous.
:::

:::{.solution}
Fix $\eps>0$, we need to find a $\delta = \delta(\eps)$ such that
\[
\abs{x-y}<\delta \implies \abs{f(x) - f(y)} < \eps && \forall x, y\in \RR
.\]
Use that $\lim_x\to \pm \infty f(x) = 0$ to choose $M\gg 0$ such that
\[
\abs{x} \geq M \implies \abs{f(x)} \leq \eps/2
,\]
then
\[
\abs{x}, \abs{y} \geq M \implies \abs{f(x) - f(y)} \leq \abs{f(x)} + \abs{f(y)} \leq \eps
.\]
So in this region choose (say) $\delta_1 < \eps$ to ensure that $B_\delta(x), B_\delta(y) \subseteq [-M, M]^c$.
On $[-M, M]$, note that this region is compact and $f$ continuous on a compact set implies uniformly continuous.
So use this to choose $\delta_2 = \delta_2(\eps)$ in this region to ensure $\abs{f(x) - f(y)} < \eps$.

This handles the cases $x, y \in (M, M)^c$, or $x,y\in [M, M]$, so it only remains to handle $x\in [M, M]$ and $y\in (M, M)^c$ (wlog, relabeling $x,y$ if necessary).
In this case, use the triangle inequality:
\[
\abs{f(x) - f(y)} 
&= \abs{f(x) - f(M) + f(M) -f(y)} \\
&\leq \abs{f(x) - f(M)} + \abs{f(M) -f(y)} \\
&\leq \eps + \abs{f(M)} + \abs{f(y)} \\
&\leq \eps + \eps + \eps 
,\]
where we've used that $M, y\in (M, M)^c$ to apply the first bound and $M, x\in [M, M]$ to apply the second.
:::

