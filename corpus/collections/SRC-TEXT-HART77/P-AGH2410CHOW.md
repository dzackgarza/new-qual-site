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
---

::: {.problem}
This result says that proper morphisms are fairly close to projective morphisms.

Let $X$ be proper over a noetherian scheme $S$.
Then there is a scheme $X'$ and a morphism $g: X' \to X$ such that $X'$ is projective over $S$, and there is an open dense subset $U \subseteq X$ such that $g$ induces an isomorphism of $\inverseof{g}(U)$ onto $U$.
Prove this in the following steps.

a. Reduce to the case $X$ irreducible.

b. Show that $X$ can be covered by finitely many open subsets $U_i$, $i = 1, \ldots, n$, each of which is quasi-projective over $S$.
   Let $U_i \injects P_i$ be an open immersion of $U_i$ into a scheme $P_i$ which is projective over $S$.

c. Let $U = \bigcap_i U_i$, and consider the map
\[
f: U \to X \fiberproduct{S} P_1 \fiberproduct{S} \cdots \fiberproduct{S} P_n
\]
deduced from the given maps $U \to X$ and $U \to P_i$.
Let $X'$ be the closed image subscheme structure on $\cl_X f(U)$ (see Ex. 3.11d).
Let $g: X' \to X$ be the projection onto the first factor, and let $h: X' \to P = P_1 \fiberproduct{S} \cdots \fiberproduct{S} P_n$ be the projection onto the product of the remaining factors.
Show that $h$ is a closed immersion, hence $X'$ is projective over $S$.

d. Show that $\inverseof{g}(U) \to U$ is an isomorphism, completing the proof.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

It is enough to prove the theorem when the underlying topological space of $X$ is irreducible.

::: pf-proof

Because $X$ is proper over the noetherian scheme $S$, it is noetherian.
Let
\[
X_1,\ldots,X_m
\]
be its irreducible components.

For each $i$, put
\[
V_i
=
X_i\setminus\bigcup_{j\ne i}X_j.
\]
This is a nonempty open subset of $X$: it is the part of the component $X_i$ which lies on no other component.

Let
\[
Y_i\hookrightarrow X
\]
be the scheme-theoretic closure of the open immersion
\[
V_i\hookrightarrow X.
\]
Then $|Y_i|=X_i$, so $Y_i$ is irreducible as a topological space.
It is a closed subscheme of the proper $S$-scheme $X$, hence is proper over $S$.
Moreover
\[
Y_i|_{V_i}=V_i
\]
scheme-theoretically: over the open set $V_i$ the given immersion is already a closed immersion onto all of $V_i$, so its scheme-theoretic image there is $V_i$ itself.

Assume the theorem known for schemes with irreducible underlying space.
For each $Y_i$ choose a projective $S$-scheme
\[
Y_i'
\]
and a morphism
\[
g_i:Y_i'\to Y_i
\]
which is an isomorphism over some dense open subset of $Y_i$.
Intersect that dense open with $V_i$; after replacing it by this smaller nonempty dense open, write it as
\[
W_i\subseteq V_i.
\]
Then $g_i$ is an isomorphism over $W_i$, and the composite
\[
Y_i'\xrightarrow{g_i}Y_i\hookrightarrow X
\]
is an isomorphism over $W_i\subseteq X$.

Set
\[
X'=\coprod_{i=1}^mY_i'.
\]
A finite disjoint union of projective $S$-schemes is projective over $S$: if
\[
Y_i'\hookrightarrow\mathbb P^{n_i}_S,
\]
embed the finitely many projective spaces into pairwise disjoint coordinate linear subspaces of one sufficiently large projective space over $S$; their finite union is closed.

The morphisms $Y_i'\to X$ combine to
\[
g:X'\to X.
\]
The opens $W_i$ are pairwise disjoint by construction, and
\[
W=\bigcup_iW_i
\]
is open and dense in $X$: it meets every irreducible component in a dense open subset.
Over $W$ the morphism $g$ is the disjoint union of the isomorphisms
\[
g_i^{-1}(W_i)\xrightarrow{\sim}W_i.
\]
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
\[
V=\Spec B\subseteq S
\]
of $s$.
The inverse image
\[
X_V=X\times_SV
\]
is of finite type over $V$.

Choose an affine open neighborhood
\[
W=\Spec A\subseteq X_V
\]
of $x$.
By Hartshorne II.3.3(c), $A$ is a finitely generated $B$-algebra.
Hence there is a surjection
\[
B[t_1,\ldots,t_N]\twoheadrightarrow A,
\]
which gives a closed immersion
\[
W\hookrightarrow\mathbb A^N_V.
\]

The affine space $\mathbb A^N_V$ is the standard open subset of
\[
\mathbb P^N_V,
\]
and $\mathbb P^N_V$ is itself an open subscheme of
\[
\mathbb P^N_S
\]
because $V\subseteq S$ is open.
Thus the composite
\[
W\longrightarrow\mathbb P^N_S
\]
is a locally closed immersion.

