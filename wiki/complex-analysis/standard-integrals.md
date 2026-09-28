---
title: Standard integrals
order: 8
---

# Standard integrals

Evaluations of standard real integrals by residues, each with its contour and the estimates for the added pieces.
The contour cases are described on [[complex-analysis/residues-and-contours/which-contour-do-i-close|Which contour do I close?]].

## $\displaystyle\int_\RR {\dx \over 1+x^2} = \pi$

**Contour.** Semicircle in $\HH$.

**Arc.** The ML estimate, since the integrand is $\bigo(1/R^2)$.

**Residues.** A simple pole at $z=i$ with residue $1/2i$, so the integral is $2\pi i \cdot {1\over 2i} = \pi$.

The same contour applies to every rational integrand whose denominator has no real zeros and degree at least two more than the numerator.

## $\displaystyle\int_\RR {\cos x \over 1+x^2} \dx = {\pi \over e}$

**Contour.** Semicircle in $\HH$, integrating $e^{iz}/(1+z^2)$ and taking real parts.

**Arc.** Jordan's lemma, or the ML estimate, since $\abs{e^{iz}}\leq 1$ on $\HH$ and $1/(1+z^2) = \bigo(1/R^2)$; for a denominator of degree one more than the numerator, only Jordan's lemma applies.

**Residues.** $\Res_{z=i} {e^{iz}\over 1+z^2} = {e^{-1}\over 2i}$, giving $2\pi i \cdot {e^{-1}\over 2i} = \pi/e$.

## $\displaystyle\int_\RR {\sin x \over x}\dx = \pi$

**Contour.** Semicircle in $\HH$, indented above the pole at the origin, integrating $e^{iz}/z$.

**Arcs.** Jordan's lemma on the large arc; the small clockwise half-circle contributes $-i\pi\Res_{z=0} (e^{iz}/z) = -i\pi$ in the limit.

**Residues.** $e^{iz}/z$ has no pole inside the indented contour, so the closed integral is zero, leaving
$$
\operatorname{PV}\int_\RR {e^{ix}\over x}\dx = i\pi
,$$
and taking imaginary parts gives $\pi$.
The principal value is needed for $e^{ix}/x$, whose real part $\cos x/x$ is not integrable near $0$; the integral of $\sin x/x$ converges as an improper integral, and $\int_\RR \abs{\sin x / x}\dx$ diverges.

## $\displaystyle\int_0^\infty {\dx \over 1+x^n} = {\pi/n \over \sin(\pi/n)}$

**Contour.** The sector of angle $2\pi/n$ bounded by $[0,R]$, the arc, and $\zeta_n[0,R]$, where $\zeta_n\coloneqq e^{2\pi i/n}$.

**Arc.** The ML estimate, for $n\geq 2$.

**Rays.** The integrand satisfies $f(\zeta_n z) = f(z)$, so the ray $\zeta_n[0,R]$, traversed toward $0$, contributes $-\zeta_n\int_0^R f$, giving
$$
(1-\zeta_n)\int_0^\infty f = 2\pi i \Res_{z = e^{i\pi/n}} f
,$$
and the single enclosed pole is at $e^{i\pi/n}$.

## $\displaystyle\int_0^\infty {x^{a-1} \over 1+x}\dx = {\pi \over \sin(\pi a)}, \quad 0 < a < 1$

**Contour.** Keyhole about the cut $[0,\infty)$, with $\arg z \in (0,2\pi)$.

**Arcs.** The large circle contributes $\bigo(R^{a-1})\to 0$ by the ML estimate, and the small circle $\bigo(\varepsilon^{a})\to 0$ because $a > 0$.

**Edges.** Below the cut the integrand carries the factor $e^{2\pi i(a-1)} = e^{2\pi i a}$, and that edge is traversed toward $0$, so
$$
\qty{1 - e^{2\pi i a}}\int_0^\infty {x^{a-1}\over 1+x}\dx = 2\pi i \Res_{z=-1} {z^{a-1}\over 1+z} = 2\pi i\, e^{i\pi(a-1)} = -2\pi i\, e^{i\pi a}
,$$
and dividing by $1-e^{2\pi i a} = -2i\,e^{i\pi a}\sin(\pi a)$ gives $\pi/\sin(\pi a)$.

## $\displaystyle\int_0^{2\pi} {\dtheta \over a + b\cos\theta} = {2\pi \over \sqrt{a^2-b^2}}, \quad a > \abs b$

**Contour.** The unit circle.

**Substitution.** $z = e^{i\theta}$, $\cos\theta = (z+z\inv)/2$, $\dtheta = \dz/iz$, turning the integral into
$$
\oint_{\abs z = 1} {2\,\dz \over i\qty{bz^2 + 2az + b}}
.$$
**Residues.** For $b\neq 0$, the roots of $bz^2+2az+b$ are $z_\pm = \qty{-a\pm\sqrt{a^2-b^2}}/b$, with product $1$, and only $z_+$ lies in the disc.
The residue of the integrand at $z_+$ is $2/\bigl(ib(z_+-z_-)\bigr) = 1/\bigl(i\sqrt{a^2-b^2}\bigr)$, and multiplying by $2\pi i$ gives the value; for $b=0$ the integral is $2\pi/a$.

## $\displaystyle\int_0^\infty {\log x \over 1+x^2}\dx = 0$

**Contour.** Semicircle in $\HH$ indented at the origin, integrating $\log z/(1+z^2)$ with $\arg z \in (-\pi/2, 3\pi/2)$.

**Result.** On the negative axis $\log z = \ln\abs z + i\pi$, so the contour gives
$$
2\int_0^\infty {\ln x \over 1+x^2}\dx + i\pi\int_0^\infty{\dx\over 1+x^2} = 2\pi i\Res_{z=i}{\log z\over 1+z^2} = \frac{i\pi^2}{2}
,$$
whose real part gives $0$ and whose imaginary part gives $\int_0^\infty {\dx\over 1+x^2} = \pi/2$.
The substitution $x\mapsto 1/x$ also shows that the integral equals its own negative.

## $\displaystyle\int_0^\infty \sin(x^2)\dx = \int_0^\infty \cos(x^2)\dx = \frac12\sqrt{\pi\over 2}$

**Contour.** The sector of angle $\pi/4$, integrating $e^{iz^2}$.

**Arc.** On $z = Re^{it}$, $\abs{e^{iz^2}} = e^{-R^2\sin 2t}$, and $\sin 2t \geq 4t/\pi$ on $[0,\pi/4]$ bounds the arc integral by $\pi/(4R)$.

**Rays.** On the ray $\arg z = \pi/4$, $iz^2 = -r^2$, so that ray contributes $-e^{i\pi/4}\int_0^\infty e^{-r^2}\dr = -e^{i\pi/4}\sqrt\pi/2$ in the limit.
No pole is enclosed, so $\int_0^\infty e^{ix^2}\dx = e^{i\pi/4}\sqrt\pi/2$, and taking real and imaginary parts gives the value.

## Added pieces that reproduce the integral

For the sector and keyhole contours, a boundary piece other than the real segment is a constant multiple of the original integral, and the value comes from solving the resulting linear equation; for the other contours, the added pieces tend to $0$ or to a multiple of a residue.
