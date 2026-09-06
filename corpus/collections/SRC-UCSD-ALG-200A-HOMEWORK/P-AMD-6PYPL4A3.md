---
schema: qual/card@1
id: P-AMD-6PYPL4A3
kind: problem
title: Groups of order 20
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 5, Exercise 3. Restored
    the source's explicit count of five isomorphism classes and the requirement
    to justify that the five groups are pairwise nonisomorphic.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    The unique Sylow 5-subgroup gives G=C5 semidirect P with |P|=4. For
    P=C4, actions into Aut(C5)=C4 have image order 1, 2, or 4, giving three
    classes. For P=V4, actions are trivial or have image the unique C2 in
    Aut(C5), giving two classes. The two abelian groups are separated by their
    Sylow 2-subgroups; among the nonabelian groups the V4-complement case is
    separated by Sylow type, and the two C4-complement cases by center order.
---

::: {.problem}
Classify groups of order $20$ up to isomorphism.
There are five such groups; justify that the five groups obtained are pairwise nonisomorphic.
:::

::: {.solution}
<1>1. Every group $G$ of order $20$ has a unique Sylow $5$-subgroup
\[
N\cong C_5.
\]
::: {.proof}
Let $n_5$ be the number of Sylow $5$-subgroups.
Sylow's theorem gives
\[
n_5\equiv1\pmod5
\qquad\text{and}\qquad
n_5\mid4.
\]
Among the divisors $1,2,4$ of $4$, only $1$ is congruent to $1$ modulo $5$.
Thus
\[
n_5=1.
\]
Hence the Sylow $5$-subgroup $N$ is normal, and $N\cong C_5$ because it has prime order.
:::

<1>2. If $P$ is a Sylow $2$-subgroup of $G$, then
\[
G\cong C_5\rtimes_\psi P,
\]
where
\[
P\cong C_4
\qquad\text{or}\qquad
P\cong C_2\times C_2.
\]
::: {.proof}
A Sylow $2$-subgroup $P$ has order $4$.
Since $|N|=5$ and $|P|=4$,
\[
N\cap P=\{1\}.
\]
Because $N\normal G$, the product $NP$ is a subgroup, and
\[
|NP|=|N||P|=20=|G|.
\]
Thus $G=NP$.
Conjugation by $P$ on $N$ gives a homomorphism
\[
\psi:P\longrightarrow\operatorname{Aut}(N),
\]
and the internal semidirect-product theorem yields
\[
G\cong N\rtimes_\psi P.
\]
Finally, every group of order $4$ is isomorphic to either $C_4$ or $C_2\times C_2$.
:::

<1>3. One has
\[
\operatorname{Aut}(C_5)\cong C_4.
\]
::: {.proof}
If $C_5=\langle a\rangle$, every automorphism is determined by
\[
a\longmapsto a^u,
\qquad
u\in(\mathbb Z/5\mathbb Z)^\times.
\]
Thus
\[
\operatorname{Aut}(C_5)\cong(\mathbb Z/5\mathbb Z)^\times.
\]
The latter group has four elements and is cyclic; for example, the residue class of $2$ has order $4$.
:::

<1>4. If $P\cong C_4$, there are exactly three semidirect products up to isomorphism.
::: {.proof}
Write
\[
P=\langle b\rangle\cong C_4.
\]
A homomorphism
\[
\psi:C_4\longrightarrow\operatorname{Aut}(C_5)\cong C_4
\]
is determined by $\psi(b)$.
Its image can have order $1$, $2$, or $4$.

There is one action with image order $1$, namely the trivial action.
There is one element of order $2$ in $C_4$, so there is one action with image order $2$.
There are two elements of order $4$, inverse to one another.
The corresponding two actions differ by precomposition with the automorphism
\[
b\longmapsto b^{-1}
\]
of $C_4$; hence their semidirect products are isomorphic by the change-of-action isomorphism from Exercise 1(b). Therefore there are exactly three isomorphism classes with $P\cong C_4$.
:::

<1>5. The three groups from <1>4 may be represented as
\[
\begin{aligned}
G_1&=C_5\times C_4\cong C_{20},\\
G_2&=\left\langle a,b\ \middle|\ a^5=b^4=1,\ bab^{-1}=a^{-1}\right\rangle,\\
G_3&=\left\langle a,b\ \middle|\ a^5=b^4=1,\ bab^{-1}=a^2\right\rangle.
\end{aligned}
\]
::: {.proof}
The first group is the semidirect product for the trivial action.

The unique element of order $2$ in $\operatorname{Aut}(C_5)$ is inversion
\[
a\longmapsto a^{-1},
\]
so the image-order-$2$ action gives $G_2$.

The automorphism
\[
a\longmapsto a^2
\]
has order $4$, because
\[
2^2\equiv4\not\equiv1\pmod5,
\qquad
2^4\equiv1\pmod5.
\]
Thus it gives a representative $G_3$ for the faithful action.
Each displayed presentation is the standard presentation of the corresponding semidirect product $C_5\rtimes C_4$, so each group has order $20$.
:::

<1>6. If $P\cong C_2\times C_2$, there are exactly two semidirect products up to isomorphism.
::: {.proof}
Write
\[
P=C_2\times C_2.
\]
Every element of $P$ has order dividing $2$.
Hence the image of any homomorphism
\[
\psi:P\longrightarrow\operatorname{Aut}(C_5)\cong C_4
\]
has exponent dividing $2$.
Thus the image is either trivial or equals the unique subgroup of order $2$ in $C_4$.

