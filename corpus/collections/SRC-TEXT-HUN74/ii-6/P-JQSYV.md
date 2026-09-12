---
schema: qual/card@1
id: P-JQSYV
kind: problem
title: Groups of orders $18$, $20$, and $30$
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
  date: 2026-09-09
  note: Checked against a Rutgers Algebra assignment identifying the problem as Hungerford II.6.9 and against an independent Hungerford solutions-manual transcription.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Classify up to isomorphism all groups of order 18. Do the same for orders 20 and 30.
:::

::: solution
We classify each order by first finding a normal Hall subgroup and then recording
the possible conjugation actions of a complement.

<1>1. Up to isomorphism there are exactly five groups of order $18$.
::: proof
Let $|G|=18=2\cdot3^2$. By Sylow,
\[
n_3\mid2,\qquad n_3\equiv1\pmod3,
\]
so $n_3=1$. Thus the Sylow $3$-subgroup $N$ is normal and has order $9$.
By Cauchy's theorem $G$ has a subgroup $C$ of order $2$, and
$N\cap C=1$, so $G=N\rtimes C$.

There are two possibilities for $N$.

If $N\cong\ZZ_9$, then
\[
\operatorname{Aut}(N)\cong(\ZZ/9\ZZ)^\times\cong\ZZ_6.
\]
An action of $C\cong\ZZ_2$ therefore has image either trivial or the unique
subgroup of order $2$. These give
\[
\ZZ_{18}
\qquad\text{and}\qquad
\ZZ_9\rtimes_{(-1)}\ZZ_2,
\]
the latter being the dihedral group of order $18$.

If $N\cong\ZZ_3^2$, then an action of $C$ is determined by an involution in
$\operatorname{GL}_2(\FF_3)$. Since $2$ is invertible in $\FF_3$, every such
operator is diagonalizable with eigenvalues in $\{1,-1\}$. Up to conjugacy there
are exactly three possibilities:
\[
I,\qquad \operatorname{diag}(1,-1),\qquad -I.
\]
They give respectively
\[
\ZZ_3^2\times\ZZ_2,
\qquad
\ZZ_3\times S_3,
\qquad
\ZZ_3^2\rtimes_{(-I)}\ZZ_2.
\]
These five groups are pairwise nonisomorphic: the two cases with cyclic Sylow
$3$-subgroup are separated from the three with Sylow subgroup $\ZZ_3^2$; within
each case the conjugation action of an involution on that characteristic Sylow
$3$-subgroup has different fixed-space dimension (or is trivial versus
nontrivial). Hence exactly five isomorphism types occur.
:::

<1>2. Up to isomorphism there are exactly five groups of order $20$.
::: proof
Let $|G|=20=2^2\cdot5$. Sylow gives
\[
n_5\mid4,\qquad n_5\equiv1\pmod5,
\]
so $n_5=1$. Thus the Sylow $5$-subgroup
\[
N\cong\ZZ_5
\]
is normal. If $P$ is a Sylow $2$-subgroup, then $|P|=4$,
$N\cap P=1$, and $NP=G$. Hence
\[
G\cong\ZZ_5\rtimes P,
\]
where $P\cong\ZZ_4$ or $P\cong\ZZ_2^2$.

Now
\[
\operatorname{Aut}(\ZZ_5)\cong\ZZ_4.
\]
For $P\cong\ZZ_4$, the image of the action homomorphism
$P\to\ZZ_4$ can have order $1$, $2$, or $4$. Up to automorphisms of source and
target these yield exactly three groups:
\[
\ZZ_5\times\ZZ_4\cong\ZZ_{20},
\]
\[
\ZZ_5\rtimes_{(\operatorname{im}=\ZZ_2)}\ZZ_4,
\qquad
\ZZ_5\rtimes_{(\operatorname{im}=\ZZ_4)}\ZZ_4.
\]

