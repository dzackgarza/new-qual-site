---
title: Finite and flat
order: 2
topics:
- Finite Morphisms
- Flatness
- Going Up
- Going Down
- Integral Extensions
---

# Finite and flat

A nonconstant morphism of smooth projective curves is flat, since the target is integral and regular of dimension one and every irreducible component of the reduced source dominates it [@Har77, Proposition III.9.7].

## Going up and going down

[[PR-RJ3P7]]

Going up is what makes a finite morphism behave like a branched cover: for $B$ integral over $A$ the map $\Spec B \to \Spec A$ is closed and surjective, every prime of $A$ is the contraction of a prime of $B$, and every chain of primes of $A$ lifts to a chain of $B$ above it [@AM18, Theorems 5.10 and 5.11].

Going down is the same statement with the chains reversed: a chain of primes of $A$ extends downwards once a prime of $B$ above its top is fixed, when $A \subseteq B$ are domains with $A$ integrally closed and $B$ integral over $A$ [@AM18, Theorem 5.16], and for every flat ring map [Stacks, Lemma 10.39.19, tag 00HS].

In geometric terms, going down says that every generization of a point of the image of $\Spec B \to \Spec A$ lifts to a generization of any chosen point above it.

## Flatness and fibres

[[D-MORFLAT]]

For a finite flat morphism $f\colon X\to Y$ with $Y$ noetherian and connected, $f_*\OO_X$ is locally free of constant rank $d$ and every fibre has length $d$ ([[D-MORFLAT]]).

## Where flatness fails

[[FE-MORNOTFLAT]]

For a projective morphism to an integral noetherian scheme, constancy of the Hilbert polynomial of the fibres implies flatness ([[T-COHFLATCHI]]).

## Flatness in examples

[[FE-SCHFFLAT]]

[[PR-MIRACLEFLAT]]

## Criteria for flatness

[[T-FLATCRIT]]
