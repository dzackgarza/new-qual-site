---
title: Which contour do I close?
order: 0
topics:
- Contour Integration
---

# Which contour do I close?

A contour integral on the exam gives you a real integral and nothing else.
The whole problem is choosing the closed curve, and the choice is decided by the *form of the integrand*, not by the theory.
This page is that decision, case by case.
Each case says what the integrand looks like, which curve to close, why the added piece vanishes, and what identity falls out.

The estimates that kill the added piece are on [[complex-analysis/residues-and-contours/arc-estimates|Arc estimates]].
The residue computations are on [[complex-analysis/residues-and-contours/computing-residues|Computing residues]].

## First: do you need residues at all?

Four ways an integral is finished before a contour is chosen.

- The integrand is holomorphic on and inside the curve.
  Then $\int_\gamma f = 0$ by Cauchy's theorem, and there is nothing to compute.

- The integrand has a primitive $F$ on the curve.
  Then $\int_\gamma f = F(\gamma(1)) - F(\gamma(0))$, which is $0$ on a closed curve.

- The integrand is $g(z)/(z-a)^n$ with $g$ holomorphic.
  That is the Cauchy integral formula, $\int_\gamma {g(z) \over (z-a)^{n}} \dz = {2\pi i \over (n-1)!} g^{(n-1)}(a)$, not a residue count.

- The curve is one you can parameterize.
  $\int_\gamma f \dz = \int_a^b f(z(t)) z'(t) \dt$, and a circle about $z_0$ is $z = z_0 + re^{i\theta}$.

## Rational, decaying at least quadratically

**Looks like:** $\displaystyle\int_\RR f$ with $f = p/q$ rational and $\deg q \geq \deg p + 2$, or more generally $f = \bigo(1/z^{1+\eps})$.

**Close with:** the semicircle in the upper half plane, $[-R, R]$ followed by $C_R = \ts{Re^{it} \st t \in [0,\pi]}$.

![](../../../../assets/assets/figures/2021-07-29_18-37-57.png)

**Why the arc dies:** the ML estimate.
$\abs{f} = \bigo(1/R^{2})$ on $C_R$ and $\length(C_R) = \pi R$, so the arc contributes $\bigo(1/R) \to 0$.

**You get:**
\[
\int_\RR f = 2\pi i \sum_{z_0 \in \HH} \Res_{z=z_0} f(z)
.\]

The poles counted are the ones in the *open upper half plane*; a pole on $\RR$ is the principal-value case below.
Closing downward instead traverses $\RR$ backwards, which is where the sign comes from: every residue theorem here assumes the counterclockwise orientation.

## Rational against a single sine or cosine

**Looks like:** $\displaystyle\int_\RR f(x)\cos(x)$ or $\displaystyle\int_\RR f(x)\sin(x)$, with $f$ rational and only $\deg q \geq \deg p + 1$.

**Close with:** the same semicircle, but integrate $f(z)e^{iz}$ rather than $f(z)\cos(z)$, and take the real or imaginary part at the end:
\[
\int_\RR f(x)\cos(x) \dx = \Re \int_\RR f(z)e^{iz}\dz
.\]

**Why the arc dies:** Jordan's lemma, which is the reason for the rewrite.
$\cos(z)$ is unbounded on $C_R$, so $f(z)\cos(z)$ has no ML bound at all; $\abs{e^{iz}} = e^{-\Im z} \leq 1$ on the upper arc, and Jordan's lemma turns the decay $M_R$ of $f$ alone into the bound $\pi M_R / a$.
That buys one whole power of $z$ over ML: linear decay is enough.

Use $e^{iz}$ and the upper arc for $\Im z \geq 0$, and $e^{-iz}$ with the lower arc otherwise, so the exponential is the decaying one.

## Rational in $\cos$ and $\sin$, over one period

**Looks like:** $\displaystyle\int_0^{2\pi} R(\cos\theta, \sin\theta) \dtheta$ with $R$ a rational function of the two.

**Close with:** the unit circle itself.
Substitute $z = e^{i\theta}$, which turns the period into the whole curve:
\[
\cos\theta = {z + z\inv \over 2}, \quad \sin\theta = {z - z\inv \over 2i}, \quad \dtheta = {\dz \over iz}
.\]

**Why nothing is added:** there is no added piece.
The interval was already closed; the substitution only recognizes it.

**You get:** a residue count inside the disc,
\[
\int_0^{2\pi} R(\cos\theta,\sin\theta) \dtheta = 2\pi i \sum_{\abs{z_0} < 1} \Res_{z=z_0} R\qty{ {z+z\inv \over 2}, {z - z\inv \over 2i} } {1 \over iz}
.\]

The factor $1/iz$ is part of the integrand, so $z = 0$ is usually one of the poles.

## A branch cut: a power $x^\alpha$

**Looks like:** $\displaystyle\int_0^\infty x^\alpha f(x)$ with $f$ rational, $\deg f \leq -2$, and $\alpha$ non-integral with $\abs{\alpha} < 1$.

**Close with:** the keyhole around the cut along $\RR_{\geq 0}$, taking $\arg z \in (0, 2\pi)$.

