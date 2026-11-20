---
schema: qual/card@1
id: P-APA17D
kind: problem
title: Character table of the quaternion group $Q_8$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 4 of the Qualifying Exam in Applied Algebra of May 30, 2017, printed p.
    4 of the nine-page paper retained at assets/attachments/APPLIED-ALGEBRA-EXAM.pdf, is the statement
    the card answers, and the paragraph at the head of the solution records that the paper prints no
    solutions, so the argument is the card's own. Checked: the statement against the paper's text layer
    at the page named; the printed presentation of Q_8 against the classes used, and the completed
    character table; `qualc.authoring check` on the card. The card carries no `pf` block, so `tmp/lam.sh`
    does not apply to it and was not run. Not checked: no retained solution set exists for this paper to compare the argument with, and
    no other card of the collection in this pass.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step, and one sentence was
    left unfinished ("...the two-dimensional irreducible representation"). It is now a `pf` with
    seven steps, each carrying a `pf-proof`, and the unfinished sentence is completed by the
    enumeration itself. The character table is unchanged. Cited by number only: the count of
    irreducible characters and the degree-sum formula for a finite group, the orthogonality
    relations, the correspondence between one-dimensional characters and the abelianisation, and
    von Dyck's theorem for the explicit two-dimensional representation. Checked: that the three
    pairs $\{\pm i\},\{\pm j\},\{\pm k\}$ are classes of size $2$, that the four rows listed are
    homomorphisms on $C_2\times C_2$, that the orthogonality equations force $a=b=c=0$, and that
    $A,B$ satisfy $A^2=B^2=-I_2$ and $BA=-AB$.
---

::: {.problem}
Let $Q_8$ denote the quaternion group $Q_8 = \{\pm 1, \pm i, \pm j, \pm k\}$ with the usual multiplication
$$
(-1)^2 = 1,\quad
(-1)i = -i = i(-1),\quad
(-1)j = -j = j(-1),\quad
(-1)k = -k = k(-1),
$$
$$
i^2 = j^2 = k^2 = -1,\quad
ij = k = -ji,\quad
ki = j = -ik,\quad
jk = i = -kj.
$$
Calculate the character table of $Q_8$.
:::

::: {.solution}

The problem is Problem 4 of the Qualifying Exam in Applied Algebra of May 30, 2017, of the nine-page paper retained at `assets/attachments/APPLIED-ALGEBRA-EXAM.pdf`. The paper prints no solutions, so nothing below is transcribed: the argument is the card's own, and what it supplies is the character table itself.

::: pf

::: pf-step

The conjugacy classes are
$$
\{1\},\qquad \{-1\},\qquad \{\pm i\},\qquad \{\pm j\},\qquad \{\pm k\},
$$
so $Q_8$ has five irreducible complex characters.

::: pf-proof

$\pm1$ are central, so each of $\{1\}$ and $\{-1\}$ is a class. For the others, conjugation by an element $g$ is an automorphism fixing $\pm1$, hence carries squares to squares: $gag^{-1}$ has square $g a^2 g^{-1}=-1$ whenever $a^2=-1$, so the three elements of square $-1$ other than $\pm i$ are the only candidates, and $gig^{-1}=i$ or $-i$; hence each pair $\{\pm i\}$, $\{\pm j\}$, $\{\pm k\}$ is a union of classes. None of the three pairs is a single class because $i$ and $-i$ are not conjugate: an element conjugating $i$ to $-i$ would need $jij^{-1}=\pm i$ with the minus sign, and $jij^{-1}=-i$ indeed, so the pair is one class of size $2$. Thus there are five classes, and a finite group has as many irreducible complex characters as conjugacy classes (the row orthogonality of the character table), so five.

:::

:::

::: pf-step

The commutator subgroup is $\{\pm1\}$, so the abelianisation is
$$
Q_8/\{\pm1\}\cong C_2\times C_2,
$$
and hence there are four one-dimensional characters.

::: pf-proof

The quotient $Q_8/\{\pm1\}$ has the four elements $\pm1,\pm i,\pm j,\pm k$ modulo sign, and its multiplication is that of the Klein four-group: $i^2=j^2=k^2=1$ and $ij=k$. The commutator subgroup of a group is the smallest normal subgroup with abelian quotient, and here the quotient by $\{\pm1\}$ is abelian while the quotient by $\{1\}$ is not, so $[Q_8,Q_8]=\{\pm1\}$; concretely $iji^{-1}j^{-1}=ij(-i)(-j)=ijij=k^2=-1$. One-dimensional characters are exactly the characters of the abelianisation, and a group of order $4$ that is not cyclic — here $C_2\times C_2$, since every nonidentity element has order $2$ — has four of them.

:::

:::

::: pf-step

