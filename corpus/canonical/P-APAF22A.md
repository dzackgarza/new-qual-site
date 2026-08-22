---
schema: qual/card@1
id: P-APAF22A
kind: problem
title: Jordan form of a $10\times 10$ map with a partial upper-triangular matrix
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Jordan Canonical Form
relations: []
review: draft
solved: false
---

::: problem
A linear map $\phi \colon \mathbb{C}^{10} \to \mathbb{C}^{10}$ is given in the standard basis $e_1, \ldots, e_{10}$ by the matrix
\[
\begin{pmatrix}
0 & 0 & * & * & * & * & * & * & * & * \\
0 & 0 & 1 & * & * & * & * & * & * & * \\
0 & 0 & 0 & 2 & * & * & * & * & * & * \\
0 & 0 & 0 & 0 & 3 & * & * & * & * & * \\
0 & 0 & 0 & 0 & 0 & 4 & * & * & * & * \\
0 & 0 & 0 & 0 & 0 & 0 & 5 & * & * & * \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 6 & * & * \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 7 & * \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 8 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix},
\]
where $*$ denotes an unknown value.

(a) Prove that $\dim \ker \phi = 2$ and that $\phi^8(e_{10}) \neq 0$.

(b) Hence, or otherwise, determine (with proof) the Jordan Normal Form of $\phi$.
:::
