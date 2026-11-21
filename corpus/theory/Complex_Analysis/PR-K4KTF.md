---
schema: qual/card@1
id: PR-K4KTF
kind: proposition
title: Meromorphic continuation of $\zeta$
slogan: 'Theta inversion continues $\zeta$ meromorphically to $\CC$, leaving one simple pole at $1$ and relating $s$ to $1-s$.'
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Zeta
  - Meromorphic Functions
relations: []
review: draft
---

::: {.proposition}
The [[D-HJYH3|Riemann zeta function]] $\zeta(s)=\sum_{n\ge1}n^{-s}$, defined for $\Re(s)>1$, extends to a [[D-7DFVJ|meromorphic]] function on $\CC$ whose only singularity is a simple [[D-AUD6K|pole]] at $s=1$.
The extension satisfies the functional equation
$$
\zeta(s) = \pi^{s-1/2}\,\frac{\Gamma\qty{\frac{1-s}{2}}}{\Gamma\qty{\frac{s}{2}}}\,\zeta(1-s).
$$

The continuation is [@SS03, ch. 6, Theorem 2.4]. The functional equation is the symmetry $\xi(s)=\xi(1-s)$ of [@SS03, ch. 6, Theorem 2.3] read through $\xi(s)=\pi^{-s/2}\Gamma\qty{s/2}\zeta(s)$, which is the $\xi$ of that section: substituting $\xi(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$ and its value at $1-s$ and solving for $\zeta(s)$ gives the display above.
:::