For a nontrivial action, the kernel has order $2$.
The automorphism group of $C_2\times C_2$ acts transitively on its three subgroups of order $2$.
Consequently any two nontrivial actions differ by precomposition with an automorphism of $P$, and Exercise 1(b) shows that their semidirect products are isomorphic.
Therefore there are exactly two isomorphism classes with $P\cong C_2\times C_2$.
:::

<1>7. The two groups from <1>6 may be represented as
\[
G_4=C_5\times C_2\times C_2
\]
and
\[
G_5
=\left\langle a,u,v\ \middle|\
 a^5=u^2=v^2=1,
 [u,v]=1,
 uau^{-1}=a^{-1},
 vav^{-1}=a
\right\rangle.
\]
::: {.proof}
The trivial action gives $G_4$.

For a nontrivial action, choose generators $u,v$ of $C_2\times C_2$ so that $u$ maps to the unique order-$2$ automorphism of $C_5$, namely inversion, and $v$ lies in the kernel.
Thus
\[
uau^{-1}=a^{-1},
\qquad
vav^{-1}=a,
\qquad
[u,v]=1.
\]
This gives the displayed presentation of $G_5$.
Equivalently,
\[
G_5\cong (C_5\rtimes C_2)\times C_2,
\]
where the first $C_2$ acts on $C_5$ by inversion.
:::

<1>8. The groups $G_1$ and $G_4$ are not isomorphic.
::: {.proof}
Both are abelian, but their Sylow $2$-subgroups have different isomorphism types:
\[
\operatorname{Syl}_2(G_1)\cong C_4,
\qquad
\operatorname{Syl}_2(G_4)\cong C_2\times C_2.
\]
An isomorphism sends Sylow $2$-subgroups to Sylow $2$-subgroups, so $G_1\not\cong G_4$.
:::

<1>9. The groups $G_2,G_3,G_5$ are nonabelian, so none is isomorphic to $G_1$ or $G_4$.
::: {.proof}
In $G_2$ and $G_5$, conjugation by the indicated element sends $a$ to $a^{-1}\ne a$.
In $G_3$, conjugation by $b$ sends $a$ to $a^2\ne a$.
Thus $G_2,G_3,G_5$ are nonabelian, whereas $G_1,G_4$ are direct products of cyclic groups and hence abelian.
:::

<1>10. The group $G_5$ is not isomorphic to either $G_2$ or $G_3$.
::: {.proof}
A Sylow $2$-subgroup of $G_5$ is
\[
\langle u,v\rangle\cong C_2\times C_2,
\]
whereas a Sylow $2$-subgroup of each of $G_2$ and $G_3$ is
\[
\langle b\rangle\cong C_4.
\]
These Sylow subgroups are not isomorphic, so $G_5$ cannot be isomorphic to $G_2$ or $G_3$.
:::

<1>11. The center of $G_2$ has order $2$.
::: {.proof}
The element $b^2$ acts trivially on $C_5$, because inversion squared is the identity.
Since $\langle b\rangle$ is abelian,
\[
b^2\in Z(G_2).
\]
Thus
\[
\langle b^2\rangle\le Z(G_2).
\]

Conversely, write an arbitrary element as $a^i b^j$ with $0\le i<5$ and $0\le j<4$.
If $a^i b^j$ commutes with $a$, then conjugation by $b^j$ fixes $a$.
The action of $b$ is inversion, so this forces $j$ to be even.
If $a^i b^j$ also commutes with $b$, then
\[
b a^i b^{-1}=a^{-i}=a^i,
\]
so
\[
2i\equiv0\pmod5,
\]
whence $i\equiv0\pmod5$.
Therefore every central element lies in $\{1,b^2\}$, and
\[
Z(G_2)=\langle b^2\rangle\cong C_2.
\]
:::

<1>12. The center of $G_3$ is trivial.
::: {.proof}
Again write an element as $a^i b^j$.
If it commutes with $a$, then the automorphism induced by $b^j$ on $C_5$ must be trivial.
The action of $b$ has order $4$, so this forces
\[
j\equiv0\pmod4.
\]
Thus a central element must have the form $a^i$.
If $a^i$ commutes with $b$, then
\[
a^i=b a^i b^{-1}=a^{2i},
\]
so
\[
i\equiv0\pmod5.
\]
Hence
\[
Z(G_3)=\{1\}.
\]
:::

<1>13. The groups $G_2$ and $G_3$ are not isomorphic.
::: {.proof}
By <1>11 and <1>12,
\[
|Z(G_2)|=2,
\qquad
|Z(G_3)|=1.
\]
Center order is an isomorphism invariant, so
\[
G_2\not\cong G_3.
\]
:::

<1>14. The five groups
\[
G_1,G_2,G_3,G_4,G_5
\]
form the complete classification of groups of order $20$ up to isomorphism.
::: {.proof}
Completeness follows from <1>1--<1>7: every group of order $20$ is $C_5\rtimes P$ with $P\cong C_4$ or $C_2\times C_2$, and all actions have been classified up to the isomorphisms of Exercise 1. Pairwise nonisomorphism follows from <1>8--<1>13. Therefore there are exactly five isomorphism classes.
:::
:::
