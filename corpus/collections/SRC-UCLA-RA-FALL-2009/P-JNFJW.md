---
schema: qual/card@1
id: P-JNFJW
kind: problem
title: Injectivity of holomorphic functions with $\operatorname{Re}(f')>0$, and the
  need for convexity
classification:
  areas:
  - real-analysis
  topics:
  - Holomorphic Functions
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against problem 8 of the UCLA Analysis Qualifying Exam, Fall 2009, from the collection provenance PDF.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Retained the segment-integral proof of injectivity. Replaced the vague
    C-shaped-domain counterexample by a sufficiently thin regular neighborhood
    of an explicit simple polygonal arc joining e^{i*pi/3} to e^{-i*pi/3}
    inside {Re(1-1/z^2)>0}; z+1/z takes the same value at the two endpoints.
---

::: {.problem}
Let $\Omega$ be an open convex region in the complex plane.
Assume $f$ is a holomorphic function on $\Omega$ and the $\text{Re}(f'(z))>0$ for all $z\in\Omega$.

a. Prove that $f$ is one-to-one.

b. Show by example that the word "convex" cannot be replaced by "connected and simply connected".
:::

::: {.solution}
<1>1. Let $z_1,z_2\in\Omega$ with $z_1\ne z_2$.
Then
\[
\frac{f(z_2)-f(z_1)}{z_2-z_1}
=\int_0^1f'((1-t)z_1+tz_2)\,dt.
\]
::: {.proof}
Convexity gives
\[
\gamma(t)=(1-t)z_1+tz_2\in\Omega
\]
for $0\le t\le1$.
The chain rule gives
\[
\frac d{dt}f(\gamma(t))
=(z_2-z_1)f'(\gamma(t)).
\]
Integrating from $0$ to $1$ yields
\[
f(z_2)-f(z_1)
=(z_2-z_1)\int_0^1f'(\gamma(t))\,dt,
\]
and division by $z_2-z_1$ gives the claim.
:::

<1>2. The map $f$ is one-to-one on $\Omega$.
::: {.proof}
Taking real parts in <1>1 gives
\[
\operatorname{Re}\frac{f(z_2)-f(z_1)}{z_2-z_1}
=\int_0^1\operatorname{Re}f'(\gamma(t))\,dt.
\]
The integrand is continuous and strictly positive, so the integral is strictly positive.
Hence
\[
\frac{f(z_2)-f(z_1)}{z_2-z_1}\ne0,
\]
which implies
\[
f(z_2)\ne f(z_1).
\]
This proves part (a).
:::

For part (b), consider
\[
F(z)=z+\frac1z,
\qquad z\ne0.
\]

<1>3. The derivative of $F$ satisfies
\[
\operatorname{Re}F'(re^{i\theta})
=1-\frac{\cos(2\theta)}{r^2}.
\]
::: {.proof}
We have
\[
F'(z)=1-\frac1{z^2}.
\]
Substituting $z=re^{i\theta}$ gives
\[
\frac1{z^2}=r^{-2}e^{-2i\theta},
\]
whose real part is $r^{-2}\cos(2\theta)$.
:::

<1>4. Let $\Gamma$ be the simple polygonal arc with successive vertices
\[
z_+=e^{i\pi/3},
\quad
a=2e^{i\pi/3},
\quad
b=2,
\quad
c=2e^{-i\pi/3},
\quad
z_-=e^{-i\pi/3}.
\]
Then
\[
\operatorname{Re}F'(z)>0
\]
for every $z\in\Gamma$.
::: {.proof}
On the radial segments $[z_+,a]$ and $[c,z_-]$, the argument is respectively $\pi/3$ and $-\pi/3$.
Thus <1>3 gives
\[
\operatorname{Re}F'(re^{\pm i\pi/3})
=1-\frac{\cos(2\pi/3)}{r^2}
=1+\frac1{2r^2}>0.
\]

Every point of the two middle line segments $[a,b]$ and $[b,c]$ has modulus at least $\sqrt3>1$.
Indeed, the line through $a=(1,\sqrt3)$ and $b=(2,0)$ has distance $\sqrt3$ from the origin, and the lower segment is its reflection.
For $|z|>1$, <1>3 gives
\[
\operatorname{Re}F'(z)
\ge1-\frac1{|z|^2}>0.
\]
Hence the real part of the derivative is positive on every segment of $\Gamma$.
:::

<1>5. There is a connected simply connected open set $\Omega$ containing $\Gamma$ such that
\[
\operatorname{Re}F'(z)>0
\]
for all $z\in\Omega$.
::: {.proof}
Set
\[
U=\{z\in\mathbb C\setminus\{0\}:\operatorname{Re}F'(z)>0\}.
\]
This is open by continuity of $F'$, and <1>4 gives
\[
\Gamma\subseteq U.
\]
The arc $\Gamma$ is compact, so it has positive distance from the closed set $\mathbb C\setminus U$.

A simple polygonal arc has arbitrarily small open regular neighborhoods homeomorphic to an open disk: take thin rectangles around its finitely many segments and small disks around its vertices, with the widths chosen so that only pieces belonging to adjacent segments meet.
Their union is an open thickening of the arc and deformation retracts onto $\Gamma$.
Choose such a regular neighborhood $\Omega$ thin enough that
\[
\overline\Omega\subseteq U.
\]
Then $\Omega$ is connected and simply connected, and by construction
\[
\operatorname{Re}F'(z)>0
\]
throughout $\Omega$.
:::

<1>6. The function $F$ is not one-to-one on $\Omega$.
::: {.proof}
Both endpoints $z_+,z_-$ of $\Gamma$ lie in $\Omega$, and they are distinct.
But
\[
\begin{aligned}
F(z_+)
&=e^{i\pi/3}+e^{-i\pi/3}=1,\\
F(z_-)
&=e^{-i\pi/3}+e^{i\pi/3}=1.
\end{aligned}
\]
Thus
\[
F(z_+)=F(z_-)
\]
with $z_+\ne z_-$.
By <1>5, $\Omega$ is connected and simply connected and satisfies
\[
\operatorname{Re}F'>0.
\]
Therefore convexity in part (a) cannot be replaced merely by connectedness and simple connectedness.
:::
:::
