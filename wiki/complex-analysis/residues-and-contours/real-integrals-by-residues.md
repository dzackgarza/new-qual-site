---
title: Real integrals by residues
order: 40
problems:
  topics: [Contour Integration]
---

# Real integrals by residues

The worked cases.
[[complex-analysis/residues-and-contours/which-contour-do-i-close|Which contour do I close?]] decides which one a given integral is; this page carries the computations and the drill.

## Rational, superlinear decay

The semicircle, with the arc killed by ML.

[[E-IZKCV]]
[[E-UDYDX]]
[[E-AKNDW]]
[[E-AKF2O]]
[[E-JZNWV]]
[[E-SPIVX]]
[[E-CFHC4]]
[[E-JK5PG]]

## Rational, linear or sublinear decay

The same semicircle, rewritten through $e^{iz}$ so that Jordan's lemma applies.

:::{.example}
For $f(z) \da {e^{iz} \over 1 + z^2}$ with $z \neq \pm i$, integrating over $\RR$ uses the semicircular contour $z = Re^{it}$ and the bound
\[
\sup_{z\in \gamma_R} \abs{f(z)}
&= \max_{t\in [0, \pi]} \abs{1 \over 1 + (Re^{it})^2 } \\
&= {1\over R^2 - 1}
.\]

:::

[[E-AXBZQ]]
[[E-FRWVZ]]
[[E-2RKYE]]

## No clear decay

Sectors and rectangles, chosen by the symmetry the integrand has.

[[E-YYRZX]]
[[E-AIQEU]]

## Singularities on the line: principal values

Indented contours, with each real pole contributing half its residue.

[[E-ZGZYQ]]
[[E-DUK6M]]

## Rational functions of $\cos$ and $\sin$

The unit circle, through $z = e^{i\theta}$.

:::{.example}
\[
\int_{0}^{2 \pi} \frac{\dtheta}{1+a^{2}-2 a \cos \theta}=\int_{S^{1}} \frac{i \dz}{(z-a)(a z-1)}=2 \pi i\left(i /\left(a^{2}-1\right)\right)=\frac{2 \pi}{1-a^{2}}
.\]

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

:::{.example}
Setting $\omega \da e^{\pi i a \over 2}$,
\[
\int_{0}^{\infty} \frac{x^{a}}{1+x^{2}} \dx =
\frac{\pi\left(i^{a}-(-i)^{a}\right)}{\left(1-1^{a}\right)}=\pi \frac{\omega-\omega^{3}}{1-\omega^{4}}=\frac{\pi}{\omega+\omega^{-1}}=\frac{\pi}{2 \cos (\pi a / 2)}
,\]
which for $a = 1/3$ is $\pi/\sqrt 3$.

:::

[[E-YAMX6]]
[[E-2HIKG]]

## Square roots and slits

:::{.concept}
For $f(z) = \sqrt{(z-z_1)(z-z_2)\cdots(z-z_n)}$, the slits must disallow winding around an odd number of the branch points $z_k$, and $z=\infty$ may itself be a branch point.

The phase factor is $-1$: for $f(z) = \sqrt z$ and $\gamma(t) = e^{2\pi i t}$ on $[0,1]$, $f(\gamma(0)) = \sqrt z$ while $f(\gamma(1)) = \sqrt{e^{2\pi i}z} = e^{i\pi}\sqrt z = -\sqrt z$.

:::

[[E-L3MG4]]
[[E-EBRU5]]
[[E-GPCW2]]
[[E-XYEP4]]
[[E-KZV2Z]]
