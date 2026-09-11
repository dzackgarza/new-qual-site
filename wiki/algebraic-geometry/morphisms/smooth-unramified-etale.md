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
