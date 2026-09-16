---
schema: qual/card@1
id: P-APAF25C
kind: problem
title: Jordan forms with eigenvalues $-2,-3$ and $\operatorname{rank}((A+2I)^3)=2$
classification:
  areas:
  - applied-algebra
  topics:
  - Jordan Canonical Form
  - Linear Algebra
relations: []
review: draft
---

::: {.problem}
Consider complex-valued square matrices $A$ satisfying:

- $A$ has exactly two distinct eigenvalues of $-2$ and $-3$, with algebraic multiplicities of $6$ and $1$, respectively;

- $\operatorname{rank}((A+2I)^3)=2$;

Now considering all possible Jordan canonical forms similar to $A$, determine and write down one, and only one, of these from each similarity class.
:::

::: {.solution}
Because the eigenvalue \(-3\) has algebraic multiplicity \(1\), its Jordan form consists of exactly one \(1\times1\) block \([-3]\).
The \(-2\)-generalized eigenspace has dimension \(6\); write the sizes of its Jordan blocks as a partition
\[
6=s_1+\cdots+s_r.
\]

<1>1. On a Jordan block \(J_s(-2)\), the operator \((A+2I)^3\) has rank
\[
\max(s-3,0).
\]
::: {.proof}
On \(J_s(-2)\), the operator \(A+2I\) is the nilpotent Jordan block \(N_s=J_s(0)\). Its third power sends
\[
e_j\longmapsto e_{j-3}
\]
for \(j>3\), and sends \(e_1,e_2,e_3\) to \(0\). Hence
\[
\operatorname{rank}(N_s^3)=
\begin{cases}
s-3,&s\ge4,\\
0,&s\le3,
\end{cases}
\]
which is \(\max(s-3,0)\).
:::

<1>2. The \(-3\) block contributes rank \(1\) to \((A+2I)^3\).
::: {.proof}
On the \(-3\)-eigenspace,
\[
A+2I=-I,
\]
so
\[
(A+2I)^3=-I.
\]
This is nonzero on a one-dimensional space and therefore has rank \(1\).
:::

<1>3. Therefore the Jordan blocks for eigenvalue \(-2\) must satisfy
\[
\sum_{j=1}^r\max(s_j-3,0)=1.
\]
::: {.proof}
Jordan form block-diagonalizes \((A+2I)^3\), so its rank is the sum of its ranks on the Jordan blocks. The total rank is \(2\) by hypothesis, and <1>2 accounts for rank \(1\) from the \(-3\) block. Hence the \(-2\) blocks must account for exactly one remaining rank.
:::

<1>4. The only partitions of \(6\) satisfying <1>3 are
\[
6=4+2
\qquad\text{and}\qquad
6=4+1+1.
\]
::: {.proof}
To make the sum in <1>3 equal to \(1\), exactly one Jordan block must have size greater than \(3\), and it must have size exactly \(4\). Every other block must have size at most \(3\). After removing the size-\(4\) block, the remaining dimension is \(2\), whose only partitions are \(2\) and \(1+1\).
A block of size \(5\) would already contribute rank \(2\), and a block of size \(6\) would contribute rank \(3\), so no other possibility exists.
:::

<1>5. Hence there are exactly two similarity classes, represented by
\[
\boxed{J_4(-2)\oplus J_2(-2)\oplus[-3]}
\]
and
\[
\boxed{J_4(-2)\oplus[-2]\oplus[-2]\oplus[-3]}.
\]
::: {.proof}
The Jordan canonical form over \(\mathbb C\) is determined uniquely up to permutation of blocks by the eigenvalues and the multiset of block sizes for each eigenvalue. By <1>4, precisely the two displayed multisets occur for eigenvalue \(-2\), while the \(-3\) part is uniquely the single block \([-3]\).
:::
:::
