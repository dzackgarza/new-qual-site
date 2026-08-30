---
title: Standard integrals
order: 8
---

# Standard integrals

The integrals that recur, each with the contour it wants and the estimate that kills the added arc.
Choosing among them is [[complex-analysis/residues-and-contours/which-contour-do-i-close|Which contour do I close?]]; this page is the answers.

## $\displaystyle\int_\RR {\dx \over 1+x^2} = \pi$

**Contour:** semicircle in $\HH$.
**Arc:** ML, since the integrand is $\bigo(1/R^2)$.
**Residues:** a simple pole at $z=i$ with $\Res = 1/2i$, so the integral is $2\pi i \cdot {1\over 2i} = \pi$.

The template for every rational integrand with denominator degree at least two more than the numerator.

## $\displaystyle\int_\RR {\cos x \over 1+x^2} \dx = {\pi \over e}$

**Contour:** semicircle in $\HH$, integrating $e^{iz}/(1+z^2)$ and taking real parts.
**Arc:** Jordan's lemma.
ML also suffices here, but not once the denominator drops to degree one.
**Residues:** $\Res_{z=i} {e^{iz}\over 1+z^2} = {e^{-1}\over 2i}$, giving $2\pi i \cdot {e^{-1}\over 2i} = \pi/e$.

## $\displaystyle\int_\RR {\sin x \over x}\dx = \pi$

**Contour:** semicircle in $\HH$, indented over the pole at the origin, integrating $e^{iz}/z$.
**Arc:** Jordan's lemma on the large arc; the small arc does *not* vanish.
**The point:** $e^{iz}/z$ has no pole inside the indented contour, so the closed integral is zero.
The indentation contributes $-i\pi\Res_{z=0} = -i\pi$, leaving
\[
\operatorname{PV}\int_\RR {e^{ix}\over x}\dx = i\pi
,\]
and taking imaginary parts gives $\pi$.
The principal value is not a technicality here: $\int \abs{\sin x / x}$ diverges.

## $\displaystyle\int_0^\infty {\dx \over 1+x^n} = {\pi/n \over \sin(\pi/n)}$

**Contour:** the sector of angle $2\pi/n$, from $[0,R]$ along the arc to $\zeta_n[0,R]$.
**Arc:** ML, for $n\geq 2$.
**Why a sector:** the integrand satisfies $f(\zeta_n z) = f(z)$, so the returning ray reproduces the integral scaled by $\zeta_n$, giving
\[
(1-\zeta_n)\int_0^\infty f = 2\pi i \Res_{z = e^{i\pi/n}} f
,\]
and the single enclosed pole is at $e^{i\pi/n}$.

## $\displaystyle\int_0^\infty {x^{a-1} \over 1+x}\dx = {\pi \over \sin(\pi a)}, \quad 0 < a < 1$

**Contour:** keyhole about the cut $[0,\infty)$, with $\arg z \in (0,2\pi)$.
**Arcs:** the large circle by ML, the small one because $a > 0$.
**Why the edges do not cancel:** below the cut the integrand carries $e^{2\pi i(a-1)}$, so
\[
\qty{1 - e^{2\pi i a}}\int_0^\infty {x^{a-1}\over 1+x}\dx = 2\pi i \Res_{z=-1} = 2\pi i\, e^{i\pi(a-1)}
,\]
and the algebra collapses to $\pi/\sin(\pi a)$.

## $\displaystyle\int_0^{2\pi} {\dtheta \over a + b\cos\theta} = {2\pi \over \sqrt{a^2-b^2}}, \quad a > \abs b$

**Contour:** the unit circle, already closed.
**Substitution:** $z = e^{i\theta}$, $\cos\theta = (z+z\inv)/2$, $\dtheta = \dz/iz$, turning the integral into
\[
\oint_{\abs z = 1} {2\,\dz \over i\qty{bz^2 + 2az + b}}
.\]
**Residues:** of the two roots of $bz^2+2az+b$ only $z_- = \qty{-a+\sqrt{a^2-b^2}}/b$ lies in the disc.

## $\displaystyle\int_0^\infty {\log x \over 1+x^2}\dx = 0$

**Contour:** semicircle in $\HH$ indented at the origin, integrating $\log z/(1+z^2)$ with $\arg z \in (-\pi/2, 3\pi/2)$.
**Why zero:** the substitution $x\mapsto 1/x$ maps the integral to its own negative, which is the fastest argument and worth trying before any contour.
The contour proof also delivers $\int_0^\infty {\dx\over 1+x^2} = \pi/2$ as the imaginary part.

## $\displaystyle\int_0^\infty \sin(x^2)\dx = \int_0^\infty \cos(x^2)\dx = \frac12\sqrt{\pi\over 2}$

**Contour:** the sector of angle $\pi/4$, integrating $e^{iz^2}$.
**Arc:** Jordan's lemma in the form for $e^{iz^2}$, using $\sin t \geq 2t/\pi$ on $[0,\pi/2]$.
**Why $\pi/4$:** on the ray $\arg z = \pi/4$ the exponent $iz^2$ becomes real and negative, so the returning integral is the Gaussian $\int_0^\infty e^{-r^2}\dr = \sqrt\pi/2$.
No pole is enclosed, so the two rays balance.

## What they have in common

Each is one of the cases on the recognition page, and in every one the work splits the same way: choose the curve so that the far side either vanishes or reproduces the integral, then count residues.
The cases where the far side *reproduces* the integral rather than vanishing are the sector and the keyhole, and those are the ones worth memorizing, since there the answer comes from an algebraic identity rather than an estimate.
