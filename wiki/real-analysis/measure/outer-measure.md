---
title: Outer measure and the construction
order: 10
topics:
- Measure Theory
- Continuity of Measure
---

# Outer measure and the construction

A measure is countably additive on a $\sigma$-algebra.
From that single axiom come the continuity rules used constantly in proofs: increasing unions pass to limits of measures, and decreasing intersections do too when the first set has finite measure.
Disjointization is the standard way to reduce a general union to the countably additive case.

[[D-QYLPH]]

[[PR-A4J4G]]

[[T-7LQ7X]]

[[FS-ACP4W]]

[[PR-KKJ6O]]

[[FT-OMADI]]

## Outer measure

Outer measure is defined on *every* subset and is countably subadditive rather than countably additive; it also satisfies $\mu^*(\varnothing)=0$ and monotonicity.
Carathéodory's criterion identifies the subsets across which outer measure splits additively; those sets form a $\sigma$-algebra, and restriction to that $\sigma$-algebra is an honest measure.
Thus measurability is not an extra decoration on the construction—it is exactly the condition that recovers additivity.

[[PR-LF7SW]]

[[D-UYOGE]]

[[FT-O4DRR]] [[FF-LA4J2]]

## Measures on $\RR^d$

Lebesgue measure is characterized by the Euclidean features one actually uses: translation invariance, the expected scaling under dilations, and the usual volume on rectangles.
Not every subset is measurable, so completion and regular approximation by open/closed sets matter whenever a proof modifies a set by a null set.
Limsup/liminf sets then turn repeated membership into a measurable event, and Borel--Cantelli converts summability of their measures into an almost-everywhere statement.

[[PR-I4YON]]

[[PR-DXWWU]]

[[FR-7YFAU]]

[[T-KZNWM]]

[[PR-NULVE]]

[[T-YMPTF]]

[[T-OTR5M]]

[[FF-GNU7E]]

[[FR-CSUMF]]

[[PR-I44DD]]

[[PR-552IH]]

[[D-BXAUS]]

[[PR-UHWNM]]

$\sigma$-finiteness is the hypothesis that lets global product/integration theorems be assembled from finite-measure pieces.
Regularity lets measurable sets be approximated from outside by open sets and, in the finite-measure Euclidean setting, from inside by compact sets; this is the bridge between measure-theoretic and topological arguments.

::: {.remark title="Carathéodory is the whole construction"}
Outer measure is defined on every set and is countably subadditive rather than countably additive; the Carathéodory criterion picks out the sets on which it is additive, and those are the measurable ones.
After Carathéodory measurability is established, the restriction of outer measure to the measurable sets is a measure, and later arguments work inside that $\sigma$-algebra.
:::

[[PR-TGQFG]]
