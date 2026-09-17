---
schema: qual/card@1
id: P-AGH2710PNBUNDLE
kind: problem
title: Projective n-space bundles over a scheme
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Bundles
  - Locally Free Sheaves
  - Descent
relations: []
review: draft
audit:
- event: solution-written
  by: chatgpt
  date: 2026-09-17
  note: Followed the card's hyperplane-extension hint, using the quotient convention checked against Stacks Project Tag 01OA. The construction works for locally factorial noetherian bases, includes disconnected bases and n=0, and does not assume that projective transition matrices already lift to a vector-bundle cocycle.
---

::: {.problem}
Let $X$ be a noetherian scheme and let $n\ge0$.

(a) By analogy with the definition of a vector bundle (Ex. 5.18), define the notion of a **projective $n$-space bundle** over $X$: a scheme $P$ with a morphism $\pi: P \to X$ such that $P$ is locally isomorphic to $U \times \PP^n$ for $U \subseteq X$ open, and the transition automorphisms on $\Spec A \times \PP^n$ are given by $A$-linear automorphisms of the homogeneous coordinate ring $A[x_0, \ldots, x_n]$, e.g. $x'_i = \sum_j a_{ij} x_j$ with $a_{ij} \in A$.

(b) If $\mce$ is a locally free sheaf of rank $n+1$ on $X$, then $\PP(\mce)$ is a $\PP^n$-bundle over $X$.

(c) Assume that $X$ is regular, and show that every $\PP^n$-bundle $P$ over $X$ is isomorphic to $\PP(\mce)$ for some locally free sheaf $\mce$ on $X$.
Can you weaken the hypothesis that $X$ is regular?

(d) Conclude, in the case $X$ regular, that there is a bijection between $\PP^n$-bundles over $X$ and equivalence classes of locally free sheaves $\mce$ of rank $n+1$ under the relation $\mce \sim \mce'$ if and only if $\mce' \cong \mce \tensor \mcm$ for some invertible sheaf $\mcm$ on $X$.
:::

::: {.hint}
For part (c), let $U\subseteq X$ be an open set with $\pi^{-1}(U)\cong\PP_U^n$, and let $\mcl_0=\OO(1)$ there.
Show that $\mcl_0$ extends to an invertible sheaf $\mcl$ on $P$, then show that $\pi_*\mcl=\mce$ is locally free and $P\cong\PP(\mce)$.
For a disconnected base, carry out this construction on each connected component.
:::

::: {.solution}
Use the convention $\PP(\mce)=\operatorname{Proj}_X\operatorname{Sym}^{\bullet}\mce$ of [[P-AGH278SECTIONSPE]].
All bundle isomorphisms are over the base scheme.

<1>1. In part (a), a projective bundle has an open cover $(U_i)$ and isomorphisms $h_i:\pi^{-1}(U_i)\to\PP_{U_i}^n$ whose changes of coordinates are projective linear.
The changes of coordinates satisfy the cocycle identity as projective automorphisms.

::: {.proof}
For every affine open $W=\Spec A\subseteq U_i\cap U_j$, require $h_j\circ h_i^{-1}$ to be induced by a graded $A$-algebra automorphism
$$
A[T_0,\ldots,T_n]\longrightarrow A[T_0,\ldots,T_n],\qquad
T_a\longmapsto\sum_b c_{ab}T_b,
\quad (c_{ab})\in\operatorname{GL}_{n+1}(A).
$$
Atlases are equivalent when their union has this property after common open refinement.
An isomorphism of bundles is an $X$-isomorphism whose local expressions are projective linear in the two atlases, as in the vector-bundle definition of [[P-AGH2518VECBUN]].

Writing $g_{ji}=h_j\circ h_i^{-1}$, the identities $g_{ii}=\id$ and $g_{kj}\circ g_{ji}=g_{ki}$ hold on their domains.
Conversely, projective coordinate changes satisfying these identities glue the schemes $\PP_{U_i}^n$ and their projections to $X$ [@Har10a, Exercise II.2.12].
This describes the required bundle notion in terms of gluing data.
Multiplying a chosen matrix by a unit does not change its projective automorphism, since the unit cancels in every homogeneous coordinate ratio.
Thus the matrices representing the $g_{ji}$ are not required to satisfy an exact matrix cocycle identity; assuming such lifts would assume the vector bundle sought in (c).
:::

