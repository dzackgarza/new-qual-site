---
schema: qual/card@1
id: E-5QAVX
kind: exercise
title: "Using derivatives"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Using derivatives"}
Let $f:\DD\to \DD$ with $f(0) = f'(0) = 0$.
Show that $\abs{f''(0)} \leq 2$ and describe all $f$ for which this is an equality.

:::

:::{.solution}
By Schwarz, $\abs{f(z)}\leq z$.
Write $g(z) \da f(z)/z$, then $\abs{g(z)}\leq 1$ and $g:\DD\to \DD$ is holomorphic since $f$ has a zero of order at least one at $0$.
Note that $f(z) = c_2z^2 + \bigo(z^3)$, where $c_0 = 0$ since $f(0) = 0$ and $c_1 = 0$ since $f'(0) = 0$.
Thus $g(z) = c_2z + \bigo(z^2)$, and $g(0) = 0$, so Schwarz applies and

- $\abs{g(z)}\leq \abs{z}$
- $\abs{g'(0)} \leq 1$

We have $g'(z) = c_2 + \bigo(z)$ so $g'(0) = c_2 = {f^{(2)}(0) \over 2!}$.
\[
1 \geq \abs{g'(0)} = \abs{c_2} = \abs{f^{(2)}(0) \over 2} \implies \abs{ f^{(2)}(0) } \leq 2!
.\]

Suppose this is an equality -- then Schwarz on $g$ shows $g$ is a rotation, so
\[
{f(z)\over z} = g(z) = \lambda z \implies f(z) = \lambda z^2 \qquad \lambda \in S^1
.\]

> Note: if $\abs{z}\leq 1$, we have $g(\DD) \subseteq \bar{\DD}$, but the open mapping theorem always guarantees $g(\DD) = \DD$.

:::
