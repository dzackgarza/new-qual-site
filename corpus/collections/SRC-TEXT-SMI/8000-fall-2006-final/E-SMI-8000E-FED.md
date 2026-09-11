---
schema: qual/card@1
id: E-SMI-8000E-FED
kind: problem
title: Proof choice — small groups or simplicity of A5
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared both proof choices with Smith 8000 Fall 2006 final part D; solved option (i)."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Used the center of a p^2-group for order 9 and Sylow plus the two possible C2-actions on C5 for order 10."
---

::: {.exercise}
Prove one:

(i) There are no nonabelian groups of order 9, and only one nonabelian group of order 10;

or

(ii) Icos (that is, $A(5)$) is a simple group.
:::

::: solution
We prove option (i).

<1>1. Every group of order $9$ is abelian.
::: proof
Let $G$ have order
$$
|G|=9=3^2.
$$
A finite $p$-group has nontrivial center, so
$$
|Z(G)|\in\{3,9\}.
$$
If $|Z(G)|=9$, then $Z(G)=G$ and $G$ is abelian.

If $|Z(G)|=3$, then
$$
|G/Z(G)|=3,
$$
so $G/Z(G)$ is cyclic. A group whose quotient by its center is cyclic is
abelian: if $gZ(G)$ generates $G/Z(G)$, every element has the form
$g^a z$ with $z\in Z(G)$, and any two such elements commute. Hence $G$ is
again abelian.

Thus there are no nonabelian groups of order $9$.
:::

<1>2. Every group of order $10$ is a semidirect product $C_5\rtimes C_2$.
::: proof
Let $|G|=10$. Sylow gives
$$
n_5\mid2,
\qquad
n_5\equiv1\pmod5.
$$
Therefore
$$
n_5=1.
$$
Let $P$ be the unique Sylow $5$-subgroup. Then
$$
P\trianglelefteq G,
\qquad
P\cong C_5.
$$

Let $Q$ be a Sylow $2$-subgroup. Then $Q\cong C_2$, and
$$
P\cap Q=1.
$$
Since
$$
|PQ|=\frac{|P||Q|}{|P\cap Q|}=10,
$$
we have $G=PQ$. Thus
$$
G\cong C_5\rtimes C_2.
$$
:::

<1>3. There are exactly two possible actions, and only one gives a nonabelian group.
::: proof
Conjugation by the generator of $C_2$ defines a homomorphism
$$
C_2\longrightarrow\operatorname{Aut}(C_5).
$$
Now
$$
\operatorname{Aut}(C_5)\cong(\mathbf Z/5\mathbf Z)^\times\cong C_4.
$$
A homomorphism from $C_2$ to $C_4$ has image either trivial or the unique
subgroup of order two.

If the action is trivial, then
$$
G\cong C_5\times C_2\cong C_{10},
$$
which is abelian.

If the action is nontrivial, choose generators $r$ of $C_5$ and $s$ of
$C_2$. The unique automorphism of order two of $C_5$ is inversion, so
$$
srs^{-1}=r^{-1}.
$$
Hence
$$
G\cong
\langle r,s\mid r^5=s^2=1,\ srs^{-1}=r^{-1}\rangle,
$$
the dihedral group of order $10$.

Therefore
$$
\boxed{\text{up to isomorphism, }D_{10}\text{ is the unique nonabelian group of order }10.}
$$
:::
:::
