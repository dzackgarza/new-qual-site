---
order: 0
title: Techniques
---

# Techniques

## Notation

- $\DD_r(a) \coloneqq \theset{z\in \CC \st \abs{z-a}< r}$, the open disc of radius $r$ about $a$.
- $\bar{\DD}_r(a) \coloneqq \theset{z\in \CC \st \abs{z-a} \leq r}$, the closed disc of radius $r$ about $a$.
- $\DD_r^*(a) \coloneqq \theset{z\in \CC \st 0 < \abs{z-a} < r}$, the punctured disc of radius $r$ about $a$.
- $\Omega$ denotes an open subset of $\CC$; it is a domain (connected) when the statement needs one, and simply connected when the statement needs primitives.
- $\OO(\Omega)$ denotes the $\CC$-algebra of [[D-E7A5W|holomorphic]] functions $f\colon\Omega \to \CC$.

## Principal results

- Estimates for derivatives: [[T-22RQZ|Cauchy's inequality]]
- [[T-2OVCI|Cauchy's theorem]]
- [[T-LA2UI|The Cauchy integral formula]] and [[T-5BLYU|the mean value property]]
- [[T-LHSMY|Morera's theorem]]
- [[T-QHIHJ|Liouville's theorem]]
- [[T-BYNL5|The maximum modulus principle]] and [[C-FRF33|the open mapping theorem]]
- [[T-CJCKL|Rouché's theorem]]
- [[T-Q3GGF|The Schwarz reflection principle]]
- [[T-DAETF|The Schwarz lemma]]
- [[T-C5VEI|The Casorati--Weierstrass theorem]] and the [[T-HWBWI|little]] and [[T-DDOWW|great]] Picard theorems
- [[D-TM4TE|Conformal maps]]
- [[T-W26VL|Automorphisms of the disc]] and [[T-VGDFW|of the upper half-plane]]
- [[T-SVF2W|The identity principle]]
- [[complex-analysis/residues-and-contours/computing-residues|Computing residues]]
- [[T-ZO5UU|Jordan's lemma]]
- [[D-CREQS|The Cauchy--Riemann equations]]
- [[T-JXDQT|The argument principle]]
- [[T-4MDS6|The Riemann mapping theorem]]
- [[T-ZZJDP|Riemann's removable singularity theorem]]
- [[D-CFBSA|Harmonic functions]] and [[T-5BLYU|the mean value property]]

[[attachments/ComplexAnalysisNotes.pdf|Complex analysis theorem summary]] is a compact statement sheet.

## Identities

The algebraic identities for $z\bar z$, $\Re z$, $\Im z$, the exponential forms of $\cos$, $\sin$, $\cosh$, $\sinh$, and the zeros and periods of the hyperbolic functions are on [[complex-analysis/basics/complex-arithmetic#Identities|Complex arithmetic]].

::: {.fact}
For $\ell\in\ZZ$,
$$
\int_{0}^{2 \pi} e^{i \ell x} \dx =
\begin{cases}
2 \pi & \ell=0, \\
0 & \ell\neq 0,
\end{cases}
$$
and the complex differentials $\dz = \dx+i\,\dy$ and $\dzbar = \dx-i\,\dy$ give the differential of a $C^1$ function as
$dF=\frac{\partial F}{\partial z}\dz+\frac{\partial F}{\partial\bar z}\dzbar$ ([[D-OAFF5|the Wirtinger operators]]).

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

The first two items are [@Ahl73, ch. 1, §1.4, Conjugation, Absolute Value], which records $\abs z^2=z\bar z$ and the characterisations of the real and purely imaginary numbers by $\bar z=\pm z$; the third is the real identity $\log\abs z=\frac12\log\abs z^2$ applied to $\abs z^2=x^2+y^2$, with $\log$ the real logarithm of [[D-4CSPM]]; the fourth is the geometric series $\frac{1}{1-\zeta}=\sum\zeta^n$ for $\abs\zeta<1$ with $\zeta=\frac{w-a}{z-a}$, which is the expansion [@Ahl73, ch. 5, §1.3, The Laurent Series] carries out for the negative powers of a Laurent development.
:::

## Holomorphy

::: {.fact title="Sufficient conditions for holomorphy"}
A function $f$ on an open set $U$ is holomorphic if any of the following holds:

- $f$ is continuous and $\int_{\bd T} f = 0$ for every closed triangle $T\subseteq U$ ([[T-LHSMY|Morera's theorem]]);
- $f$ has a holomorphic primitive on $U$;
- $f$ is locally the sum of a convergent power series.

The first is [[T-LHSMY|Morera's theorem]]; the second holds because the derivative of a holomorphic function is holomorphic, which is [@Ahl73, ch. 4, §2.3, Higher Derivatives], so a primitive of $f$ is holomorphic and hence so is $f$; the third is part (iii) of [@Ahl73, ch. 2, §2.4, Theorem 2], that a power series is an analytic function on its disc of convergence.
:::

::: {.fact}
\envlist

- If $f$ is holomorphic with no zeros, then $1/f$ is holomorphic; applying the maximum modulus principle or Liouville's theorem to $1/f$ gives the minimum modulus principle and constancy of entire functions bounded below by a positive constant.
- If $f$ is holomorphic and nonvanishing on a simply connected domain $\Omega$, then $f = e^g$ for some holomorphic $g$ on $\Omega$, and $f^{1/n} \coloneqq \exp\qty{{1\over n}g}$ is a holomorphic $n$th root.
- If $f$ is holomorphic on a neighborhood of $\bar\DD$ and $\abs{f} = 1$ on $\bd \DD$, then $f$ is a unimodular constant times a finite Blaschke product ([[P-OOVED]]).
- The substitutions $z\mapsto 1/z$, $f\mapsto 1/f$, and $w = e^z$ transfer statements between $0$ and $\infty$, between zeros and poles, and between strips and annuli.

The first item is [@Ahl73, ch. 4, §3.2, Zeros and Poles], which notes that $g=1/f$ is defined and analytic where $f\neq0$; the minimum principle is the maximum principle applied to that $1/f$, and the constancy follows as for Liouville. The second is [@Ahl73, ch. 4, §4.3, Exact Differentials in Simply Connected Regions], which constructs a single-valued logarithm of a nonvanishing function on a simply connected region; the $n$th root is $e^{g/n}$ as in [[D-T6INB]]. The third is [[P-OOVED]], the factorisation of a function of modulus one on the circle into a unimodular constant and a finite product of [[D-MFPYG|Blaschke factors]].
:::

## Constancy

::: {.fact title="Criteria for a holomorphic function to be constant"}
Let $f$ be holomorphic on a domain $U$.
Then $f$ is constant if any of the following holds:

- $f' = 0$ on $U$; by the Cauchy--Riemann equations it suffices that $u_x = u_y = 0$ for $u = \Re f$.
- One of $\Re f$, $\Im f$, $\abs{f}$, or $\arg f$ (for a continuous branch) is constant.
- $\abs f$ attains a maximum in $U$, or $f$ is nonvanishing and $\abs f$ attains a minimum in $U$.
- $f(U)$ is not open, for instance $f(U)\subseteq\RR$ or $f(U)\subseteq \bd\DD_r(0)$ ([[C-FRF33|open mapping theorem]]).
- $U$ is bounded, $f$ extends continuously to $\bar U$, $f$ has no zeros in $U$, and $\abs f$ is constant on $\bd U$: the maximum modulus principle applied to $f$ and to $1/f$ shows $\abs f$ is constant.

If moreover $U = \CC$, then $f$ is constant if any of the following holds:

- $f$ is bounded ([[T-QHIHJ|Liouville's theorem]]); if also $f(z)\to 0$ as $z\to\infty$, then $f\equiv 0$.
- $\abs f\geq M$ for some $M>0$, by Liouville's theorem applied to $1/f$.
- $e^f$ or $e^{-f}$ is bounded, since $\abs{e^{f}} = e^{\Re f}$.
- $f$ is periodic with two $\RR$-linearly independent periods, since then $f$ is bounded by its bound on a closed fundamental parallelogram.
- $f$ omits two values of $\CC$, for instance when $f(\CC)$ misses an open set ([[T-HWBWI|little Picard theorem]]).

If $f$ and $g$ are holomorphic on a domain $U$ and $f-g$ has a zero set with a limit point in $U$, then $f = g$ ([[T-SVF2W|identity principle]]).

:::

## Singularities

::: {.fact title="Classifying an isolated singularity"}
Let $f$ be holomorphic on a punctured disc about $z_0$.

- $z_0$ is [[D-BQLJV|removable]] if and only if $f$ is bounded near $z_0$.
- $z_0$ is a [[D-AUD6K|pole]] if and only if $\abs{f(z)}\to\infty$ as $z\to z_0$.
- $z_0$ is a [[D-AUD6K|pole of order $m$]] if and only if $f(z) = (z-z_0)^{-m}g(z)$ with $g$ holomorphic near $z_0$ and $g(z_0)\neq 0$, equivalently if $1/f$ has a zero of order $m$ at $z_0$, equivalently if the Laurent expansion at $z_0$ has lowest term of degree $-m$.
- $z_0$ is [[D-VKP6N|essential]] if and only if $\lim_{z\to z_0} f(z)$ exists neither in $\CC$ nor as $\infty$, equivalently if the Laurent expansion at $z_0$ has infinitely many terms of negative degree.
  Two sequences $z_k\to z_0$ along which $f$ has different limits show this.

A meromorphic function $f$ and its derivative $f'$ have the same poles, and at such a pole the order of $f'$ is one more than the order of $f$.

The three classifications are [@Ahl73, ch. 4, §3.1, Removable Singularities. Taylor's Theorem], whose Theorem 7 is the removable criterion $\lim(z-z_0)f(z)=0$, and [@Ahl73, ch. 4, §3.2, Zeros and Poles], which defines a pole by $f(z)\to\infty$, reads its order off the zero of $1/f$ and off the lowest Laurent term, and calls the remaining case essential. The two-sequence test is the definition read negatively, and the statement about $f'$ follows by differentiating the factorisation $f=(z-z_0)^{-m}g$ with $g(z_0)\neq0$.
:::

::: {.fact}
If $h$ has an essential singularity at $z_0$, then by the [[T-DDOWW|great Picard theorem]], in every punctured neighborhood of $z_0$, $h$ takes every value of $\CC$ infinitely often with at most one exception.

:::

## Zeros

::: {.fact}
Let $f$ be holomorphic near $z_0$.

- $f$ has a zero of order $n$ at $z_0$ if and only if $f^{(k)}(z_0) = 0$ for $0\leq k<n$ and $f^{(n)}(z_0) \neq 0$.
- If $f(z_0)\neq 0$, then $f$ is nonzero on a neighborhood of $z_0$ by continuity.
- If $f(z_0) = 0$ and $f$ is not identically zero near $z_0$, then $f$ is nonzero on a punctured neighborhood of $z_0$.
- Dividing by a finite Blaschke product with the same zeros in $\DD$ gives a function without zeros in $\DD$ with the same modulus on $\bd\DD$.
- Zeros in a region are counted by [[T-CJCKL|Rouché's theorem]] and [[T-JXDQT|the argument principle]].

:::

## Estimates

::: {.fact}
\envlist

- For $\abs a\neq \abs b$, the reverse triangle inequality gives
$$
{1\over \abs{a\pm b}} \leq {1\over \abs{\abs{a} - \abs{b} } }.
$$
- [[T-LA2UI|The Cauchy integral formula]] bounds $\abs{f}$ at an interior point by an integral of $\abs f$ over the curve.
- [[T-22RQZ|Cauchy's inequalities]] bound the derivatives, $\abs{f^{(n)}(z_0)} \leq n!M/R^n$ for $M = \max_{\abs{z-z_0} = R}\abs f$.
- If $u_n$ are harmonic on a bounded domain $U$, continuous on $\bar U$, and $u_n$ converges uniformly on $\bd U$, then $u_n$ converges uniformly on $\bar U$, by the maximum principle applied to $u_n - u_m$.
- For $f\colon[a,b]\to\RR$ differentiable with $\abs{f'} \leq M$, the mean value theorem gives $\abs{f(x) - f(y)} \leq M\abs{x-y}$.
- If $h$ is holomorphic on $\DD$ with $\abs h\leq 1$ and $h(0) = 0$, then $\abs{h(z)}\leq\abs z$ by the [[T-DAETF|Schwarz lemma]].

The first inequality is the reverse triangle inequality of [@Ahl73, ch. 1, §1.5, Inequalities]; the fourth is the maximum principle applied to the harmonic difference, [@Ahl73, ch. 4, §6, Theorem 23]; the fifth is the mean value theorem, [@Rud76, ch. 5, Theorem 5.10], applied to each coordinate of $f$.
:::

::: {.example}
In the criterion that a zero-free $f$ with $\abs f$ constant on $\bd U$ is constant, the hypothesis that $f$ has no zeros is necessary: $f(z) = z$ has $\abs f = 1$ on $\bd\DD$ and is not constant.

:::

## Polynomials

::: {.fact}
An entire function $f$ is a polynomial if and only if $f^{(n)} = 0$ for all sufficiently large $n$, if and only if $f$ has a pole or a removable singularity at $\infty$.
Cauchy's inequality shows $f^{(n)} = 0$ for $n>d$ when $\abs{f(z)}\leq C\abs z^d$ for large $\abs z$.

The three conditions are equivalent because a function with a removable singularity or a pole at $\infty$ has the growth $\abs{f(z)}\le C\abs z^d$ there, which is the hypothesis of the Cauchy-inequality argument displayed; and an entire function whose $n$-th derivative vanishes for all large $n$ has a Taylor series that terminates, so it is a polynomial. The inequality used is [[T-22RQZ|Cauchy's inequality]].
:::
