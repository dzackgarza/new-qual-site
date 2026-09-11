---
schema: qual/card@1
id: P-AGH212DUPLE
kind: problem
title: The $d$-uple embedding of $\PP^n$ in $\PP^N$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Veronese Embedding
  - Homogeneous Ideals
  - Twisted Cubic
relations: []
review: draft
---

::: problem
For given $n, d > 0$, let $M_0, M_1, \ldots, M_N$ be all the monomials of degree $d$ in the $n+1$ variables $x_0,\ldots,x_n$, where $N = \binom{n+d}{n} - 1$.
Define $\rho_d : \PP^n \to \PP^N$ by
\[
\rho_d\qty{ \tv{a_0 : \cdots : a_n} } = \tv{ M_0(a) : \cdots : M_N(a) } .
\]
This is the **$d$-uple embedding** of $\PP^n$ in $\PP^N$.
For example, when $n = 1$ and $d = 2$ we have $N = 2$, and the image of the $2$-uple embedding of $\PP^1$ in $\PP^2$ is a conic.

1. Let $\theta: k[y_0,\ldots,y_N] \to k[x_0,\ldots,x_n]$ be the homomorphism sending $y_i \mapsto M_i$, and let $\mfa = \ker \theta$.
   Show that $\mfa$ is a homogeneous prime ideal, so that $Z(\mfa)$ is a projective variety in $\PP^N$.
2. Show that the image of $\rho_d$ is exactly $Z(\mfa)$.
3. Show that $\rho_d$ is a homeomorphism of $\PP^n$ onto the projective variety $Z(\mfa)$.
4. Show that the twisted cubic curve in $\PP^3$ is the $3$-uple embedding of $\PP^1$ in $\PP^3$, for a suitable choice of coordinates.
:::
