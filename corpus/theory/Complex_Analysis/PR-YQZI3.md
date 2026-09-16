---
schema: qual/card@1
id: PR-YQZI3
kind: proposition
title: Meromorphic continuation of $\Gamma$
classification:
  areas:
  - complex-analysis
  topics:
  - Gamma Function
  - Meromorphic Functions
relations: []
review: draft
---

::: {.proposition}
The [[D-Q3MYK|Gamma function]], defined by $\Gamma(s)=\int_0^\infty t^{s-1}e^{-t}\dt$ for $\Re s>0$, extends to a [[D-7DFVJ|meromorphic]] function on $\CC$ whose only singularities are simple [[D-R4BDD|poles]] at $s=0,-1,-2,\ldots$.
:::

::: {.proof}
For $\Re s>0$, integration by parts gives $\Gamma(s+1)=s\Gamma(s)$, and $\Gamma$ is holomorphic there by [[PR-NLV6Q]].
For $n\ge1$ define, on $\ts{s\st\Re s>-n}$,
$$
\Gamma_n(s)\coloneqq\frac{\Gamma(s+n)}{s(s+1)\cdots(s+n-1)}.
$$
Since $\Re(s+n)>0$, the numerator is holomorphic on this half-plane, so $\Gamma_n$ is meromorphic there with at most simple poles at $0,-1,\ldots,-(n-1)$.
Iterating $\Gamma(s+1)=s\Gamma(s)$ shows $\Gamma_n=\Gamma$ on $\Re s>0$, so by the identity theorem $\Gamma_n$ and $\Gamma_{n+1}$ agree on $\ts{\Re s>-n}$ minus the poles.
The functions $\Gamma_n$ therefore define one meromorphic function on $\CC$.
At $s=-k$ with $0\le k\le n-1$, the numerator is $\Gamma(n-k)=(n-k-1)!\neq0$ and exactly one factor of the denominator vanishes, simply, so $-k$ is a simple pole.
:::