Let $P_W$ be its scheme-theoretic closure in $\mathbb P^N_S$.  Then
\[
W\hookrightarrow P_W
\]
is an open immersion and
\[
P_W\hookrightarrow\mathbb P^N_S
\]
is a closed immersion.  Hence $P_W$ is projective over $S$, and $W$ is quasi-projective over $S$.

:::

:::

::: {.pf-step #s3}

There is a finite open cover
\[
X=U_1\cup\cdots\cup U_n
\]
such that every $U_i$ is quasi-projective over $S$.

::: pf-proof

The neighborhoods from step [](#s2){.pf-ref} cover $X$.  Since $X$ is proper over $S$, it is of finite type, hence quasi-compact because $S$ is noetherian and the structure morphism is proper.  Thus finitely many of the quasi-projective neighborhoods suffice.

:::

:::

::: {.pf-step #s4}

For each $i$, choose an open immersion
\[
j_i:U_i\hookrightarrow P_i
\]
with $P_i$ projective over $S$.
The open subset
\[
U=\bigcap_{i=1}^nU_i
\]
is nonempty and dense in $X$.

::: pf-proof

The first assertion is the definition of quasi-projectivity.

Since $X$ is irreducible, every nonempty open subset is dense, and any finite intersection of nonempty open subsets is nonempty.  Thus the finite intersection $U$ is nonempty, open, and dense.

:::

:::

::: {.pf-step #s5}

Put
\[
P=P_1\times_S\cdots\times_SP_n.
\]
Then $P$ is projective over $S$.

::: pf-proof

Projective morphisms are stable under finite products by Hartshorne II.4.8 together with II.4.9.  Hence the structure morphism
\[
P\to S
\]
is projective.

:::

:::

::: {.pf-step #s6}

The maps
\[
U\hookrightarrow X,
\qquad
U\hookrightarrow U_i\xrightarrow{j_i}P_i
\]
define a morphism
\[
f:U\longrightarrow Q:=X\times_SP,
\]
given on points by
\[
x\longmapsto\bigl(x,j_1(x),\ldots,j_n(x)\bigr).
\]
Let
\[
X'\hookrightarrow Q
\]
be the scheme-theoretic image of $f$.

::: pf-proof

The universal property of the fibre product gives the displayed morphism from its coordinate maps.

Since $U$ is noetherian, the morphism $f$ is quasi-compact and quasi-separated.  Hartshorne II.3.11 therefore supplies its scheme-theoretic image, a closed subscheme $X'\subseteq Q$ through which $f$ factors minimally.

:::

:::

::: {.pf-step #s7}

Let
\[
g:X'\to X,
\qquad
h:X'\to P
\]
be the restrictions of the two projections from $Q=X\times_SP$.
The morphism $h$ is proper.

::: pf-proof

The projection
\[
Q=X\times_SP\longrightarrow P
\]
is the base change of the proper morphism
\[
X\longrightarrow S
\]
along $P\to S$.
Hence $Q\to P$ is proper.

The inclusion $X'\hookrightarrow Q$ is a closed immersion, hence proper.  Therefore their composite
\[
h:X'\to P
\]
is proper.

:::

:::

::: {.pf-step #s8}

For each $i$, let
\[
O_i=U_i\times_SP\subseteq Q.
\]
Then the opens $O_i$ cover $Q$, and hence
\[
X_i'=X'\cap O_i
\]
cover $X'$.

::: pf-proof

The opens $U_i$ cover $X$, so their inverse images under the projection
\[
Q\to X
\]
cover $Q$.  Intersecting with the closed subscheme $X'$ gives an open cover of $X'$.

:::

:::

::: {.pf-step #s9}

Let
\[
\pi_i:P\to P_i
\]
be the $i$th projection and define
\[
G_i
=
U_i\times_{P_i}P,
\]
where $U_i\to P_i$ is $j_i$ and $P\to P_i$ is $\pi_i$.
Then
\[
G_i\to P
\]
is an open immersion.

::: pf-proof

The morphism $G_i\to P$ is the base change of the open immersion
\[
j_i:U_i\hookrightarrow P_i
\]
along $\pi_i:P\to P_i$.  Open immersions are stable under base change.

:::

:::

::: {.pf-step #s10}

There is a closed immersion
\[
G_i\hookrightarrow O_i=U_i\times_SP.
\]

::: pf-proof

The morphism is the graph of the composite
\[
U_i\xrightarrow{j_i}P_i
\]
in the $i$th projective factor, together with the unrestricted remaining factors.

More explicitly, the graph
\[
\Gamma_{j_i}:U_i\longrightarrow U_i\times_SP_i
\]
is a closed immersion because $P_i$ is separated over $S$; projective morphisms are separated.  Base changing this graph along the product of the remaining factors gives
\[
G_i\hookrightarrow U_i\times_SP=O_i.
\]
Thus it is a closed immersion.

:::

:::

::: {.pf-step #s11}

The image $f(U)$ is contained in every $G_i\subseteq O_i$, and consequently
\[
X_i'=X'\cap O_i
\]
is a closed subscheme of $G_i$.

::: pf-proof

For $x\in U$, the $i$th projective coordinate of $f(x)$ is by definition $j_i(x)$.
Hence
\[
f(U)\subseteq G_i.
\]

Inside the open scheme $O_i$, the subscheme $G_i$ is closed by step [](#s10){.pf-ref}.  The restriction of the scheme-theoretic image $X'$ to $O_i$ is the scheme-theoretic image of
\[
f^{-1}(O_i)=U\longrightarrow O_i.
\]
Because this morphism factors through the closed subscheme $G_i$, minimality of the scheme-theoretic image gives a factorization
\[
X_i'\hookrightarrow G_i.
\]
This factor is again a closed immersion.

:::

:::

::: {.pf-step #s12}

The restriction
\[
h|_{X_i'}:X_i'\longrightarrow P
\]
is an immersion for every $i$.

::: pf-proof

By step [](#s11){.pf-ref},
\[
X_i'\hookrightarrow G_i
\]
is a closed immersion, and by step [](#s9){.pf-ref},
\[
G_i\hookrightarrow P
\]
is an open immersion.  Their composition is therefore an immersion.

:::

:::

::: {.pf-step #s13}

The morphism
\[
h:X'\to P
\]
is an immersion.

::: pf-proof

Being an immersion is local on the source.  The open subsets $X_i'$ cover $X'$ by step [](#s8){.pf-ref}, and the restriction of $h$ to each is an immersion by step [](#s12){.pf-ref}.  Hence $h$ is an immersion.

:::

:::

::: {.pf-step #s14}

A proper immersion is a closed immersion.
Hence
\[
\boxed{h:X'\hookrightarrow P}
\]
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
\[
X'\to S
\]
is projective.

:::

:::

::: {.pf-step #s16}

Inside the open subscheme
\[
O=U\times_SP\subseteq Q,
\]
the morphism
\[
f:U\to O
\]
is a closed immersion.

::: pf-proof

The morphism $U\to P$ is the product of the maps
\[
j_i|_U:U\to P_i.
\]
The scheme $P$ is separated over $S$, being projective.  Therefore the graph
\[
U\longrightarrow U\times_SP=O
\]
of $U\to P$ is a closed immersion.  This graph is precisely $f$.

:::

:::

::: {.pf-step #s17}

The restriction of $X'$ to $O$ is exactly $f(U)$ scheme-theoretically:
\[
\boxed{X'\cap O=f(U).}
\]

::: pf-proof

The scheme-theoretic image commutes with restriction to an open subscheme for the quasi-compact morphism $f$.  Thus
\[
X'\cap O
\]
is the scheme-theoretic image of
\[
f:U\to O.
\]
But step [](#s16){.pf-ref} shows that this map is already a closed immersion.  Its scheme-theoretic image is therefore its closed image $f(U)$ itself.

:::

:::

::: {.pf-step #s18}

The inverse image of $U\subseteq X$ under $g$ is
\[
g^{-1}(U)=X'\cap O=f(U).
\]

::: pf-proof

The inverse image under the projection
\[
g:X'\to X
\]
of $U$ is the intersection of $X'$ with the inverse image of $U$ in $Q=X\times_SP$, namely
\[
U\times_SP=O.
\]
Apply step [](#s17){.pf-ref}.

:::

:::

::: {.pf-step #s19}

The morphism
\[
\boxed{g^{-1}(U)\xrightarrow{\sim}U}
\]
is an isomorphism.

::: pf-proof

By step [](#s18){.pf-ref}, the source is the graph $f(U)$.  The first projection
\[
f(U)\longrightarrow U
\]
is inverse to the graph morphism
\[
f:U\longrightarrow f(U).
\]
Thus $g$ restricts to an isomorphism over $U$.

:::

:::

::: {.pf-step #s20}

This proves Chow's lemma.

::: pf-proof

In the irreducible case, steps [](#s3){.pf-ref} and [](#s4){.pf-ref} produce the finite quasi-projective cover and dense open $U$ requested in part (b). Steps [](#s5){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref}, [](#s8){.pf-ref}, [](#s9){.pf-ref}, [](#s10){.pf-ref}, [](#s11){.pf-ref}, [](#s12){.pf-ref}, [](#s13){.pf-ref}, [](#s14){.pf-ref} and [](#s15){.pf-ref} construct the projective scheme $X'$ and prove part (c). Steps [](#s16){.pf-ref}, [](#s17){.pf-ref}, [](#s18){.pf-ref} and [](#s19){.pf-ref} prove part (d).

Finally step [](#s1){.pf-ref} reduces the general noetherian proper scheme to this irreducible case.  Hence there exist a projective $S$-scheme $X'$ and a morphism
\[
g:X'\to X
\]
which is an isomorphism over a dense open subset of $X$.

:::

:::

::: pf-qed

Step [](#s20){.pf-ref} is the stated theorem.

:::

:::

:::
