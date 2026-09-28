---
schema: qual/card@1
id: P-APA23F
kind: problem
title: Character table of the alternating group $A_4$
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
Find the character table of the alternating group $A_4$ of even permutations in $S_4$.
:::

::: {.solution}
Let
\[
V_4=\{1,(12)(34),(13)(24),(14)(23)\}\trianglelefteq A_4.
\]

<1>1. The conjugacy classes of $A_4$ are
\[
\{1\},
\qquad
C_2=\{(12)(34),(13)(24),(14)(23)\},
\]
and two classes $C_3,C_3^{-1}$ of four $3$-cycles each.
::: {.proof}
The three double transpositions are conjugate in $A_4$, so they form a class of size $3$.
There are eight $3$-cycles in $A_4$. The centralizer in $A_4$ of a $3$-cycle is the cyclic subgroup it generates, of order $3$, so its conjugacy class has size
\[
|A_4|/3=4.
\]
Hence the eight $3$-cycles split into exactly two classes of size $4$. Inversion interchanges those two classes; denote them by $C_3$ and $C_3^{-1}$.
The class sizes $1+3+4+4=12$ exhaust $A_4$.
:::

<1>2. Since
\[
A_4/V_4\cong C_3,
\]
there are three one-dimensional characters. If $\omega=e^{2\pi i/3}$ and $C_3$ maps to a chosen generator of the quotient, their values are
\[
\begin{array}{c|rrrr}
&1&C_2&C_3&C_3^{-1}\\ \hline
\chi_1&1&1&1&1\\
\chi_2&1&1&\omega&\omega^2\\
\chi_3&1&1&\omega^2&\omega.
\end{array}
\]
::: {.proof}
The commutator quotient of $A_4$ is $A_4/V_4\cong C_3$. Inflating the three characters of $C_3$ gives the displayed characters. Every element of $V_4$ maps to the identity, while the two classes of $3$-cycles map to the two nontrivial elements of $C_3$.
:::

<1>3. Let $A_4$ act on $\mathbb C^4$ by permuting the standard basis, and let
\[
W=\{(z_1,z_2,z_3,z_4):z_1+z_2+z_3+z_4=0\}.
\]
Then $W$ is a $3$-dimensional representation with character
\[
\chi_4=(3,-1,0,0)
\]
on the four classes above.
::: {.proof}
The permutation character on $\mathbb C^4$ is the number of fixed points. Its values are
\[
4,\ 0,\ 1,\ 1
\]
on the identity, a double transposition, and either class of $3$-cycles. The permutation module splits as the trivial line spanned by $(1,1,1,1)$ plus $W$. Subtracting the trivial character gives
\[
(4,0,1,1)-(1,1,1,1)=(3,-1,0,0).
\]
:::

<1>4. The character $\chi_4$ is irreducible.
::: {.proof}
Using the class sizes,
\[
\langle\chi_4,\chi_4\rangle
=\frac1{12}\left(1\cdot9+3\cdot1+4\cdot0+4\cdot0\right)=1.
\]
Hence $W$ is irreducible.
:::

<1>5. Therefore the complete character table of $A_4$ is
\[
\boxed{
\begin{array}{c|rrrr}
&1&C_2&C_3&C_3^{-1}\\
\text{class size}&1&3&4&4\\ \hline
\chi_1&1&1&1&1\\
\chi_2&1&1&\omega&\omega^2\\
\chi_3&1&1&\omega^2&\omega\\
\chi_4&3&-1&0&0
\end{array}}
\]
with $\omega=e^{2\pi i/3}$.
::: {.proof}
The four rows are irreducible by <1>2 and <1>4. Their degree squares sum to
\[
1^2+1^2+1^2+3^2=12=|A_4|,
\]
so they account for all irreducible representations.
:::
:::
