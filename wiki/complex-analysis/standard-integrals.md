---
title: Standard integrals
order: 8
---

# Standard integrals

Each integral below is evaluated on the contour that suits the shape of its integrand; the decision procedure is on [[complex-analysis/residues-and-contours/which-contour-do-i-close|Which contour do I close?]].
The value comes from [[T-HRPNO|the residue theorem]] once the boundary pieces are known: for the sector and keyhole contours a boundary piece other than the real segment is a constant multiple of the original integral, and the value solves the resulting linear equation, while for the other contours the added pieces tend to $0$ or to a multiple of a residue.

## Rational and trigonometric integrands

::: {.example title="$\displaystyle\int_\RR {\dx\over 1+x^2} = \pi$"}
Close the contour with the semicircle of radius $R$ in $\HH$.
The arc contributes $\bigo(1/R)$ by the [[T-SFXI7|ML estimate]], so it vanishes in the limit.
The integrand has a simple pole at $z=i$ with residue $1/(2i)$, and $2\pi i\cdot{1\over 2i} = \pi$.
:::

::: {.proposition title="Rational integrands with denominator two degrees higher"}
If $f = p/q$ is rational, $q$ is free of real zeros, and $\deg q\geq\deg p+2$, then
$$
\int_\RR f(x)\dx = 2\pi i\sum_{z_0\in\HH}\Res_{z=z_0}f,
$$
the sum over the [[D-AUD6K|poles]] in $\HH$, the arc integral being $\bigo(R^{-1})$ by the [[T-SFXI7|ML estimate]].

This is item 2 of [@Ahl73, ch. 4, §5.3], which states the criterion and that the integral over the semicircle tends to $0$.
:::

