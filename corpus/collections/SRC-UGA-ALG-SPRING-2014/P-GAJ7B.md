---
schema: qual/card@1
id: P-GAJ7B
kind: problem
title: Structure of a Sylow $3$-subgroup of $S_9$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Permutations
  - Group Presentations
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $G\subset S_9$ be a Sylow-3 subgroup of the symmetric group on 9 letters.

a. Show that $G$ contains a subgroup $H$ isomorphic to $\ZZ_3 \cross \ZZ_3 \cross \ZZ_3$ by exhibiting an appropriate set of cycles.

b. Show that $H$ is normal in $G$.

c. Give generators and relations for $G$ as an abstract group, such that all generators have order 3. Also exhibit elements of $S_9$ in cycle notation corresponding to these generators.

d. Without appealing to the previous parts of the problem, show that $G$ contains an element of order 9.
:::

::: {.solution}
The $3$-part of $9!$ is
\[
3^{\lfloor9/3\rfloor+\lfloor9/9\rfloor}=3^4,
\]
so a Sylow $3$-subgroup of $S_9$ has order $81$. Since all Sylow $3$-subgroups are conjugate, after relabeling the letters we may work with the standard one below.

Set
\[
a=(123),\qquad b=(456),\qquad c=(789).
\]
These cycles are disjoint, so they commute and each has order $3$. Hence
\[
H=\langle a,b,c\rangle\cong C_3^3
\]
has order $27$.

Let
\[
d=(147)(258)(369).
\]
Then $d$ has order $3$ and conjugation cyclically permutes the three generators:
\[
dad^{-1}=b,\qquad dbd^{-1}=c,\qquad dcd^{-1}=a.
\]
Thus $d$ normalizes $H$. Since $d\notin H$,
\[
G_0=\langle H,d\rangle=H\rtimes\langle d\rangle
\]
has order $27\cdot3=81$, so it is a Sylow $3$-subgroup. Any given Sylow $3$-subgroup $G$ is conjugate to $G_0$, and the conjugate of $H$ supplies the subgroup requested in (a). Also $H\triangleleft G_0$; equivalently, in any Sylow $G$, the corresponding subgroup has index $3$, hence is normal in the $3$-group $G$.

An abstract presentation is
\[
\begin{aligned}
G\cong\langle a,b,c,d\mid {}&a^3=b^3=c^3=d^3=1,\\
&[a,b]=[a,c]=[b,c]=1,\\
&dad^{-1}=b,\ dbd^{-1}=c,\ dcd^{-1}=a\rangle.
\end{aligned}
\]
All generators have order $3$, and the displayed cycles realize them in $S_9$.

For (d), independently of the preceding construction, the $9$-cycle
\[
z=(1\ 2\ 3\ 4\ 5\ 6\ 7\ 8\ 9)
\]
has order $9$. Its cyclic subgroup is a $3$-subgroup of $S_9$, hence lies in some Sylow $3$-subgroup $P$. Since all Sylow $3$-subgroups are conjugate, for the given $G$ there is $g\in S_9$ with $gPg^{-1}=G$. Then $gzg^{-1}\in G$ has order $9$.
:::
