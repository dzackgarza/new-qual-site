---
schema: qual/card@1
id: PR-7OT2Z
kind: proposition
title: The ideal-variety correspondence
slogan: 'Over an algebraically closed field, radical, prime, and maximal ideals correspond contravariantly to closed sets, irreducible sets, and points.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Varieties
  - Nullstellensatz
  - Prime Ideals
relations:
- kind: uses
  target: T-JRTS2
review: draft
prompts:
- Which ideals correspond to closed subsets of $\AA^n$?
- Which ideals correspond to irreducible closed subsets?
- What is the coordinate ring of a closed subset, and when is it a domain?
- Show that the algebraic sets are the closed sets of a topology on $\AA^n$.
- Show that the maximal ideals of $k[x_1,\ldots,x_n]$ are the ideals $(x_1-a_1,\ldots,x_n-a_n)$ when $k$ is algebraically closed, and that this fails otherwise.
- Show that every finitely generated $k$-algebra that is a domain is the coordinate ring of an affine variety.
- Show that $I(V)$ and $\sqrt{I}$ are ideals, and that $V$ and $I$ are inclusion-reversing.
- Show that a set of $d \leq 2n$ points of $\AA^n_k$, no $n+1$ of which lie on an affine hyperplane, is the common zero set of polynomials of degree at most $2$.
- Show that $V(y - x^2) \cong \AA^1$ and $V(y - x^2, z - x^3) \cong \AA^1$ as affine varieties.
- Show that the nodal cubic $V(y^2 - x^3 - x^2)$ has the parametrization $t \mapsto (t^2 - 1, t^3 - t)$.
---

::: {.proposition}
Over an algebraically closed field $k$, the maps $V$ and $I$ are mutually inverse, order-reversing bijections between the radical ideals of $k[x_1,\ldots,x_n]$ and the Zariski-closed subsets of $\AA^n$.
Under that bijection:

| Ideal $J$ | Closed set $V(J)$ |
| --- | --- |
| radical | closed |
| prime | irreducible |
| maximal | a point |
| $(1)$ | $\emptyset$ |
| $(0)$ | $\AA^n$ |
:::

::: {.proposition title="Operations on vanishing sets and ideals"}
Let $\mfa, \mfa_1, \mfa_2$ and $\mfa_i$ ($i \in I$) be ideals of $A \coloneqq k[x_1,\ldots,x_n]$, and let $Y_j$ ($j \in J$) be subsets of $\AA^n$.
Then
$$
\bigcap_{i \in I} V(\mfa_i) = V\Big(\sum_{i \in I} \mfa_i\Big), \qquad
V(\mfa_1) \union V(\mfa_2) = V(\mfa_1 \mfa_2), \qquad
\AA^n \sm V(\mfa) = \bigcup_{f \in \mfa} D(f), \qquad
D(fg) = D(f) \intersect D(g),
$$
and
$$
I\Big(\bigcup_{j \in J} Y_j\Big) = \bigcap_{j \in J} I(Y_j), \qquad
V(I(Y)) = \overline{Y} \text{ for } Y \subseteq \AA^n .
$$
If $k$ is algebraically closed, then $V(\mfa_1) \subseteq V(\mfa_2)$ if and only if $\sqrt{\mfa_1} \supseteq \sqrt{\mfa_2}$.
[@Har77, §I.1]
:::

::: {.proposition title="Maximal ideals and coordinate rings"}
Let $k$ be algebraically closed.
The maximal ideals of $k[x_1,\ldots,x_n]$ are exactly the ideals $(x_1 - a_1, \ldots, x_n - a_n)$ with $(a_1,\ldots,a_n) \in \AA^n$, and they correspond to the points of $\AA^n$.
For an affine variety $Y$ the coordinate ring $A(Y)$ is a finitely generated $k$-algebra and a domain; conversely, every finitely generated $k$-algebra that is a domain is $A(Y)$ for some affine variety $Y$.
[@Har77, §I.1]
:::

::: {.example}
Over $k = \RR$ the ideal $(x^2+1) \subseteq \RR[x]$ is maximal and is not of the form $(x - a)$.
:::

::: {.remark}
For a radical ideal $J\subseteq k[x_1,\ldots,x_n]$, the closed set $V(J)$ is irreducible exactly when $J$ is prime, equivalently when $k[x_1,\ldots,x_n]/J$ is a domain.

For a closed $X \subseteq \AA^n$, its coordinate ring is
$$
k[X]\coloneqq k[x_1,\ldots,x_n]/I(X).
$$
The closed subsets of $X$ correspond contravariantly to the radical ideals of $k[X]$, and $X$ is irreducible exactly when $k[X]$ is a domain.
:::

::: {.remark title="The Zariski topology and the maps $V$ and $I$"}
$V(1)=\emptyset$ and $V(0)=\AA^n$. By the operations above, finite unions and arbitrary intersections of algebraic sets are algebraic, so the algebraic sets are the closed sets of a topology [@Har77, Prop. I.1.1].
$I(Y)$ is an ideal: a sum of polynomials that vanish on $Y$ vanishes on $Y$, and so does every multiple of one. $\sqrt{J}$ is an ideal: if $f^r,g^s\in J$, then every term of the binomial expansion of $(f+g)^{r+s-1}$ is in $J$.
If $J_1\subseteq J_2$ then $V(J_1)\supseteq V(J_2)$, and if $Y_1\subseteq Y_2$ then $I(Y_1)\supseteq I(Y_2)$ [@Har77, Prop. I.1.2].
:::

::: {.remark title="Points cut out by quadrics"}
Let $\Gamma\subseteq\AA^n_k$ be $d\leq 2n$ points, no $n+1$ of which lie on an affine hyperplane. Then $\Gamma$ is the zero set of the polynomials of degree at most $2$ that vanish on it.
In $\PP^n\supseteq\AA^n$ these points are in linear general position, and $d\leq 2n$ points in linear general position in $\PP^n$ are cut out by quadrics [@Har92, Lecture 1]. For $q\notin\Gamma$, split $\Gamma$ into two sets of at most $n$ points such that the span of neither set contains $q$. The product of two hyperplanes, one through each set and neither through $q$, is a quadric that contains $\Gamma$ and not $q$. Dehomogenizing gives the affine statement.
:::

::: {.example title="Two curves isomorphic to $\AA^1$, and the nodal cubic"}
The maps $t\mapsto(t,t^2)$ and $(x,y)\mapsto x$ are mutually inverse morphisms between $\AA^1$ and $V(y-x^2)$; on coordinate rings, $k[x,y]/(y-x^2)\cong k[x]$. Likewise $t\mapsto(t,t^2,t^3)$ identifies $\AA^1$ with $V(y-x^2,z-x^3)$, since $k[x,y,z]/(y-x^2,z-x^3)\cong k[x]$ [@Har77, Ex. I.1.1].
For the nodal cubic, set $x=t^2-1$ and $y=t^3-t=t(t^2-1)$. Then $y^2=t^2(t^2-1)^2=(x+1)x^2=x^3+x^2$. The values $t=\pm1$ both map to the node $(0,0)$, and each line $y=tx$ through the node meets the cubic again exactly at the image of $t$.
:::
