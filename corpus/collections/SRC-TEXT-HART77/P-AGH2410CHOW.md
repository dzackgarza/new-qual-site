---
schema: qual/card@1
id: P-AGH2410CHOW
kind: problem
title: Chow's lemma
classification:
  areas:
  - algebraic-geometry
  topics:
  - Proper Morphisms
  - Projective Morphisms
  - Birational Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against Hartshorne II.4.10 and the standard proof of Chow's lemma by graph closure in a product of projective compactifications.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Repaired the proof that h is a closed immersion. The former step claimed
    that being an immersion is local on the source, which is false (the fold
    map from two disjoint points to one point restricts to isomorphisms on
    both source components). The replacement follows the published proof,
    EGA II, Théorème 5.6.1, étape D) (Grothendieck, Éléments de géométrie
    algébrique II, Publ. Math. IHÉS 8 (1961), pp. 108-109), verified against
    the Numdam scan: the graph of u_i : G_i -> X is closed because X is
    separated over S, and the full inverse image h^{-1}(G_i) is a closed
    subscheme of that graph, so h^{-1}(G_i) -> G_i is a closed immersion;
    the G_i cover h(X'), and closed immersions are local on the target.
    Steps s1-s11 and s14-s20 were re-read and left unchanged; the
    scheme-theoretic image argument of steps s16-s19 is untouched.
---

::: {.problem}
This result says that proper morphisms are fairly close to projective morphisms.

Let $X$ be proper over a noetherian scheme $S$.
Then there is a scheme $X'$ and a morphism $g: X' \to X$ such that $X'$ is projective over $S$, and there is an open dense subset $U \subseteq X$ such that $g$ induces an isomorphism of $\inverseof{g}(U)$ onto $U$.
Prove this in the following steps.

(a) Reduce to the case $X$ irreducible.

(b) Show that $X$ can be covered by finitely many open subsets $U_i$, $i = 1, \ldots, n$, each of which is quasi-projective over $S$. Let $U_i \injects P_i$ be an open immersion of $U_i$ into a scheme $P_i$ which is projective over $S$.

(c) Let $U = \bigcap_i U_i$, and consider the map
$$
f: U \to X \fiberproduct{S} P_1 \fiberproduct{S} \cdots \fiberproduct{S} P_n
$$
deduced from the given maps $U \to X$ and $U \to P_i$.
Let $X'$ be the scheme-theoretic closure of $f(U)$ in the displayed product, as in Exercise II.3.11(d).
Let $g: X' \to X$ be the projection onto the first factor, and let $h: X' \to P = P_1 \fiberproduct{S} \cdots \fiberproduct{S} P_n$ be the projection onto the product of the remaining factors.
Show that $h$ is a closed immersion, hence $X'$ is projective over $S$.

(d) Show that $\inverseof{g}(U) \to U$ is an isomorphism, completing the proof.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

It is enough to prove the theorem when the underlying topological space of $X$ is irreducible.

::: pf-proof

Because $X$ is proper over the noetherian scheme $S$, it is noetherian.
Let
$$
X_1,\ldots,X_m
$$
be its irreducible components.

For each $i$, put
$$
V_i
=
X_i\setminus\bigcup_{j\ne i}X_j.
$$
This is a nonempty open subset of $X$: it is the part of the component $X_i$ which lies on no other component.

Let
$$
Y_i\hookrightarrow X
$$
be the scheme-theoretic closure of the open immersion
$$
V_i\hookrightarrow X.
$$
Then $\underlyingspace{Y_i}=X_i$, so $Y_i$ is irreducible as a topological space.
It is a closed subscheme of the proper $S$-scheme $X$, hence is proper over $S$.
Moreover
$$
Y_i\restrict_{V_i}=V_i
$$
scheme-theoretically: over the open set $V_i$ the given immersion is already a closed immersion onto all of $V_i$, so its scheme-theoretic image there is $V_i$ itself.

Assume the theorem known for schemes with irreducible underlying space.
For each $Y_i$ choose a projective $S$-scheme
$$
Y_i'
$$
and a morphism
$$
g_i:Y_i'\to Y_i
$$
which is an isomorphism over some dense open subset of $Y_i$.
Intersect that dense open with $V_i$; after replacing it by this smaller nonempty dense open, write it as
$$
W_i\subseteq V_i.
$$
Then $g_i$ is an isomorphism over $W_i$, and the composite
$$
Y_i'\xrightarrow{g_i}Y_i\hookrightarrow X
$$
is an isomorphism over $W_i\subseteq X$.

Set
$$
X'=\coprod_{i=1}^mY_i'.
$$
A finite disjoint union of projective $S$-schemes is projective over $S$: if
$$
Y_i'\hookrightarrow\PP^{n_i}_S,
$$
embed the finitely many projective spaces into pairwise disjoint coordinate linear subspaces of one sufficiently large projective space over $S$; their finite union is closed.

The morphisms $Y_i'\to X$ combine to
$$
g:X'\to X.
$$
The opens $W_i$ are pairwise disjoint by construction, and
$$
W=\bigcup_iW_i
$$
is open and dense in $X$: it meets every irreducible component in a dense open subset.
Over $W$ the morphism $g$ is the disjoint union of the isomorphisms
$$
g_i^{-1}(W_i)\xrightarrow{\sim}W_i.
$$
Hence $g^{-1}(W)\to W$ is an isomorphism.

Thus the irreducible case implies the general case, including the nonreduced scheme structure on the dense open.

:::

:::

::: {.pf-step #s2}

We now assume $X$ irreducible.
Every point $x\in X$ has an open neighborhood which is quasi-projective over $S$.

::: pf-proof

Let $s\in S$ be the image of $x$.
Choose an affine open neighborhood
$$
V=\Spec B\subseteq S
$$
of $s$.
The inverse image
$$
X_V=X\times_SV
$$
is of finite type over $V$.

Choose an affine open neighborhood
$$
W=\Spec A\subseteq X_V
$$
of $x$.
By Hartshorne II.3.3(c), $A$ is a finitely generated $B$-algebra.
Hence there is a surjection
$$
B[t_1,\ldots,t_N]\twoheadrightarrow A,
$$
which gives a closed immersion
$$
W\hookrightarrow\AA^N_V.
$$

The affine space $\AA^N_V$ is the standard open subset of
$$
\PP^N_V,
$$
and $\PP^N_V$ is itself an open subscheme of
$$
\PP^N_S
$$
because $V\subseteq S$ is open.
Thus the composite
$$
W\longrightarrow\PP^N_S
$$
is a locally closed immersion.

Let $P_W$ be its scheme-theoretic closure in $\PP^N_S$.  Then
$$
W\hookrightarrow P_W
$$
is an open immersion and
$$
P_W\hookrightarrow\PP^N_S
$$
is a closed immersion.  Hence $P_W$ is projective over $S$, and $W$ is quasi-projective over $S$.

:::

:::

::: {.pf-step #s3}

There is a finite open cover
$$
X=U_1\cup\cdots\cup U_n
$$
such that every $U_i$ is quasi-projective over $S$.

::: pf-proof

The neighborhoods from step [](#s2){.pf-ref} cover $X$.  Since $X$ is proper over $S$, it is of finite type, hence quasi-compact because $S$ is noetherian and the structure morphism is proper.  Thus finitely many of the quasi-projective neighborhoods suffice.

:::

:::

::: {.pf-step #s4}

For each $i$, choose an open immersion
$$
j_i:U_i\hookrightarrow P_i
$$
with $P_i$ projective over $S$.
The open subset
$$
U=\bigcap_{i=1}^nU_i
$$
is nonempty and dense in $X$.

::: pf-proof

The first assertion is the definition of quasi-projectivity.

Since $X$ is irreducible, every nonempty open subset is dense, and any finite intersection of nonempty open subsets is nonempty.  Thus the finite intersection $U$ is nonempty, open, and dense.

:::

:::

::: {.pf-step #s5}

Put
$$
P=P_1\times_S\cdots\times_SP_n.
$$
Then $P$ is projective over $S$.

::: pf-proof

Projective morphisms are stable under finite products by Hartshorne II.4.8 together with II.4.9.  Hence the structure morphism
$$
P\to S
$$
is projective.

:::

:::

::: {.pf-step #s6}

The maps
$$
U\hookrightarrow X,
\qquad
U\hookrightarrow U_i\xrightarrow{j_i}P_i
$$
define a morphism
$$
f:U\longrightarrow Q:=X\times_SP,
$$
given on points by
$$
x\longmapsto\bigl(x,j_1(x),\ldots,j_n(x)\bigr).
$$
Let
$$
X'\hookrightarrow Q
$$
be the scheme-theoretic image of $f$.

::: pf-proof

The universal property of the fibre product gives the displayed morphism from its coordinate maps.

Since $U$ is noetherian, the morphism $f$ is quasi-compact and quasi-separated.  Hartshorne II.3.11 therefore supplies its scheme-theoretic image, a closed subscheme $X'\subseteq Q$ through which $f$ factors minimally.

:::

:::

::: {.pf-step #s7}

Let
$$
g:X'\to X,
\qquad
h:X'\to P
$$
be the restrictions of the two projections from $Q=X\times_SP$.
The morphism $h$ is proper.

::: pf-proof

The projection
$$
Q=X\times_SP\longrightarrow P
$$
is the base change of the proper morphism
$$
X\longrightarrow S
$$
along $P\to S$.
Hence $Q\to P$ is proper.

The inclusion $X'\hookrightarrow Q$ is a closed immersion, hence proper.  Therefore their composite
$$
h:X'\to P
$$
is proper.

:::

:::

::: {.pf-step #s8}

For each $i$, let
$$
O_i=U_i\times_SP\subseteq Q.
$$
Then the opens $O_i$ cover $Q$, and hence
$$
X_i'=X'\cap O_i
$$
cover $X'$.

::: pf-proof

The opens $U_i$ cover $X$, so their inverse images under the projection
$$
Q\to X
$$
cover $Q$.  Intersecting with the closed subscheme $X'$ gives an open cover of $X'$.

:::

:::

::: {.pf-step #s9}

Let
$$
\pi_i:P\to P_i
$$
be the $i$th projection and define
$$
G_i
=
U_i\times_{P_i}P,
$$
where $U_i\to P_i$ is $j_i$ and $P\to P_i$ is $\pi_i$.
Then
$$
G_i\to P
$$
is an open immersion.

::: pf-proof

The morphism $G_i\to P$ is the base change of the open immersion
$$
j_i:U_i\hookrightarrow P_i
$$
along $\pi_i:P\to P_i$.  Open immersions are stable under base change.

:::

:::

::: {.pf-step #s10}

There is a closed immersion
$$
G_i\hookrightarrow O_i=U_i\times_SP.
$$

::: pf-proof

The morphism is the graph of the composite
$$
U_i\xrightarrow{j_i}P_i
$$
in the $i$th projective factor, together with the unrestricted remaining factors.

More explicitly, the graph
$$
\Gamma_{j_i}:U_i\longrightarrow U_i\times_SP_i
$$
is a closed immersion because $P_i$ is separated over $S$; projective morphisms are separated.  Base changing this graph along the product of the remaining factors gives
$$
G_i\hookrightarrow U_i\times_SP=O_i.
$$
Thus it is a closed immersion.

:::

:::

::: {.pf-step #s11}

The image $f(U)$ is contained in every $G_i\subseteq O_i$, and consequently
$$
X_i'=X'\cap O_i
$$
is a closed subscheme of $G_i$.

::: pf-proof

For $x\in U$, the $i$th projective coordinate of $f(x)$ is by definition $j_i(x)$.
Hence
$$
f(U)\subseteq G_i.
$$

Inside the open scheme $O_i$, the subscheme $G_i$ is closed by step [](#s10){.pf-ref}.  The restriction of the scheme-theoretic image $X'$ to $O_i$ is the scheme-theoretic image of
$$
f^{-1}(O_i)=U\longrightarrow O_i.
$$
Because this morphism factors through the closed subscheme $G_i$, minimality of the scheme-theoretic image gives a factorization
$$
X_i'\hookrightarrow G_i.
$$
This factor is again a closed immersion.

:::

:::

::: {.pf-step #s12}

For each $i$, let
$$
u_i:G_i\xrightarrow{\pi_i}j_i(U_i)\xrightarrow{j_i^{-1}}U_i\hookrightarrow X
$$
be the composite, where $G_i\to j_i(U_i)$ is the projection $\pi_i$ restricted to its image.
The graph
$$
\Gamma_{u_i}\subseteq X\times_SG_i
$$
is a closed subscheme, and the projection of $\Gamma_{u_i}$ onto $G_i$ is an isomorphism.

::: pf-proof

Because $X$ is proper over $S$, it is separated over $S$, so the diagonal $\Delta_{X/S}:X\to X\times_SX$ is a closed immersion.
In the Cartesian square
$$
\begin{array}{ccc}
\Gamma_{u_i}&\longrightarrow&X\times_SG_i\\
\downarrow&&\downarrow{\scriptstyle(x,p)\mapsto(x,u_i(p))}\\
X&\xrightarrow{\Delta_{X/S}}&X\times_SX,
\end{array}
$$
the upper left corner is the graph of $u_i$:  the fibre product consists of the pairs $(x,p)$ with $x=u_i(p)$.
Closed immersions are stable under base change, so $\Gamma_{u_i}$ is a closed subscheme of $X\times_SG_i$.
The inverse of the projection is $p\mapsto(u_i(p),p)$, and both composites are the identity.

This graph, and the use made of it in the next two steps, is step D) of the published proof of Chow's lemma in EGA II (Grothendieck, Éléments de géométrie algébrique II, Publications Mathématiques de l'IHÉS, Tome 8 (1961), Théorème 5.6.1, pp. 108–109).
That proof constructs the same scheme-theoretic image $X'$ of the graph morphism $U\to X\times_SP$;  EGA's $g$, $W_k$, $V'_k$, $u_k$ and $T_k$ are this proof's $h$, $G_i$, $h^{-1}(G_i)$, $u_i$ and $\Gamma_{u_i}$.
EGA works with separated $S$-schemes of finite type (in the 1961 edition of EGA a schéma is by definition separated);  here $X$ is separated over $S$ because it is proper over $S$.

:::

:::

::: {.pf-step #s13}

For every $i$, the restriction of $h$ to the full inverse image,
$$
\boxed{h^{-1}(G_i)\longrightarrow G_i,}
$$
is a closed immersion.

::: pf-proof

The preimage of the open $G_i\subseteq P$ under the projection $Q\to P$ is the open $X\times_SG_i\subseteq Q$, and it contains $f(U)$ because $j(U)\subseteq G_i$.
As in step [](#s11){.pf-ref}, the restriction of the scheme-theoretic image to this open is the scheme-theoretic image of the restricted morphism, so
$$
h^{-1}(G_i)=X'\cap(X\times_SG_i)
$$
is the scheme-theoretic image of $f:U\to X\times_SG_i$.

For $x\in U$ the two composites
$$
p_1\circ f,\qquad u_i\circ p_2\circ f:U\longrightarrow X
$$
are equal:  both send $x$ to $x$, the second because $j_i^{-1}(\pi_i(j(x)))=x$.
Hence $f$ factors through the closed subscheme $\Gamma_{u_i}\subseteq X\times_SG_i$.
Minimality of the scheme-theoretic image gives a factorization
$$
h^{-1}(G_i)\hookrightarrow\Gamma_{u_i},
$$
and this factor is again a closed immersion.

On $h^{-1}(G_i)$ the morphism $h$ is the second projection of $X\times_SG_i$ composed with this closed immersion.
Composing instead with the isomorphism $\Gamma_{u_i}\cong G_i$ of step [](#s12){.pf-ref} therefore exhibits $h^{-1}(G_i)\to G_i$ as a closed immersion.

:::

:::

::: {.pf-step #s13b}

The morphism
$$
\boxed{h:X'\longrightarrow P}
$$
is an immersion.

::: pf-proof

Put $G=G_1\cup\cdots\cup G_n$, an open subset of $P$.
By step [](#s8){.pf-ref} the opens $X_i'$ cover $X'$, and by step [](#s11){.pf-ref} each $X_i'$ is a closed subscheme of $G_i$.
The composite $X_i'\hookrightarrow G_i\hookrightarrow P$, the second arrow being the open immersion of step [](#s9){.pf-ref}, agrees with $h\restrict_{X_i'}$:  every map involved is one of the evident inclusions into $Q$ or projections of $Q$, and $h$ is the second projection of $Q$.
Hence $h(X')\subseteq G$, and $h$ factors through the open immersion $G\hookrightarrow P$.

The opens $G_i$ cover $G$, and by step [](#s13){.pf-ref} each restriction $h^{-1}(G_i)\to G_i$ is a closed immersion.
Being a closed immersion is local on the target:  affine-locally it is the surjectivity of a ring homomorphism, which can be checked after localizing at finitely many elements generating the unit ideal, and the condition on underlying topological spaces is local as well.
Hence $h:X'\to G$ is a closed immersion, and composing with the open immersion $G\hookrightarrow P$ shows that $h$ is an immersion.
This is the target-open assembly of EGA II, Théorème 5.6.1, step D) (pp. 108–109), where the opens $W_k$ cover the image $g(X')$ in place of the whole target.

:::

:::

::: {.pf-step #s14}

A proper immersion is a closed immersion.
Hence
$$
\boxed{h:X'\hookrightarrow P}
$$
is a closed immersion.

::: pf-proof

An immersion factors as an open immersion followed by a closed immersion onto a locally closed subscheme of the target.
A proper morphism is closed, so the image of the proper immersion $h$ is closed in $P$.
Thus the locally closed image is actually closed, and the immersion is a closed immersion.

Equivalently, a proper monomorphism is a closed immersion.

:::

:::

::: {.pf-step #s15}

The scheme $X'$ is projective over $S$.

::: pf-proof

By step [](#s5){.pf-ref}, $P$ is projective over $S$.  By step [](#s14){.pf-ref}, $X'$ is a closed subscheme of $P$.  A closed immersion followed by a projective morphism is projective.  Hence
$$
X'\to S
$$
is projective.

:::

:::

::: {.pf-step #s16}

Inside the open subscheme
$$
O=U\times_SP\subseteq Q,
$$
the morphism
$$
f:U\to O
$$
is a closed immersion.

::: pf-proof

The morphism $U\to P$ is the product of the maps
$$
j_i\restrict_U:U\to P_i.
$$
The scheme $P$ is separated over $S$, being projective.  Therefore the graph
$$
U\longrightarrow U\times_SP=O
$$
of $U\to P$ is a closed immersion.  This graph is precisely $f$.

:::

:::

::: {.pf-step #s17}

The restriction of $X'$ to $O$ is exactly $f(U)$ scheme-theoretically:
$$
\boxed{X'\cap O=f(U).}
$$

::: pf-proof

The scheme-theoretic image commutes with restriction to an open subscheme for the quasi-compact morphism $f$.  Thus
$$
X'\cap O
$$
is the scheme-theoretic image of
$$
f:U\to O.
$$
But step [](#s16){.pf-ref} shows that this map is already a closed immersion.  Its scheme-theoretic image is therefore its closed image $f(U)$ itself.

:::

:::

::: {.pf-step #s18}

The inverse image of $U\subseteq X$ under $g$ is
$$
g^{-1}(U)=X'\cap O=f(U).
$$

::: pf-proof

The inverse image under the projection
$$
g:X'\to X
$$
of $U$ is the intersection of $X'$ with the inverse image of $U$ in $Q=X\times_SP$, namely
$$
U\times_SP=O.
$$
Apply step [](#s17){.pf-ref}.

:::

:::

::: {.pf-step #s19}

The morphism
$$
\boxed{g^{-1}(U)\xrightarrow{\sim}U}
$$
is an isomorphism.

::: pf-proof

By step [](#s18){.pf-ref}, the source is the graph $f(U)$.  The first projection
$$
f(U)\longrightarrow U
$$
is inverse to the graph morphism
$$
f:U\longrightarrow f(U).
$$
Thus $g$ restricts to an isomorphism over $U$.

:::

:::

::: {.pf-step #s20}

This proves Chow's lemma.

::: pf-proof

In the irreducible case, steps [](#s3){.pf-ref} and [](#s4){.pf-ref} produce the finite quasi-projective cover and dense open $U$ requested in part (b). Steps [](#s5){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref}, [](#s8){.pf-ref}, [](#s9){.pf-ref}, [](#s10){.pf-ref}, [](#s11){.pf-ref}, [](#s12){.pf-ref}, [](#s13){.pf-ref}, [](#s13b){.pf-ref}, [](#s14){.pf-ref} and [](#s15){.pf-ref} construct the projective scheme $X'$ and prove part (c). Steps [](#s16){.pf-ref}, [](#s17){.pf-ref}, [](#s18){.pf-ref} and [](#s19){.pf-ref} prove part (d).

Finally step [](#s1){.pf-ref} reduces the general noetherian proper scheme to this irreducible case.  Hence there exist a projective $S$-scheme $X'$ and a morphism
$$
g:X'\to X
$$
which is an isomorphism over a dense open subset of $X$.

:::

:::

:::

:::
