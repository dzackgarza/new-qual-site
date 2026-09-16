---
title: Counterexamples
order: 8
topics:
- Counterexamples
- Logic and Quantifiers
---

# Counterexamples

Each entry names a statement and gives a counterexample, or states the correct version.

## Limits and continuity

**Continuity does not imply differentiability.** $\abs x$ is continuous and not differentiable at $0$, and Weierstrass's function is continuous on $\RR$ and differentiable nowhere.

**Differentiability does not imply continuous differentiability.** $f(x)=x^2\sin(1/x)$ for $x\neq0$, $f(0)=0$, is differentiable on $\RR$, and $f'$ is not continuous at $0$.

**Continuity on a bounded interval does not imply uniform continuity.** $1/x$ is continuous on $(0,1)$ and not uniformly continuous; a continuous function on a closed bounded interval is uniformly continuous.

**A continuous function on a bounded interval need not attain its bounds.** $x$ on $(0,1)$ attains neither its supremum nor its infimum; a continuous function on a compact set attains both.

**Sequential criterion for continuity.** If $\lim_n f(x_n)$ exists for every sequence $x_n\to a$, then $f$ is continuous at $a$: interleaving two sequences shows that all these limits are equal, and the constant sequence $x_n=a$ shows that the common limit is $f(a)$.
Hence two sequences $x_n\to a$ and $y_n\to a$ with $\lim f(x_n)\neq\lim f(y_n)$ show that $f$ is not continuous at $a$.

## Sequences and series

**Terms tending to zero do not imply convergence.** $\sum 1/n$ diverges.

**Convergence does not imply absolute convergence.** $\sum (-1)^{n+1}/n$ converges and $\sum 1/n$ diverges; by the Riemann rearrangement theorem, the terms of a conditionally convergent series can be rearranged to converge to any real number.

**A convergent sequence need not be eventually monotone.** $(-1)^n/n$ converges to $0$ and is not eventually monotone.

**Pointwise convergence does not preserve continuity.** $x^n$ on $[0,1]$ converges pointwise to the function equal to $0$ on $[0,1)$ and $1$ at $1$.

**Uniform convergence does not preserve differentiability.** $f_n(x)=\sqrt{x^2+1/n}$ is differentiable and converges uniformly on $\RR$ to $\abs x$.
Uniform convergence preserves continuity and Riemann integrability; if $f_n\to f$ pointwise, each $f_n$ is continuously differentiable, and $f_n'$ converges uniformly, then $f$ is differentiable and $f'=\lim f_n'$.

## Derivatives and integrals

**A derivative need not be continuous.** The derivative of $x^2\sin(1/x)$, extended by $0$, is discontinuous at $0$.
Every derivative has the intermediate value property (Darboux's theorem), so a function without it, such as a step function, is not a derivative.

**A bounded function need not be Riemann integrable.** The indicator function of $\QQ\intersect[0,1]$ is bounded and not Riemann integrable.

**Lebesgue's criterion.** A function on $[a,b]$ is Riemann integrable if and only if it is bounded and its set of discontinuities has measure zero; in particular its points of continuity are dense in $[a,b]$.

**$f' = 0$ implies $f$ constant only on an interval.** On $(0,1)\union(2,3)$, the function equal to $0$ on $(0,1)$ and $1$ on $(2,3)$ has derivative $0$ and is not constant.

## Algebra and linear algebra

**Repeated eigenvalues do not prevent diagonalizability.** The identity matrix $I_2$ has the repeated eigenvalue $1$ and is diagonal.

**A real square matrix need not have a real eigenvector.** The rotation $\matt{0}{-1}{1}{0}$ has characteristic polynomial $x^2+1$ and no real eigenvalue.

**Equal characteristic polynomials do not imply similarity.** $\matt{0}{0}{0}{0}$ and $\matt{0}{1}{0}{0}$ both have characteristic polynomial $x^2$ and are not similar; the $4\times4$ matrices $J_2(0)\oplus J_2(0)$ and $J_2(0)\oplus J_1(0)\oplus J_1(0)$ also have the same minimal polynomial $x^2$ and are not similar.

**A group of prime power order need not be abelian.** Groups of order $p$ and $p^2$ are abelian, and the dihedral group $D_4$ of order $8$ is not.
