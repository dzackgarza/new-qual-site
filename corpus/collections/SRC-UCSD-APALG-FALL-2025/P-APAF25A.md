---
schema: qual/card@1
id: P-APAF25A
kind: problem
title: Unitary form placing two distinct eigenvalues in a $2\times 2$ block
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Inner Product Spaces
relations: []
review: draft
---

::: problem
Given $n\geq 3$, fix $A\in M_n(\mathbb{C})=\mathbb{C}^{n\times n}$ satisfying that there exist two eigenvalues $\alpha,\beta$ of $A$ with $\alpha\neq\beta$.
Prove there exists unitary $Q\in M_n(\mathbb{C})$ such that
\[
Q^H AQ=\begin{bmatrix}
\alpha & \delta & v^H \\
0 & \beta & 0 \\
0 & w & B
\end{bmatrix},
\]
for some $\delta\in\mathbb{C}$, $v,w\in\mathbb{C}^{n-2}$, and $B\in M_{n-2}(\mathbb{C})$.

(Notationally: for all $m,n\geq 1$, $z^H=\overline{z}^T$ for all $z\in M_{m,n}(\mathbb{C})=\mathbb{C}^{m\times n}$.)
:::
