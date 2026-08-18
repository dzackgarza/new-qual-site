---
order: 30
sort: 025
title: "Exercises: Contour integration" 
---

# Exercises: Contour Integration

## Residues

[[E-QF7KI]]

## Rational Functions 

### Superlinear Decay

[[E-IZKCV]]
[[E-UDYDX]]
[[E-AKNDW]]
[[E-AKF2O]]
[[E-JZNWV]]
[[E-SPIVX]]

### Linear or sublinear decay

[[E-AXBZQ]]

### No clear decay

[[E-YYRZX]]
[[E-AIQEU]]

## Singularities along $\RR$, Principal Values

[[E-ZGZYQ]]
[[E-DUK6M]]

## Rational functions of $\cos, \sin$

[[E-BEIHP]]
[[E-Z4JCZ]]
[[E-JKROF]]

## Branch Cuts

### Logarithms

[[E-FJJA6]]
[[E-EOMTI]]
[[E-KC6DS]]
[[E-HHSCS]]

### Power Functions

[[E-YAMX6]]
[[E-2HIKG]]

### Square Roots / Slits

:::{.concept}
\envlist

- The residue at $\infty$: if $\Gamma$ is a positively oriented curve (counterclockwise about $z=0$), then
\[
\Res_{z=\infty}f(z) = -{1\over 2\pi i}\oint_\Gamma f(z) \dz,\quad \Res_{z=\infty}f(z) = \Res_{z=0} -{1\over z^2}f\qty{1\over z}
.\]
- Slits: for $f(z) = \sqrt{(z-z_1)(z-z_2)\cdots (z-z_n)}$, one needs to introduce slits that disallow winding around an odd number of the branch points $z_k$.
  - Be sure to check to see if $z=\infty$ is a branch point!
- A standard argument: for $f(z) = \sqrt{z}$, take a path $\gamma(t) = e^{2\pi i t}$ for $t\in [0, 1]$.
  Then $f(\gamma(0)) = f(z)$ and $f(\gamma(1)) = \sqrt{e^{2\pi i} z} = e^{i\pi}\sqrt{z} = -\sqrt{z}$, so the monodromy/phase factor introduced by square roots is $-1$.

:::

[[E-L3MG4]]
[[E-EBRU5]]
[[E-GPCW2]]
[[E-XYEP4]]
[[E-KZV2Z]]