<1>2. A locally free sheaf $\mce$ of rank $n+1$ gives the projective bundle in (b).

::: {.proof}
Choose a frame for $\mce$ on each affine open $U_i$ of a cover.
It identifies its symmetric algebra with the polynomial algebra in $n+1$ degree-one variables, and hence identifies $\PP(\mce)|_{U_i}$ with $\PP_{U_i}^n$.
Two frames differ by an invertible matrix of regular functions on their overlap.
The same matrix changes the degree-one generators of their symmetric algebras and induces the required projective coordinate change.
These identifications satisfy the cocycle identity because they arise from the single sheaf $\mce$.
Changing the frames gives an equivalent atlas.
:::

<1>3. For (c), it suffices to assume that every local ring of the noetherian scheme $X$ is a unique factorization domain.
Under this hypothesis, each connected component of $X$ is integral and open and closed, and $P$ is locally factorial as well.

::: {.proof}
This hypothesis is local factoriality.
It holds for regular $X$ because a regular local ring is factorial [@Har10a, Remark II.6.11.1A].
Local factoriality also makes every local ring a domain.
As in [[P-AGH279PICPE]], step <1>1, the finitely many irreducible components of a noetherian scheme with domain local rings are disjoint, reduced, and open and closed.
Thus they are the integral connected components.

On a standard affine chart of a bundle trivialization, a local ring of $P$ at a point above $x\in X$ is a localization of a polynomial ring over $\OO_{X,x}$.
Polynomial rings over a UFD and their localizations are UFDs.
Hence $P$ is locally factorial.
It is noetherian because finitely many trivializing opens on $X$, each covered by finitely many standard affine charts upstairs, give a finite noetherian affine cover.

Over an integral component of $X$, each trivializing open has integral inverse image, and any two such inverse images have nonempty intersection over the generic point of the base.
Consequently their union is integral.
All the required constructions can be made separately on these finitely many components and then combined.
We therefore assume $X$ is integral and nonempty for steps <1>4--<1>5.
The case $n=0$ is immediate: $\PP_U^0=U$ and all transition maps over $U$ are the identity, so $P\cong X=\PP(\OO_X)$.
Assume henceforth that $n\ge1$.
:::

<1>4. The bundle $P$ carries an invertible sheaf $\mathcal L$ which restricts to degree one on every fibre.

::: {.proof}
Choose a nonempty affine trivializing open $U\subseteq X$.
Inside $P|_U\cong\PP_U^n$, choose the coordinate hyperplane $H_U$ and let $H$ be its reduced closure in $P$.
It is an integral codimension-one closed subscheme: its generic point lies in the open $P|_U$ and has codimension one there and in $P$.
At any point of $H$, its ideal is a height-one prime in the factorial local ring of $P$, hence is generated by one nonzero element.
That element is a non-zero-divisor because the local ring is a domain.
The ideal sheaf of $H$ is coherent, and a generator of its stalk generates on a neighborhood; thus this stalkwise calculation makes $H$ an effective Cartier divisor.
Put $\mathcal L=\OO_P(H)$.
Its restriction to $P|_U$ is $\OO(1)$, as required by the hint.

On any nonempty affine trivializing open $V\subseteq X$, both $V$ and $\PP_V^n$ are noetherian, integral, locally factorial, and separated.
The class-group calculation in [[P-AGH261CLPROJBUN]], together with the Cartier–Weil comparison [@Har10a, Proposition II.6.11 and Corollary II.6.16], gives
$$
\Pic(\PP_V^n)\cong\Pic(V)\oplus\ZZ.
$$
Consequently
$$
\mathcal L|_{P|_V}\cong\pi_V^*\mathcal M_V\otimes\OO_{\PP_V^n}(d_V)
$$
for an invertible sheaf $\mathcal M_V$ and an integer $d_V$.
The opens $U$ and $V$ meet because $X$ is integral.
At a point of their intersection, the transition between the projective trivializations preserves $\OO(1)$, while a sheaf pulled back from $V$ is trivial on the fibre.
Since $\Pic(\PP^n_{\kappa(x)})\cong\ZZ$ for $n\ge1$, comparison on that fibre gives $d_V=1$.
This holds for every such $V$, so $\mathcal L$ has degree one on every fibre.
:::

