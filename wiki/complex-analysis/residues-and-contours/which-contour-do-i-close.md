---
title: Which contour do I close?
order: 0
topics:
- Contour Integration
---

# Which contour do I close?

A real integral is evaluated by residues after it is written as a limit of integrals over closed curves.

The estimates for the added pieces are on [[complex-analysis/residues-and-contours/arc-estimates|Arc estimates]], and residue computations are on [[complex-analysis/residues-and-contours/computing-residues|Computing residues]].

## Integrals that need no residues

- If $f$ is holomorphic on a neighborhood of the closed region bounded by $\gamma$, then $\int_\gamma f = 0$ by Cauchy's theorem.

- If $f$ has a primitive $F$ on a neighborhood of $\gamma$, then $\int_\gamma f = F(\gamma(1)) - F(\gamma(0))$, which is $0$ for a closed curve.

- If $f(z) = g(z)/(z-a)^n$ with $g$ holomorphic inside and on a positively oriented simple closed curve $\gamma$ around $a$, the Cauchy integral formula gives $\int_\gamma {g(z) \over (z-a)^{n}} \dz = {2\pi i \over (n-1)!} g^{(n-1)}(a)$.

- For a parameterized curve $z\colon[a,b]\to\CC$, $\int_\gamma f \dz = \int_a^b f(z(t)) z'(t) \dt$; a circle about $z_0$ is $z = z_0 + re^{i\theta}$.

## Rational, decaying at least quadratically

**Integrand.** $\displaystyle\int_\RR f$ with $f = p/q$ rational, $q$ without real zeros, and $\deg q \geq \deg p + 2$; more generally $f = \bigo(1/\abs z^{1+\varepsilon})$ on the upper half plane.

**Contour.** The segment $[-R, R]$ followed by the upper semicircle $C_R = \theset{Re^{it} \st t \in [0,\pi]}$.

![Left: the segment from -R to R closed by the upper semicircle C_R, counterclockwise. Right: the segment closed by the lower semicircle, clockwise.](../../../../assets/assets/figures/2021-07-29_18-37-57.png)

**Arc estimate.** The ML estimate: $\abs{f} = \bigo(1/R^{2})$ on $C_R$ and $\length(C_R) = \pi R$, so the arc integral is $\bigo(1/R)$.

**Result.**
$$
\int_\RR f = 2\pi i \sum_{z_0 \in \HH} \Res_{z=z_0} f(z)
.$$

The sum is over poles in the open upper half plane.
Closing in the lower half plane gives a clockwise contour and $\int_\RR f = -2\pi i \sum_{\Im z_0<0} \Res_{z=z_0} f(z)$.

## Rational against a sine or cosine

**Integrand.** $\displaystyle\int_\RR f(x)\cos(ax) \dx$ or $\displaystyle\int_\RR f(x)\sin(ax)\dx$ with $a>0$, $f = p/q$ real rational, $q$ without real zeros, and $\deg q \geq \deg p + 1$.

**Contour.** The same semicircle, applied to $f(z)e^{iaz}$, with
$$
\int_\RR f(x)\cos(ax) \dx = \Re \int_\RR f(x)e^{iax}\dx, \qquad \int_\RR f(x)\sin(ax) \dx = \Im \int_\RR f(x)e^{iax}\dx
,$$
the integrals over $\RR$ taken as limits of integrals over $[-R,R]$.

**Arc estimate.** Jordan's lemma: $\abs{e^{iaz}} = e^{-a\Im z} \leq 1$ on the upper half plane, and $\abs{\int_{C_R} e^{iaz} f(z)\dz} \leq \pi M_R/a$ with $M_R = \sup_{C_R}\abs f = \bigo(1/R)$.
The functions $\cos(az)$ and $\sin(az)$ grow like $e^{aR}/2$ on $C_R$, which is why the integrand is rewritten with $e^{iaz}$.

For $e^{-iax}$ with $a>0$, the lower semicircle is used instead.
Along a vertical line $\Re z = a$, the same reasoning applies to $e^{\pm z}$: since $\abs{e^{z}} = e^{\Re z}$, an integrand with a factor $e^{z}$ is closed by a semicircle in the left half plane $\Re z<a$, and one with $e^{-z}$ in the right half plane.

