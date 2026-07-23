---
sort: 025
title: "Exercises: Contour integration" 
---

# Exercises: Contour Integration

## Residues


[[E-6FC66]]
## Rational Functions 

### Superlinear Decay

[[E-K4656]]
[[E-ICRWN]]
[[E-36ATB]]
[[E-BX3TQ]]
[[E-MV3XK]]
[[E-C2HNL]]
### Linear or sublinear decay

[[E-NL5TU]]
### No clear decay

[[E-ZD6JU]]
[[E-SIRWS]]
## Singularities along $\RR$, Principal Values

[[E-KFKVU]]
[[E-6GHUM]]
## Rational functions of $\cos, \sin$

[[E-HR3G3]]
[[E-3WV5U]]
[[E-NDI7K]]
## Branch Cuts

### Logarithms

[[E-7HCAG]]
[[E-VGRBA]]
[[E-J6PJP]]
[[E-5AYG6]]
### Power Functions

[[E-S6EOX]]
[[E-TGUAH]]
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

[[E-MLTM2]]
[[E-JVANT]]
[[E-3FGMU]]
[[E-UFFIL]]
[[E-XP2DK]]
