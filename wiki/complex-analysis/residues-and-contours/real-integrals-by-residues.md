---
title: Real integrals by residues
order: 40
topics: [Contour Integration]
---

# Real integrals by residues

Worked evaluations and exercises, grouped by the contour cases on [[complex-analysis/residues-and-contours/which-contour-do-i-close|Which contour do I close?]].

## Rational, superlinear decay

Upper semicircle; the arc integral tends to $0$ by the ML estimate.

[[E-IZKCV]]
[[E-UDYDX]]
[[E-AKNDW]]
[[E-AKF2O]]
[[E-JZNWV]]
[[E-SPIVX]]
[[E-CFHC4]]
[[E-JK5PG]]

## Rational against $e^{iz}$

Upper semicircle applied to $f(z)e^{iz}$; the arc integral tends to $0$ by Jordan's lemma.

::: {.example}
For $f(z) \coloneqq {e^{iz} \over 1 + z^2}$ on the upper semicircle $\gamma_R$, $z = Re^{it}$ with $R>1$, the factor $1/(1+z^2)$ satisfies
$$
\begin{aligned}
\sup_{z\in \gamma_R} \abs{f(z)}
&= \max_{t\in [0, \pi]} \abs{1 \over 1 + (Re^{it})^2 } \\
&= {1\over R^2 - 1}
\end{aligned},$$
so Jordan's lemma bounds the arc integral by $\pi/(R^2-1)$.

:::

[[E-AXBZQ]]
[[E-FRWVZ]]
[[E-2RKYE]]

## No clear decay

Sectors and rectangles, determined by a rotation or translation symmetry of the integrand.

[[E-YYRZX]]
[[E-AIQEU]]

## Singularities on the line: principal values

Semicircles indented above each real simple pole, each of which contributes $i\pi$ times its residue.

[[E-ZGZYQ]]
[[E-DUK6M]]

## Rational functions of $\cos$ and $\sin$

The unit circle, through $z = e^{i\theta}$.

::: {.example}
For real $a$ with $\abs a<1$, the only pole of the integrand inside $S^1$ is $z=a$:
$$
\int_{0}^{2 \pi} \frac{\dtheta}{1+a^{2}-2 a \cos \theta}=\int_{S^{1}} \frac{i \dz}{(z-a)(a z-1)}=2 \pi i\left(i /\left(a^{2}-1\right)\right)=\frac{2 \pi}{1-a^{2}}
.$$

:::

[[E-BEIHP]]
[[E-Z4JCZ]]
[[E-JKROF]]

## Branch cuts: logarithms

[[E-FJJA6]]
[[E-EOMTI]]
[[E-KC6DS]]
[[E-HHSCS]]
[[E-22P3T]]
[[E-Z66NC]]

## Branch cuts: powers

::: {.example}
For $-1<a<1$, with the branch $\arg z\in(0,2\pi)$ on the keyhole contour, the poles $i$ and $-i$ have $z^a = e^{\pi i a/2}$ and $e^{3\pi i a/2}$.
Setting $\omega \coloneqq e^{\pi i a \over 2}$,
$$
\int_{0}^{\infty} \frac{x^{a}}{1+x^{2}} \dx =
\frac{2\pi i}{1-e^{2\pi i a}}\left(\frac{\omega}{2i}-\frac{\omega^{3}}{2i}\right)=\pi \frac{\omega-\omega^{3}}{1-\omega^{4}}=\frac{\pi}{\omega+\omega^{-1}}=\frac{\pi}{2 \cos (\pi a / 2)}
,$$
which for $a = 1/3$ is $\pi/\sqrt 3$.

:::

[[E-YAMX6]]
[[E-2HIKG]]

## Square roots and slits

::: {.concept}
For $f(z) = \sqrt{(z-z_1)(z-z_2)\cdots(z-z_n)}$, a branch exists on the complement of slits that prevent closed curves from winding around an odd number of the branch points $z_k$; for $n$ odd, $z=\infty$ is also a branch point.

Continuation once around a branch point multiplies $\sqrt{\cdot}$ by $-1$: for $f(z) = \sqrt z$ and $\gamma(t) = e^{2\pi i t}$ on $[0,1]$, $f(\gamma(0)) = \sqrt z$ while $f(\gamma(1)) = \sqrt{e^{2\pi i}z} = e^{i\pi}\sqrt z = -\sqrt z$.

:::

[[E-L3MG4]]
[[E-EBRU5]]
[[E-GPCW2]]
[[E-XYEP4]]
[[E-KZV2Z]]