## Rational in $\cos$ and $\sin$, over one period

**Integrand.** $\displaystyle\int_0^{2\pi} R(\cos\theta, \sin\theta) \dtheta$ with $R$ a rational function of two variables, finite on the unit circle.

**Contour.** The unit circle, by the substitution $z = e^{i\theta}$:
$$
\cos\theta = {z + \inverseof{z} \over 2}, \quad \sin\theta = {z - \inverseof{z} \over 2i}, \quad \dtheta = {\dz \over iz}
.$$
No pieces are added; the substitution writes the integral over $[0,2\pi]$ as an integral over $S^1$.

**Result.**
$$
\int_0^{2\pi} R(\cos\theta,\sin\theta) \dtheta = 2\pi i \sum_{\abs{z_0} < 1} \Res_{z=z_0} R\qty{ {z+\inverseof{z} \over 2}, {z - \inverseof{z} \over 2i} } {1 \over iz}
.$$

The factor $1/iz$ can contribute a pole at $z = 0$.

## A branch cut: a power $x^\alpha$

**Integrand.** $\displaystyle\int_0^\infty x^\alpha f(x)\dx$ with $f$ rational, without poles on $[0,\infty)$, $\deg f \leq -2$, and $\alpha\in(-1,1)$ nonintegral.

**Contour.** The keyhole around the cut along $[0,\infty)$, with the branch $\arg z \in (0, 2\pi)$ of $z^\alpha$.

![The keyhole contour: the circle C_R of radius R, the two edges of the cut along the positive real axis from r to R, and the small circle C_r of radius r about 0.](../../../../assets/assets/figures/2021-12-14_17-19-31.png)

**Estimates.** The large circle of radius $R$ contributes $\bigo(R^{\alpha-1})\to 0$ by the ML estimate, and the small circle of radius $\varepsilon$ contributes $\bigo(\varepsilon^{1+\alpha}) \to 0$ because $\alpha > -1$.

**Result.** Above the cut the integrand is $x^\alpha f(x)$; below it $\arg z = 2\pi$, so the integrand is $e^{2\pi i \alpha}x^\alpha f(x)$ and the edge is traversed from $\infty$ to $0$.
Hence
$$
\qty{1 - e^{2\pi i \alpha}} \int_0^\infty x^\alpha f(x) \dx = 2\pi i \sum \Res\qty{z^\alpha f(z)}
,$$
the sum over all poles of $f$.

## A branch cut: a logarithm

**Integrand.** $\displaystyle\int_0^\infty f(x)\log(x)\dx$, or $\displaystyle\int_0^\infty f(x)\dx$ for $f$ even computed through $\int f(z)\log z\dz$.

**Contour.** An indented semicircle, or the keyhole.

![The indented semicircle: the segment from -R to R with a small half-circle C_r of radius r above 0, closed by the upper semicircle C_R.](../../../../assets/assets/figures/2021-12-14_17-20-48.png)

![The contour gamma_{R,epsilon}: from -R to -epsilon, the half-circle of radius epsilon above 0, from epsilon to R, and the upper semicircle back to -R.](../../../../assets/assets/figures/2021-12-22_05-14-24.png)

**Limits used in the estimates.** With the branch $\arg z\in(0,2\pi)$, for $x>0$, and for $n\geq 1$ and $c\neq 0$,
$$
\lim_{\varepsilon \decreasesto 0} \log(x - i\varepsilon) = \ln(x) + 2\pi i, \qquad \lim_{x\to 0} {x\ln(x) \over x^n + c} = 0
.$$

**Rotated rays.** For $\zeta = e^{i\theta}$ and $g$ with $g(\zeta x) = g(x)$ for $x>0$, the integral of $\log(z)g(z)$ along the ray $z = \zeta x$ is
$$
\zeta\int_0^\infty \log(\zeta x)g(\zeta x) \dx = \zeta\int_0^\infty \ln(x)g(x)\dx + i\theta\,\zeta\int_0^\infty g(x)\dx
,$$
so a contour made of $[0,\infty)$ and this ray gives a linear relation involving $\int_0^\infty \ln(x)g(x)\dx$ and $\int_0^\infty g(x)\dx$.

