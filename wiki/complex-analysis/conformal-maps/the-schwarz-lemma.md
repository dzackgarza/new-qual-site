---
title: The Schwarz lemma
order: 20
topics:
- Schwarz Lemma
- Fixed Points
- Hyperbolic Metric
---

# The Schwarz lemma

A holomorphic self-map of the disc that fixes the origin cannot move any point further from the origin, and its derivative at the origin cannot exceed $1$ in modulus. The equality case forces a rotation, and that is what turns the two bounds into the classification of the automorphisms of the disc and into the statement that a holomorphic self-map contracts the hyperbolic distance.

[[T-DAETF]]

The proof in [@SS03, ch. 8, Lemma 2.1] divides by $z$ and applies the [[T-BYNL5|maximum modulus principle]] to the result, which is holomorphic at $0$ because $f(0)=0$.

## The equality case

The two numbered clauses are bounds; the unnumbered closing sentence is the part used in arguments, because equality at one interior point other than the origin, or equality in the derivative at it, identifies $f$ as a rotation rather than merely bounding it. Every identification of an automorphism on this page goes through that sentence.

::: {.example title="The hypothesis $f(0)=0$ cannot be dropped"}
For $a\in\DD\sm\theset{0}$ the Blaschke factor $\psi_a$ maps $\DD$ to $\DD$ and $\psi_a(0) = a$, so $\abs{\psi_a(0)} = \abs a>0 = \abs 0$: without the normalization at $0$ a holomorphic self-map of the disc need not contract the distance to the origin.
Composing with $\psi_a$ restores the hypothesis.
:::

## Automorphisms of the disc

[[T-W26VL]]

The classification of $\Aut_\CC(\DD)$ is what the lemma is for, and [@SS03, ch. 8, Theorem 2.2] derives it from the equality case, applied to $f\circ\psi_\alpha$ where $\alpha$ is the point carried to $0$, and then to the inverse of that map. The [[D-MFPYG|Blaschke factors]] are the [[D-TM4TE|biholomorphisms]] of the disc that move a prescribed point to the origin, and a map fixing the origin is a rotation by the equality case, so the automorphisms are exactly the Blaschke factors followed by rotations.

## The Schwarz--Pick lemma and the hyperbolic metric

[[T-SCHPK]]

The derivative form is the lemma applied to $\psi_{f(z)}\circ f\circ\psi_z$, which reintroduces the normalization at the origin at each point, and the equivalent form on the card is contractivity of the [[D-2HXLN|hyperbolic distance]] [@SS03, ch. 8, Problem 3(a)], the derivative form being [@SS03, ch. 8, Exercise 13(b)] and the pseudo-hyperbolic form part (a) of that exercise.

The equality cases of the two forms are not the same assertion, and the difference is the pair $z=w$. Equality in the derivative form at a point, and equality of either distance at a pair of distinct points, each force $f$ to be an [[D-MFPYG|automorphism]] of the disc; at a single point both distances are $0$ on both sides, so the distance form holds there for every self-map, as it does for $z^2$, which is not an automorphism, and nothing about $f'$ follows from it. The [[T-DAETF|Schwarz lemma]]'s own equality clause is the case at the origin, where what equality forces is a rotation rather than an arbitrary automorphism.

The isometry group of that distance and the geometry it induces are on [[complex-analysis/conformal-maps/the-hyperbolic-metric|The hyperbolic metric]], and the automorphisms of the disc are treated as Möbius transformations on [[complex-analysis/conformal-maps/mobius-transformations|Möbius transformations]].

## Problems

### The equality case and fixed points

Equality in the lemma, or the normalization that produces it, identifies the map rather than bounding it: a self-map fixing the origin, a map with two fixed points, or a map whose second derivative attains its bound is forced into a prescribed form, and the normalized bound also counts the solutions of an equation.

[[E-QFOOL]] [[E-VYIZJ]] [[P-UMNCP-S11-04]] [[E-XKMVX]]

### Bounds for a normalized map

Each of these fixes the value, or the derivative, of a self-map at one point and asks what follows elsewhere: either a bound, or the impossibility of such a map. The route in every case is the lemma applied after composing with the automorphism that moves that point to the origin.

[[E-SS8.EX-11]] [[E-5I2NN]] [[P-BERK91S-07]] [[P-JHUSP02CAD]] [[E-JSPEB]] [[P-UMNCP-F11-04]] [[P-8CA20]]

### The lemma used elsewhere

The lemma is also a tool inside other arguments: it gives Liouville's theorem back, identifies a Blaschke factor as an involution, and transports to the upper half-plane, to the pseudo-hyperbolic distance and to an iteration scheme.

[[E-XQX6X]] [[E-ZSOC4]] [[E-SS8.EX-10]] [[E-SS8.EX-13]] [[P-UMNCP-S10-08]]
