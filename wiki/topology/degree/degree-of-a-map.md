---
title: Degree of a map
order: 241
topics:
- Degree
- Homology
- Suspension
---

# Degree of a map

[[D-XC53X]]

## Properties of the degree

::: {.proposition title="Properties of the degree"}
Let $n\geq 1$ and $f,g\colon S^n\to S^n$.

- A constant map has degree $0$.
- $\deg\id_{S^n} = 1$.
- $\deg (f\circ g) = \deg f \cdot \deg g$.
- If $f\homotopic g$, then $f_* = g_*$, so $\deg f = \deg g$. Conversely, by Hopf's theorem, maps of equal degree are homotopic.
- If $f$ is a homotopy equivalence with homotopy inverse $h$, then $\deg f\cdot\deg h = \deg\id = 1$, so $\deg f = \pm 1$.
- For $1\leq i\leq n+1$, the reflection $R_i\colon S^n\to S^n$, $(x_1, \ldots, x_i, \ldots, x_{n+1}) \mapsto (x_1, \ldots, - x_i, \ldots, x_{n+1})$, has degree $-1$.
- The antipodal map $x\mapsto -x$ on $S^n\subseteq \RR^{n+1}$ is the composite $R_1\circ\cdots\circ R_{n+1}$, so it has degree $(-1)^{n+1}$.
[@Hat02, §2.2, "Degree"]

:::

## Exercises

[[E-EYILL]]

[[E-ZXKDY]]