## A pole on the real line

**Integrand.** $\displaystyle\int_\RR f$ where $f$ has simple poles on $\RR$.
The integral diverges, and the principal value is
$$
\operatorname{PV} \int_{-\infty}^{\infty} f(x) \dx = \lim_{R\to\infty}\lim_{\varepsilon \decreasesto 0}\qty{\int_{-R}^{x_{0}-\varepsilon} f + \int_{x_{0}+\varepsilon}^{R} f}
$$
for a single pole $x_0$, and analogously for several.

**Contour.** The semicircle, indented by a small half-circle above each real pole.
An indentation below a real pole $x_0$ instead puts $x_0$ inside the contour; the counterclockwise half-circle then contributes $+i\pi\Res_{z=x_0} f$, the residue sum gains $2\pi i\Res_{z=x_0} f$, and the result below is unchanged.

**Estimates.** The integral over the large arc tends to $0$ by the ML estimate when $f = \bigo(1/\abs z^{1+\varepsilon})$ on the upper half plane, and by Jordan's lemma when $f(z) = g(z)e^{iaz}$ with $a>0$ and $g = \bigo(1/\abs z)$.
By [[T-SSNLT]], an arc of angle $\theta$ about a simple pole contributes $i\theta \Res$ in the limit, so each clockwise half-circle contributes $-i\pi\Res$.

**Result.**
$$
\operatorname{PV} \int_\RR f = 2\pi i \sum_{z_0 \in \HH} \Res_{z=z_0} f + i\pi \sum_{x_0 \in \RR} \Res_{z=x_0} f
.$$

## Symmetry under rotation or translation: sectors and rectangles

**Integrand.** A function whose values on a rotated ray or a translated line are a constant multiple of its values on the real axis.

- If $f(\zeta z) = f(z)$ for $\zeta = e^{2\pi i/m}$, use the sector $\theset{0\leq\arg z\leq 2\pi/m,\ \abs z\leq R}$.
  If the arc integral tends to $0$, the ray $z = \zeta x$, traversed toward $0$, contributes $-\zeta\int_0^\infty f$, so $(1 - \zeta)\int_0^\infty f$ is $2\pi i$ times the sum of the residues in the sector.
  For $f(x) = 1/(1+x^n)$ and $\zeta = e^{2\pi i/n}$ this gives $\int_0^\infty {\dx \over 1 + x^n} = {\pi/n \over \sin(\pi/n)}$.
  For a rational $f$ on the keyhole, the two edges of the cut are the case $\zeta = e^{2\pi i} = 1$, and their integrals cancel; inserting a factor $\log z$ breaks the cancellation, as in [the logarithm case](#a-branch-cut-a-logarithm).

- If $f(z + ib) = cf(z)$ for real $b$ and constant $c$, use the rectangle with vertices $\pm R$ and $\pm R + ib$.
  If the vertical edges contribute integrals tending to $0$, the top edge contributes $-c\int_\RR f$, so $(1-c)\int_\RR f$ is $2\pi i$ times the sum of the residues in the strip $0<\Im z<b$.

## A half-line, by symmetry

For $f$ even, $\int_0^\infty f = \frac12 \int_\RR f$, and a contour for $\int_\RR f$ applies.
For $f$ not even with $f(\zeta z) = f(z)$ for a root of unity $\zeta$, the sector with edge $\zeta[0,\infty)$ applies.

## The standard contours

![Three standard contours: the upper semicircle gamma_R; the semicircle mu_R indented at 0 by a half-circle of radius 1/R; and the keyhole eta_R around the positive real axis with inner circle of radius 1/R.](../../../../assets/assets/figures/2021-12-23_18-51-55.png)

## Bounding denominators

The reverse triangle inequality bounds a denominator from below: for $\abs z\neq\abs w$,
$$
\abs{z-w} \geq \abs{\abs{z} - \abs{w}} \implies {1\over \abs{z-w}} \leq {1 \over \abs{\abs z - \abs w}}
,$$
and the same bound holds for $\abs{z+w} = \abs{z - (-w)}$.
