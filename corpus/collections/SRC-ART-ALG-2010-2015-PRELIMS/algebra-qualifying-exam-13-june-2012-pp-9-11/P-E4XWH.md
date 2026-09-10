---
schema: qual/card@1
id: P-E4XWH
kind: problem
title: A nonabelian group with all proper subgroups normal, abelian groups with non-normal
  subgroups, groups of order $p^2$, missing subgroup orders, infinite torsion groups,
  and non-isomorphic subgroups of order $p^k$
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Counterexamples
  - Normal Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared all six requests with June 2012 Groups 2 in the retained extraction and corrected the generic prelim classification to algebra."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked every possible proper subgroup order in Q8, the center argument for order p squared, the induction for every divisor of an abelian group order, and the exact subgroup types in the order-eight example."
---

::: {.problem}
For each of the following, either give an example or explain why no such example exists.
One or two sentence answers will suffice; you don't need to give formal proofs.

a. A non-abelian group all of whose proper subgroups are normal.

b. An abelian group with a subgroup which is not normal.

c. A non-abelian group of order $p^2$ where $p$ is prime.

d. An abelian group $G$ of order $n$ and a divisor $d$ of $n$ such that $G$ has no subgroup of order $d$.

e. An infinite group all of whose elements have finite order.

f. A prime $p$ and a finite group $G$ of order $p^{k+1}m$ where $p$ does not divide $m$, such that $G$ has non-isomorphic subgroups of order $p^k$.
:::

::: solution
Write $C_r=\mathbb Z/r\mathbb Z$.

<1>1. In part (a), the quaternion group $Q_8$ is an example.

::: proof
The quaternion group is
$Q_8=\{1,-1,i,-i,j,-j,k,-k\}$, with
$i^2=j^2=k^2=-1$, $ij=k$, and $ji=-k$ [@DF04].
Thus it is nonabelian. By Lagrange's theorem, a proper
subgroup has order $1$, $2$, or $4$.
The identity subgroup is normal. The only element of order
$2$ is $-1$, since each of $\pm i,\pm j,\pm k$ squares
to $-1$. Hence the only subgroup of order $2$ is
$\{1,-1\}$, which is central and normal.
Every subgroup of order $4$ has index $2$ and is normal:
for an element outside it, the left and right cosets are
both its complement. This covers all proper subgroup orders.
:::

<1>2. No example exists in part (b).

::: proof
If $G$ is abelian and $H\leq G$, then $ghg^{-1}=h$ for
every $g\in G$ and $h\in H$. Hence $gHg^{-1}=H$ for
every $g$, so every subgroup is normal.
:::

<1>3. No example exists in part (c): every group of order
$p^2$ is abelian.

::: proof
For a noncentral element, the size of its conjugacy class
is $[G:C_G(g)]$, a power of $p$ greater than $1$, so it
is divisible by $p$. Splitting $G$ into conjugacy classes
therefore gives $|G|\equiv|Z(G)|\pmod p$.
The center contains the identity, and its order divides
$p^2$. Consequently $|Z(G)|$ is $p$ or $p^2$.

If $|Z(G)|=p^2$, then $G=Z(G)$ is abelian. Otherwise
$G/Z(G)$ has prime order and is cyclic. Choose $g\in G$
whose coset generates this quotient. Every element of $G$
is $g^a z$ for some integer $a$ and $z\in Z(G)$.
Two such elements commute, because their powers of $g$
commute and their central factors commute with everything.
Thus $G$ is abelian in this case as well.
:::

<1>4. No example exists in part (d).

::: proof
We prove by induction on $|G|$ that every finite abelian
group has a subgroup of each positive order dividing $|G|$.
For $d=1$, the identity subgroup works; this includes the
base case $|G|=1$.

Suppose $d>1$ and choose a prime $p\mid d$. Since
$p\mid|G|$, Cauchy's theorem supplies an element of order
$p$, generating a subgroup $N$ of order $p$ [@DF04].
It is normal because $G$ is abelian. The quotient $G/N$
is abelian of order $|G|/p<|G|$, and $d/p$ divides its
order. By induction it has a subgroup $\overline H$ of
order $d/p$. The inverse image of $\overline H$ in $G$
is a subgroup consisting of $d/p$ cosets of $N$, each
of size $p$. Its order is $d$, as required.
:::

<1>5. In part (e), take $\bigoplus_{n\geq1}C_2$.

::: proof
This is the group of sequences $(a_1,a_2,\ldots)$ with
$a_n\in\mathbb Z/2\mathbb Z$ and only finitely many
nonzero coordinates, under coordinatewise addition.
It is infinite because the sequences having a single $1$
in position $n$ are distinct as $n$ varies. Every element
added to itself is zero, so every element has order $1$
or $2$, and in particular finite order.
:::

<1>6. In part (f), take $p=2$, $k=2$, $m=1$, and
$G=C_4\times C_2$.

::: proof
This group has order $8=2^{2+1}\cdot1$, with $2\nmid1$.
The subgroup $H_1=\langle(1,0)\rangle$ has order $4$
and is cyclic. The subgroup
$$
H_2=\langle(2,0),(0,1)\rangle
=\{(0,0),(2,0),(0,1),(2,1)\}
$$
also has order $4=2^k$, but every nonidentity element
has order $2$. Thus $H_2\cong C_2\times C_2$ and
$H_1\cong C_4$ are not isomorphic, since an isomorphism
preserves element orders.
:::
:::
