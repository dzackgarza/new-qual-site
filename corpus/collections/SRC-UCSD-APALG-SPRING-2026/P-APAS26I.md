---
schema: qual/card@1
id: P-APAS26I
kind: problem
title: Irreducible decomposition of the permutation representation of $S_n$; character table of $S_3$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Permutations
  - Character Theory
relations: []
review: draft
---

::: problem
Let $n \ge 2$.
Let $S_n = \operatorname{Aut}\{1, \ldots, n\}$ be the symmetric group, and consider the unitary representation $(V, \varphi)$ of $S_n$ in which
\[
V = \bigoplus_{i=1}^{n} \mathbb{C}|i\rangle, \qquad \varphi(\pi)|i\rangle = |\pi(i)\rangle.
\]
Decompose $(V, \varphi)$ into irreducible unitary representations of $S_n$, with proof.
Write out the character table of $S_3$.
:::

::: solution
Let
\[
u=|1\rangle+\cdots+|n\rangle.
\]
Then the line
\[
U=\mathbb C u
\]
is fixed pointwise by $S_n$, so it is the trivial representation.

Let
\[
W=\left\{\sum_{i=1}^n c_i|i\rangle:\sum_{i=1}^n c_i=0\right\}.
\]
Then $W$ is $S_n$-stable and
\[
V=U\oplus W.
\]
We show that $W$ is irreducible. Let $0\ne W'\subseteq W$ be an $S_n$-stable subspace and choose
\[
v=\sum_i c_i|i\rangle\in W',\qquad v\ne0.
\]
Since $\sum_i c_i=0$, not all $c_i$ are equal; choose $i,j$ with $c_i\ne c_j$. Then
\[
v-(ij)v=(c_i-c_j)(|i\rangle-|j\rangle)\in W'.
\]
Hence $|i\rangle-|j\rangle\in W'$. Applying permutations shows that every difference $|p\rangle-|q\rangle$ lies in $W'$. These differences span $W$, so $W'=W$. Thus $W$ is irreducible.

Therefore
\[
\boxed{V\cong \mathbf1\oplus S^{(n-1,1)}.}
\]

For $S_3$, use the conjugacy classes represented by $e$, $(12)$, and $(123)$, of sizes $1,3,2$. The irreducible character table is
\[
\begin{array}{c|rrr}
& e&(12)&(123)\\
\hline
\mathbf1&1&1&1\\
\operatorname{sgn}&1&-1&1\\
\mathrm{std}&2&0&-1
\end{array}
\]
where $\mathrm{std}=S^{(2,1)}$ is the two-dimensional summand above.
:::
