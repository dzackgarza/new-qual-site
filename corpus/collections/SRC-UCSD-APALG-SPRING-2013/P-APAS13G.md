---
schema: qual/card@1
id: P-APAS13G
kind: problem
title: "Quaternion group of order $8$: conjugacy classes and character table"
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. Checked every part: the rewriting relations (ab = ba^3 from left-multiplying, a^3b = ba from cubing the relation, and b^3 = b a^2 so that a b^3 = b a); the normal form and why the eight listed elements are exactly Q (surjection from eight pairs to a group of order 8, which uses the order being part of the statement); centrality of a^2 via (bab^{-1})^2 = a^6 = a^2; the conjugacies a^{-1}ba = a^2 b and a^{-1}(ab)a = a^3 b computed with the rewriting rule; the quotient Q/H (both generators of order 2, commuting, and not C4 because C4 has one involution while aH and bH are two); the four inflated linear characters read coset by coset, with each conjugacy class checked to lie in a single coset; and the fifth character's values from the four orthogonality equations, solved explicitly rather than by inspection. The prose's claim that "the simultaneous orthogonality equations force psi(C3) = psi(C4) = psi(C5) = 0" is now an actual solution of the four equations, which is why the step is longer than the prose. Every entry of the table was checked against the standard table of Q8. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair.
---

::: {.problem}
Let $Q$ be the quaternion group of order $8$ defined by the relations
$$
a^4=1,\quad a^2=b^2,\quad\text{and}\quad b^{-1}ab=a^3.
$$

(a) Show that $ba=ab^3=a^3b$ and, hence, that every element of $Q$ is of the form $a^i$ or $a^ib$ for some $i\in\{0,1,2,3\}$.

(b) Verify that the conjugacy classes of $Q$ are $C_1=\{1\}$, $C_2=\{a^2\}$, $C_3=\{a,a^3\}$, $C_4=\{b,a^2b\}$, and $C_5=\{ab,a^3b\}$.

(c) Show that $H=\{1,a^2\}$ is a normal subgroup of $Q$ for which $Q/H$ is isomorphic to $\ZZ_2\times\ZZ_2$.

(d) Give the character table for the lifting of the four linear characters of $Q/H$ to $Q$.

(e) Use parts (c) and (d) to give the complete character table for $Q$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own. The order $8$ of $Q$ is part of the statement ("the quaternion group of order $8$"), and the classes are written $C_1=\{1\}$, $C_2=\{a^2\}$, $C_3=\{a,a^3\}$, $C_4=\{b,a^2b\}$, $C_5=\{ab,a^3b\}$.

::: pf