For $P\cong\ZZ_2^2$, the image has order $1$ or $2$; all nonzero maps
$\ZZ_2^2\to\ZZ_2\le\ZZ_4$ are equivalent under
$\operatorname{Aut}(\ZZ_2^2)$. Hence there are exactly two further groups:
\[
\ZZ_5\times\ZZ_2^2,
\qquad
\ZZ_5\rtimes_{(\operatorname{im}=\ZZ_2)}\ZZ_2^2.
\]

The five are pairwise nonisomorphic. First, their Sylow $2$-subgroups distinguish
the $\ZZ_4$ cases from the $\ZZ_2^2$ cases. Within either family, the kernel (or
equivalently the image size) of the conjugation action on the characteristic
Sylow $5$-subgroup distinguishes the listed possibilities. Thus there are exactly
five groups of order $20$.
:::

<1>3. Every group of order $30$ has a normal cyclic subgroup of order $15$.
::: proof
Let $|G|=30=2\cdot3\cdot5$. Sylow gives
\[
n_5\in\{1,6\},\qquad n_3\in\{1,10\}.
\]
The alternatives $n_5=6$ and $n_3=10$ cannot both occur, because the six Sylow
$5$-subgroups contribute $6(5-1)=24$ nonidentity elements and the ten Sylow
$3$-subgroups contribute $10(3-1)=20$ distinct nonidentity elements, already
more than $29$.

Thus at least one of the Sylow $3$- and $5$-subgroups is normal. Let $P_5$ and
$P_3$ be Sylow subgroups. If both are normal, then $P_3P_5$ is a subgroup of
order $15$. If only $P_3$ is normal, then conjugation by $P_5$ on $P_3$ gives a
homomorphism
\[
P_5\to\operatorname{Aut}(P_3)\cong\ZZ_2,
\]
which is trivial because $|P_5|=5$; hence $P_5$ normalizes and centralizes
$P_3$, so again $P_3P_5$ is a subgroup of order $15$. Similarly, if only $P_5$
is normal, conjugation by $P_3$ on $P_5$ maps a group of order $3$ into
\operatorname{Aut}(\ZZ_5)\cong\ZZ_4$ and is trivial, so $P_3P_5$ is again a
subgroup of order $15$.

Call this subgroup $N$. Since $[G:N]=2$, it is normal. Also any group of order
$15$ is cyclic: its Sylow $5$-subgroup is normal, and its Sylow $3$-subgroup
acts trivially on it because there is no element of order $3$ in
$\operatorname{Aut}(\ZZ_5)$. Hence
\[
N\cong\ZZ_{15}.
\]
:::

<1>4. Up to isomorphism there are exactly four groups of order $30$.
::: proof
By <1>3, $G$ has a normal subgroup $N\cong\ZZ_{15}$. Cauchy's theorem supplies
an involution $t\in G$, necessarily outside the odd-order subgroup $N$. Thus
\[
G\cong\ZZ_{15}\rtimes\ZZ_2.
\]

By the Chinese remainder theorem,
\[
\operatorname{Aut}(\ZZ_{15})
\cong\operatorname{Aut}(\ZZ_3)\times\operatorname{Aut}(\ZZ_5)
\cong\ZZ_2\times\ZZ_4.
\]
An action of $\ZZ_2$ is determined by an element of order dividing $2$. There
are exactly four such elements: the identity, inversion on the $3$-part only,
inversion on the $5$-part only, and inversion on both parts. Therefore the four
groups are
\[
\ZZ_{30},
\qquad
S_3\times\ZZ_5,
\qquad
\ZZ_3\times(\ZZ_5\rtimes_{(-1)}\ZZ_2),
\qquad
\ZZ_{15}\rtimes_{(-1)}\ZZ_2.
\]
The last two may be described as the product of $\ZZ_3$ with the dihedral group
of order $10$, and the dihedral group of order $30$, respectively.

These groups are pairwise nonisomorphic because the action of an involution on
the characteristic subgroups of orders $3$ and $5$ is respectively trivial or
inversion in the four distinct combinations. Hence there are exactly four
isomorphism types of groups of order $30$.
:::
:::
