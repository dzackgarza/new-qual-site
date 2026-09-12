---
schema: qual/card@1
id: P-V6LPH
kind: problem
title: 'Groups of order $30$: normal subgroups of orders $3$, $5$, and $15$, presentations,
  and classification'
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Group Presentations
relations: []
review: draft
---

::: problem
Let $G$ be a group of order 30.

a. Show that $G$ contains normal subgroups of orders 3, 5, and 15.

b. Give all possible presentations and relations for $G$.

c. Determine how many groups of order 30 there are up to isomorphism.
:::

::: solution
Let $n_p$ denote the number of Sylow $p$-subgroups of $G$. Sylow's
theorems give
\[
n_3\in\{1,10\},\qquad n_5\in\{1,6\}.
\]
They cannot both be nonnormal: otherwise the ten Sylow $3$-subgroups would
contribute $10(3-1)=20$ distinct nonidentity elements of order $3$, while the
six Sylow $5$-subgroups would contribute $6(5-1)=24$ distinct nonidentity
elements of order $5$, already more than the $29$ nonidentity elements of
$G$. Hence a Sylow $3$- or Sylow $5$-subgroup is normal.

Suppose first that a Sylow $5$-subgroup $P_5$ is normal, and let $P_3$ be a
Sylow $3$-subgroup. Then $H=P_5P_3$ is a subgroup and
\[
|H|={|P_5||P_3|\over |P_5\cap P_3|}=15.
\]
The same conclusion follows with $3$ and $5$ interchanged if a Sylow
$3$-subgroup is normal. Every group of order $15$ is cyclic: inside $H$, the
Sylow counts satisfy
\[
n_5\equiv1\pmod5,\quad n_5\mid3,
\qquad
n_3\equiv1\pmod3,\quad n_3\mid5,
\]
so both Sylow subgroups are normal; their product is therefore
$C_5\times C_3\cong C_{15}$. Thus $H\cong C_{15}$, and since $[G:H]=2$,
$H\triangleleft G$.

The cyclic group $H$ has unique subgroups of orders $3$ and $5$. They are
characteristic in $H$, hence normal in $G$. This proves (a), including the
normal subgroup $H$ of order $15$.

For (b) and (c), let $H=\langle r\rangle$ with $|r|=15$. By Cauchy's theorem
$G$ contains an element $s$ of order $2$. Since $H$ has odd order,
$H\cap\langle s\rangle=1$, and therefore
\[
G=H\rtimes\langle s\rangle.
\]
Conjugation by $s$ is an automorphism of $H$, so for some
$a\in(\ZZ/15\ZZ)^\times$,
\[
srs^{-1}=r^a.
\]
Since $s^2=1$, this automorphism has square $1$, hence
$a^2\equiv1\pmod{15}$. By the Chinese remainder theorem this means
$a\equiv\pm1\pmod3$ and $a\equiv\pm1\pmod5$, giving exactly
\[
a\in\{1,4,11,14\}.
\]
Consequently every group of order $30$ has one of the four presentations
\[
\boxed{
G_a=\langle r,s\mid r^{15}=s^2=1,\ srs^{-1}=r^a\rangle,
\qquad a\in\{1,4,11,14\}.}
\]
Conversely each presentation is the semidirect product
$C_{15}\rtimes C_2$ for the indicated order-$2$ automorphism, so it has order
$30$.

These four groups are pairwise nonisomorphic. Every involution lies outside
$H$, and
\[
(sr^k)^2=r^{(a+1)k}.
\]
Thus the numbers of involutions for $a=1,4,11,14$ are respectively
\[
1,\quad 5,\quad 3,\quad 15.
\]
Hence the four presentations give four distinct isomorphism classes. More
familiarly, they are
\[
C_{30},\qquad C_3\times D_{10},\qquad C_5\times S_3,
\qquad D_{30},
\]
where $D_{10}$ and $D_{30}$ denote dihedral groups of orders $10$ and $30$.
Therefore there are exactly
\[
\boxed{4}
\]
groups of order $30$ up to isomorphism.
:::
