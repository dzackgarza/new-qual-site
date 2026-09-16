---
schema: qual/card@1
id: P-APA17D
kind: problem
title: Character table of the quaternion group $Q_8$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
---

::: {.problem}
Let $Q_8$ denote the quaternion group $Q_8 = \{\pm 1, \pm i, \pm j, \pm k\}$ with the usual multiplication
\[
(-1)^2 = 1,\quad
(-1)i = -i = i(-1),\quad
(-1)j = -j = j(-1),\quad
(-1)k = -k = k(-1),
\]
\[
i^2 = j^2 = k^2 = -1,\quad
ij = k = -ji,\quad
ki = j = -ik,\quad
jk = i = -kj.
\]
Calculate the character table of $Q_8$.
:::

::: {.solution}
The conjugacy classes are
\[
\{1\},\qquad \{-1\},\qquad \{\pm i\},\qquad \{\pm j\},\qquad \{\pm k\}.
\]
Indeed, \(\pm1\) are central, and conjugation permutes each pair \(\{\pm i\}\), \(\{\pm j\}\), \(\{\pm k\}\) internally.
Thus \(Q_8\) has five irreducible complex characters.

The commutator subgroup is \(\{\pm1\}\), so the abelianization is
\[
Q_8/\{\pm1\}\cong C_2\times C_2.
\]
Hence there are four one-dimensional characters. Writing the three nontrivial quotient characters by their values on the images of \(i,j\), we obtain
\[
\begin{array}{c|ccccc}
 & 1 & -1 & \{\pm i\} & \{\pm j\} & \{\pm k\}\\ \hline
\chi_1 & 1&1&1&1&1\\
\chi_2 & 1&1&1&-1&-1\\
\chi_3 & 1&1&-1&1&-1\\
\chi_4 & 1&1&-1&-1&1
\end{array}
\]
where the value on \(\pm k=\pm ij\) is the product of the values on \(i\) and \(j\).

The sum of squares of irreducible degrees equals \(|Q_8|=8\). The four linear characters contribute \(4\), so the remaining irreducible has degree \(2\). Let it be \(\chi_5\). Orthogonality with \(\chi_1,\dots,\chi_4\), together with the class sizes \(1,1,2,2,2\), forces
\[
\chi_5=(2,-2,0,0,0).
\]
Equivalently, one may realize it by
\[
i\mapsto \begin{pmatrix} i&0\\0&-i\end{pmatrix},\qquad
j\mapsto \begin{pmatrix}0&1\\-1&0\end{pmatrix},
\]
for which \(-1\mapsto -I_2\) and all of \(\pm i,\pm j,\pm k\) have trace \(0\).
Therefore the complete character table is
\[
\begin{array}{c|ccccc}
 & 1 & -1 & \{\pm i\} & \{\pm j\} & \{\pm k\}\\ \hline
\chi_1 & 1&1&1&1&1\\
\chi_2 & 1&1&1&-1&-1\\
\chi_3 & 1&1&-1&1&-1\\
\chi_4 & 1&1&-1&-1&1\\
\chi_5 & 2&-2&0&0&0
\end{array}.
\]
:::
