---
schema: qual/card@1
id: T-CJCKL
kind: theorem
title: Rouché's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Winding Number
  - Meromorphic Functions
relations: []
review: draft
---

::: {.theorem ref="Rouche"}
Let $\Omega\subseteq\CC$ be open, let $M$ and $m$ be [[D-7DFVJ|meromorphic]] on $\Omega$, and let $\gamma$ be a piecewise smooth [[D-YKB3V|toy contour]] in $\Omega$ whose interior $\Omega_\gamma$ satisfies $\overline{\Omega_\gamma}\subseteq\Omega$.
Assume that $M$ and $m$ have no poles on $\gamma$ and that
$$
\abs{m(z)}<\abs{M(z)}\quad\text{for all } z\in\gamma.
$$
For a meromorphic function $h$, write $Z_h$ and $P_h$ for the numbers of [[D-65VIK|zeros]] and [[D-AUD6K|poles]] of $h$ in $\Omega_\gamma$, counted with multiplicity.
Then the [[D-PJ7JM|winding numbers]] of $M\circ\gamma$ and $(M+m)\circ\gamma$ about $0$ agree, and
$$
Z_M-P_M=Z_{M+m}-P_{M+m}.
$$
In particular, if $M$ and $m$ are [[D-E7A5W|holomorphic]] on $\Omega$, then $M$ and $M+m$ have the same number of zeros in $\Omega_\gamma$.
:::
