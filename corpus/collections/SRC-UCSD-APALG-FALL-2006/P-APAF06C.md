---
schema: qual/card@1
id: P-APAF06C
kind: problem
title: Center when $G/Z(G)$ is cyclic; center of a nonabelian group of order $p^3$; order-$16$ example
classification:
  areas:
  - applied-algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $G$ be a group and let $Z(G)$ denote its center.

(a) Show that if $G/Z(G)$ is cyclic then $G = Z(G)$.

(b) Show that if $\operatorname{card}(G) = p^3$, for some prime number $p$ and $G$ is non-commutative then $\operatorname{card}(Z(G)) = p$.

(c) Construct a non-commutative group $G$ of cardinality (order) $16$ whose center $Z(G)$ is not cyclic.

Note.
As usual, $\operatorname{card}(X)$ denotes the cardinality of the set $X$.
:::

::: {.solution}
<1>1. If $G/Z(G)$ is cyclic, then $G=Z(G)$.
::: {.proof}
Suppose
\[
G/Z(G)=\langle gZ(G)\rangle.
\]
Then every element of $G$ has the form
\[
g^m z
\]
with $m\in\mathbb Z$ and $z\in Z(G)$. Hence if
\[
x=g^m z_1,\qquad y=g^n z_2,
\]
then, since $z_1,z_2$ are central,
\[
xy=g^{m+n}z_1z_2=g^{n+m}z_2z_1=yx.
\]
Thus $G$ is abelian, so every element lies in its center and $G=Z(G)$. This proves part (a).
:::

<1>2. If $G$ is a finite group of order $p^3$, then $|Z(G)|$ is divisible by $p$.
::: {.proof}
Let $G$ act on itself by conjugation. The class equation is
\[
|G|=|Z(G)|+\sum_i [G:C_G(x_i)],
\]
where the sum runs over representatives of the noncentral conjugacy classes. Since $G$ is a $p$-group, each index $[G:C_G(x_i)]$ is a power of $p$; for a noncentral element it is greater than $1$, hence divisible by $p$. Therefore
\[
|Z(G)|\equiv |G|\equiv0\pmod p.
\]
In particular the center is nontrivial.
:::

<1>3. If $|G|=p^3$ and $G$ is nonabelian, then
\[
|Z(G)|=p.
\]
::: {.proof}
By <1>2, the center has order $p$, $p^2$, or $p^3$.
If $|Z(G)|=p^3$, then $Z(G)=G$, so $G$ is abelian, contradiction.
If $|Z(G)|=p^2$, then
\[
|G/Z(G)|=p,
\]
so $G/Z(G)$ is cyclic. By <1>1 this again forces $G=Z(G)$, contradiction.
Thus the only possibility is $|Z(G)|=p$. This proves part (b).
:::

<1>4. Let
\[
D_8=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle
\]
be the dihedral group of order $8$. Then
\[
Z(D_8)=\langle r^2\rangle\cong C_2.
\]
::: {.proof}
Every element of $D_8$ is uniquely of the form $r^i$ or $r^is$ with $0\le i<4$.
A power $r^i$ commutes with $s$ exactly when
\[
r^i=sr^is=r^{-i},
\]
which is equivalent to $2i\equiv0\pmod4$, so $i\equiv0$ or $2$.
No reflection $r^is$ commutes with $r$, since
\[
(r^is)r=r^{i-1}s,
\qquad
r(r^is)=r^{i+1}s,
\]
and these would be equal only if $r^2=1$, which is false in $D_8$.
Hence the center is exactly $\{1,r^2\}$.
:::

<1>5. The group
\[
G=D_8\times C_2
\]
is nonabelian of order $16$ and has noncyclic center.
::: {.proof}
Its order is
\[
|G|=|D_8|\,|C_2|=8\cdot2=16.
\]
It is nonabelian because $D_8$ is nonabelian.
For arbitrary groups $H,K$,
\[
Z(H\times K)=Z(H)\times Z(K),
\]
since $(h,k)$ commutes with every $(h',k')$ exactly when $h$ commutes with every $h'$ and $k$ commutes with every $k'$.
Therefore, by <1>4,
\[
Z(G)=Z(D_8)\times C_2
\cong C_2\times C_2,
\]
which is not cyclic. This proves part (c).
:::
:::
