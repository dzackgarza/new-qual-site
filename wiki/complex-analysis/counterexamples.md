---
title: Counterexamples
order: 9
topics:
- Counterexamples
---

# Counterexamples

Examples showing that a theorem fails when one of its hypotheses is removed, grouped by theorem.

## Liouville's theorem

**Holomorphy on a proper subset.** $f(z) = z$ on $\DD$ is bounded and holomorphic and not constant; Liouville's theorem requires $f$ to be entire.

**Boundedness on $\RR$ only.** $f(z) = \sin z$ is entire and bounded on $\RR$, and $\abs{\sin(iy)} = \sinh\abs y \to \infty$ as $\abs y\to\infty$.

::: {.remark}
An entire function with $\abs{f(z)} \leq C\abs z^n$ for large $\abs z$ is a polynomial of degree at most $n$ ([[complex-analysis/cauchy-theory/cauchy-estimates-and-liouville|Cauchy estimates and Liouville]]), so $f(z)=z^n$ is nonconstant under this bound.
:::

## The identity principle

**Limit point outside the domain.** $f(z) = \sin(\pi/z)$ on $\CC\smz$ vanishes at the points $1/k$, which accumulate at $0\notin\CC\smz$, and $f\not\equiv 0$.

**No limit point.** Distinct polynomials of degree at most $n$ can agree at $n$ points; a finite set has no limit point.

## The maximum and minimum modulus principles

**Zeros in the minimum modulus principle.** $f(z) = z$ on $\DD$ is nonconstant, and $\abs f$ has its minimum at the interior point $0$, a zero of $f$.

**Unbounded domains.** On the strip $S\coloneqq\ts{\abs{\Im z}<\pi/2}$, the function $f(z) = \exp(e^z)$ is holomorphic on $\overline S$ with $\abs f = 1$ on $\bd S$, since $e^z = \pm i e^x$ there, and $f(x) = \exp(e^x)$ is unbounded on $\RR\subseteq S$.
The bound $\max_{\overline\Omega}\abs f = \max_{\bd\Omega}\abs f$ requires $\Omega$ bounded; the Phragmén--Lindelöf principle gives versions on unbounded domains under growth hypotheses.

## Singularities

**All three types on the same punctured disc.** On $\DD\smz$, $1$ has a removable singularity, $1/z$ a pole, and $e^{1/z}$ an essential singularity at $0$.

**Bounded near an undefined point.** $\sin(z)/z$ is holomorphic and bounded on a punctured disc about $0$, and by Riemann's theorem it extends holomorphically with value $1$.

**Singularities outside the classification.** $\sqrt z$ and $\Log z$ have branch points at $0$ and no Laurent expansion on any punctured disc about $0$, so the classification into removable singularities, poles, and essential singularities does not apply.
$1/\sin(\pi/z)$ has a non-isolated singularity at $0$.

## Convergence

**Pointwise limits.** A pointwise limit of holomorphic functions need not be holomorphic: by Runge's theorem there are polynomials converging pointwise on $\CC$ to a discontinuous function.
By Montel's theorem, a sequence of holomorphic functions whose pointwise limit is not holomorphic is not uniformly bounded on compact subsets.

**Univalent maps with a constant limit.** $f_n(z) = z/n$ is injective for each $n$, and $f_n\to 0$ locally uniformly; Hurwitz's theorem allows the limit of univalent functions to be constant.

## Conformal maps

**$\CC$ and $\DD$ are not biholomorphic.** Any holomorphic map $\CC\to\DD$ is a bounded entire function, hence constant by Liouville's theorem; the Riemann mapping theorem requires $\Omega \neq \CC$.

**Nonvanishing derivative without injectivity.** $e^z$ has derivative $e^z \neq 0$ everywhere and $e^0 = e^{2\pi i}$; nonvanishing derivative gives only local injectivity.

**Injective with vanishing derivative, over $\RR$.** $x\mapsto x^3$ is injective on $\RR$, has derivative $0$ at $0$, and has inverse $x^{1/3}$, which is not differentiable at $0$.
An injective holomorphic function has nonvanishing derivative ([[C-FVT4V]]).

## Holomorphy

**Real differentiable and not holomorphic.** $f(z) = \bar z$ is real differentiable everywhere and fails the Cauchy--Riemann equations; its difference quotient $\bar h/h$ depends on the direction of $h$.

**Cauchy--Riemann equations at one point.** $f(x+iy) = \sqrt{\abs{xy}}$ has $u_x = u_y = v_x = v_y = 0$ at $0$, so the Cauchy--Riemann equations hold there, but along $y = x$ the difference quotient is $\abs x/\bigl((1+i)x\bigr)$, which has no limit as $x\to 0$.

**Invertible real Jacobian without conformality.** $f(z) = \bar z$ has invertible real Jacobian at every point and reverses signed angles; a conformal map is holomorphic with nonvanishing derivative.
