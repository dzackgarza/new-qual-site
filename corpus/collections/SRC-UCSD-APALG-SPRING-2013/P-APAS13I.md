---
schema: qual/card@1
id: P-APAS13I
kind: problem
title: External tensor product of representations of a direct product of groups
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
---

::: {.problem}
Let $G$ and $H$ be finite groups and let $A\colon G\to\mathrm{GL}_n(\mathbb{C})$ and $B\colon H\to\mathrm{GL}_m(\mathbb{C})$ be representations of $G$ and $H$ respectively.

(a) Show that $A\times B\colon G\times H\to\mathrm{GL}_{nm}(\mathbb{C})$ is a representation where for $(\sigma,\tau)\in G\times H$,
\[
A\times B((\sigma,\tau))=A(\sigma)\otimes B(\tau)
\]
and for matrices $M$ and $N$, $M\otimes N$ is the Kronecker product of $M$ and $N$.

(b) Show that $A\times B$ is an irreducible representation of $G\times H$ if and only if $A$ is an irreducible representation of $G$ and $B$ is an irreducible representation of $H$.

(c) Show that every irreducible representation of $G\times H$ is of the form $A\times B$ where $A$ is an irreducible representation of $G$ and $B$ is an irreducible representation of $H$.

(d) Show that it is not always the case that if $C$ is a representation of $G\times H$, then $C$ is similar to a representation of the form $A\times B\colon G\times H\to\mathrm{GL}_n(\mathbb{C})$ where $A$ is a representation of $G$ and $B$ is a representation of $H$.
(Hint: Consider the two-dimensional representations of $S_2\times S_2$.)
:::

::: {.solution}
For part (a), recall the Kronecker-product identity
\[
(M_1\otimes N_1)(M_2\otimes N_2)
=(M_1M_2)\otimes(N_1N_2).
\]
Hence for \((\sigma_1,\tau_1),(\sigma_2,\tau_2)\in G\times H\),
\[
\begin{aligned}
(A\times B)((\sigma_1,\tau_1)(\sigma_2,\tau_2))
&=A(\sigma_1\sigma_2)\otimes B(\tau_1\tau_2)\\
&=(A(\sigma_1)\otimes B(\tau_1))(A(\sigma_2)\otimes B(\tau_2)).
\end{aligned}
\]
Thus \(A\times B\) is a representation of \(G\times H\).

Let \(\chi_A,\chi_B\) be the characters of \(A,B\). The character of the external tensor product is
\[
\chi_{A\times B}(g,h)=\chi_A(g)\chi_B(h),
\]
because \(\operatorname{tr}(M\otimes N)=\operatorname{tr}(M)\operatorname{tr}(N)\).
Therefore
\[
\begin{aligned}
\langle \chi_{A\times B},\chi_{A\times B}\rangle_{G\times H}
&=\frac1{|G||H|}
\sum_{g\in G}\sum_{h\in H}|\chi_A(g)|^2|\chi_B(h)|^2\\
&=\langle\chi_A,\chi_A\rangle_G\,
  \langle\chi_B,\chi_B\rangle_H.
\end{aligned}
\]
A complex representation of a finite group is irreducible exactly when the norm of its character is \(1\). Since each factor on the right is a positive integer, the product equals \(1\) if and only if both factors equal \(1\). Hence
\[
A\times B\text{ is irreducible}
\iff A\text{ and }B\text{ are irreducible}.
\]

For part (c), let
\[
A_1,\ldots,A_r
\quad\text{and}\quad
B_1,\ldots,B_s
\]
be complete sets of irreducible representations of \(G\) and \(H\), respectively, with dimensions \(d_i\) and \(e_j\). By part (b), each \(A_i\times B_j\) is irreducible. They are pairwise inequivalent because their characters are pairwise orthogonal:
\[
\langle \chi_{A_i\times B_j},\chi_{A_{i'}\times B_{j'}}\rangle
=\langle\chi_{A_i},\chi_{A_{i'}}\rangle_G
 \langle\chi_{B_j},\chi_{B_{j'}}\rangle_H.
\]
Moreover,
\[
\sum_{i,j}(d_ie_j)^2
=\left(\sum_i d_i^2\right)
 \left(\sum_j e_j^2\right)
=|G||H|=|G\times H|.
\]
For a finite group, the sum of the squares of the dimensions of all inequivalent irreducible representations equals the group order. Thus the already constructed irreducibles \(A_i\times B_j\) exhaust all irreducible representations of \(G\times H\).

For part (d), identify \(S_2\cong C_2=\{0,1\}\), and define a two-dimensional representation
\[
C:C_2\times C_2\longrightarrow \operatorname{GL}_2(\mathbb C)
\]
by
\[
C(s,t)=
\begin{pmatrix}
(-1)^s&0\\
0&(-1)^t
\end{pmatrix}.
\]
This is the direct sum of the two distinct linear characters
\[
(s,t)\mapsto(-1)^s,
\qquad
(s,t)\mapsto(-1)^t.
\]

Suppose \(C\) were similar to an external tensor product \(A\times B\) of total dimension \(2\). Then
\[
(\dim A)(\dim B)=2,
\]
so one factor has dimension \(1\). If \(\dim A=1\), then every element of the first \(C_2\)-factor acts on \(A\times B\) by a scalar matrix; if \(\dim B=1\), then every element of the second factor acts by a scalar matrix. Similarity preserves the property of being scalar.

But in \(C\),
\[
C(1,0)=\begin{pmatrix}-1&0\\0&1\end{pmatrix},
\qquad
C(0,1)=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\]
and neither matrix is scalar. Hence \(C\) is not similar to any external tensor product representation. Therefore arbitrary representations of \(G\times H\) need not themselves be single external tensor products, even though every irreducible representation is one.
:::
