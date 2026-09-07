---
schema: qual/card@1
id: P-ALGF06C
kind: problem
title: "Center of a group with cyclic central quotient and p-groups of order p^3"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 2.1 of the official UCSD Algebra Qualifying Examination, Fall 2006; all three parts agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the cyclic-central-quotient argument, the class-equation proof for groups of order p^3, and the D_8 times C_2 example with center C_2 times C_2.
---

::: {.problem}
Let $G$ be a group and let $Z(G)$ denote its center.

(a) Show that if $G/Z(G)$ is cyclic then $G = Z(G)$.

(b) Show that if $\operatorname{card}(G) = p^3$ for some prime number $p$ and $G$ is non-commutative, then $\operatorname{card}(Z(G)) = p$.

(c) Construct a non-commutative group $G$ of cardinality (order) 16 whose center $Z(G)$ is not cyclic.
:::


::: {.solution}
<1>1. If $G/Z(G)$ is cyclic, then $G$ is abelian and hence $G=Z(G)$.
::: {.proof}
Suppose
\[
G/Z(G)=\langle gZ(G)\rangle.
\]
For arbitrary $a,b\in G$, there are integers $r,s$ and elements $z_1,z_2\in Z(G)$ such that
\[
a=g^r z_1,
\qquad
b=g^s z_2.
\]
Since $z_1,z_2$ commute with every element of $G$,
\[
ab
=g^{r+s}z_1z_2
=g^{s+r}z_2z_1
=ba.
\]
Thus every pair of elements of $G$ commutes, so $G$ is abelian.
Therefore every element lies in the center and
\[
G=Z(G).
\]
:::

<1>2. If $|G|=p^3$ and $G$ is noncommutative, then $|Z(G)|=p$.
::: {.proof}
Let $G$ act on itself by conjugation.
For $g\in G$, the conjugacy class of $g$ has cardinality
\[
[G:C_G(g)].
\]
If $g\notin Z(G)$, then $C_G(g)$ is a proper subgroup of the $p$-group $G$, so
\[
[G:C_G(g)]
\]
is a positive power of $p$ and is therefore divisible by $p$.
The class equation consequently gives
\[
|G|
=|Z(G)|+
\sum_{\text{noncentral classes }C}|C|,
\]
where every summand in the sum is divisible by $p$.
Since $|G|=p^3$ is divisible by $p$, it follows that $p$ divides $|Z(G)|$.
Hence
\[
|Z(G)|\in\{p,p^2,p^3\}.
\]

The case $|Z(G)|=p^3$ would give $Z(G)=G$, contrary to the hypothesis that $G$ is noncommutative.
If $|Z(G)|=p^2$, then
\[
|G/Z(G)|=p,
\]
so $G/Z(G)$ is cyclic.
By <1>1 this would again imply $G=Z(G)$, a contradiction.
Therefore the only possibility is
\[
|Z(G)|=p.
\]
:::

<1>3. There is a noncommutative group of order $16$ whose center is not cyclic.
::: {.proof}
Let
\[
D_8=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle
\]
be the dihedral group of order $8$, and let $C_2=\langle t\mid t^2=1\rangle$.
Set
\[
G:=D_8\times C_2.
\]
Then
\[
|G|=8\cdot2=16,
\]
and $G$ is noncommutative because $D_8$ is noncommutative.

We first compute the center of $D_8$.
The elements $1$ and $r^2$ commute with both $r$ and $s$, so
\[
\{1,r^2\}\subseteq Z(D_8).
\]
If $r^k$ commutes with $s$, then
\[
r^k=s r^k s=r^{-k},
\]
so $2k\equiv0\pmod4$, and hence $k\equiv0$ or $2\pmod4$.
On the other hand, no element $r^k s$ commutes with $r$, because
\[
r(r^k s)=r^{k+1}s,
\qquad
(r^k s)r=r^{k-1}s,
\]
and equality would imply $r^2=1$, which is false in $D_8$.
Thus
\[
Z(D_8)=\{1,r^2\}\cong C_2.
\]

For direct products,
\[
Z(H\times K)=Z(H)\times Z(K),
\]
because $(h,k)$ commutes with every $(h',k')$ exactly when $h$ commutes with every $h'$ and $k$ commutes with every $k'$.
Since $C_2$ is abelian,
\[
Z(G)
=Z(D_8)\times C_2
\cong C_2\times C_2.
\]
The group $C_2\times C_2$ is not cyclic, so this $G$ has all the required properties.
:::
:::
