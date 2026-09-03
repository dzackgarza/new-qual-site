---
order: 60
topics:
- Riemann Integrability
- Integrals
---

# Riemann Integrability

The Riemann integral of a bounded function $f \colon [a,b] \to \RR$ is defined via upper and lower sums over partitions.
The key question is: which functions are Riemann integrable?

## The Lebesgue criterion

The complete answer is the Lebesgue criterion, which connects Riemann integrability to measure theory.

::: {.proposition}
[[PR-TDH2A]] A bounded function $f \colon [a,b] \to \RR$ is Riemann integrable if and only if its set of discontinuities $D_f$ has Lebesgue measure zero.
:::

This means "most" bounded functions are Riemann integrable — the discontinuity set must be small (null), but can be infinite.
The Cantor set is uncountable yet has measure zero, so a function discontinuous exactly on the Cantor set is Riemann integrable.

## Key consequences

**Continuous functions are Riemann integrable.** Continuity means $D_f = \emptyset$, which is certainly null.

**Monotone functions are Riemann integrable.** A monotone function on $[a,b]$ has at most countably many discontinuities, and countable sets have measure zero.

**Bounded functions with finitely many discontinuities are Riemann integrable.** Finite sets have measure zero.

## A function that fails

::: {.example}
[[FE-FJAKV]] The Dirichlet function $f(x) = \chi_\QQ$ is Lebesgue integrable (it equals zero a.e.) but not Riemann integrable, since $D_f = \RR$ has positive measure.
:::

The upper Riemann sums are always $b-a$ and the lower sums are always $0$, so the integral cannot exist in the Riemann sense.

## Relationship to the Lebesgue integral

Every Riemann integrable function is Lebesgue integrable, and the integrals agree.
But the Lebesgue integral is strictly more general: $\chi_\QQ$ is Lebesgue integrable with $\int \chi_\QQ = 0$, yet not Riemann integrable.
The Lebesgue criterion is the bridge: Riemann integrability is exactly the condition that makes the two theories coincide.
