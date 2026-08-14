---
schema: qual/card@1
id: P-UPCWX
kind: problem
title: "Let $f$ be differentiable on $[a, b]$. Say that $f$ is uniformly\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - calculus
  - continuity
  - uniform-continuity
relations: []
review: draft
---
:::{.problem title="?"}
Let $f$ be differentiable on $[a, b]$.
Say that $f$ is *uniformly differentiable* iff 

\[  
\forall \varepsilon > 0,\, \exists \delta > 0 \text{ such that } \quad \abs{x-y} < \delta \implies \abs{ {f(x) - f(y) \over x-y}  - f'(y)}  < \eps
.\]

Prove that $f$ is uniformly differentiable on $[a, b] \iff f'$ is continuous on $[a, b]$.
:::

:::{.solution}
$\implies$:
Fix $\eps>0$ and choose $\delta = \delta(\eps)$ to get a bound corresponding to $\eps/2$, then for all $x,y$ with $\abs{x-y} < \delta$ on $[a, b]$, we have
\[
\abs{f'(x) - f'(y) } \leq 
\abs{f'(x) - {f(x) - f(y) \over x- y} } + \abs{ {f(x) - f(y) \over x-y} - f'(y)} < \eps
.\]
This uses uniformity to bound by $\eps/2$ the terms involving $f'(x)$ and $f'(y)$ respectively.
So $f'$ is in fact uniformly continuous on $[a, b]$.

$\impliedby$:
Let $\eps> 0$ and $x,y\in [a, b]$ be arbitrary.
Then by the MVT, we can a $\xi\in [x, y]$ with $f'(\xi)(x-y) = f(x) - f(y)$.
Then use continuity of $f'$ to choose $\delta = \delta(\eps, x, y)$ so that $\abs{x-y} < \delta \implies \abs{f(x) - f(y)} < \eps$, and note that $\abs{x-\xi} \leq \abs{x-y} < \delta$, so 
\[
\abs{ {f(x) - f(y) \over x-y } - f'(y) } = \abs{ f'(\xi) - f'(y)} < \eps
.\]



:::

