---
schema: qual/card@1
id: P-ZBUS2
kind: problem
title: Character table of $A_4$
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Character Theory
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Do you know any representation theory?
What about representations of \(A_4\)?

Give a nontrivial one.
What else is there?
How many irreducible representations do we have?
What are their degrees?
Write the character table of \(A_4\).
:::

::: {.solution}
**Goal.** Describe the representations of $A_4$ and write its character table.

<1>1. $A_4$ has order $12$ and $4$ conjugacy classes.
<2>1. $|A_4| = 12$.
::: {.proof}
$A_4$ is the alternating group on $4$ letters, of order $4!/2 = 12$.
:::
<2>2. The conjugacy classes are: $\theset{1}$ (size $1$), the double transpositions $\theset{(12)(34), (13)(24), (14)(23)}$ (size $3$), the $3$-cycles (size $4$), and the other $3$-cycles (size $4$).
::: {.proof}
the conjugacy classes of $A_4$ are determined by cycle type, with the $3$-cycles splitting into two classes.
:::

<1>2. $A_4$ has $4$ irreducible representations.
::: {.proof}
the number of irreducible representations equals the number of conjugacy classes, which is $4$.
:::

<1>3. The degrees of the irreducible representations.
<2>1. $A_4$ has a normal subgroup $V = \theset{1, (12)(34), (13)(24), (14)(23)} \cong \ZZ/2 \times \ZZ/2$ of order $4$.
::: {.proof}
the Klein four-group is normal in $A_4$.
:::
<2>2. $A_4/V \cong \ZZ/3$, giving three $1$-dimensional representations (the characters of $\ZZ/3$).
::: {.proof}
the quotient is cyclic of order $3$, with three linear characters.
:::
<2>3. The remaining representation has degree $3$ (since $1^2 + 1^2 + 1^2 + 3^2 = 12$).
::: {.proof}
the sum of squares of degrees is $|A_4| = 12$.
:::

<1>4. The character table.
<2>1. The three linear characters are $\chi_1 = 1$ (trivial), and $\chi_2, \chi_3$ the two nontrivial characters of $\ZZ/3$ (with values $\omega, \omega^2$ on the $3$-cycles, where $\omega = e^{2\pi i/3}$).
::: {.proof}
pull back the characters of $A_4/V \cong \ZZ/3$.
:::
<2>2. The $3$-dimensional character $\chi_4$ is the permutation character minus the trivial character.
::: {.proof}
$A_4$ acts on $4$ letters; the permutation character has values (number of fixed points), and $\chi_4 = \chi_{\text{perm}} - \chi_1$.
:::
<2>3. The character table is:
$$
\begin{array}{c|cccc}
 & 1 & (12)(34) & (123) & (132) \\
\hline
\chi_1 & 1 & 1 & 1 & 1 \\
\chi_2 & 1 & 1 & \omega & \omega^2 \\
\chi_3 & 1 & 1 & \omega^2 & \omega \\
\chi_4 & 3 & -1 & 0 & 0
\end{array}
$$
::: {.proof}
$\chi_4(1) = 3$; $\chi_4((12)(34)) = 0 - 1 = -1$ (a double transposition fixes no letter); $\chi_4((123)) = 1 - 1 = 0$ (a $3$-cycle fixes one letter).
:::

<1>5. Q.E.D.
::: {.proof}
<1>4.3 is the character table of $A_4$.
:::
:::
