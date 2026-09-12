---
schema: qual/card@1
id: P-APAS18E
kind: problem
title: Character table of $A_4$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
---

::: problem
Let $A_4$ be the index two subgroup of $S_4$ consisting of even permutations.
Find the character table of $A_4$.
:::

::: solution
The conjugacy classes of \(A_4\) are
\[
C_1=\{e\},\qquad
C_2=\{(12)(34),(13)(24),(14)(23)\},
\]
and the eight \(3\)-cycles split into two classes of four elements, for example
\[
C_3=\{(123),(134),(142),(243)\},\qquad
C_4=C_3^{-1}.
\]
Thus \(A_4\) has four irreducible complex characters.

The normal Klein four subgroup
\[
V_4=\{e,(12)(34),(13)(24),(14)(23)\}
\]
has quotient \(A_4/V_4\cong C_3\). Let \(\omega=e^{2\pi i/3}\). Inflating the three characters of \(C_3\) gives three one-dimensional characters of \(A_4\):
\[
\begin{array}{c|cccc}
 & C_1&C_2&C_3&C_4\\ \hline
\chi_1&1&1&1&1\\
\chi_2&1&1&\omega&\omega^2\\
\chi_3&1&1&\omega^2&\omega
\end{array}.
\]
Since the sum of squares of irreducible degrees is \(12\), the remaining irreducible has degree \(3\). The natural permutation representation of \(A_4\) on four letters has character equal to the number of fixed points; subtracting the trivial constituent gives a \(3\)-dimensional irreducible character
\[
\chi_4=(3,-1,0,0).
\]
Therefore the complete character table is
\[
\begin{array}{c|cccc}
 & e&(12)(34)&(123)&(132)\\ \hline
\chi_1&1&1&1&1\\
\chi_2&1&1&\omega&\omega^2\\
\chi_3&1&1&\omega^2&\omega\\
\chi_4&3&-1&0&0
\end{array},
\]
where the last two columns represent the two conjugacy classes of \(3\)-cycles.
:::