![](../../../../assets/assets/figures/2021-12-14_17-19-31.png)

**Why the added pieces die:** the large circle by ML, the small one because $\alpha > -1$ makes $\eps^{1+\alpha} \to 0$.

**You get:** the two edges of the cut do not cancel, and that is the whole trick.
Above the cut the integrand is $x^\alpha f(x)$; below it the same points carry $\arg z = 2\pi$, so the integrand is $e^{2\pi i \alpha}x^\alpha f(x)$ and the edge is traversed backwards.
Hence
\[
\qty{1 - e^{2\pi i \alpha}} \int_0^\infty x^\alpha f(x) \dx = 2\pi i \sum \Res\qty{z^\alpha f(z)}
,\]
the sum over every pole of $f$ off the cut.

## A branch cut: a logarithm

**Looks like:** $\displaystyle\int_0^\infty f(x)\log(x)$, or $\displaystyle\int_0^\infty f(x)$ where $f$ is even and you want the $\log$ to do the work.

**Close with:** an indented semicircle, or the same keyhole.

![](../../../../assets/assets/figures/2021-12-14_17-20-48.png)

![](../../../../assets/assets/figures/2021-12-22_05-14-24.png)

**Two facts that come up every time:**
\[
\lim_{\eps \decreasesto 0} \ln(x - i\eps) = \ln(x) + 2\pi i, \qquad \lim_{x\to 0} {x\ln(x) \over x^n + c} = 0
.\]
The constant $c$ in the second cannot be dropped.

**The rotation trick:** if $f(z) = \log(z)g(z)$ and $\int g$ is easy, close along a rotation of $\RR$.
The substitution sends $\log(\zeta x) \leadsto \ln\abs{x} + i\theta$, so if $g$ is $\zeta\dash$invariant,
\[
\int \log(\zeta x)g(\zeta x) = \int \log(x)g(x) + i\theta\int g(x)
,\]
and the unknown integral appears on both sides.

## A pole sitting on the contour

**Looks like:** $\displaystyle\int_\RR p(x)/q(x)$ where $q$ has a real root, or any integrand singular at a point of the path.
The integral does not converge; what is being asked for is the principal value
\[
\operatorname{PV} \int_{-\infty}^{\infty} \frac{f(x)}{x-x_{0}} \dx = \lim_{\eps \decreasesto 0}\qty{\int_{-\infty}^{x_{0}-\eps} f + \int_{x_{0}+\eps}^{\infty} f}
.\]

**Close with:** the semicircle, indented by a small arc *over* each real pole.

![](../../../../assets/assets/figures/2021-12-21_23-40-15.png)

**Why the indentation does not die:** it does not shrink to nothing.
By the small-arc lemma an arc of angle $\theta$ about a simple pole contributes $i\theta \Res$ in the limit, and each indentation here is a half-circle traversed clockwise, contributing $-i\pi\Res$.

**You get:** the poles on the line count half,
\[
\operatorname{PV} \int_\RR f = 2\pi i \sum_{z_0 \in \HH} \Res_{z=z_0} f + i\pi \sum_{x_0 \in \RR} \Res_{z=x_0} f
.\]

## No decay at all: replication

**Looks like:** an integrand that does not shrink on any large arc, so no semicircle can work, but which repeats itself under a symmetry.

**Close with:** the curve the symmetry chooses, so that the far side reproduces the integral you want with a constant in front.

- $f(\zeta_m z) = f(z)$ for $\zeta_m$ a root of unity: a sector of angle $2\pi/m$.
  The returning ray gives $\zeta_m \int f$, so $(1 - \zeta_m)\int f$ is a residue count.
  This is how $\int_0^\infty {\dx \over 1 + x^n} = {\pi/n \over \sin(\pi/n)}$ falls out.

  ![](../../../../assets/assets/figures/2021-12-21_21-14-04.png)

  ![](../../../../assets/assets/figures/2021-12-21_21-17-25.png)

- $f(z + ib) = cf(z)$ for a real $b$: a rectangle of height $b$.
  The top edge reproduces the bottom, the two vertical edges vanish, and the integral is again recovered up to a constant.

## A half-line, by symmetry

**Looks like:** $\displaystyle\int_0^\infty f$ where $f$ is even.

**Close with:** nothing new.
$\int_0^\infty f = \frac12 \int_\RR f$, and the problem is one of the cases above.
If $f$ is not even, look for the sector instead.

## The standard contours, together

![](../../../../assets/assets/figures/2021-12-23_18-51-55.png)

![](../../../../assets/assets/figures/2021-12-21_21-10-30.png)

## Estimates you will reach for

Use the reverse triangle inequality to bound a denominator from below:
\[
\abs{z-w} \geq \abs{\abs{z} - \abs{w}} \implies {1\over \abs{z-w}} \leq \abs{1 \over \abs z - \abs w}
,\]
and the same for $\abs{z+w}$ by writing it as $\abs{z - (-w)}$.
For exponentials, $e^{-x}$ is decreasing on $\RR$, so $a \leq b \implies e^{-a} \geq e^{-b}$.
