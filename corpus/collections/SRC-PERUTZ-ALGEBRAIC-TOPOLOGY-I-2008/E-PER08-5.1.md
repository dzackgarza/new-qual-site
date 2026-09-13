---
schema: qual/card@1
id: E-PER08-5.1
kind: problem
title: Four basic examples of covering maps
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Exercise 5.1 of the vendored Perutz Fall 2008 Algebraic Topology I notes; repaired doubled TeX escapes in the ingested statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified explicit evenly covered neighborhoods for the quotient, power, finite-product, and antipodal quotient maps.
---

::: {.problem}
Show that each of the following is a covering map.

1. The quotient map
   \[
   \mathbb R\longrightarrow \mathbb R/\mathbb Z.
   \]

2. For $n\ge1$, the map
   \[
   S^1\longrightarrow S^1,
   \qquad e^{it}\longmapsto e^{int}.
   \]

3. A finite product of covering maps; for example,
   \[
   \mathbb R^n\longrightarrow(\mathbb R/\mathbb Z)^n=\mathbb R^n/\mathbb Z^n.
   \]

4. The quotient map
   \[
   S^n\longrightarrow\mathbb{RP}^n
   \]
   identifying antipodal points.
:::

::: {.solution}
Recall that a surjection $p:\widetilde X\to X$ is a covering map if every $x\in X$ has an open neighborhood $U$ such that
\[
p^{-1}(U)=\coprod_{\alpha}V_\alpha
\]
is a disjoint union of open sets and every restriction
\[
p|_{V_\alpha}:V_\alpha\to U
\]
is a homeomorphism.

<1>1. The quotient map $q:\mathbb R\to\mathbb R/\mathbb Z$ is a covering map.
::: {.proof}
Fix $[x]\in\mathbb R/\mathbb Z$ and set
\[
I=(x-1/4,x+1/4),
\qquad
U=q(I).
\]
Because $I$ has length less than $1$, no two distinct points of $I$ differ by an integer. Thus
\[
q|_I:I\to U
\]
is injective; it is also an open continuous surjection, hence a homeomorphism.

Moreover,
\[
q^{-1}(U)=\coprod_{k\in\mathbb Z}(I+k).
\]
The intervals $I+k$ are pairwise disjoint, and translation by $k$ followed by $q$ shows that
\[
q|_{I+k}:I+k\to U
\]
is a homeomorphism for every $k$. Hence $U$ is evenly covered.
:::

<1>2. The map $p_n:S^1\to S^1$, $p_n(z)=z^n$, is a covering map.
::: {.proof}
Fix $e^{i\theta}\in S^1$. Choose $0<\varepsilon<\pi$ and let
\[
U=\{e^{iu}:|u-\theta|<\varepsilon\}.
\]
This is an open arc on which the argument is single-valued.

For $j=0,\dots,n-1$, define
\[
V_j=
\left\{
 e^{iv}:
 \left|v-\frac{\theta+2\pi j}{n}\right|<\frac{\varepsilon}{n}
\right\}.
\]
These arcs are pairwise disjoint and
\[
p_n^{-1}(U)=\coprod_{j=0}^{n-1}V_j.
\]
On $V_j$, the inverse branch is
\[
e^{iu}\longmapsto
\exp\left(\frac{i(u+2\pi j)}{n}\right),
\]
so each restriction
\[
p_n|_{V_j}:V_j\to U
\]
is a homeomorphism. Thus $p_n$ is an $n$-sheeted covering.
:::

<1>3. A finite product of covering maps is a covering map.
::: {.proof}
It suffices to prove the assertion for two factors; induction then gives every finite product.

Let
\[
p_i:\widetilde X_i\to X_i
\qquad(i=1,2)
\]
be covering maps. Fix $(x_1,x_2)\in X_1\times X_2$. Choose evenly covered neighborhoods $U_i$ of $x_i$ with
\[
p_i^{-1}(U_i)=\coprod_{\alpha_i}V_{i,\alpha_i}
\]
and each
\[
p_i|_{V_{i,\alpha_i}}:V_{i,\alpha_i}\xrightarrow{\cong}U_i.
\]
Then
\[
(p_1\times p_2)^{-1}(U_1\times U_2)
=
\coprod_{\alpha_1,\alpha_2}
V_{1,\alpha_1}\times V_{2,\alpha_2},
\]
and on each component
\[
(p_1\times p_2)|_{V_{1,\alpha_1}\times V_{2,\alpha_2}}
=
(p_1|_{V_{1,\alpha_1}})\times(p_2|_{V_{2,\alpha_2}}),
\]
which is a homeomorphism onto $U_1\times U_2$.

Taking the $n$-fold product of the covering $\mathbb R\to\mathbb R/\mathbb Z$ from <1>1 gives
\[
\mathbb R^n\to(\mathbb R/\mathbb Z)^n.
\]
:::

<1>4. The antipodal quotient $q:S^n\to\mathbb{RP}^n$ is a covering map.
::: {.proof}
Fix a point $[x]\in\mathbb{RP}^n$, represented by a unit vector $x\in S^n$. Define
\[
U=\{[y]\in\mathbb{RP}^n:\langle x,y\rangle\neq0\}.
\]
This is well defined because replacing $y$ by $-y$ changes the sign but not the nonvanishing of the inner product. It is an open neighborhood of $[x]$.

Its preimage is the disjoint union of the two open hemispheres
\[
H_+=\{y\in S^n:\langle x,y\rangle>0\},
\qquad
H_-=\{y\in S^n:\langle x,y\rangle<0\}.
\]
Every projective point in $U$ has exactly one representative in $H_+$ and exactly one in $H_-$. Therefore
\[
q|_{H_+}:H_+\to U
\]
and
\[
q|_{H_-}:H_-\to U
\]
are continuous bijections. Their inverses choose, respectively, the unique representative having positive or negative inner product with $x$; these choices vary continuously because the sign cannot change inside $U$. Hence both restrictions are homeomorphisms.

Thus $U$ is evenly covered and
\[
S^n\to\mathbb{RP}^n
\]
is a two-sheeted covering.
:::
:::
