---
title: Projective morphisms
order: 7
topics:
- Projective Morphisms
- Relative Proj
- Ample Line Bundles
---

# Projective morphisms

A morphism is projective when its source embeds in a projective space over its target, and this is the class on which the cohomological theorems of the next chapters are proved: finiteness of cohomology, Serre vanishing, and the Euler characteristic and Hilbert polynomial all require a morphism that factors through $\PP^n_Y$.
The page builds that class properly: $\Proj$ of a sheaf of graded $\OO_Y$-algebras is the relative construction that produces the embeddings, projectivity implies properness, and an invertible sheaf that is very ample is the certificate that a given morphism is projective.

## Proj of a graded ring

[[D-DEFGRRNG]]

[[D-SCHPROJ]]

[[T-SCHPRJC]]

The definition is forced once one asks which homogeneous primes to keep: $\Proj S$ is the set of homogeneous primes not containing the irrelevant ideal $S_+$, with the topology and structure sheaf making the charts $D_+(f)=\Spec S_{(f)}$ for homogeneous $f$ of positive degree.
The hypothesis that $S$ is generated in degree one is what makes the charts cover in the expected way; without it $\Proj S$ still exists but is not the projective variety attached to the grading.

## Relative Proj

[[D-SCHRELSPECPROJ]]

Replacing the graded ring by a sheaf of graded algebras gives the relative construction, and it is the one used: for a quasicoherent sheaf $\mce$ of $\OO_Y$-modules the symmetric algebra $\operatorname{Sym}^\bullet\mce$ has relative Proj the projective bundle $\PP(\mce)\to Y$, whose fibre over a point $y$ is $\PP(\mce\tensor\kappa(y))$.
Everything said about projectivity over a field therefore applies fibrewise over $Y$, with ampleness the condition that fixes an embedding at once and not merely on each fibre.

## Projective morphisms are proper

[[D-MORPROJ]]

Properness of a projective morphism is a composition of three facts: a closed immersion is proper, properness is stable under composition, and $\PP^N_\ZZ\to\Spec\ZZ$ is universally closed by elimination theory — given a closed subset of $\PP^N_Y$ defined by homogeneous equations, the locus of $y$ where it meets the fibre is closed because it is cut out by the coefficients of the resultant of those equations.
The converse fails, and the gap is worth knowing: a proper morphism need not be projective, and the standard counterexample is a smooth complete threefold that admits no embedding in any projective space.

## Ample and very ample sheaves

[[D-MODAMPLE]]

[[T-DIVMAPPN]]

The certificate is a sheaf rather than a map: $\mcl$ is very ample over $Y$ when some $\iota\colon X\to\PP^n_Y$ has $\iota^*\OO(1)\cong\mcl$, so a morphism is projective exactly when such an $\mcl$ exists.
In practice the map is written down from sections: a generating set $s_0,\ldots,s_n\in H^0(X,\mcl)$ gives $\varphi\colon X\to\PP^n_Y$, and $\varphi$ is a closed immersion exactly when the sections separate points and tangent directions.
Ampleness is the weaker and better-behaved condition, stable under pullback and satisfied by $\OO(1)$ on projective space; on a finite type scheme over a noetherian ring, $\mcl$ is ample exactly when some power is very ample [@Har77, Chapter II, §7].

## Consequences used later

A projective morphism is proper and of finite type, so its higher direct images are coherent, the theorem on formal functions applies, and the Hilbert polynomial of a coherent sheaf is defined fibrewise [@Har77, Sections III.5 and III.8].
That is the list of hypotheses behind [[algebraic-geometry/cohomology/projective-schemes|the cohomology of projective schemes]], and it is why the cohomology chapter is stated for projective rather than for complete morphisms.
An example of the construction in the wild is the blowup, which is the relative $\Proj$ of a Rees algebra and is therefore projective ([[algebraic-geometry/varieties/blowups|blowups]]).
