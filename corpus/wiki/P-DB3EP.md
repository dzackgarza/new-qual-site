---
schema: qual/card@1
id: P-DB3EP
kind: problem
title: Equivalence of $A\mathbf{x}=\mathbf{b}$ with the corresponding system of linear
  equations
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Matrices
  - Rank and Nullity
relations: []
review: draft
solved: false
---

::: problem
$\impliedby$: Suppose that $A\vector x = \vector b$ has a solution $\vector x$.

Write $A = [\vector a_1, \vector a_2, \cdots \vector a_m]^t$ in block form with each $\vector a_i$ a row of $A$.
By definition, a solution to this equation is a $\vector x = (x_i)$ such that for each $i$, we have $\inner{\vector a_i}{\vector x} = b_i$ (by carrying out the matrix multiplication).

But 

\begin{align*}
\inner{\vector a_i}{\vector x} &= b_i \\
\implies \sum_{j=1}^m a_{ij} x_j &= b_i
,\end{align*}

which says that the collection $x_1, \cdots, x_n$ solves the equation
$$
a_{i1} x_1 + a_{i2} x_2 + \cdots a_{im} = b_i
$$

for every $i$, which is exactly the statement that the $x_i$ simultaneously solve the given system.

$\implies$:
Suppose that the given system has a simultaneous solutions $x_1, x_2, \cdots, x_n$, and consider the matrix equation $A\vector x = \vector b$.

Letting $\vector x = [x_1, x_2, \cdots, x_n]$, we can rewrite
$$
b_i = a_{i1}x_1 + a_{i2} x_2 + \cdots + a_{im} x_m = \inner{\vector a_i}{\vector x},
$$

where $\vector a_i = [a_{i1}, a_{i2}, \cdots, a_{im}]$.

But then $\vector a_i$ is the $i$th row of $A$, and $A\vector x = \vector b$ has a solution iff there is a $\vector x$ such that $\inner{\vector a_i}{\vector x} = b_i$ for all $i$, which is exactly what we've constructed.
:::
