---
schema: qual/card@1
id: P-APA17A
kind: problem
title: Jordan form from the rank sequence of a $10\times 10$ nilpotent matrix
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Jordan Canonical Form
relations: []
review: draft
---

::: problem
Let $A \in \mathbb{C}^{10 \times 10}$ be a matrix such that
\[
\operatorname{rank} A = 7,\quad
\operatorname{rank} A^2 = 4,\quad
\operatorname{rank} A^3 = 1,\quad
\operatorname{rank} A^4 = 0.
\]
Determine all possibilities of Jordan's canonical form for $A$.
:::

::: solution
Since
\[
A^4=0,
\]
the matrix \(A\) is nilpotent. Therefore every Jordan block of \(A\) is a nilpotent Jordan block \(J_m(0)\).

From the given ranks,
\[
\dim\ker A=10-7=3,
\]
\[
\dim\ker A^2=10-4=6,
\]
\[
\dim\ker A^3=10-1=9,
\]
and
\[
\dim\ker A^4=10.
\]
Thus the successive increments are
\[
3,\quad 3,\quad 3,\quad 1.
\]

For a nilpotent matrix, the quantity
\[
\dim\ker A^k-\dim\ker A^{k-1}
\]
is exactly the number of Jordan blocks of size at least \(k\). Therefore:

- there are \(3\) Jordan blocks in total;
- all \(3\) have size at least \(2\);
- all \(3\) have size at least \(3\);
- exactly \(1\) has size at least \(4\);
- no block has size at least \(5\), since \(A^4=0\).

Hence one block has size \(4\), while the other two have size exactly \(3\). Their sizes sum to
\[
4+3+3=10,
\]
so this accounts for the entire matrix.

Therefore there is only one possible Jordan canonical form:
\[
\boxed{
J_4(0)\oplus J_3(0)\oplus J_3(0).}
\]
:::
