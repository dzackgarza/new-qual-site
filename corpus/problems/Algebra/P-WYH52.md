---
schema: qual/card@1
id: P-WYH52
kind: problem
title: Character table of $S_5$
classification:
  areas:
  - algebra
  topics:
  - Character Theory
  - Representation Theory
  - Permutations
relations: []
review: draft
---

::: {.problem}
Construct the character table of $S_5$.
:::

::: {.solution}
The conjugacy classes are indexed by partitions of $5$. In the order
\[
1^5,\quad 2\,1^3,\quad 2^2 1,\quad 3\,1^2,\quad 3\,2,\quad 4\,1,\quad 5,
\]
their sizes are
\[
1,\ 10,\ 15,\ 20,\ 20,\ 30,\ 24.
\]
The irreducible characters are indexed by the same partitions. The full table is

\[
\begin{array}{c|rrrrrrr}
 &1^5&2\,1^3&2^2 1&3\,1^2&3\,2&4\,1&5\\ \hline
[5]       &1& 1& 1& 1& 1& 1& 1\\
[4,1]     &4& 2& 0& 1&-1& 0&-1\\
[3,2]     &5& 1& 1&-1& 1&-1& 0\\
[3,1,1]   &6& 0&-2& 0& 0& 0& 1\\
[2,2,1]   &5&-1& 1&-1&-1& 1& 0\\
[2,1,1,1] &4&-2& 0& 1& 1& 0&-1\\
[1^5]     &1&-1& 1& 1&-1&-1& 1
\end{array}
\]

Here is a construction of the rows.

Let $V$ be the $4$-dimensional standard representation, obtained from the permutation representation on five letters by removing the trivial summand. Its character is
\[
\chi_V(g)=\#\operatorname{Fix}(g)-1,
\]
which gives the row $[4,1]$. Tensoring by the sign character gives the row $[2,1,1,1]$.

For any representation with character $\chi$,
\[
\chi_{\operatorname{Sym}^2 V}(g)
=\frac{\chi(g)^2+\chi(g^2)}2,
\qquad
\chi_{\wedge^2 V}(g)
=\frac{\chi(g)^2-\chi(g^2)}2.
\]
For the standard representation of $S_5$,
\[
\operatorname{Sym}^2V\cong [5]\oplus[4,1]\oplus[3,2],
\]
so subtracting the trivial and standard rows yields the character $[3,2]$. Also
\[
\wedge^2V\cong[3,1,1],
\]
which yields the $6$-dimensional row. Finally, tensoring $[3,2]$ by sign gives $[2,2,1]$.

The weighted inner products using the displayed class sizes are
\[
\langle\chi_\lambda,\chi_\mu\rangle
=\frac1{120}\sum_C |C|\chi_\lambda(C)\chi_\mu(C)
=\delta_{\lambda\mu},
\]
so these seven characters are pairwise distinct irreducibles. Their squared dimensions sum to
\[
1^2+4^2+5^2+6^2+5^2+4^2+1^2=120=|S_5|,
\]
so the table is complete.
:::
