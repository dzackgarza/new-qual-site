---
schema: qual/card@1
id: P-AGH2215VARTOSCH
kind: problem
title: Varieties over an algebraically closed field embed fully faithfully into schemes
classification:
  areas:
  - algebraic-geometry
  topics:
  - Varieties
  - Schemes
  - Residue Fields
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.2.15 statement and source-order placement after II.2.14.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read Mark Haiman, Varieties as Schemes (Berkeley Math 256, March 2019), 8.8
    with the proof in 8.10 (PDF p. 18, text version `tmp/sources/haiman-varieties-as-schemes.md`), which establishes the functorial
    equivalence between classical varieties over an algebraically closed
    field and reduced algebraic schemes over it, hence the bijection of Hom
    sets that part (c) asks for. Rechecked the card's own construction: for
    each P the affine neighbourhoods with f(V_0) in W_0, the ring map B to
    A, the induced affine-variety morphism agreeing with f on V_0, and t(f)
    = F on each affine chart. Not checked: the converse direction in the
    notes for nonaffine varieties beyond the covering argument quoted.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Part (c) now follows Haiman's proof as its own two steps rather than
    citing it: step haiman-local-description is the first paragraph of 8.10,
    PDF p. 19, resting on the identity O(X) = O_X(X) of 8.9 on PDF p. 18,
    and step haiman-affine-case is the rest of 8.10, PDF pp. 18--19. The
    steps that followed, which build f from F chart by chart, are kept and
    now read as the details of those two steps; map-surjective says so. The
    notes carry no printed folio, so PDF pages are given, as the earlier
    event noted. Read against the book: Hartshorne II Ex. 2.15(c) on
    printed p. 81 asks for the bijection onto Hom of k-schemes, which
    Haiman's Theorem 8.8 gives for the schemes t(V), t(W) of II.2.6; the
    hypothesis that k be algebraically closed is Hartshorne's, and Haiman's
    too. Not checked: Haiman's 8.2--8.7, on which his 8.8 rests, beyond
    reading that the soberization of a variety is Spec of its coordinate
    ring on the affine charts this card uses.
---

::: {.problem}
(a) Let $V$ be a variety over the algebraically closed field $k$.
Show that a point $P \in t(V)$ is a closed point if and only if its residue field is $k$.

(b) If $f: X \to Y$ is a morphism of schemes over $k$ and $P \in X$ is a point with residue field $k$, then $f(P) \in Y$ also has residue field $k$.

(c) Now show that if $V, W$ are any two varieties over $k$, then the natural map
$$
\Hom_{\mathsf{Var}_k}(V, W) \to \Hom_{\Sch_k}\qty{t(V), t(W)}
$$
is bijective.
(Injectivity is easy. The hard part is to show it is surjective.)
:::

::: {.solution}

Part (c) is Mark Haiman's proof, *Varieties as Schemes* (Berkeley Math 256, March 2019), Theorem 8.8 with its proof in 8.10, text version `tmp/sources/haiman-varieties-as-schemes.md`. The notes carry no printed folio, so the places are cited by section and by PDF page of the copy at `tmp/sources/haiman-varieties-as-schemes.pdf`: the theorem on PDF p. 18, its proof on PDF pp. 18--19, and the identity $\OO(X)=\OO_X(X)$ that it uses in 8.9 on PDF p. 18. Steps [](#haiman-local-description){.pf-ref} and [](#haiman-affine-case){.pf-ref} are its two steps; the steps after them supply, for this statement, the details Haiman leaves to the reader.

::: pf

