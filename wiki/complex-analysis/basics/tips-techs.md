---
order: 0
title: Techniques
---

# Techniques

> A great deal of content borrowed from [Chris Eur's complex analysis notes (Stanford)](https://web.stanford.edu/~chriseur/notes_pdf/Eur_ComplexAnalysis_Notes.pdf).

## Notation

- $\DD_r(a) \coloneqq \ts{z\in \CC \st \abs{z-a}< r}$, the open disc of radius $r$ about $a$.
- $\bar{\DD}_r(a) \coloneqq \ts{z\in \CC \st \abs{z-a} \leq r}$, the closed disc of radius $r$ about $a$.
- $\DD_r^*(a) \coloneqq \ts{z\in \CC \st 0 < \abs{z-a} < r}$, the punctured disc of radius $r$ about $a$.
- $\Delta \coloneqq \DD_1(0)$, the open unit disc; $\bar\Delta \coloneqq \bar{\DD}_1(0)$, the closed unit disc; $\Delta^* \coloneqq \DD_1^*(0)$, the punctured unit disc.
- $\Omega$ denotes an open simply connected subset of $\CC$.
- $\OO(\Omega) = \Hol(\Omega) = \Hol(\Omega, \CC)$ denotes the $\CC$-algebra of holomorphic functions $f\colon\Omega \to \CC$.

## Principal results

- Estimates for derivatives: [[complex-analysis/cauchy-theory/cauchy-estimates-and-liouville|Cauchy's inequality]]
- [[complex-analysis/cauchy-theory/cauchys-theorem|Cauchy's theorem]]
- [[complex-analysis/cauchy-theory/the-integral-formula|Cauchy's integral formula and the mean value property]]
- [[complex-analysis/cauchy-theory/morera-and-converses|Morera's theorem]]
- [[complex-analysis/cauchy-theory/cauchy-estimates-and-liouville|Liouville's theorem]]
- [[complex-analysis/cauchy-theory/maximum-modulus-and-open-mapping|The maximum modulus principle and the open mapping theorem]]
- [[complex-analysis/counting-zeros/rouches-theorem|Rouché's theorem]]
- [[complex-analysis/cauchy-theory/schwarz-reflection|The Schwarz reflection principle]]
- [[complex-analysis/conformal-maps/the-schwarz-lemma|The Schwarz lemma]]
- [[complex-analysis/singularities/casorati-weierstrass-and-picard|The Casorati--Weierstrass theorem and the Picard theorems]]
- [[complex-analysis/conformal-maps/build-me-a-map|Conformal maps]]
- [[complex-analysis/conformal-maps/blaschke-factors-and-automorphisms|Automorphisms of the disc and the plane]]
- [[complex-analysis/cauchy-theory/the-identity-principle|The identity principle]]
- [[complex-analysis/residues-and-contours/computing-residues|Computing residues]]
- [[T-ZO5UU|Jordan's lemma]]
- [[complex-analysis/holomorphic-functions/the-cauchy-riemann-equations|The Cauchy--Riemann equations]]
- [[complex-analysis/counting-zeros/the-argument-principle|The argument principle]]
- [[complex-analysis/conformal-maps/the-riemann-mapping-theorem|The Riemann mapping theorem]]
- [[complex-analysis/singularities/removable-poles-essential|Riemann's removable singularity theorem]]
- [[complex-analysis/holomorphic-functions/harmonic-functions|Harmonic functions and the mean value property]]

[[attachments/ComplexAnalysisNotes.pdf|Complex analysis theorem summary]] is a compact statement sheet.

## Identities

The algebraic identities for $z\bar z$, $\Re z$, $\Im z$, the exponential forms of $\cos$, $\sin$, $\cosh$, $\sinh$, and the zeros and periods of the hyperbolic functions are on [[complex-analysis/basics/complex-arithmetic#Identities|Complex arithmetic]].

::: {.fact}
$$
\begin{aligned}
dz &= dx + i\,dy, \\
d\bar z &= dx - i\,dy, \\
f_z &= f_x = f_y / i \quad \text{for } f \text{ holomorphic},
\end{aligned}
$$
and for $\ell\in\ZZ$,
$$
\int_{0}^{2 \pi} e^{i \ell x} \dx =
\begin{cases}
2 \pi & \ell=0, \\
0 & \ell\neq 0.
\end{cases}
$$

:::

::: {.fact}
\envlist

- $\abs{f}^2 = f\bar{f}$.
- $z$ is purely imaginary if and only if $\bar{z} = -z$, and $z\in \RR$ if and only if $\bar z = z$.
- $\log\abs{z} = {1\over 2}\log\qty{\abs{z}^2} = {1\over 2}\log\qty{x^2 + y^2}$ for $z = x+iy\neq 0$.
- For $w, z, a\in\CC$ with $\abs{w-a}<\abs{z-a}$,
$$
\frac{1}{z-w}
=\frac{1}{(z-a)\qty{1-\frac{w-a}{z-a}}}
=\sum_{n=0}^{\infty}\frac{(w-a)^n}{(z-a)^{n+1}}.
$$
The standard expansions, generalized binomial coefficients, Cauchy products, and inverses of power series are on [[complex-analysis/basics/series-reference|Series reference]].

:::

## Holomorphy

::: {.fact title="Sufficient conditions for holomorphy"}
A function $f$ on an open set $U$ is holomorphic if any of the following holds:

- $f$ is continuous and $\int_{\bd T} f = 0$ for every closed triangle $T\subseteq U$ ([[complex-analysis/cauchy-theory/morera-and-converses|Morera's theorem]]);
- $f$ has a holomorphic primitive on $U$;
- $f$ is locally the sum of a convergent power series.

:::

::: {.fact}
\envlist

- If $f$ is holomorphic with no zeros, then $1/f$ is holomorphic; applying the maximum modulus principle or Liouville's theorem to $1/f$ gives the minimum modulus principle and constancy of entire functions bounded below by a positive constant.
- If $f$ is holomorphic and nonvanishing on a simply connected domain $\Omega$, then $f = e^g$ for some holomorphic $g$ on $\Omega$, and $f^{1/n} \coloneqq \exp\qty{{1\over n}g}$ is a holomorphic $n$th root.
- If $f$ is holomorphic on a neighborhood of $\bar\DD$ and $\abs{f} = 1$ on $\bd \DD$, then $f$ is a unimodular constant times a finite Blaschke product.
- The substitutions $z\mapsto 1/z$, $f\mapsto 1/f$, and $w = e^z$ transfer statements between $0$ and $\infty$, between zeros and poles, and between strips and annuli.

:::

## Constancy

::: {.fact title="Criteria for a holomorphic function to be constant"}
Let $f$ be holomorphic on a domain $U$.
Then $f$ is constant if any of the following holds:

- $f' = 0$ on $U$; by the Cauchy--Riemann equations it suffices that $u_x = u_y = 0$ for $u = \Re f$.
- One of $\Re f$, $\Im f$, $\abs{f}$, or $\arg f$ (for a continuous branch) is constant.
- $\abs f$ attains a maximum in $U$, or $f$ is nonvanishing and $\abs f$ attains a minimum in $U$.
- $f(U)$ is not open, for instance $f(U)\subseteq\RR$ or $f(U)\subseteq \bd\DD_r(0)$ ([[complex-analysis/cauchy-theory/maximum-modulus-and-open-mapping|open mapping theorem]]).
- $U$ is bounded, $f$ extends continuously to $\bar U$, $f$ has no zeros in $U$, and $\abs f$ is constant on $\bd U$: the maximum modulus principle applied to $f$ and to $1/f$ shows $\abs f$ is constant.

If moreover $U = \CC$, then $f$ is constant if any of the following holds:

- $f$ is bounded ([[complex-analysis/cauchy-theory/cauchy-estimates-and-liouville|Liouville's theorem]]); if also $f(z)\to 0$ as $z\to\infty$, then $f\equiv 0$.
- $\abs f\geq M$ for some $M>0$, by Liouville's theorem applied to $1/f$.
- $e^f$ or $e^{-f}$ is bounded, since $\abs{e^{f}} = e^{\Re f}$.
- $f$ is periodic with two $\RR$-linearly independent periods, since then $f$ is bounded by its bound on a closed fundamental parallelogram.
- $f$ omits two values of $\CC$, for instance when $f(\CC)$ misses an open set (little Picard theorem).

If $f$ and $g$ are holomorphic on a domain $U$ and $f-g$ has a zero set with a limit point in $U$, then $f = g$ ([[complex-analysis/cauchy-theory/the-identity-principle|identity principle]]).

:::

## Singularities

::: {.fact title="Classifying an isolated singularity"}
Let $f$ be holomorphic on a punctured disc about $z_0$.

- $z_0$ is removable if and only if $f$ is bounded near $z_0$.
- $z_0$ is a pole if and only if $\abs{f(z)}\to\infty$ as $z\to z_0$.
- $z_0$ is a pole of order $m$ if and only if $f(z) = (z-z_0)^{-m}g(z)$ with $g$ holomorphic near $z_0$ and $g(z_0)\neq 0$, equivalently if $1/f$ has a zero of order $m$ at $z_0$, equivalently if the Laurent expansion at $z_0$ has lowest term of degree $-m$.
- $z_0$ is essential if and only if $\lim_{z\to z_0} f(z)$ exists neither in $\CC$ nor as $\infty$, equivalently if the Laurent expansion at $z_0$ has infinitely many terms of negative degree.
  Two sequences $z_k\to z_0$ along which $f$ has different limits show this.

A meromorphic function $f$ and its derivative $f'$ have the same poles.

:::

::: {.fact}
If $h$ has an essential singularity at $z_0$, then by the great Picard theorem, in every punctured neighborhood of $z_0$, $h$ takes every value of $\CC$ infinitely often with at most one exception.
With $h \coloneqq f/g$, this shows $f(z) = cg(z)$ for infinitely many $z$ near $z_0$, for all but at most one $c\in\CC$.

:::

## Zeros

::: {.fact}
Let $f$ be holomorphic near $z_0$.

- $f$ has a zero of order $n$ at $z_0$ if and only if $f^{(k)}(z_0) = 0$ for $0\leq k<n$ and $f^{(n)}(z_0) \neq 0$.
- If $f(z_0)\neq 0$, then $f$ is nonzero on a neighborhood of $z_0$ by continuity.
- If $f(z_0) = 0$ and $f$ is not identically zero near $z_0$, then $f$ is nonzero on a punctured neighborhood of $z_0$.
- Dividing by a finite Blaschke product with the same zeros in $\DD$ gives a function without zeros in $\DD$ with the same modulus on $\bd\DD$.
- Zeros in a region are counted by [[complex-analysis/counting-zeros/rouches-theorem|Rouché's theorem]] and [[complex-analysis/counting-zeros/the-argument-principle|the argument principle]].

:::

## Estimates

::: {.fact}
\envlist

- For $\abs a\neq \abs b$, the reverse triangle inequality gives
$$
{1\over \abs{a\pm b}} \leq {1\over \abs{\abs{a} - \abs{b} } }.
$$
- The Cauchy integral formula bounds derivatives of $f$ by the maximum of $\abs f$ on a circle, and bounds $\abs{f}$ at interior points by an integral of $\abs f$ over a curve.
- If $u_n$ are harmonic on a bounded domain $U$, continuous on $\bar U$, and $u_n$ converges uniformly on $\bd U$, then $u_n$ converges uniformly on $\bar U$, by the maximum principle applied to $u_n - u_m$.
- For $f\colon[a,b]\to\RR$ differentiable with $\abs{f'} \leq M$, the mean value theorem gives $\abs{f(x) - f(y)} \leq M\abs{x-y}$.
- If $h$ is holomorphic on $\DD$ with $\abs h\leq 1$ and $h(0) = 0$, then $\abs{h(z)}\leq\abs z$ by the [[complex-analysis/conformal-maps/the-schwarz-lemma|Schwarz lemma]]; applied to $h \coloneqq f/g$ this gives $\abs{f(z)}\leq\abs{z}\abs{g(z)}$.

:::

::: {.example}
In the criterion that a zero-free $f$ with $\abs f$ constant on $\bd U$ is constant, the hypothesis that $f$ has no zeros is necessary: $f(z) = z$ has $\abs f = 1$ on $\bd\DD$ and is not constant.

:::

## Polynomials

::: {.fact}
An entire function $f$ is a polynomial if and only if $f^{(n)} = 0$ for all sufficiently large $n$, if and only if $f$ has a pole or a removable singularity at $\infty$.
Cauchy's inequality shows $f^{(n)} = 0$ for $n>d$ when $\abs{f(z)}\leq C\abs z^d$ for large $\abs z$.

:::
