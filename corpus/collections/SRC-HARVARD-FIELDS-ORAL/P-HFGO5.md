---
schema: qual/card@1
id: P-HFGO5
kind: problem
title: A quadratic intermediate field in a quartic extension
classification:
  areas: [algebra]
  topics: [Galois Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Fields and Galois Theory oral-question extraction; the local statement resolves the extraction's garbled intermediate-field notation as F subset L subset E with [L:F]=2.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
In the preceding quartic-extension problem, suppose there is an intermediate field $F\subseteq L\subseteq E$ with $[L:F]=2$.
Improve the bound on the normal-closure degree and describe the corresponding Galois group constraints.
:::

::: solution
In this situation
\[
[K:F]=8,
\]
and
\[
\operatorname{Gal}(K/F)\cong D_8,
\]
the transitive dihedral subgroup of $S_4$ of order $8$.

<1>1. The quadratic extension $L/F$ is Galois.
::: proof
The extension $L/F$ is separable because $L$ lies in the separable extension
$E/F$. A separable quadratic extension is normal: if
\[
m(x)=x^2+ax+b
\]
is the minimal polynomial of a generator and one root $\lambda$ lies in $L$,
then its other root $-a-\lambda$ also lies in $L$. Hence $L/F$ is Galois.
:::

<1>2. Let
\[
G=\operatorname{Gal}(K/F),
\quad
H=\operatorname{Gal}(K/E),
\quad
J=\operatorname{Gal}(K/L).
\]
Then $H\le J\trianglelefteq G$, with
\[
[G:H]=4,
\qquad
[G:J]=2.
\]
::: proof
The inclusions reverse under the Galois correspondence. The two index formulas
are the degrees $[E:F]=4$ and $[L:F]=2$. By <1>1, $L/F$ is Galois, so its
corresponding subgroup $J$ is normal in $G$.
:::

<1>3. In the transitive action of $G$ on the four cosets $G/H$, the subgroup
$J$ produces a $G$-invariant partition into two blocks of size $2$.
::: proof
The two cosets of $J$ in $G$ partition the four cosets of $H$ into two sets,
each containing
\[
[J:H]=\frac{[G:H]}{[G:J]}=2
\]
points. Since $J\trianglelefteq G$, left multiplication by $G$ permutes these
two sets. Thus the degree-$4$ permutation action is imprimitive with a block
system of type $2+2$.
:::

<1>4. Hence $G$ embeds in
\[
S_2\wr S_2\cong D_8,
\]
so $|G|\le8$.
::: proof
The full subgroup of $S_4$ preserving a fixed partition into two unordered
pairs is the wreath product $S_2\wr S_2$, of order
\[
2^2\cdot2=8.
\]
By <1>3, the image of $G$ preserves such a partition.
:::

<1>5. Since $E/F$ is nonnormal, $|G|\ne4$; therefore $|G|=8$.
::: proof
The action on four points is transitive, so $4\mid |G|$. By <1>4,
$|G|\le8$, hence $|G|$ is $4$ or $8$. If $|G|=4$, then
\[
[K:F]=[E:F]=4
\]
and $E=K$, contradicting that $E/F$ is nonnormal. Therefore $|G|=8$.
:::

<1>6. The transitive subgroup $G\le S_4$ of order $8$ is a Sylow
$2$-subgroup of $S_4$, hence isomorphic to $D_8$.
::: proof
The $2$-part of $|S_4|=24$ is $8$. Thus a subgroup of order $8$ is Sylow, and
the Sylow $2$-subgroups of $S_4$ are dihedral of order $8$.
:::
:::