::: {.pf-step #point-corresponds-to-subvariety}
A point of $t(V)$ corresponds to an irreducible closed subvariety
$$
Z\subseteq V,
$$
and its residue field is the function field
$$
\boxed{
\kappa(\eta_Z)=k(Z).
}
$$

::: pf-proof
Choose an affine open subset
$$
U=\Spec A
$$
of the associated scheme meeting the point $\eta_Z$.  In the classical variety, this corresponds to an affine open subset of $V$, and
$$
Z\cap U
$$
is defined by a prime ideal
$$
\mfp \subseteq A.
$$
The point $\eta_Z$ is the prime $\mfp$.  Its residue field is
$$
\kappa(\mfp)
=\Frac(A/\mfp),
$$
which is precisely the rational function field of the irreducible variety $Z$.
:::

:::

::: {.pf-step #closed-point-residue-field-k}
If $P\in t(V)$ is a closed point, then
$$
\boxed{\kappa(P)=k.}
$$

::: pf-proof
A closed point of $t(V)$ corresponds to an ordinary closed point
$$
p\in V.
$$
Choose an affine neighborhood with coordinate ring $A$.  The point is a maximal ideal
$$
\mfm \subseteq A.
$$
Since $A$ is a finitely generated $k$-algebra and $k$ is algebraically closed, the weak Nullstellensatz gives
$$
A/\mfm \cong k.
$$
This quotient is the residue field at the closed point.
:::

:::

::: {.pf-step #residue-field-k-implies-closed}
Conversely, if
$$
P\in t(V)
$$
has residue field $k$, then $P$ is closed.

::: pf-proof
Let $Z$ be the irreducible closed subvariety whose generic point is $P$.  By step [](#point-corresponds-to-subvariety){.pf-ref},
$$
k(Z)=\kappa(P)=k.
$$
The transcendence degree of the function field of an irreducible variety equals its dimension, so
$$
\dim Z
=\trdeg_k k(Z)
=0.
$$

An irreducible zero-dimensional variety over an algebraically closed field is a single closed point.  Therefore
$$
Z=\{P\},
$$
so $P$ is closed in $t(V)$.
:::

:::

::: {.pf-step #closed-iff-residue-field-k}
Hence
$$
\boxed{
P\in t(V)\text{ is closed}
\iff
\kappa(P)=k.
}
$$

::: pf-proof
Combine steps [](#closed-point-residue-field-k){.pf-ref} and [](#residue-field-k-implies-closed){.pf-ref}.
:::

:::

::: {.pf-step #morphism-preserves-residue-field-k}
Let
$$
f:X\longrightarrow Y
$$
be a morphism of schemes over $k$, and let $P\in X$ satisfy
$$
\kappa(P)=k.
$$
Then
$$
\boxed{\kappa(f(P))=k.}
$$

::: pf-proof
Put
$$
Q=f(P).
$$
The local homomorphism
$$
f_P^\sharp:
\OO_{Y,Q}
\longrightarrow
\OO_{X,P}
$$
induces an injective homomorphism of residue fields
$$
\kappa(Q)
\hookrightarrow
\kappa(P)=k.
$$
Because $f$ is a morphism over $k$, the composite
$$
k
\longrightarrow
\kappa(Q)
\longrightarrow
k
$$
is the identity.  Thus the image of $\kappa(Q)$ inside $k$ contains the image of $k$, which is all of $k$.  Since it is also a subfield of $k$, the image is exactly $k$.

The injection is therefore a $k$-algebra isomorphism
$$
\kappa(Q)\cong k.
$$
:::

:::

::: {.pf-step #haiman-local-description}
A morphism of varieties is the same thing as a compatible system of morphisms between affine open subvarieties.

::: pf-proof
This is the first paragraph of Haiman's proof of Theorem 8.8, §8.10, PDF p. 19.

By §8.9, PDF p. 18, every global regular function on a classical affine variety is a polynomial, $\OO(X)=\OO_X(X)$; consequently, for a polynomial function $f$ on an affine variety $X$, the open subspace $X_f$ is again an affine variety with coordinate ring $\OO(X)_f$. Hence the open subsets of a classical variety that are isomorphic to affine varieties form a base of its topology.

To give a morphism $f:X\to X'$ of classical varieties is therefore equivalent to giving a system of compatible morphisms $f_U:U\to W$ from open affine subvarieties $U$ covering $X$ to open affine subvarieties $W\subseteq X'$, the compatibility being agreement on the intersections, which are covered by affine opens in their turn.

Morphisms $g:Y\to Y'$ of schemes have the same local description, since affine open subschemes form a base of the topology of a scheme.
:::

:::

::: {.pf-step #haiman-affine-case}
For affine varieties the morphisms correspond bijectively to $k$-algebra homomorphisms of coordinate rings, and the same holds for affine schemes, so for affine $V$ and $W$ the map $\Hom(V,W)\to\Hom(t(V),t(W))$ is bijective.

::: pf-proof
This is the rest of Haiman's proof of Theorem 8.8, §8.10, PDF pp. 18--19.

Let $X$ and $X'$ be classical affine varieties over $k$ with coordinate rings $R=\OO(X)$ and $R'=\OO(X')$. By §8.9 the canonical homomorphism $\OO(X)\to\OO_X(X)$ is an isomorphism, so a morphism $f:X\to X'$ is exactly a ringed-space morphism into an affine scheme over $k$, that is, a $k$-algebra homomorphism $R'\to R$; the correspondence is functorial because it is the functor $(X,\OO_X)\mapsto\OO_X(X)$.

For affine $k$-schemes $Y=\Spec R$ and $Y'=\Spec R'$ the same argument, now by the universal property of the spectrum, gives a functorial bijection between $k$-morphisms $Y\to Y'$ and $k$-algebra homomorphisms $R'\to R$.

Composing one bijection with the inverse of the other, and noting that $t$ carries the affine variety with coordinate ring $R$ to $\Spec R$, gives the bijection for affine $V$ and $W$.
:::

:::

::: {.pf-step #f-sends-closed-points-set-map}
Let
$$
F:t(V)\longrightarrow t(W)
$$
be a morphism of schemes over $k$.  Then $F$ sends closed points to closed points and therefore determines a set map
$$
\boxed{
f:V\longrightarrow W.
}
$$

::: pf-proof
By step [](#closed-iff-residue-field-k){.pf-ref}, the closed points of $t(V)$ are exactly the points with residue field $k$.  By step [](#morphism-preserves-residue-field-k){.pf-ref}, $F$ sends each such point to a point of $t(W)$ whose residue field is $k$, which by step [](#closed-iff-residue-field-k){.pf-ref} is closed.

The closed points of $t(V)$ and $t(W)$ identify respectively with the ordinary points of the classical varieties $V$ and $W$.  Restricting the underlying map of $F$ to those closed points gives the stated set map $f$.
:::

:::

::: {.pf-step #f-continuous}
The map $f:V\to W$ is continuous in the Zariski topology.

::: pf-proof
The classical variety $V$ identifies with the subspace of closed points of $t(V)$, and similarly for $W$.  Let
$$
C\subseteq W
$$
be closed.  The corresponding subset
$$
t(C)\subseteq t(W)
$$
is closed, and its closed points are exactly $C$.

Since $F$ is continuous,
$$
F^{-1}(t(C))
$$
is closed in $t(V)$.  Intersecting with the closed-point subspace $V$ gives
$$
f^{-1}(C),
$$
which is therefore closed in $V$.  Hence $f$ is continuous.
:::

:::

::: {.pf-step #affine-neighborhoods-exist}
Fix $P\in V$.  There are affine open neighborhoods
$$
P\in V_0\subseteq V,
\qquad
f(P)\in W_0\subseteq W,
$$
such that
$$
f(V_0)\subseteq W_0.
$$

::: pf-proof
Choose an affine open neighborhood
$$
W_0\subseteq W
$$
of $f(P)$.  The corresponding open subscheme
$$
t(W_0)\subseteq t(W)
$$
has open inverse image
$$
F^{-1}(t(W_0))
\subseteq t(V).
$$
Its closed points form the open subset
$$
f^{-1}(W_0)\subseteq V,
$$
which contains $P$.

Affine opens form a basis for a variety, so choose an affine open
$$
P\in V_0\subseteq f^{-1}(W_0).
$$
Then
$$
f(V_0)\subseteq W_0.
$$
:::

:::

::: {.pf-step #f-restriction-induced-by-ring-hom}
Write
$$
V_0=\Spec_{\mathrm{var}}A,
\qquad
W_0=\Spec_{\mathrm{var}}B
$$
for their affine coordinate rings.  The restriction
$$
F\restrict_{t(V_0)}:
t(V_0)=\Spec A
\longrightarrow
t(W_0)=\Spec B
$$
is induced by a $k$-algebra homomorphism
$$
\varphi:B\longrightarrow A.
$$

::: pf-proof
By step [](#affine-neighborhoods-exist){.pf-ref}, the scheme morphism $F$ maps the open subscheme $t(V_0)$ into $t(W_0)$.  Both are affine schemes associated to the affine varieties.  The affine anti-equivalence therefore identifies the restricted morphism with a unique ring homomorphism
$$
B\to A.
$$
Because $F$ is a morphism over $k$, this homomorphism is a $k$-algebra homomorphism.
:::

:::

::: {.pf-step #f0-agrees-with-f-on-v0}
The $k$-algebra map $\varphi:B\to A$ defines a morphism of affine varieties
$$
f_0:V_0\longrightarrow W_0,
$$
and on closed points
$$
f_0=f\restrict_{V_0}.
$$

::: pf-proof
The classical affine-coordinate correspondence sends a $k$-algebra homomorphism
$$
B\to A
$$
to a morphism of affine varieties
$$
\Spec_{\mathrm{var}}A
\to
\Spec_{\mathrm{var}}B.
$$

The associated scheme morphism is exactly the affine scheme morphism induced by the same ring map, namely
$$
F\restrict_{t(V_0)}.
$$
Hence their maps on closed points agree.  By definition of $f$ in step [](#f-sends-closed-points-set-map){.pf-ref}, this says
$$
f_0=f\restrict_{V_0}.
$$
:::

:::

::: {.pf-step #f-is-morphism-of-varieties}
The set map $f:V\to W$ is a morphism of varieties.

::: pf-proof
Every point $P\in V$ has an affine neighborhood $V_0$ on which step [](#f0-agrees-with-f-on-v0){.pf-ref} identifies $f$ with a morphism of affine varieties.  Regularity of a map of varieties is local on the source and target.  Therefore $f$ is a morphism globally.
:::

:::

::: {.pf-step #tf-equals-f-original}
The associated scheme morphism
$$
t(f):t(V)\longrightarrow t(W)
$$
is the original morphism $F$.

::: pf-proof
On each affine neighborhood $V_0$ from step [](#affine-neighborhoods-exist){.pf-ref}, both
$$
t(f)\restrict_{t(V_0)}
\quad\text{and}\quad
F\restrict_{t(V_0)}
$$
are the affine scheme morphism induced by the same ring homomorphism
$$
\varphi:B\to A
$$
from step [](#f-restriction-induced-by-ring-hom){.pf-ref}.  Thus they agree on an open cover of $t(V)$, hence agree globally.
:::

:::

::: {.pf-step #map-surjective}
Therefore the natural map
$$
\Hom_{\mathsf{Var}_k}(V,W)
\longrightarrow
\Hom_{\Sch_k}(t(V),t(W))
$$
is surjective.

::: pf-proof
In Haiman's form, §8.10, PDF p. 19: by step [](#haiman-local-description){.pf-ref} a variety morphism is a compatible system of morphisms of affine open subvarieties, and a scheme morphism has the same local description, so a scheme morphism $F$ restricts on each affine chart to a morphism of affine schemes over $k$; by step [](#haiman-affine-case){.pf-ref} each of those comes from a morphism of affine varieties, and compatibility on overlaps, which are again covered by affine opens, glues the pieces.

The steps that follow carry out that gluing for the present statement, since the closed points of $t(V)$ are the points of $V$ with residue field $k$: steps [](#f-sends-closed-points-set-map){.pf-ref} and [](#f-continuous){.pf-ref} extract the underlying map $f$, step [](#affine-neighborhoods-exist){.pf-ref} produces affine neighbourhoods with $f(V_0)\subseteq W_0$, step [](#f-restriction-induced-by-ring-hom){.pf-ref} is the affine-case bijection of step [](#haiman-affine-case){.pf-ref} and step [](#f0-agrees-with-f-on-v0){.pf-ref} reads it off on closed points, step [](#f-is-morphism-of-varieties){.pf-ref} glues the pieces to a morphism of varieties, and step [](#tf-equals-f-original){.pf-ref} checks that the glued morphism induces $F$ itself.
:::

:::

::: {.pf-step #map-injective}
The same natural map is injective.

::: pf-proof
If
$$
t(f)=t(g),
$$
then the two associated scheme morphisms have the same map on closed points.  Under the identification of the closed points of $t(V)$ and $t(W)$ with the ordinary points of $V$ and $W$, this means
$$
f(P)=g(P)
$$
for every $P\in V$.

A morphism of varieties is in particular a function on the underlying point sets, so equality pointwise gives
$$
f=g.
$$
:::

:::

::: {.pf-step #t-fully-faithful}
Hence the functor
$$
t:\mathsf{Var}_k\longrightarrow\Sch_k
$$
is fully faithful:
$$
\boxed{
\Hom_{\mathsf{Var}_k}(V,W)
\xrightarrow{\sim}
\Hom_{\Sch_k}(t(V),t(W)).
}
$$

::: pf-proof
Surjectivity is step [](#map-surjective){.pf-ref} and injectivity is step [](#map-injective){.pf-ref}.
:::

:::

::: pf-qed
Steps [](#point-corresponds-to-subvariety){.pf-ref}, [](#closed-point-residue-field-k){.pf-ref}, [](#residue-field-k-implies-closed){.pf-ref} and [](#closed-iff-residue-field-k){.pf-ref} prove part (a), step [](#morphism-preserves-residue-field-k){.pf-ref} proves part (b), and steps [](#haiman-local-description){.pf-ref}, [](#haiman-affine-case){.pf-ref}, [](#f-sends-closed-points-set-map){.pf-ref}, [](#f-continuous){.pf-ref}, [](#affine-neighborhoods-exist){.pf-ref}, [](#f-restriction-induced-by-ring-hom){.pf-ref}, [](#f0-agrees-with-f-on-v0){.pf-ref}, [](#f-is-morphism-of-varieties){.pf-ref}, [](#tf-equals-f-original){.pf-ref}, [](#map-surjective){.pf-ref}, [](#map-injective){.pf-ref} and [](#t-fully-faithful){.pf-ref} prove part (c).
:::

:::

:::

::: {.remark title="Published solution"}
Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Chapter II §2, Exercise 2.15, PDF pp. 16--17, text version `tmp/sources/hartshorne-solutions-kim.md`, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`: (a) a closed point of $t(V)$ is a maximal ideal and the Nullstellensatz gives residue field $k$; (b) the residue-field maps form the tower $k\to k(f(P))\to k(P)=k$; (c) $f$ sends closed points to closed points, and then: "This is indeed a map of varieties, if we look at the corresponding affine charts. Now we want to show that $f$ is the same as the map induced from $f_c$. Basically we need to show that if two maps of schemes $\Spec A\to\Spec B$ agree on closed points, then they induce the same maps at the level of schemes ... This follows from the fact that there is a functorial embedding $A\hookrightarrow\prod_{\operatorname{maxSpec}A}k$".
The proof above is the same route with the chart step carried out rather than asserted: for each $P$ it produces affine neighbourhoods with $f(V_0)\subseteq W_0$, shows that $F$ is there the affine-variety morphism of the $k$-algebra map $B\to A$, obtains continuity and regularity, and concludes $t(f)=F$; in (a) it also proves the converse direction through $\dim Z=\trdeg_k k(Z)$. Part (c), the surjectivity, has no complete published solution in the retained sets; the sets searched are recorded in `COMPLAINTS.md`.

There is one outside them, and part (c) of the proof above is now that source's argument rather than the card's own. Mark Haiman, *Varieties as Schemes* (Math 256, Berkeley, March 2019), text version `tmp/sources/haiman-varieties-as-schemes.md`, proves the full equivalence rather than the exercise. Theorem 8.8, PDF p. 18, states it: "Let $k$ be an algebraically closed field. The constructions in §8.2 and §8.3 give a functorial equivalence between the categories of classical varieties and reduced affine schemes over $k$. Specifically, morphisms $f:X\to X'$ between classical varieties are in functorial one-to-one correspondence with $k$-morphisms $g:Y\to Y'$ between the schemes associated to them by the soberization construction in §8.2." Its proof is 8.10, PDF pp. 18--19, and it has two steps, both reproduced as steps of the solution above: that on a classical variety the open subsets isomorphic to affine varieties form a base of the topology, so that a morphism is a compatible system of morphisms of affine open subvarieties, schemes having the same local description; and that for affine varieties the morphisms correspond bijectively to $k$-algebra homomorphisms of coordinate rings, which is the same statement for affine schemes. Step [](#haiman-local-description){.pf-ref} is the first and step [](#haiman-affine-case){.pf-ref} the second; the identity $\OO(X)=\OO_X(X)$ they use is Haiman's 8.9 on PDF p. 18. Haiman's correspondence is between $V$ and $\Spec$ of its coordinate ring, which is the scheme $t(V)$ built in Hartshorne's II.2.6, so the bijection of part (c) is his. What the card adds is the verification of his two steps for this statement, and parts (a) and (b), on which the identification of the closed points of $t(V)$ with the points of $V$ rests; the notes carry no printed folio, so PDF pages are cited. Agree with the source throughout: (c) is its argument, transcribed.
:::
