---
schema: qual/card@1
id: P-ALGF09D
kind: problem
title: "Every finite group appears as a Galois group over some field extension"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 4 of the official UCSD Algebra Qualifying Examination, Fall 2009; the statement agrees with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the faithful permutation action of G on a rational function field over F and supplied the finite fixed-field theorem showing that the resulting extension is Galois with full automorphism group G.
---

::: {.problem}
Let $G$ be any finite group and $F$ any field.
Show that there exist fields $L$ and $E$ with $F \subseteq L \subseteq E$, such that $E$ is Galois over $L$ with the Galois group of $E/L$ being isomorphic to $G$.
:::

::: {.solution}
For each $g\in G$, let $x_g$ be an indeterminate, with all of the $x_g$ algebraically independent over $F$, and set
\[
E:=F(x_g:g\in G).
\]

<1>1. The group $G$ acts faithfully on $E$ by $F$-automorphisms.
::: {.proof}
For $h\in G$, define
\[
\sigma_h(x_g):=x_{hg}
\qquad(g\in G),
\]
and let $\sigma_h$ fix $F$ pointwise.
Because the variables are algebraically independent, this permutation of the variables extends uniquely to an automorphism of the polynomial ring and hence of its fraction field $E$.
Moreover,
\[
\sigma_h\sigma_k(x_g)=x_{hkg}=\sigma_{hk}(x_g),
\]
so
\[
h\longmapsto\sigma_h
\]
is a homomorphism
\[
G\longrightarrow\operatorname{Aut}_F(E).
\]
It is injective: if $h\neq1$, then
\[
\sigma_h(x_1)=x_h\neq x_1.
\]
Thus we identify $G$ with a finite subgroup of $\operatorname{Aut}_F(E)$.
:::

<1>2. Let a finite group $H$ act faithfully by automorphisms on a field $K$, and set $K^H:=\{a\in K:\sigma(a)=a\text{ for all }\sigma\in H\}$.
Then
\[
[K:K^H]=|H|
\]
and
\[
\operatorname{Gal}(K/K^H)=H.
\]
::: {.proof}
Write
\[
H=\{\sigma_1,\ldots,\sigma_m\},
\qquad m=|H|.
\]
We use the linear independence of distinct field homomorphisms: the maps $\sigma_i:K\to K$ are linearly independent over $K$ as functions.
Indeed, if a nontrivial relation with the fewest nonzero coefficients were
\[
\sum_{i=1}^r c_i\sigma_i=0,
\qquad c_i\neq0,
\]
choose $a\in K$ with $\sigma_1(a)\neq\sigma_r(a)$.
Evaluating at $ab$ and subtracting $\sigma_r(a)$ times the relation evaluated at $b$ yields a shorter nontrivial relation, a contradiction.

This independence implies that there exist elements
\[
a_1,\ldots,a_m\in K
\]
for which the matrix
\[
A=(\sigma_i(a_j))_{i,j}
\]
is invertible.
Otherwise every such evaluation matrix would have rank $<m$, which would give a nonzero linear relation among the functions $\sigma_i$.

Fix $b\in K$.
Because $A$ is invertible, there are unique $c_1,\ldots,c_m\in K$ such that
\[
\sigma_i(b)=\sum_{j=1}^m c_j\sigma_i(a_j)
\qquad(1\le i\le m).
\]
Let $\tau\in H$.
Applying $\tau$ to all these equations replaces every $\sigma_i$ by $\tau\sigma_i$, which merely permutes the rows because $H$ is a group.
Therefore the coefficients $\tau(c_j)$ solve the same linear system as the $c_j$.
By uniqueness,
\[
\tau(c_j)=c_j
\]
for every $j$ and every $\tau\in H$.
Hence
\[
c_j\in K^H.
\]
Taking the row corresponding to the identity automorphism gives
\[
b=\sum_{j=1}^m c_j a_j.
\]
Thus $a_1,\ldots,a_m$ span $K$ over $K^H$, so
\[
[K:K^H]\le m.
\]

On the other hand, a finite field extension has at most its degree many embeddings into an algebraic closure over the base field.
The $m$ distinct automorphisms in $H$ all fix $K^H$, so
\[
m\le [K:K^H].
\]
Consequently
\[
[K:K^H]=m=|H|.
\]
The extension has exactly its degree many $K^H$-automorphisms, hence is finite Galois, and all of its automorphisms are the elements of $H$.
Therefore
\[
\operatorname{Gal}(K/K^H)=H.
\]
:::

<1>3. Taking the fixed field of the action in <1>1 produces the required extension.
::: {.proof}
Set
\[
L:=E^G.
\]
Because every element of $G$ fixes $F$ pointwise,
\[
F\subseteq L\subseteq E.
\]
Applying <1>2 to the faithful action of $G$ on $E$ gives
\[
[E:L]=|G|
\]
and shows that $E/L$ is Galois with
\[
\operatorname{Gal}(E/L)=G.
\]
Thus every finite group occurs as a Galois group over some extension of the prescribed field $F$.
:::
:::
