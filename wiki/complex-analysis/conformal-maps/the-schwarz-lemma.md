---
title: The Schwarz lemma
order: 20
topics:
- Schwarz Lemma
- Fixed Points
- Hyperbolic Metric
---

# The Schwarz lemma

[[T-DAETF]]

[[FF-5H4UZ]]

## Consequences

::: {.fact title="Invariant form"}
For holomorphic $f\colon\DD\to\DD$ and $z\in\DD$,
$$
\frac{\abs{f'(z)}}{1-\abs{f(z)}^2}\leq\frac{1}{1-\abs z^2},
$$
equivalently $f$ does not increase [[D-2HXLN|hyperbolic distance]].
Equality for one $z$ forces $f$ to be an automorphism of $\DD$, and then $f$ is a [[D-MFPYG|Blaschke factor]] followed by a rotation ([[T-W26VL]]).

This is [@SS03, ch. 8, Exercise 13(b)], and the pseudo-hyperbolic form $\rho(f(z),f(w))\le\rho(z,w)$ is part (a) of the same exercise.
:::

::: {.example title="The hypothesis $f(0)=0$ cannot be dropped"}
For $a\in\DD\sm\theset{0}$ the Blaschke factor $\psi_a$ maps $\DD$ to $\DD$ and $\psi_a(0) = a$, so $\abs{\psi_a(0)} = \abs a>0 = \abs 0$: without the normalization at $0$ a holomorphic self-map of the disc need not contract the distance to the origin.
Composing with $\psi_a$ restores the hypothesis, which is how the invariant form is proved.
:::

## Exercises

[[P-ZRVTI]] [[E-SS8.EX-11]] [[E-ZSOC4]] [[E-SS8.EX-13]] [[E-QFOOL]] [[E-SS8.EX-10]] [[P-BERK91S-07]] [[E-XQX6X]] [[P-UMNCP-S11-04]] [[P-UMNCP-S10-08]] [[E-VYIZJ]] [[E-5I2NN]] [[P-8CA20]] [[E-JSPEB]] [[E-XKMVX]] [[P-UMNCP-F11-04]] [[P-JHUSP02CAD]]
