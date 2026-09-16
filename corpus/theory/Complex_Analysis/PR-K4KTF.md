---
schema: qual/card@1
id: PR-K4KTF
kind: proposition
title: Meromorphic continuation of $\zeta$
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
:::

::: {.proof}
For $t>0$ let $\theta(t)\coloneqq\sum_{n\in\ZZ}e^{-\pi n^2t}$.
By Poisson summation $\theta(1/t)=t^{1/2}\theta(t)$, and $\abs{\theta(t)-1}\le ce^{-\pi t}$ for $t\ge1$.
For $\Re(s)>1$ put
$$
\xi(s)\coloneqq\frac12\int_0^\infty r^{s/2-1}\qty{\theta(r)-1}\,dr.
$$
Integrating term by term, $\int_0^\infty r^{s/2-1}e^{-\pi n^2r}\,dr=\pi^{-s/2}n^{-s}\Gamma(s/2)$, so $\xi(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$ for $\Re(s)>1$.
Splitting the integral at $r=1$ and applying $\theta(1/r)=r^{1/2}\theta(r)$ on $(0,1)$ gives
$$
\xi(s)=\frac{1}{s-1}-\frac1s+\frac12\int_1^\infty\qty{r^{s/2-1}+r^{-s/2-1/2}}\qty{\theta(r)-1}\,dr,
$$
where the integral is entire in $s$ by the exponential decay of $\theta-1$.
So $\xi$ extends meromorphically to $\CC$ with simple poles only at $0$ and $1$, and the right side is unchanged under $s\mapsto1-s$, so $\xi(s)=\xi(1-s)$.
Since $1/\Gamma$ is entire with a simple zero at $s=0$, $\zeta(s)=\pi^{s/2}\xi(s)/\Gamma(s/2)$ is meromorphic on $\CC$; the pole of $\xi$ at $0$ cancels against the zero of $1/\Gamma(s/2)$, leaving only the simple pole at $s=1$.
Writing $\xi(s)=\xi(1-s)$ in terms of $\zeta$ gives the functional equation.
:::
