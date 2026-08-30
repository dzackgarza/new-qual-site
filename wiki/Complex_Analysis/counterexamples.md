---
title: Counterexamples
order: 9
problems:
  topics:
  - Counterexamples
---

# Counterexamples

Filed by the hypothesis they show is load-bearing.
Half the true-or-false questions on the exam are one of these with the hypothesis quietly removed, so the useful form to remember is not the example but the theorem it breaks.

## Liouville

**Bounded and holomorphic, but not constant** -- drop *entire*. $f(z) = z$ on $\DD$ is bounded and holomorphic; the theorem needs the whole plane.

**Entire and bounded on $\RR$, but not constant.** $f(z) = \sin z$ is bounded on the real line and unbounded on $\CC$: $\abs{\sin(iy)} \to \infty$.
Real intuition is the trap.

**Entire and nonconstant with $\abs f \leq C\abs z^n$** -- this does not contradict anything, it is the polynomial case.
The conclusion weakens from constant to polynomial of degree at most $n$.

## The identity principle

**Zeros accumulating, but $f\not\equiv 0$** -- the limit point must lie *inside* the domain.
$f(z) = \sin(\pi/z)$ on $\CC\smz$ vanishes at every $1/k$, and those accumulate at $0$, which is not in the domain.

**Agreement on a set with no limit point.** Two distinct polynomials agree at finitely many points; a set must accumulate for the theorem to apply.

## The maximum and minimum principles

**An interior minimum of $\abs f$** -- drop *nonvanishing*. $f(z) = z$ on $\DD$ has $\abs f$ minimized at the interior point $0$.
This is why the minimum modulus principle carries a hypothesis the maximum principle does not.

**A maximum on an unbounded domain.** The principle is about a maximum being attained; on an unbounded region a supremum need not be attained anywhere, and Phragmén--Lindelöf is what replaces it.

## Singularities

**Holomorphic on a punctured disc, with every kind of behaviour at the puncture.** The three cases are realized by $1$ (removable), $1/z$ (pole), and $e^{1/z}$ (essential) -- the same domain, three classifications.

**Bounded near the singularity, and still not defined there** -- this is exactly what Riemann's theorem removes.
$\sin(z)/z$ at $0$: the singularity is there only because nobody assigned a value.

**A singularity that is not in the classification at all.** $\sqrt z$ and $\Log z$ at $0$ are branch points and admit no Laurent expansion, so the removable/pole/essential trichotomy does not apply.
$1/\sin(\pi/z)$ has a non-isolated singularity at $0$.

## Convergence

**A pointwise limit of holomorphic functions that is not holomorphic.** Pointwise is not enough; the theorem needs locally uniform convergence.
By Montel, read backwards: a sequence whose pointwise limit fails to be differentiable somewhere cannot have been uniformly bounded on compact sets.

**A locally uniform limit of injective functions that is not injective** -- the constant escape clause in Hurwitz.
$f_n(z) = z/n$ are each injective, and the limit is constant.
This is precisely the case the Riemann mapping theorem must rule out.

## Conformal maps

**$\CC$ and $\DD$ are not biholomorphic** -- the Riemann mapping theorem needs $\Omega \neq \CC$.
Any holomorphic $\CC\to\DD$ is a bounded entire function, hence constant by Liouville.

**Nonvanishing derivative without injectivity.** $e^z$ has $f' = e^z \neq 0$ everywhere and is not injective on $\CC$; $f'\neq 0$ gives *local* injectivity only.

**Injective in the real sense, not the complex one.** $x\mapsto x^3$ is injective on $\RR$ with a vanishing derivative at $0$ and a non-differentiable inverse.
No holomorphic function behaves this way, which is what makes the inverse function theorem stronger over $\CC$.

## Holomorphy itself

**Real differentiable and not holomorphic.** $f(z) = \bar z$ has partial derivatives everywhere and fails Cauchy--Riemann; the difference quotient depends on the direction of approach.

**Cauchy--Riemann satisfied and still not holomorphic.** The equations at a single point are not enough; holomorphy needs them on a neighborhood, with the partials continuous.

**Nonvanishing derivative without holomorphy.** $\bar z$ again: conformality is holomorphic *plus* $f'\neq 0$, and the first half cannot be dropped.
