---
title: Smooth, unramified, and étale
order: 4
topics:
- Smooth Morphisms
- Étale Morphisms
- Jacobian Criterion
---

# Smooth, unramified, and étale

Three conditions on a morphism that all say "the fibres are as nice as the base allows", differing in the relative dimension they permit.
The organising statement is that étale is smooth of relative dimension $0$, and that unramified is the half of étale that flatness is missing from.

## Unramified and étale

[[D-MORUNR]]

[[D-MORETALE]]

The differentials give the working criterion in both cases: unramified is $\Omega_{X/Y} = 0$, and étale is that together with flatness.
For a map of curves the condition is that every ramification index is $1$, which is the same $e_p$ that Riemann--Hurwitz counts, so this is not a separate theory from [[algebraic-geometry/curves-and-surfaces/index|curves]].

## Ramification, measured

[[D-IV2RAM]]

Ramified is the negation of unramified, and it is measured rather than merely observed: $e_p$ counts how far the pulled-back uniformizer is from being one, and the length of $(\Omega_{X/Y})_p$ turns that count into the divisor Riemann--Hurwitz adds up.
The two agree only when $e_p$ is invertible in $k$, and the follow-up is always which way the discrepancy runs.

[[PR-IV2DEGREVEN]]

The parity statement costs one line and is the cheapest check available on a branching count, which is why it is asked for immediately after a genus computation.

## Étale covers

[[D-IV2ETCOV]]

Finite étale is the algebraic covering space, and the projective line has only the trivial ones, by the same Riemann--Hurwitz with the ramification term set to zero.
The affine line is where this fails in characteristic $p$, and the two answers side by side are the test of whether the étale fundamental group has been understood or recited.

## Smoothness

[[D-MORSM]]

[[T-MORSMREG]]

Smooth is a property of a morphism, regular is a property of a local ring, and they agree over a perfect field and not otherwise.
The failure is always inseparability, and the single example $\Spec \FF_p(t)[x]/(x^p - t)$ answers every version of the question.

[[PR-MORJAC]]

The jacobian criterion is the only computational tool here, and the thing that gets dropped in the answer is that one must also impose the equations of $X$: a point where the jacobian drops rank is singular only if it lies on $X$.

## Where smoothness fails

[[FE-MORFROB]]

[[T-MORGEN]]

Frobenius is the example that defeats every cheap criterion at once, and generic smoothness is the theorem it obstructs, which is why characteristic zero appears in the statement.
Generic *flatness* needs no such hypothesis, and keeping the two apart is the usual follow-up.
