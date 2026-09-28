---
schema: qual/card@1
id: P-APAS21H
kind: problem
title: Character table of $A_4$ and the Wedderburn decomposition of $\mathbb{C}[A_4]$
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
Find the character table of the alternating subgroup $A_4$ of the symmetric group $S_4$.
The group algebra of $A_4$ is isomorphic to a direct sum
\[
\mathbb{C}[A_4] \cong \operatorname{Mat}_{n_1}(\mathbb{C}) \oplus \cdots \oplus \operatorname{Mat}_{n_r}(\mathbb{C})
\]
of matrix algebras over $\mathbb{C}$.
Determine $r$ and the numbers $n_1, \dots, n_r > 0$.
:::

::: {.solution}
The conjugacy classes of $A_4$ are
\[
C_1=\{1\},\qquad
C_2=\{(12)(34),(13)(24),(14)(23)\},
\]
and the eight $3$-cycles split into two classes of four elements, for example
\[
C_3=\{(123),(134),(142),(243)\},\qquad C_4=C_3^{-1}.
\]
Hence there are four irreducible characters.

Let $\omega=e^{2\pi i/3}$. The normal Klein four subgroup
\[
V_4=\{1,(12)(34),(13)(24),(14)(23)\}
\]
has quotient $A_4/V_4\cong C_3$. Inflating the three characters of $C_3$ gives three linear characters. The remaining irreducible character has degree $3$, because
\[
12=1^2+1^2+1^2+d^2
\]
forces $d=3$. It is the character of the standard three-dimensional representation obtained from the permutation representation of $A_4$ on four letters after removing the trivial line. Thus the character table is
\[
\begin{array}{c|cccc}
 & C_1&C_2&C_3&C_4\\\hline
\chi_1&1&1&1&1\\
\chi_2&1&1&\omega&\omega^2\\
\chi_3&1&1&\omega^2&\omega\\
\chi_4&3&-1&0&0
\end{array}
\]
(the two $3$-cycle columns may be interchanged).

By Maschke's theorem and Wedderburn decomposition,
\[
\mathbb C[A_4]\cong\bigoplus_{\chi\in\operatorname{Irr}(A_4)}
\operatorname{Mat}_{\chi(1)}(\mathbb C).
\]
Therefore
\[
\boxed{\mathbb C[A_4]\cong
\mathbb C\oplus\mathbb C\oplus\mathbb C\oplus\operatorname{Mat}_3(\mathbb C)}.
\]
So $r=4$ and, up to order,
\[
(n_1,n_2,n_3,n_4)=(1,1,1,3).
\]
:::
