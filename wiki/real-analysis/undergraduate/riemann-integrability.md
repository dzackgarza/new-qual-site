---
title: Riemann integrability
order: 60
topics:
- Riemann Integrability
- Integrals
---

# Riemann integrability

[[D-1EBNU]]

## The Lebesgue criterion

[[PR-TDH2A]]

::: {.example}
The Cantor set $C$ is uncountable and has measure zero, so the bounded function $\chi_C$ on $[0,1]$, which is discontinuous exactly on $C$, is Riemann integrable, with integral $0$.

:::

## Consequences

::: {.corollary}
Let $f\colon[a,b]\to\RR$ be bounded.

- If $f$ is continuous, then $f$ is Riemann integrable.

- If $f$ is monotone, then $f$ is Riemann integrable.

- If $f$ has finitely many discontinuities, then $f$ is Riemann integrable.
:::

::: {.remark}
The three cases are read off the Lebesgue criterion above: a continuous $f$ has $D_f=\varnothing$, a monotone $f$ has $D_f$ countable, and a function with finitely many discontinuities has $D_f$ finite and hence null. The first two are also [@Rud76, ch. 6, Theorem 6.8] and [@Rud76, ch. 6, Theorem 6.9], which prove them from the definition rather than through the criterion.
:::

## A function that is not Riemann integrable

[[FE-FJAKV]]

## Relation to the Lebesgue integral

::: {.proposition}
If $f\colon[a,b]\to\RR$ is Riemann integrable, then $f$ is Lebesgue integrable on $[a,b]$ and the two integrals are equal [@Rud76, ch. 11, Theorem 11.33(a)].

:::
