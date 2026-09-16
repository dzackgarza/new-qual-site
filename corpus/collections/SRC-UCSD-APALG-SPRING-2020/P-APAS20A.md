---
schema: qual/card@1
id: P-APAS20A
kind: problem
title: Extremal dimensions of $\ker(\phi^2)$ and $\ker((\phi-\mathrm{id})^2)$ from partial matrix data
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
---

::: {.problem}
Let $\phi\colon\mathbb{C}^8\to\mathbb{C}^8$ be a linear map whose matrix with respect to the standard basis is of the form
\[
\begin{pmatrix}
1 & * & * & * & * & * & * & * \\
0 & 1 & * & * & * & * & * & * \\
0 & 0 & 1 & * & * & * & * & * \\
0 & 0 & 0 & 1 & * & * & * & * \\
0 & 0 & 0 & 0 & 0 & * & * & * \\
0 & 0 & 0 & 0 & 0 & 0 & * & * \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & * \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix},
\]
where $*$ represents an unknown value.
Suppose moreover that we are told
\[
\dim\ker\phi=2,\qquad
\dim\ker(\phi-\mathrm{id})=2,\qquad
\phi^5-2\phi^4+\phi^3=0.
\]
Determine, with proof, the maximum and minimum possible values of
\[
\dim\ker(\phi^2)\qquad\text{and}\qquad\dim\ker\bigl((\phi-\mathrm{id})^2\bigr).
\]
:::

::: {.solution}
Because the displayed matrix is upper triangular, its characteristic polynomial is
\[
\chi_\phi(t)=t^4(t-1)^4.
\]
Thus the generalized \(0\)-eigenspace and generalized \(1\)-eigenspace each have dimension \(4\).

The polynomial identity in the hypothesis factors as
\[
\phi^5-2\phi^4+\phi^3=\phi^3(\phi-I)^2=0.
\]
Hence every Jordan block for the eigenvalue \(0\) has size at most \(3\), and every Jordan block for the eigenvalue \(1\) has size at most \(2\).

Moreover,
\[
\dim\ker\phi=2
\]
is the number of Jordan blocks for the eigenvalue \(0\). Therefore the \(0\)-primary Jordan blocks form a partition of \(4\) into exactly two parts, each at most \(3\). The only possibilities are
\[
(3,1)\qquad\text{or}\qquad(2,2).
\]
For a nilpotent Jordan block of size \(r\), the kernel of its square has dimension \(\min(2,r)\). Consequently,
\[
\dim\ker\phi^2=
\begin{cases}
\min(2,3)+\min(2,1)=3,&(3,1),\\
\min(2,2)+\min(2,2)=4,&(2,2).
\end{cases}
\]
Thus
\[
\boxed{\min\dim\ker\phi^2=3,\qquad \max\dim\ker\phi^2=4.}
\]

Similarly,
\[
\dim\ker(\phi-I)=2
\]
shows that there are exactly two Jordan blocks for the eigenvalue \(1\). They have total size \(4\), and each has size at most \(2\); hence the only possibility is
\[
(2,2).
\]
Therefore both blocks are killed by \((\phi-I)^2\), and
\[
\boxed{\dim\ker((\phi-I)^2)=4}
\]
for every matrix satisfying the hypotheses. In particular, both its minimum and maximum are \(4\).

Finally, both possibilities for the \(0\)-primary part really occur within the displayed upper-triangular form. For the \(1\)-primary part use two blocks \(J_2(1)\) on the first four coordinates. On the last four coordinates use either
\[
J_3(0)\oplus J_1(0)
\]
or
\[
J_2(0)\oplus J_2(0).
\]
Both resulting block-diagonal matrices have the required diagonal and upper-triangular shape and satisfy all three hypotheses. Hence the extrema above are attained.
:::
