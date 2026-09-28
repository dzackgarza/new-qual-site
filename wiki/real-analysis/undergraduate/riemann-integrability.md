---
title: Riemann integrability
order: 60
topics:
- Riemann Integrability
- Integrals
---

# Riemann integrability

A bounded function $f \colon [a,b] \to \RR$ is Riemann integrable if its upper and lower Darboux integrals, the infimum of the upper sums and the supremum of the lower sums over partitions of $[a,b]$, are equal.

## The Lebesgue criterion

[[PR-TDH2A]]

::: {.example}
The Cantor set $C$ is uncountable and has measure zero, so the bounded function $\chi_C$ on $[0,1]$, which is discontinuous exactly on $C$, is Riemann integrable, with integral $0$.

:::

## Consequences

::: {.corollary}
Let $f\colon[a,b]\to\RR$ be bounded.

- If $f$ is continuous, then $f$ is Riemann integrable, since $D_f=\emptyset$.

- If $f$ is monotone, then $f$ is Riemann integrable, since $D_f$ is countable and hence null.

- If $f$ has finitely many discontinuities, then $f$ is Riemann integrable.

:::

## A function that is not Riemann integrable

[[FE-FJAKV]]

## Relation to the Lebesgue integral

::: {.proposition}
If $f\colon[a,b]\to\RR$ is Riemann integrable, then $f$ is Lebesgue integrable on $[a,b]$ and the two integrals are equal.

:::

::: {.remark}
The converse fails: $\chi_{\QQ\cap[0,1]}$ is Lebesgue integrable with integral $0$ and not Riemann integrable.

:::
