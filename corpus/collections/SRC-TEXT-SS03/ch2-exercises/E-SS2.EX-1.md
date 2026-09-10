---
schema: qual/card@1
id: E-SS2.EX-1
kind: problem
title: "SS 2.1: The Fresnel integrals"
classification:
  areas:
  - complex-analysis
  topics: ["Cauchy's Theorem", 'Contour Integration', 'Residues']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: exercise
1. Prove that

$$
\int_ {0} ^ {\infty} \sin (x ^ {2}) d x = \int_ {0} ^ {\infty} \cos (x ^ {2}) d x = \frac {\sqrt {2 \pi}}{4}.
$$

These are the Fresnel integrals.
Here, $\int _ { 0 } ^ { \infty }$ is interpreted as lim $R {  } { \infty } \int _ { 0 } ^ { R }$

[Hint: Integrate the function $e ^ { - z ^ { 2 } }$ over the path in Figure 14. Recall that $\textstyle \int _ { - \infty } ^ { \infty } e ^ { - x ^ { 2 } } d x = { \sqrt { \pi } } . ]$

Figure 14. The contour in Exercise 1
:::

::: solution
For $R>0$, integrate the entire function $e^{-z^2}$ around the positively oriented boundary of the sector
\[
0\le |z|\le R,
\qquad
0\le \arg z\le \frac{\pi}{4}.
\]
Cauchy's theorem gives
\[
\int_0^R e^{-x^2}\,dx
+\int_{\Gamma_R}e^{-z^2}\,dz
-e^{i\pi/4}\int_0^R e^{-ir^2}\,dr=0,
\tag{1}
\]
where $\Gamma_R$ is the circular arc $z=Re^{i\theta}$, $0\le\theta\le\pi/4$.

We first show that the arc integral tends to $0$. Since
\[
|e^{-z^2}|=e^{-R^2\cos(2\theta)},
\]
we have, after putting $u=\pi/4-\theta$,
\[
\left|\int_{\Gamma_R}e^{-z^2}\,dz\right|
\le R\int_0^{\pi/4}e^{-R^2\sin(2u)}\,du.
\]
For $0\le u\le\pi/4$, concavity of $\sin$ on $[0,\pi/2]$ gives
\[
\sin(2u)\ge \frac{4u}{\pi}.
\]
Therefore
\[
\left|\int_{\Gamma_R}e^{-z^2}\,dz\right|
\le R\int_0^{\pi/4}e^{-4R^2u/\pi}\,du
\le \frac{\pi}{4R}\longrightarrow0.
\tag{2}
\]

Letting $R\to\infty$ in (1), using
\[
\int_0^\infty e^{-x^2}\,dx=\frac{\sqrt\pi}{2},
\]
and (2), yields
\[
\frac{\sqrt\pi}{2}
=e^{i\pi/4}\int_0^\infty e^{-ir^2}\,dr.
\]
Hence
\[
\int_0^\infty e^{-ir^2}\,dr
=e^{-i\pi/4}\frac{\sqrt\pi}{2}
=\frac{\sqrt{2\pi}}{4}(1-i).
\]
Taking real and imaginary parts gives
\[
\int_0^\infty \cos(x^2)\,dx=\frac{\sqrt{2\pi}}{4},
\qquad
-\int_0^\infty \sin(x^2)\,dx=-\frac{\sqrt{2\pi}}{4}.
\]
Thus
\[
\boxed{
\int_0^\infty \sin(x^2)\,dx
=
\int_0^\infty \cos(x^2)\,dx
=rac{\sqrt{2\pi}}{4}}
\]
as required.
:::