::: {.pf-step #rewrite}
$ba=ab^3=a^3b$.

::: pf-proof
The relation $b^{-1}ab=a^3$, left-multiplied by $b$, gives $ab=ba^3$. Cubing $b^{-1}ab=a^3$ gives $b^{-1}a^3b=a^9=a$ (as $a^4=1$), and left-multiplying by $b$ gives $a^3b=ba$. Finally $b^3=b\cdot b^2=ba^2$ because $b^4=(b^2)^2=(a^2)^2=a^4=1$, so $b^3=b^{-1}=b^{-1}b^4=ba^2$; hence
$$
ab^3=a(ba^2)=(ab)a^2=(ba^3)a^2=ba^5=ba .
$$
:::

:::

::: {.pf-step #normalform}
Every element of $Q$ is $a^ib^j$ with $i\in\{0,1,2,3\}$ and $j\in\{0,1\}$, and the eight elements $1,a,a^2,a^3,b,ab,a^2b,a^3b$ are exactly the elements of $Q$.

::: pf-proof
A word in $a^{\pm1},b^{\pm1}$ can be reduced to the form $a^ib^j$: replace $a^{-1}$ by $a^3$ and $b^{-1}$ by $b^3=ba^2$ (step [](#rewrite){.pf-ref}), and move every $a$ to the left of every $b$ using $ab=ba^3$ and $ba=a^3b$ from step [](#rewrite){.pf-ref}. Then $b^2=a^2$ lets $j$ be reduced to $0$ or $1$, and $a^4=1$ lets $i$ be taken modulo $4$. So the map $(i,j)\mapsto a^ib^j$ from the eight pairs onto $Q$ is surjective, and since $\cardinality Q=8$ it is a bijection, which is the second assertion. This is part (a).
:::

:::

::: {.pf-step #center}
$a^2$ is central and $bab^{-1}=a^3$.

::: pf-proof
From $ab=ba^3$ (step [](#rewrite){.pf-ref}) one gets $bab^{-1}=a^3b b^{-1}=a^3$, using $ba=a^3b$. Then
$$
ba^2b^{-1}=(bab^{-1})^2=(a^3)^2=a^6=a^2,
$$
so $a^2$ commutes with $b$, and it commutes with $a$, hence with all of $Q$ by step [](#normalform){.pf-ref}.
:::

:::

::: {.pf-step #classes}
The sets $C_1,\dots,C_5$ are the conjugacy classes of $Q$.

::: pf-proof
$C_1=\{1\}$ is a class. $C_2=\{a^2\}$ is a class because $a^2$ is central (step [](#center){.pf-ref}). Next, $b^{-1}ab=a^3$ by hypothesis, so $a$ and $a^3$ are conjugate and $C_3$ is a single class. Also
$$
a^{-1}ba=a^3ba=a^3\cdot a^3b=a^6b=a^2b,
$$
using $ba=a^3b$ (step [](#rewrite){.pf-ref}), so $b\sim a^2b$ and $C_4$ is a class; and
$$
a^{-1}(ab)a=ba=a^3b,
$$
so $ab\sim a^3b$ and $C_5$ is a class. The five sets are disjoint and contain all eight elements by step [](#normalform){.pf-ref}, so they are all the conjugacy classes. This is part (b).
:::

:::

::: {.pf-step #quotient}
$H=\{1,a^2\}$ is normal in $Q$ and $Q/H\cong C_2\times C_2$.

::: pf-proof
$H$ is contained in the centre (step [](#center){.pf-ref}), and any subgroup of the centre is normal. In $Q/H$ the element $aH$ satisfies $(aH)^2=a^2H=H$ and $aH\ne H$ because $a\notin H$, so $aH$ has order $2$; likewise $bH$ has order $2$. Moreover $ba=a^3b$ gives $baH=a^3bH=abH$ because $a^3a^{-1}=a^2\in H$, so the two generators commute and $Q/H$ is abelian of order $4$ generated by two distinct involutions. An abelian group of order $4$ is $C_4$ or $C_2\times C_2$, and it is not $C_4$ because $C_4$ has a unique element of order $2$ while $aH\ne bH$ are two. So $Q/H\cong C_2\times C_2$. This is part (c).
:::

:::

::: {.pf-step #linear}
The four linear characters of $Q$ have the table
$$
\begin{array}{c|ccccc}
 & C_1&C_2&C_3&C_4&C_5\\ \hline
1          &1&1& 1& 1& 1\\
\chi_a     &1&1&-1& 1&-1\\
\chi_b     &1&1& 1&-1&-1\\
\chi_{ab}  &1&1&-1&-1& 1
\end{array}
$$

::: pf-proof
$Q/H=\{H,aH,bH,abH\}$, and a character of $Q/H$ inflated to $Q$ is constant on the classes $C_i$ because each $C_i$ lies in a single coset: $C_1\subseteq H$, $C_2\subseteq H$ (as $a^2\in H$), $C_3\subseteq aH$ (as $a^3a^{-1}=a^2\in H$), $C_4\subseteq bH$ (as $a^2b\,b^{-1}=a^2\in H$) and $C_5\subseteq abH$ (as $a^3b\,(ab)^{-1}=a^3bb^{-1}a^{-1}=a^2\in H$). The group $C_2\times C_2$ has the four characters $1,\chi_a,\chi_b,\chi_a\chi_b$ with $\chi_a(aH)=-1$, $\chi_a(bH)=1$, $\chi_b(aH)=1$, $\chi_b(bH)=-1$; reading each on the coset containing $C_i$ gives the displayed table, where the rows are indexed by the trivial character and by $\chi_a,\chi_b,\chi_{ab}$ so named. The naming of the three nontrivial ones is interchangeable. This is part (d).
:::

:::

::: {.pf-step #degree}
$Q$ has exactly five irreducible complex characters, and their degrees are $1,1,1,1,2$.

::: pf-proof
The number of irreducible complex characters equals the number of conjugacy classes, which is five (step [](#classes){.pf-ref}). The four characters of step [](#linear){.pf-ref} are distinct irreducible characters of degree $1$. If $d$ is the degree of the remaining one, the sum of squares of the degrees equals $\cardinality Q=8$, so $8=4+d^2$ and $d=2$.
:::

:::

::: {.pf-step #values}
The degree-$2$ irreducible character $\psi$ has $\psi(C_2)=-2$ and $\psi(C_3)=\psi(C_4)=\psi(C_5)=0$.

::: pf-proof
Write $\psi_i=\psi(C_i)$. Column orthogonality of the four linear rows against $\psi$ (equivalently, $\langle\psi,\chi\rangle=0$ for each of them) and the trivial character give, with class sizes $1,1,2,2,2$ and $\psi_1=2$,
$$
2+\psi_2+2\psi_3+2\psi_4+2\psi_5=0,\qquad
2+\psi_2-2\psi_3+2\psi_4-2\psi_5=0,
$$
$$
2+\psi_2+2\psi_3-2\psi_4-2\psi_5=0,\qquad
2+\psi_2-2\psi_3-2\psi_4+2\psi_5=0 .
$$
Adding the last three gives $3(2+\psi_2)-2(\psi_3+\psi_4+\psi_5)=0$, and the first gives $(2+\psi_2)+2(\psi_3+\psi_4+\psi_5)=0$; together these force $2+\psi_2=0$, so $\psi_2=-2$, and $\psi_3+\psi_4+\psi_5=0$. Substituting $\psi_2=-2$ in the second and third equations gives $\psi_4=\psi_3+\psi_5$ and $\psi_3=\psi_4+\psi_5$; substituting the second of these into the first gives $\psi_4=\psi_4+2\psi_5$, so $\psi_5=0$, and then $\psi_3=\psi_4$ and $2\psi_3=0$, so all three vanish.
:::

:::

::: {.pf-step #complete}
The complete character table of $Q$ is
$$
\begin{array}{c|ccccc}
 & C_1&C_2&C_3&C_4&C_5\\ \hline
1          &1& 1& 1& 1& 1\\
\chi_a     &1& 1&-1& 1&-1\\
\chi_b     &1& 1& 1&-1&-1\\
\chi_{ab}  &1& 1&-1&-1& 1\\
\psi       &2&-2& 0& 0& 0
\end{array}
$$
and $\psi$ is irreducible.

::: pf-proof
The first four rows are step [](#linear){.pf-ref}, the last is step [](#values){.pf-ref} with the degree from step [](#degree){.pf-ref}. Its norm is
$$
\frac18\Bigl(2^2+(-2)^2+2\cdot0^2+2\cdot0^2+2\cdot0^2\Bigr)=\frac18(4+4)=1,
$$
using the class sizes $1,1,2,2,2$, so $\psi$ is irreducible; with five irreducible characters in all (step [](#degree){.pf-ref}) the table is complete. This is part (e).
:::

:::

:::
:::
