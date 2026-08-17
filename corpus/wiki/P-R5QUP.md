---
schema: qual/card@1
id: P-R5QUP
kind: problem
title: "What is the Jordan normal form over $\\mathbb{C}$ of a $7 \\times 7$ mat\u2026"
classification:
  areas:
  - algebra
  topics:
  - jordan-canonical-form
  - eigenvalues-and-eigenvectors
  - trace
relations: []
review: draft
solved: true
---
What is the Jordan normal form over $\mathbb{C}$ of a $7 \times 7$ matrix $A$ which satisfies all of the following conditions:

a.
$A$ has real coefficients,

b.
$\mathrm{rk} A=5$,

c.
$\mathrm{rk} A^{2}=4$,

d.
$\mathrm{rk} A-I=6$,

e.
$\mathrm{rk} A^{3}-I=4$,

f.
$\operatorname{tr} A=1 ?$


:::{.solution}
\envlist

- We'll use rank-nullity throughout: $\rank M + \dim \ker M = 7$.
- Also note that 
\[
Av = \lambda v
\implies
A^nv = A^{n-1}Av = A^{n-1}\lambda v = \cdots = \lambda^n v
,\]
  so if $\lambda \in \spec(A)$ then $\lambda^n\in \spec(A^n)$.
  Conversely, $\lambda\in \spec(A^n) \implies \lambda^{1\over n}\in \spec(A)$, which we'll use several times.
- Since $5 = \rank A = \rank(A - 0\cdot I)$,  we have $\dim \ker(A-0\cdot I) = 2$ contributing an eigenvalue of $\lambda = 0$ with multiplicity $2$.

- Since $4 = \rank A^2 = \rank(A^2 - 0\cdot \lambda) = \rank(A-0\cdot \lambda)^2$, we have that $\dim \ker(A-0\cdot I)^2 = 3$.
  Since $\dim \ker (A-0\cdot I)^1 = 2 < 3$, this means there is 1 generalized eigenvector associated to $\lambda = 0$.

- Since $6 = \rank(A-1\cdot I)$, $\dim \ker (A- 1\cdot I) = 1$, contributing $\lambda = 1$ with multiplicity 1.
- Since $\rank(A^3-1\cdot I) = 4$, we have $\dim \ker (A^3-1\cdot I) = 3$, contributing $\lambda = 1$ *now to $\spec(A^3)$* instead of $\spec(A)$.
  Thus some unknown cube roots of 1 are contributed to $\spec(A)$, so any of $1=\zeta_3^0, \zeta_3, \zeta_3^2$ are possibilities at this point.
  Call these three contributions $z_1, z_2, z_3$, which may not be distinct.

- Now use that $\tr(A) = \sum_{i=1}^n \lambda_i$ is the sum of the diagonal on $\JCF(A)$, using that trace is a similarity invariant, to write
\[
1 = \tr(A) = (0 + 0) + (0) + (1) + (z_1 + z_2 + z_3) \implies z_1 + z_2 + z_3 = 0 
,\]
which is actually enough to force $z_1 = 1, z_2 = \zeta_3, z_3 = \zeta_3^2$, since no other combination sums to zero.
That $1 + \zeta_3 + \zeta_3^2 = 0$ is a general fact.

- Since $\lambda=1$ occurs twice as an eigenvalue but $\dim \ker(A-1\cdot I) = 1$, the two copies of $\lambda = 1$ must occur in a nontrivial Jordan block.
- So we get a Jordan form
\[
\JCF(A) = 
\begin{bmatrix}
0 & & & & & & 
\\
& 0 & 1 & & & & 
\\
& & 0 & & & & 
\\
& & & 1 & 1 & & 
\\
& & & & 1 & & 
\\
& & & & & \zeta_3 & 
\\
& & & & & & \zeta_3^2
\\
\end{bmatrix}
.\]

:::

