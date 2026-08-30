---
title: Counterexamples
order: 8
problems:
  topics:
  - Counterexamples
---

# Counterexamples

The largest of the cross-cutting pages, because half the paper is "is this true", and the answer is usually no with a named witness.

## Convergence and integration

**The limit of the integrals is the integral of the limit** -- false, three ways, and each blocks a different theorem:

- $f_n = n\chi_{[0,1/n]}$, mass escaping to height;
- $f_n = \frac1n\chi_{[0,n]}$, escaping to width, and uniformly bounded, which shows why bounded convergence needs finite measure;
- $f_n = \chi_{[n,n+1]}$, escaping to infinity.

In each, no integrable $g$ dominates.

**$L^p$ convergence implies a.e. convergence** -- false: the typewriter sequence, marching intervals of shrinking width around $[0,1]$, converges in $L^1$ and nowhere pointwise.
A subsequence does converge a.e., which is the correct statement.

**a.e. convergence implies $L^p$ convergence** -- false, by any of the three escapes above.

## Measure

**Every set is measurable** -- false, by the Vitali construction, and it needs choice.

**Lebesgue measurable equals Borel** -- false: Lebesgue is the completion, so a subset of the Cantor set can be Lebesgue measurable and not Borel.

**A composition of measurable functions is measurable** -- false: the Cantor function carries a null set onto positive measure, so measurable $\circ$ continuous can fail.
Continuous $\circ$ measurable is always fine, and the order is the point.

**A set of positive measure contains an interval** -- false: the fat Cantor set.

## $L^p$ spaces

**$L^p \subseteq L^q$ for some ordering** -- false on $\RR$: $\frac1{\sqrt x}\chi_{(0,1)}$ is in $L^1$ and not $L^2$; $\frac1x\chi_{(1,\infty)}$ is in $L^2$ and not $L^1$.
The inclusion $L^q\subseteq L^p$ for $p<q$ holds only on finite measure spaces.

**$(L^\infty)^* = L^1$** -- false, though $(L^1)^* = L^\infty$ holds for $\sigma\dash$finite measures.

**Every $L^p$ is a Hilbert space** -- false: only $p=2$ satisfies the parallelogram law.

## Undergraduate

**A pointwise limit of continuous functions is continuous** -- false: $x^n$ on $[0,1]$.

**A uniform limit of differentiable functions is differentiable** -- false: uniform convergence controls values, not derivatives.
It is true if the derivatives converge uniformly, which is the correct hypothesis.

**Differentiable implies continuously differentiable** -- false: $x^2\sin(1/x)$.

**A continuous function on a bounded set is uniformly continuous** -- false without compactness: $1/x$ on $(0,1)$.

More are on [[Real_Analysis/counterexamples-undergraduate|the undergraduate counterexample list]].
