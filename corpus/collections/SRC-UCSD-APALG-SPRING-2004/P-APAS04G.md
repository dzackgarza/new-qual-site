---
schema: qual/card@1
id: P-APAS04G
kind: problem
title: Character table of the order-$8$ group with $a^4=1$, $a^2=b^2$, $b^{-1}ab=a^3$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
  - Group Theory
relations: []
review: draft
---

::: problem
Let $G$ be the group of order $8$ defined by the relations
\[
a^4=1\quad\text{and}\quad a^2=b^2\quad\text{and}\quad b^{-1}ab=a^3.
\]

(a) Show that $ab=b^3a$ and that every element of $G$ is of the form $b^k$ or $b^ka$ where $k=0,\ldots,3$.

(b) Given that the conjugacy classes of $G$ are
\begin{align*}
C_1&=\{1\},\\
C_2&=\{b^2\},\\
C_3&=\{b,b^3\},\\
C_4&=\{a,b^2a\},\\
C_5&=\{ba,b^3a\},
\end{align*}

(i) Show that $H=\{1,b^2\}$ is a normal subgroup of $G$ for which $G/H$ is isomorphic to $Z_2\times Z_2$.

(ii) Give the character character table for the lifting of the $4$ linear characters of $G/H$ to $G$.

(iii) Find the complete character table for $G$.
:::

::: {.solution}
<1>1. The relations imply
\[
ab=b^3a,
\]
and every element of $G$ has the form $b^k$ or $b^ka$ with $0\le k<4$.
::: {.proof}
From
\[
b^{-1}ab=a^3
\]
we get
\[
ab=ba^3.
\]
Also $a^2=b^2$. Since
\[
b^{-1}a^2b=(b^{-1}ab)^2=a^6=a^2,
\]
the element $a^2=b^2$ is central. Hence
\[
ba^3=ba^2a=bb^2a=b^3a,
\]
so $ab=b^3a$.

Using this relation, every word in $a,b$ can be moved into the form $b^ka^\varepsilon$ with $\varepsilon\in\{0,1\}$: replace every occurrence of $a^2$ by $b^2$ and move the remaining $a$ to the right. Since $b^4=(b^2)^2=(a^2)^2=a^4=1$, we may take $0\le k<4$. The problem states that $|G|=8$, so these eight normal forms are precisely all elements of $G$.
:::

<1>2. The subgroup
\[
H=\{1,b^2\}
\]
is normal, and
\[
G/H\cong C_2\times C_2.
\]
::: {.proof}
The element $b^2=a^2$ is central by <1>1, so $H\trianglelefteq G$.
In the quotient,
\[
(aH)^2=a^2H=H,
\qquad
(bH)^2=b^2H=H.
\]
Moreover $G/H$ has order $4$. It is not cyclic: every nonidentity element has order $2$. Hence
\[
G/H\cong C_2\times C_2.
\]
:::

<1>3. The four linear characters lifted from $G/H$ have the following values on the five conjugacy classes:
\[
\begin{array}{c|rrrrr}
& C_1 & C_2 & C_3 & C_4 & C_5\\ \hline
\chi_0&1&1&1&1&1\\
\chi_1&1&1&-1&1&-1\\
\chi_2&1&1&1&-1&-1\\
\chi_3&1&1&-1&-1&1
\end{array}.
\]
::: {.proof}
Every linear character of $C_2\times C_2$ is determined by independently sending the two generators $bH$ and $aH$ to $\pm1$. All such characters are trivial on $H$, so they take value $1$ on $C_1$ and $C_2$.
The classes $C_3,C_4,C_5$ map respectively to $bH,aH,baH$, giving exactly the four rows displayed above.
:::

<1>4. There is a two-dimensional representation $\rho$ of $G$ given by
\[
\rho(a)=
\begin{pmatrix}
i&0\\
0&-i
\end{pmatrix},
\qquad
\rho(b)=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}.
\]
Its character has values
\[
\chi_4=(2,-2,0,0,0)
\]
on $C_1,\ldots,C_5$.
::: {.proof}
Both matrices square to $-I$, so
\[
\rho(a)^2=\rho(b)^2=-I,
\qquad
\rho(a)^4=I.
\]
A direct multiplication gives
\[
\rho(b)^{-1}\rho(a)\rho(b)=\rho(a)^{-1}=\rho(a)^3,
\]
so the defining relations of $G$ are satisfied.

The traces are
\[
\operatorname{tr}I=2,
\qquad
\operatorname{tr}(-I)=-2,
\]
and each of $\rho(a),\rho(b),\rho(ba)$ has trace $0$. Since character values are constant on conjugacy classes, this gives the stated row.
:::

<1>5. The representation $\rho$ is irreducible, and the complete character table of $G$ is
\[
\boxed{
\begin{array}{c|rrrrr}
& C_1 & C_2 & C_3 & C_4 & C_5\\
\text{class size}&1&1&2&2&2\\ \hline
\chi_0&1&1&1&1&1\\
\chi_1&1&1&-1&1&-1\\
\chi_2&1&1&1&-1&-1\\
\chi_3&1&1&-1&-1&1\\
\chi_4&2&-2&0&0&0
\end{array}.}
\]
::: {.proof}
For $\chi_4$,
\[
\langle\chi_4,\chi_4\rangle
=\frac1{8}(4+4)=1,
\]
so $\rho$ is irreducible.
The four linear characters are irreducible automatically. Their degree squares sum to
\[
1+1+1+1+4=8=|G|,
\]
so these five irreducibles exhaust all irreducible representations of $G$.
:::
:::
