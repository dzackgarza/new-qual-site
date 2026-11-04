---
schema: qual/card@1
id: P-UCI13H3-5
kind: problem
title: $\oint_{\abs z=2}\frac{4z^7-1}{z^8-2z+1}\,dz$
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
  - Rouché
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Find the integral
$$
\int_{\abs z=2}\frac{4z^7-1}{z^8-2z+1}\,dz.
$$
:::

::: {.solution}
The denominator $q(z)=z^8-2z+1$ satisfies $q'(z)=8z^7-2$, so the integrand is $\tfrac12q'(z)/q(z)$.

::: pf

::: {.pf-step #zeros-inside}
All eight zeros of $q$ lie inside $|z|=2$, and they are simple.

::: pf-proof
On $|z|=2$ we have $\abs{z^8}=256>5\ge\abs{2z-1}$, so by Rouché's theorem $q(z)=z^8-(2z-1)$ has exactly as many zeros inside $|z|=2$ as $z^8$, namely $8$.
The zeros are simple because $q$ and $q'$ have no common zero: $q'(z)=0$ gives $z^7=\tfrac14$, whence $z^8=z/4$ and $q(z)=\tfrac z4-2z+1=1-\tfrac{7z}{4}$, which vanishes only for $z=\tfrac47$, and $(\tfrac47)^7\ne\tfrac14$.
:::

:::

::: {.pf-step #residues}
$\displaystyle\int_{\abs z=2}\frac{q'(z)}{q(z)}\,dz=16\pi i$.

::: pf-proof
The function $q'/q$ has simple poles exactly at the zeros of $q$, all of which lie inside the circle, and the residue at a simple zero $\zeta$ equals the multiplicity, which is $1$.
The residue theorem gives $\int_{\abs z=2}q'/q\,dz=2\pi i\cdot8=16\pi i$.
:::

:::

::: {.pf-step #value}
$\displaystyle\int_{\abs z=2}\frac{4z^7-1}{z^8-2z+1}\,dz=\boxed{8\pi i}$.

::: pf-proof
The integrand equals $\tfrac12q'/q$, so the integral is $\tfrac12\cdot16\pi i=8\pi i$ by step [](#residues){.pf-ref}.
:::

:::

:::

:::