Writing the three nontrivial quotient characters by their values on the images of $i,j$,
$$
\begin{array}{c|ccccc}
 & 1 & -1 & \{\pm i\} & \{\pm j\} & \{\pm k\}\\ \hline
\chi_1 & 1&1&1&1&1\\
\chi_2 & 1&1&1&-1&-1\\
\chi_3 & 1&1&-1&1&-1\\
\chi_4 & 1&1&-1&-1&1
\end{array}
$$
where the value on $\pm k$ is the product of the values on $i$ and $j$.

::: pf-proof

A character of the quotient $C_2\times C_2$ is determined by its two values on the generators $\bar i,\bar j$, each $\pm1$, and $\bar k=\bar i\bar j$ forces the value there to be the product. This gives the four rows listed, with $\chi_1$ the trivial character, and each row is a homomorphism because the target $\{\pm1\}$ is abelian. On $-1$ — the identity of the quotient, since $-1\in\{\pm1\}$ — every character takes the value $1$, which is the second column.

:::

:::

::: pf-step

The sum of squares of the irreducible degrees is $\cardinality{Q_8}=8$; the four linear characters contribute $4$, so the remaining irreducible has degree $2$.

::: pf-proof

For a finite group the sum of the squares of the degrees of the irreducible complex characters equals the order of the group, and the number of irreducibles equals the number of classes, five by step 1. Four of them are linear by step 2, so $1+1+1+1+d^2=8$ with $d\ge1$ an integer, giving $d=2$.

:::

:::

::: pf-step

Let $\chi_5$ be that character. Orthogonality with $\chi_1,\dots,\chi_4$, together with the class sizes $1,1,2,2,2$, forces
$$
\chi_5=(2,-2,0,0,0).
$$

::: pf-proof

The inner product of characters is $\langle\chi,\psi\rangle=\frac1{\abs{G}}\sum_{g}\chi(g)\overline{\psi(g)}$, which with the class sizes $1,1,2,2,2$ is $\frac18\bigl(1\cdot\chi(1)\overline{\psi(1)}+1\cdot\chi(-1)\overline{\psi(-1)}+2\sum_{C}\chi(C)\overline{\psi(C)}\bigr)$ over the three pairs. Orthogonality to the trivial character $\chi_1$ gives $\frac18(2-2+2(a+b+c))=0$ where $a,b,c$ are the values of $\chi_5$ on $\{\pm i\},\{\pm j\},\{\pm k\}$; orthogonality to $\chi_2,\chi_3,\chi_4$ gives $\frac18(2-2+2(-a-b+c))=0$, $\frac18(2-2+2(-a+b-c))=0$ and $\frac18(2-2+2(a-b-c))=0$. Adding and subtracting these three relations gives $a=b=c=0$, and then the first relation gives $2-2=0$ automatically. The value at $1$ is the degree, $2$, and the value at $-1$ is fixed by orthogonality to $\chi_1$ to be $-2$. Hence $\chi_5=(2,-2,0,0,0)$, and $\langle\chi_5,\chi_5\rangle=\frac18(4+4)=1$, so it is irreducible.

:::

:::

::: pf-step

Equivalently, one may realize it by
$$
i\mapsto \begin{pmatrix} i&0\\0&-i\end{pmatrix},\qquad
j\mapsto \begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$
for which $-1\mapsto -I_2$ and all of $\pm i,\pm j,\pm k$ have trace $0$.

::: pf-proof

Set $A=\operatorname{diag}(i,-i)$ and $B=\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}$. Then $A^2=B^2=-I_2$, $AB=\begin{psmallmatrix}0&i\\ i&0\end{psmallmatrix}$ and $BA=-AB$, so $A,B,AB$ give a representation of the presentation of $Q_8$ (von Dyck's theorem), with $-1\mapsto -I_2$. The traces are $\operatorname{tr}A=\operatorname{tr}(-A)=0$, likewise for $B$ and $AB$, and $\operatorname{tr}(\pm I_2)=\pm2$. So the character of this representation is $(2,-2,0,0,0)$, which is $\chi_5$.

:::

:::

::: pf-step

Therefore the complete character table is
$$
\begin{array}{c|ccccc}
 & 1 & -1 & \{\pm i\} & \{\pm j\} & \{\pm k\}\\ \hline
\chi_1 & 1&1&1&1&1\\
\chi_2 & 1&1&1&-1&-1\\
\chi_3 & 1&1&-1&1&-1\\
\chi_4 & 1&1&-1&-1&1\\
\chi_5 & 2&-2&0&0&0
\end{array}.
$$

::: pf-proof

The five rows are the four linear characters of steps 2 and 3 and the degree-$2$ character of steps 4 and 5, realized by step 6. Steps 1 and 4 account for all five irreducible characters, so the table is complete, and its rows are pairwise orthogonal by construction.

:::

:::

:::
:::
