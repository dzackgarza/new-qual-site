---
title: The statements
order: 10
topics:
- Measure Theory
---

# The statements

Tonelli and Fubini have the same conclusion—replace an integral on a product by either iterated integral—but their hypotheses pay for different things.
The decision rule is on [[real-analysis/fubini-tonelli/which-one-applies|Which one applies?]]; keep the exact statements here so the hypotheses can be checked cold.

## Tonelli: nonnegative measurable functions

For $f\ge0$ measurable, Tonelli permits the iterated integrals without assuming the answer is finite.
This is the theorem for changing the order of summation/integration when every term is nonnegative: the value may be $+\infty$, but the interchange itself is valid.

[[T-6PRW3]]

[[FT-4JRQX]]

## Fubini: integrable functions

Fubini assumes $f\in L^1$ on the product.
That hypothesis gives integrable sections almost everywhere and finite iterated integrals, all equal to the product integral.
If signs are present and absolute integrability has not been established, changing the order is exactly the step that still needs proof.

[[T-4GPEF]]

[[FT-T7OAO]]

[[T-X7XZX]]

[[FT-H6AWV]] [[FT-VHK2H]]

## Other interchanges

The same discipline applies to sums, derivatives, and integrals: identify a theorem whose hypotheses justify the interchange rather than treating the symbols formally.
For nonnegative sums, Tonelli/monotone convergence is often enough; differentiation under the integral needs its own domination or regularity hypothesis.

[[PR-V4MOK]]

[[PR-JW3QE]]

[[E-WXIRH]]