::: {.example title="$\displaystyle\int_\RR {\cos x\over 1+x^2}\dx = {\pi\over e}$"}
Integrate $e^{iz}/(1+z^2)$ over the semicircle in $\HH$ and take real parts.
The arc vanishes by [[T-ZO5UU|Jordan's lemma]], or by the [[T-SFXI7|ML estimate]] together with $\abs{e^{iz}}\leq 1$ on $\HH$ and $1/(1+z^2) = \bigo(1/R^2)$; for a denominator of degree one more than the numerator only Jordan's lemma applies.
The residue at $z=i$ is $e^{-1}/(2i)$, so the integral is $2\pi i\cdot e^{-1}/(2i) = \pi/e$.
:::

::: {.example title="$\displaystyle\int_\RR {\sin x\over x}\dx = \pi$"}
Integrate $e^{iz}/z$ over the semicircle in $\HH$ indented above the pole at the origin.
[[T-ZO5UU|Jordan's lemma]] kills the large arc, and the small clockwise half-circle contributes $-i\pi\Res_{z=0}(e^{iz}/z) = -i\pi$ in the limit.
No pole lies inside the indented contour, so the closed integral vanishes and
$$
\PV\int_\RR {e^{ix}\over x}\dx = i\pi,
$$
whose imaginary part is $\pi$.
The [[D-PV4RQ|principal value]] is needed for $e^{ix}/x$, whose real part $\cos x/x$ is not integrable near $0$; the integral of $\sin x/x$ converges as an improper integral, while $\int_\RR \abs{\sin x/x}\dx$ diverges.
:::

::: {.example title="$\displaystyle\int_0^{2\pi} {\dtheta\over a+b\cos\theta} = {2\pi\over\sqrt{a^2-b^2}}$, $a>\abs b$"}
Integrate over the unit circle, substituting $z = e^{i\theta}$, $\cos\theta = (z+\inverseof z)/2$, and $\dtheta = \dz/iz$, which turns the integral into
$$
\oint_{\abs z = 1} {2\,\dz\over i\qty{bz^2+2az+b}}.
$$
For $b\neq 0$ the roots of $bz^2+2az+b$ are $z_\pm = \qty{-a\pm\sqrt{a^2-b^2}}/b$, their product is $1$, and only $z_+$ lies in the disc.
The residue of the integrand at $z_+$ is $2/\bigl(ib(z_+-z_-)\bigr) = 1/\bigl(i\sqrt{a^2-b^2}\bigr)$, and multiplying by $2\pi i$ gives the value; for $b=0$ the integral is $2\pi/a$.
:::

## Integrands with a branch cut

::: {.example title="$\displaystyle\int_0^\infty {x^{a-1}\over 1+x}\dx = {\pi\over\sin(\pi a)}$, $0<a<1$"}
Take the keyhole contour about the cut $[0,\infty)$ with $\arg z\in(0,2\pi)$.
The ML estimate bounds the large circle by $\bigo(R^{a-1})\to 0$ and the small circle by $\bigo(\varepsilon^{a})\to 0$, since $a>0$.
Below the cut the integrand carries the factor $e^{2\pi i(a-1)} = e^{2\pi i a}$, and that edge is traversed toward $0$, so
$$
\qty{1-e^{2\pi i a}}\int_0^\infty {x^{a-1}\over 1+x}\dx = 2\pi i\Res_{z=-1}{z^{a-1}\over 1+z} = 2\pi i\,e^{i\pi(a-1)} = -2\pi i\,e^{i\pi a},
$$
and dividing by $1-e^{2\pi i a} = -2i\,e^{i\pi a}\sin(\pi a)$ gives $\pi/\sin(\pi a)$.
:::

::: {.example title="$\displaystyle\int_0^\infty {\log x\over 1+x^2}\dx = 0$"}
Take the semicircle in $\HH$ indented at the origin and integrate $\log z/(1+z^2)$ with $\arg z\in(-\pi/2,3\pi/2)$.
On the negative axis $\log z = \ln\abs z+i\pi$, so the contour gives
$$
2\int_0^\infty {\ln x\over 1+x^2}\dx + i\pi\int_0^\infty{\dx\over 1+x^2} = 2\pi i\Res_{z=i}{\log z\over 1+z^2} = {i\pi^2\over 2},
$$
whose real part gives $0$ and whose imaginary part gives $\int_0^\infty \dx/(1+x^2) = \pi/2$.
The substitution $x\mapsto 1/x$ also shows that the integral equals its own negative.
:::

## A sector contour

::: {.example title="$\displaystyle\int_0^\infty {\dx\over 1+x^n} = {\pi/n\over\sin(\pi/n)}$, $n\geq 2$"}
Take the sector of angle $2\pi/n$ bounded by $[0,R]$, the arc, and $\zeta_n[0,R]$, where $\zeta_n\coloneqq e^{2\pi i/n}$.
The arc contributes nothing by the ML estimate, for $n\geq 2$.
The integrand satisfies $f(\zeta_n z) = f(z)$, so the ray $\zeta_n[0,R]$, traversed toward $0$, contributes $-\zeta_n\int_0^R f$, and
$$
(1-\zeta_n)\int_0^\infty f = 2\pi i\Res_{z = e^{i\pi/n}} f,
$$
the only enclosed pole being $z_0 = e^{i\pi/n}$, where $z_0^n = -1$ and the residue of $1/(1+z^n)$ is $1/(nz_0^{n-1}) = -z_0/n$.
Dividing, $\int_0^\infty \dx/(1+x^n) = -2\pi i\,z_0/\bigl(n(1-\zeta_n)\bigr) = \pi/\bigl(n\sin(\pi/n)\bigr)$, since $1-\zeta_n = -2i\,e^{i\pi/n}\sin(\pi/n)$.
:::

::: {.example title="$\displaystyle\int_0^\infty {x^{a-1}\over 1+x^n}\dx = {\pi/n\over\sin(\pi a/n)}$, $0<a<n$"}
Take the same sector of angle $2\pi/n$ and, on it, the branch of $z^{a-1}$ with $\arg z\in[0,2\pi/n]$.
On the ray $z = \zeta_n t$ one has $\dz = \zeta_n\dt$ and $(\zeta_n t)^{a-1} = e^{2\pi i(a-1)/n}t^{a-1}$, so that ray, traversed toward $0$, contributes $-e^{2\pi i a/n}\int_0^R x^{a-1}/(1+x^n)\dx$, and
$$
\qty{1-e^{2\pi i a/n}}\int_0^\infty{x^{a-1}\over 1+x^n}\dx = 2\pi i\Res_{z=z_0}{z^{a-1}\over 1+z^n},
$$
with $z_0 = e^{i\pi/n}$ the only enclosed pole.
There the residue is $z_0^{a-1}/(nz_0^{n-1}) = z_0^{a-n}/n = -e^{i\pi a/n}/n$, and $1-e^{2\pi i a/n} = -2ie^{i\pi a/n}\sin(\pi a/n)$, so the integral is $\pi/\bigl(n\sin(\pi a/n)\bigr)$.
The case $a = n$ is excluded, and there the integral diverges logarithmically, the integrand being asymptotic to $1/x$.
:::

::: {.example title="$\displaystyle\int_0^\infty \sin(x^2)\dx = \int_0^\infty \cos(x^2)\dx = \frac12\sqrt{\pi\over 2}$"}
Take the sector of angle $\pi/4$ and integrate $e^{iz^2}$.
On $z = Re^{it}$ one has $\abs{e^{iz^2}} = e^{-R^2\sin 2t}$, and $\sin 2t\geq 4t/\pi$ on $[0,\pi/4]$ bounds the arc integral by $\pi/(4R)$.
On the ray $\arg z = \pi/4$ one has $iz^2 = -r^2$, so that ray contributes $-e^{i\pi/4}\int_0^\infty e^{-r^2}\dr = -e^{i\pi/4}\sqrt\pi/2$ in the limit.
No pole is enclosed, so $\int_0^\infty e^{ix^2}\dx = e^{i\pi/4}\sqrt\pi/2$, and taking real and imaginary parts gives the value.
:::
