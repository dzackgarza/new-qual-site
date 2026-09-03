---
title: Counterexamples
order: 8
topics:
- Counterexamples
- Logic and Quantifiers
---

# Counterexamples

The prelim's true-or-false questions, filed by the statement each refutes.

## Limits and continuity

**Continuous implies differentiable** -- false: $\abs x$, and Weierstrass's nowhere-differentiable function for the extreme case.

**Differentiable implies continuously differentiable** -- false: $x^2\sin(1/x)$ extended by $0$.

**A continuous function on a bounded interval is uniformly continuous** -- false without closedness: $1/x$ on $(0,1)$.

**A continuous function attains its bounds** -- false without compactness: $x$ on $(0,1)$.

**If $\lim f(x_n)$ exists for every sequence $x_n\to a$ then $f$ is continuous at $a$** -- true, and the standard way to disprove continuity is to exhibit two sequences with different limits.

## Sequences and series

**Terms going to zero implies convergence** -- false: the harmonic series.

**Absolute convergence and convergence are the same** -- false: the alternating harmonic series converges and not absolutely, and its terms can be rearranged to any value.

**A convergent sequence is monotone eventually** -- false: $(-1)^n/n$.

**Pointwise convergence preserves continuity** -- false: $x^n$ on $[0,1]$.

**Uniform convergence preserves differentiability** -- false; it preserves continuity and integrability, and differentiability needs the derivatives to converge uniformly.

## Derivatives and integrals

**A derivative is continuous** -- false, as above, but a derivative does satisfy the intermediate value property, so not every function is a derivative.

**Bounded implies Riemann integrable** -- false: the indicator of the rationals.

**Riemann integrable implies continuous somewhere dense** -- true in the sense that the discontinuities form a null set, which is Lebesgue's criterion.

**$f' = 0$ implies constant** -- true on an interval, false on a disconnected domain.

## Algebra and linear algebra

**A matrix with repeated eigenvalues is not diagonalizable** -- false: the identity.

**Every square matrix has an eigenvector over $\RR$** -- false: a rotation.

**Two matrices with the same characteristic polynomial are similar** -- false, and the minimal polynomial does not settle it either.

**A group of prime power order is abelian** -- false above $p^2$: $D_4$.
