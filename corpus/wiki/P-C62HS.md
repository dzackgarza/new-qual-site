---
schema: qual/card@1
id: P-C62HS
kind: problem
title: A contraction of a compact metric space has a fixed point
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Metric Spaces
  - Compactness
relations: []
review: draft
---

:::{.problem title="?"}
Prove that if $(X, d)$ is a compact metric space, $f : X \to X$ is a
continuous map, and $C$ is a constant with $0 < C < 1$ such that 
$$
d(f (x), f (y)) \leq C \cdot d(x, y) \quad \forall x, y
,$$ 
then $f$ has a fixed point.

:::

:::{.solution}
\envlist

- Define a new function
\begin{align*}
g: X \to \RR \\
x &\mapsto d_X(x, f(x))
.\end{align*}

- Attempt to minimize. Claim: $g$ is a continuous function.
- Given claim, a continuous function on a compact space attains its infimum, so set 
    \begin{align*}
    m \definedas \inf_{x\in X} g(x) 
    \end{align*} 
    and produce $x_0\in X$ such that $g(x) = m$.
- Then 
  \begin{align*}
  m> 0 \iff d(x_0, f(x_0)) > 0 \iff x_0 \neq f(x_0)
  .\end{align*} 
- Now apply $f$ and use the assumption that $f$ is a contraction to contradict minimality of $m$:
\begin{align*}
d(f(f(x_0)), f(x_0)) 
&\leq C\cdot d(f(x_0), x_0) \\ 
&< d(f(x_0), x_0) \quad\text{since } C<1\\
&\leq m
\end{align*}

- Proof that $g$ is continuous: use the definition of $g$, the triangle inequality, and that $f$ is a contraction:
\begin{align*}
d(x, f(x)) &\leq d(x, y) + d(y, f(y)) + d(f(x), f(y)) \\
\implies d(x, f(x)) - d(y, f(y)) &\leq d(x, y) + d(f(x), f(y)) \\
\implies g(x) - g(y) &\leq d(x, y) + C\cdot d(x, y)  = (C+1) \cdot d(x, y)\\
\end{align*}
  - This shows that $g$ is Lipschitz continuous with constant $C+1$ (implies uniformly continuous, but not used).

:::

