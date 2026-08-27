---
schema: qual/card@1
id: E-SMI-8000E-JF2
kind: exercise
title: Characteristic roots lie in the minimal polynomial; primary subspaces
subtitle: Smith 8000e jordan forms 2
classification:
  areas:
  - algebra
  topics:
  - Modules over PIDs
relations: []
review: draft
---

::: {.exercise}
(i) If $A$ is a $3 \times 3$ matrix with $\mathrm{ch}(t) = (X - 4)^3$, find all Jordan forms for $A$, each with its minimal polynomial.

(ii) If $\mathrm{ch}(t) = \prod (X - t)^{m_t}$ is the characteristic polynomial of $f: M \to M$, prove every root of $\mathrm{ch}(t)$ is also a root of the minimal polynomial $m(t)$, and if

$$
M_t = \ts{v \in M : \text{for some } r > 0, \ (T - t)^r v = 0}
$$

is the primary subspace of $M$ corresponding to the root $t$, prove that $\dim(M_t) = m_t$.

(iii) Use determinants to compute $\mathrm{ch}(t)$ for these matrices:

$$
A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}, \quad
B = \begin{bmatrix} 3 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 1 & 2 \end{bmatrix}, \quad
C = \begin{bmatrix} 1 & -1 & 4 \\ 3 & 2 & -1 \\ 2 & 1 & -1 \end{bmatrix}, \quad
D = \begin{bmatrix} 1 & -2 & -1 & 0 \\ 1 & 0 & -3 & 0 \\ -1 & -2 & 1 & 0 \\ 1 & 2 & 1 & 2 \end{bmatrix}.
$$
:::
