---
title: Crepant resolutions
order: 12
topics:
- Resolution of Singularities
- Du Val Singularities
- Discrepancy
---

# Crepant resolutions

A resolution of singularities replaces a singular variety by a smooth one, and it changes the canonical class unless the change is the one this chapter is about: the question is when a resolution changes it by nothing.
A morphism with $K_Y=f^*K_X$ is crepant, and on a surface the singularities that admit such a resolution are exactly the du Val ones, whose resolution is crepant with exceptional curves of self-intersection $-2$.
That is the statement that names the ADE classification in geometry, and it is the reason the crepant condition, not smoothness alone, is what a minimal model wants.

## Resolutions and discrepancy

[[D-VARCREPANT]]

The discrepancy is the measure: writing $K_Y=f^*K_X+\sum a_iE_i$ over the exceptional prime divisors, the coefficients $a_i$ are the discrepancies, they do not depend on the choice of $K_X$ inside its linear equivalence class, and the classes of singularities are defined by bounding them.
So crepant means all discrepancies zero, terminal means all positive, canonical means all nonnegative, and the three are nested conditions on a singularity rather than on a resolution.
A blowup of a smooth point of a surface has discrepancy $1$ along its exceptional curve, which is why it is not crepant, and $\CC^4/\{\pm1\}$ has no crepant resolution because every exceptional divisor of every resolution has positive discrepancy.

## Log resolutions and the existence question

[[D-VARLOGRES]]

Existence of a resolution is Hironaka's theorem in characteristic zero, and it is stated in the log form because that is the form in which it is proved: a resolution that is an isomorphism away from a divisor, with the divisor's normal crossings preserved.
Crepant resolutions are much rarer than resolutions and do not exist in general; which singularities admit one is a question with a dimensional answer — in dimension two it is the du Val list below, in dimension three it is the minimal model programme's, and terminal singularities admit none.

## Du Val singularities

[[D-SRFADE]]

The ADE singularities are the same list seen four ways: as the hypersurface equations in the table, as the quotients $\CC^2/G$ for $G\subseteq\SL_2(\CC)$, as the rational double points, and as the canonical surface singularities.
Each identification is a theorem, and the one this page needs is the third row of the theorem above: the exceptional locus of the minimal resolution is a configuration of smooth rational curves of self-intersection $-2$ whose dual graph is the Dynkin diagram of the same name.

[[FE-TORMINRES]]

The following computation shows the whole mechanism in one line, and it is worth doing by hand once: for an exceptional curve $E$ with $E^2=-2$, adjunction gives
$$
2g(E)-2=E\cdot(E+K_Y)=-2+E\cdot K_Y ,
$$
so $E\cdot K_Y=0$ when $E\cong\PP^1$, and the class $K_Y-f^*K_X$ is supported on the exceptional curves and pairs to zero with each of them.
The intersection form on a resolution of a du Val singularity is negative definite, so a class supported there that pairs to zero with every curve is zero — that is the proof that the minimal resolution is crepant.

## Exceptional curves and what a resolution may not do

[[PR-VAREM1]]

[[T-SRFCAST]]

A curve of self-intersection $-1$ is contractible and a curve of self-intersection $-2$ is not, and the two facts are the same computation read in both directions: Castelnuovo's criterion says that a $(-1)$-curve on a smooth surface can be blown down, and Riemann–Roch plus adjunction say that a $(-2)$-curve cannot.
So the minimal resolution of a surface is the one with no $(-1)$-curves left to contract; for a du Val singularity that resolution is also the crepant one, and its exceptional curves are precisely the $(-2)$'s, which is why the two conditions coincide in this dimension and separate in the next.

## Blowups and the canonical class

[[FE-SRFBLOW]]

A blowup at a smooth point changes $K$ by $+E$ and changes the intersection form by subtracting one from the self-intersection of every curve through the point, which is the calculation behind both Castelnuovo and the surface classification.
Iterating it produces every birational map between smooth surfaces ([[T-SRFZMT]]), so the canonical class of a surface is determined up to the classes of the curves blown up — which is exactly the statement that discrepancy is well defined.
The crepant condition is the case where nothing accumulates along the exceptional locus, and it is the condition under which two smooth models of the same singularity theory have the same canonical class.

## Crepant resolutions beyond surfaces

In dimension three crepant resolutions exist for Gorenstein canonical singularities but are not unique in general, and the flop connects them; the McKay correspondence — the observation that the cohomology of a crepant resolution reproduces the representation theory of the finite group in the du Val case — is the reason they are studied at all.
In the toric setting the existence question becomes a fan computation: a crepant resolution is a subdivision in which every new ray lies at lattice distance one from the cone it subdivides, and for a toric surface that computation produces the chains of $(-2)$-curves of the du Val list, whose lengths are read off the continued fraction of the cone ([[PR-FULKSQ]]).
