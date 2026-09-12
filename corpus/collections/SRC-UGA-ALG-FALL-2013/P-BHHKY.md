---
schema: qual/card@1
id: P-BHHKY
kind: problem
title: Classification of groups of order $30$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
---

::: problem
Let $G$ be a group of order 30.

a. Show that $G$ has a subgroup of order 15.

b. Show that every group of order 15 is cyclic.

c. Show that $G$ is isomorphic to some semidirect product $\ZZ_{15} \semidirect \ZZ_2$.

d. Exhibit three nonisomorphic groups of order 30 and prove that they are not isomorphic.
You are not required to use your answer to (c).
:::

::: solution
(a) Let $n_p$ be the number of Sylow $p$-subgroups of $G$. Sylow's theorems
give
\[
n_3\in\{1,10\},\qquad n_5\in\{1,6\}.
\]
They cannot both be nonnormal, since otherwise the Sylow $3$-subgroups would
contribute $10(3-1)=20$ distinct nonidentity elements of order $3$ and the
Sylow $5$-subgroups would contribute $6(5-1)=24$ distinct nonidentity
elements of order $5$.

Thus a Sylow $3$- or Sylow $5$-subgroup is normal. Multiplying that normal
Sylow subgroup by a Sylow subgroup for the other prime gives a subgroup $H$
of order $15$.

(b) If $|H|=15$, then
\[
n_5\equiv1\pmod5,\quad n_5\mid3,
\qquad
n_3\equiv1\pmod3,\quad n_3\mid5.
\]
Hence both Sylow subgroups are unique and normal. Their intersection is
trivial, so they commute, and
\[
H\cong C_5\times C_3\cong C_{15}.
\]

(c) The subgroup $H$ from (a) has index $2$, so $H\triangleleft G$. By (b),
$H\cong C_{15}$. By Cauchy's theorem $G$ contains an element $s$ of order
$2$. Since $H$ has odd order,
\[
H\cap\langle s\rangle=1,
\]
and $|H\langle s\rangle|=30$, so $G=H\langle s\rangle$. Therefore
\[
G\cong C_{15}\rtimes C_2.
\]

(d) Three examples are
\[
C_{30},\qquad C_3\times D_{10},\qquad D_{30},
\]
where $D_{10}$ and $D_{30}$ denote the dihedral groups of orders $10$ and
$30$. They have respectively $1$, $5$, and $15$ elements of order $2$:
$C_{30}$ has its unique element of order $2$; $C_3\times D_{10}$ has one
involution for each of the five reflections of $D_{10}$; and all fifteen
reflections in $D_{30}$ are involutions. Hence these groups are pairwise
nonisomorphic.
:::
