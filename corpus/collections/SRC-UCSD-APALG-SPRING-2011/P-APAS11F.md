---
schema: qual/card@1
id: P-APAS11F
kind: problem
title: Conjugacy classes and character table of $A_4$ via $A_4/D\cong\mathbb{Z}_3$
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
Let $S_4$ denote the symmetric group on $4$ elements and $A_4$ denote the alternating group, i.e. $A_4=\{\sigma\in S_4:\operatorname{sign}(\sigma)=1\}$.

(a) Find the conjugacy classes of $A_4$.

(b) Let $D=\{\varepsilon,(1,2)(3,4),(1,3)(2,4),(1,4)(2,3)\}$.
Show that $D$ is a normal subgroup of $A_4$ and that $A_4/D$ is isomorphic to $\mathbb{Z}_3$.

(c) Give the character table for $\mathbb{Z}_3$.

(d) Find the lifting of the irreducible characters of $\mathbb{Z}_3$ to $A_4$.

(e) Use (d) to complete the character table of $A_4$.
:::

::: {.solution}
The even permutations in $S_4$ are the identity, the three double transpositions, and the eight $3$-cycles.

For (a), the conjugacy classes in $A_4$ are
\[
C_1=\{e\},
\]
\[
C_2=\{(12)(34),(13)(24),(14)(23)\},
\]
and two classes of four $3$-cycles, for example
\[
C_3=\{(123),(142),(134),(243)\},
\qquad
C_4=C_3^{-1}.
\]
The splitting of the $S_4$ class of $3$-cycles follows because the centralizer in $A_4$ of a $3$-cycle has order $3$, so its $A_4$-conjugacy class has size $12/3=4$.

For (b), $D=C_1\cup C_2$ is a subgroup: it is the Klein four group. Since it is a union of conjugacy classes, it is normal in $A_4$. Its index is $3$, so $A_4/D$ has order $3$ and is therefore cyclic:
\[
A_4/D\cong \mathbb Z/3\mathbb Z.
\]

For (c), let $\omega=e^{2\pi i/3}$. The character table of $C_3=\langle t\rangle$ is
\[
\begin{array}{c|ccc}
&t^0&t&t^2\\ \hline
1&1&1&1\\
\psi&1&\omega&\omega^2\\
\bar\psi&1&\omega^2&\omega
\end{array}.
\]

For (d), inflate these three characters through the quotient map $A_4\to A_4/D$. Since $D$ is the kernel, all three inflated characters take value $1$ on $C_1$ and $C_2$. Choosing the quotient generator so that $C_3$ maps to $t$, the three characters are
\[
\begin{array}{c|rrrr}
&C_1&C_2&C_3&C_4\\ \hline
\chi_1&1&1&1&1\\
\chi_2&1&1&\omega&\omega^2\\
\chi_3&1&1&\omega^2&\omega.
\end{array}
\]

For (e), $A_4$ has four conjugacy classes, hence four irreducible complex characters. The first three above are already irreducible and one-dimensional, so exactly one irreducible character $\chi_4$ remains. The sum-of-squares formula gives
\[
12=1^2+1^2+1^2+\chi_4(1)^2,
\]
so $\chi_4(1)=3$.

The natural permutation representation of $A_4$ on four letters has character equal to the number of fixed points. Removing its invariant trivial line gives a $3$-dimensional representation with character
\[
\chi_4(g)=\#\operatorname{Fix}(g)-1.
\]
Thus
\[
\chi_4(C_1)=3,\qquad
\chi_4(C_2)=-1,\qquad
\chi_4(C_3)=\chi_4(C_4)=0.
\]
Hence the full character table is
\[
\begin{array}{c|rrrr}
&C_1&C_2&C_3&C_4\\ \hline
\chi_1&1&1&1&1\\
\chi_2&1&1&\omega&\omega^2\\
\chi_3&1&1&\omega^2&\omega\\
\chi_4&3&-1&0&0.
\end{array}
\]
:::