<1>5. With $\mce=\pi_*\mathcal L$, the sheaf $\mce$ is locally free of rank $n+1$, and $P\cong\PP(\mce)$ over $X$.

::: {.proof}
On an affine trivializing open $V$ of step <1>4, the degree-one section calculation gives
$$
\mce|_V
\cong\pi_{V*}(\pi_V^*\mathcal M_V\otimes\OO(1))
\cong\mathcal M_V\otimes\OO_V^{\oplus(n+1)}.
$$
The tensor identity follows by trivializing the invertible sheaf $\mathcal M_V$ on $V$; the remaining identity is $\pi_{V*}\OO(1)=\OO_V^{\oplus(n+1)}$ [@Har10a, Theorem III.5.1].
Thus $\mce$ is locally free of the asserted finite rank and is coherent because $X$ is noetherian.

The counit
$$
\pi^*\mce=\pi^*\pi_*\mathcal L\longrightarrow\mathcal L
$$
is surjective: locally it is the usual evaluation of the $n+1$ coordinate sections of $\OO(1)$, tensored with $\pi_V^*\mathcal M_V$.
The invertible-quotient construction of [[P-AGH278SECTIONSPE]], after base change along $\pi:P\to X$, therefore gives an $X$-morphism $j:P\to\PP(\mce)$.
After further trivializing $\mathcal M_V$, its coordinate ratios are exactly the standard coordinate ratios on $\PP_V^n$.
Hence $j$ is locally the identity map between the two projective-space trivializations.
It follows that $j$ is a projective-bundle isomorphism globally.
Combining the construction on the components gives the result for the original $X$.
This proves (c) under local factoriality, and in particular under regularity.
:::

<1>6. Local factoriality is strictly weaker than regularity, even among affine varieties.

::: {.proof}
Over an algebraically closed field of characteristic different from two, let
$$
Z=\Spec k[x_0,x_1,x_2,x_3,x_4]/(x_0^2+x_1^2+x_2^2+x_3^2+x_4^2).
$$
The quadric calculation in [[P-AGH265QUADRIC]], steps <1>1 and <1>4, makes its coordinate ring a normal noetherian domain with zero class group.
It is therefore a UFD [@Har10a, Proposition II.6.2], and every localization is factorial.
At the origin, however, the maximal ideal modulo its square has dimension five over $k$, because the only defining relation is quadratic.
The local ring has dimension four: it is a polynomial regular local ring of dimension five modulo a nonzero hypersurface equation [@AM18, Chapter 11].
Thus its embedding dimension exceeds its Krull dimension, so that local ring is not regular.
This supplies a locally factorial, nonregular base to which steps <1>3--<1>5 still apply.
:::

<1>7. For regular $X$, the map $\mce\mapsto\PP(\mce)$ gives the bijection in (d).

::: {.proof}
Step <1>2 constructs a bundle from each locally free sheaf of rank $n+1$, and step <1>5 proves that every bundle arises in this way.
For $n\ge1$, [[P-AGH279PICPE]], steps <1>5--<1>6, proves that two such projectivizations are isomorphic over $X$ exactly when the sheaves differ by tensoring with an invertible sheaf.
The isomorphism constructed there from an invertible twist is locally induced by a linear change of frame, so it is an isomorphism of the bundles defined in step <1>1.
This proves that the fibres of the assignment are precisely the equivalence classes in (d).

For $n=0$, all projective-space bundles are $X$, and any two rank-one sheaves differ by an invertible twist, namely $\mce'=\mce\otimes(\mce'\otimes\mce^{-1})$.
Thus the classification also holds in this case, and the empty base has the corresponding unique empty bundle.
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 give (a) and (b).
Steps <1>3--<1>6 prove (c), including the requested weaker hypothesis and an example separating it from regularity.
Step <1>7 proves (d).
:::
:::
