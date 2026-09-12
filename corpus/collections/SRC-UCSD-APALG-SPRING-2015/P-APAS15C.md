---
schema: qual/card@1
id: P-APAS15C
kind: problem
title: Character table of $S_4$, Kronecker product of Specht modules, and its endomorphism algebra
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
  - Symmetric Functions
relations: []
review: draft
---

::: problem
(1) Write down the character table of the symmetric group $S_4$.

(2) For $\lambda \vdash 4$, let $S^\lambda$ denote the corresponding irreducible representation of $S_4$.
Endow the tensor product $S^{(3,1)} \otimes S^{(2,2)} \otimes S^{(2,1,1)}$ with a $S_4$-module structure by
\[
\sigma.(u \otimes v \otimes w) := (\sigma.u) \otimes (\sigma.v) \otimes (\sigma.w)
\]
for $\sigma \in S_4$, $u \in S^{(3,1)}$, $v \in S^{(2,2)}$, and $w \in S^{(2,1,1)}$.
(This is the Kronecker product.)
Find the decomposition of $S^{(3,1)} \otimes S^{(2,2)} \otimes S^{(2,1,1)}$ into irreducible $S_4$-modules.

(3) Describe the structure (as a product of matrix algebras over $\mathbb{C}$) of the algebra of $S_4$-endomorphisms $\operatorname{End}_{S_4}(S^{(3,1)} \otimes S^{(2,2)} \otimes S^{(2,1,1)})$.
:::

::: solution
The conjugacy classes of \(S_4\) are indexed by the partitions of \(4\):
\[
(1^4),\quad (2,1,1),\quad (2,2),\quad (3,1),\quad (4),
\]
with respective class sizes
\[
1,\quad 6,\quad 3,\quad 8,\quad 6.
\]
The irreducible characters, indexed by the same partitions, are
\[
\begin{array}{c|rrrrr}
& (1^4)&(2,1,1)&(2,2)&(3,1)&(4)\\ \hline
\chi^{(4)}       &1& 1& 1& 1& 1\\
\chi^{(3,1)}     &3& 1&-1& 0&-1\\
\chi^{(2,2)}     &2& 0& 2&-1& 0\\
\chi^{(2,1,1)}   &3&-1&-1& 0& 1\\
\chi^{(1^4)}     &1&-1& 1& 1&-1
\end{array}.
\]

Let
\[
V=S^{(3,1)}\otimes S^{(2,2)}\otimes S^{(2,1,1)}.
\]
For the diagonal \(S_4\)-action, the character is the pointwise product
\[
\chi_V=\chi^{(3,1)}\chi^{(2,2)}\chi^{(2,1,1)}.
\]
Using the table above gives
\[
\chi_V=(18,0,2,0,0)
\]
on the five conjugacy classes.

The multiplicity of \(S^\lambda\) in \(V\) is
\[
m_\lambda=\langle \chi_V,\chi^\lambda\rangle
=\frac1{24}\sum_C |C|\chi_V(C)\overline{\chi^\lambda(C)}.
\]
Substituting the class sizes and character values gives
\[
m_{(4)}=1,
\quad m_{(3,1)}=2,
\quad m_{(2,2)}=2,
\quad m_{(2,1,1)}=2,
\quad m_{(1^4)}=1.
\]
Therefore
\[
\boxed{
V\cong
S^{(4)}\oplus2S^{(3,1)}\oplus2S^{(2,2)}\oplus2S^{(2,1,1)}\oplus S^{(1^4)}.}
\]
As a dimension check,
\[
1+2\cdot3+2\cdot2+2\cdot3+1=18
=3\cdot2\cdot3=\dim V.
\]

For part (3), if a semisimple \(G\)-module has decomposition
\[
V\cong\bigoplus_i m_iV_i
\]
with the \(V_i\) pairwise nonisomorphic irreducibles, then Schur's lemma gives
\[
\operatorname{End}_G(V)\cong\prod_i M_{m_i}(\mathbb C).
\]
Applying this to the multiplicities above yields
\[
\boxed{
\operatorname{End}_{S_4}(V)
\cong
\mathbb C\times M_2(\mathbb C)\times M_2(\mathbb C)\times M_2(\mathbb C)\times\mathbb C.}
\]
Equivalently,
\[
\operatorname{End}_{S_4}(V)\cong \mathbb C^2\times M_2(\mathbb C)^3.
\]
:::
