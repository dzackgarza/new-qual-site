---
schema: qual/card@1
id: P-APA17E
kind: problem
title: Irreducible decomposition of cubic forms under $S_4$ and $\operatorname{End}_{S_4}(V)$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
---

::: problem
Consider the action of the symmetric group $S_4$ on the vector space $V = \mathbb{C}[x_1, x_2, x_3, x_4]_3$ of homogeneous cubic polynomials in the variables $x_1, x_2, x_3,$ and $x_4$ given by subscript permutation:
\[
\sigma \cdot f(x_1, x_2, x_3, x_4) := f(x_{\sigma(1)}, x_{\sigma(2)}, x_{\sigma(3)}, x_{\sigma(4)})
\]
for $\sigma \in S_4$ and $f \in \mathbb{C}[x_1, x_2, x_3, x_4]$.
Calculate the decomposition of $V$ into a direct sum of irreducible $S_4$-modules and determine the structure (as a product of matrix rings over $\mathbb{C}$) of the endomorphism algebra $\operatorname{End}_{S_4}(V)$.
:::

::: solution
Let \(W=\mathbb C^4\) be the permutation representation of \(S_4\). Then
\[
V=\mathbb C[x_1,x_2,x_3,x_4]_3\cong \operatorname{Sym}^3(W).
\]
For a finite-dimensional representation with character \(\chi\), the symmetric-cube character is
\[
\chi_{\operatorname{Sym}^3}(g)
=\frac{\chi(g)^3+3\chi(g)\chi(g^2)+2\chi(g^3)}6.
\]
For the permutation representation \(W\), \(\chi(g)\) is the number of fixed points of \(g\). On representatives of the five conjugacy classes
\[
1,\quad (12),\quad (12)(34),\quad (123),\quad (1234),
\]
we have
\[
\chi_W=(4,2,0,1,0).
\]
Using the formula above gives
\[
\chi_V=(20,6,0,2,0).
\]

The irreducible character table of \(S_4\), in the same class order, is
\[
\begin{array}{c|ccccc}
 & 1&(12)&(12)(34)&(123)&(1234)\\ \hline
\chi^{(4)}&1&1&1&1&1\\
\chi^{(3,1)}&3&1&-1&0&-1\\
\chi^{(2,2)}&2&0&2&-1&0\\
\chi^{(2,1,1)}&3&-1&-1&0&1\\
\chi^{(1^4)}&1&-1&1&1&-1
\end{array}
\]
and the corresponding class sizes are
\[
1,\ 6,\ 3,\ 8,\ 6.
\]
Taking inner products with \(\chi_V\) gives
\[
\langle \chi_V,\chi^{(4)}\rangle=3,\qquad
\langle \chi_V,\chi^{(3,1)}\rangle=4,
\]
\[
\langle \chi_V,\chi^{(2,2)}\rangle=1,\qquad
\langle \chi_V,\chi^{(2,1,1)}\rangle=1,
\qquad
\langle \chi_V,\chi^{(1^4)}\rangle=0.
\]
Therefore
\[
V\cong
3S^{(4)}\oplus4S^{(3,1)}\oplus S^{(2,2)}\oplus S^{(2,1,1)}.
\]
As a dimension check,
\[
3\cdot1+4\cdot3+1\cdot2+1\cdot3=20=\dim V.
\]

If
\[
V\cong\bigoplus_\lambda m_\lambda S^\lambda,
\]
then Schur's lemma gives
\[
\operatorname{End}_{S_4}(V)
\cong \prod_\lambda M_{m_\lambda}(\mathbb C).
\]
Hence
\[
\operatorname{End}_{S_4}(V)
\cong
M_3(\mathbb C)\times M_4(\mathbb C)\times\mathbb C\times\mathbb C.
\]
:::

