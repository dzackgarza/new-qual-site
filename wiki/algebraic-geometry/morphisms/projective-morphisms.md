---
title: Projective morphisms
order: 7
topics:
- Projective Morphisms
- Relative Proj
- Ample Line Bundles
---

# Projective morphisms

A morphism is projective when its source is a closed subscheme of $\PP^n_Y$ over its target, and the cohomological theorems of the next chapters are stated for that class: finiteness of cohomology, Serre vanishing, the Euler characteristic and the Hilbert polynomial all use a morphism that factors through some $\PP^n_Y$ [@Har77, Sections III.5 and III.8].

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

A projective morphism of noetherian schemes is proper [@Har77, Theorem II.4.9].
The converse fails: a nonsingular complete threefold over $\CC$ that admits no embedding in any projective space exists [@Har77, Appendix B, Example 3.4.1].

## Ample and very ample sheaves

[[D-MODAMPLE]]

[[T-DIVMAPPN]]

The certificate is a sheaf rather than a map: $\mcl$ is very ample over $Y$ when some $\iota\colon X\to\PP^n_Y$ has $\iota^*\OO(1)\cong\mcl$, so a morphism is projective exactly when such an $\mcl$ exists.
In practice the map is written down from sections: a generating set $s_0,\ldots,s_n\in H^0(X,\mcl)$ gives $\varphi\colon X\to\PP^n_Y$, and $\varphi$ is a closed immersion exactly when the sections separate points and tangent directions.
A very ample sheaf is ample, and on a scheme of finite type over a noetherian ring $\mcl$ is ample exactly when some power of $\mcl$ is very ample [@Har77, Chapter II, §7].
Ampleness is preserved by restriction to a closed subscheme and by pullback along a finite surjective morphism: for $f\colon X\to Y$ finite and surjective, $\mcl$ is ample on $Y$ if and only if $f^*\mcl$ is ample on $X$ [@Har77, Exercise III.5.7].
It is not preserved by pullback along an arbitrary morphism: for $\pi\colon\widetilde X\to X$ the blowup of a point of a surface, $\pi^*\mcl$ restricts to the trivial sheaf on the exceptional curve $E$, since $\pi$ maps $E$ to a point, so $\pi^*\mcl\cdot E=0$ and an ample divisor has positive intersection with every irreducible curve [@Har77, Theorem V.1.10].

## Consequences used later

A projective morphism is proper and of finite type, so its higher direct images are coherent, the theorem on formal functions applies, and the Hilbert polynomial of a coherent sheaf is defined fibrewise [@Har77, Sections III.5 and III.8].
These are the hypotheses of [[algebraic-geometry/cohomology/projective-schemes|the cohomology of projective schemes]].
A blowup is the relative $\Proj$ of a Rees algebra, hence projective ([[algebraic-geometry/varieties/blowups|blowups]]).
