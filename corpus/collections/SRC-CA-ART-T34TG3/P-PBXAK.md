---
schema: qual/card@1
id: P-PBXAK
kind: problem
title: Maximum principle for harmonic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Harmonic Functions
  - Open Mapping Theorem
relations: []
review: draft
---

::: problem
Prove that maximum principle for harmonic functions, i.e.

a. If $u$ is a non-constant real-valued harmonic function in a region $\Omega$, then $u$ can not attain a maximum or a minimum in $\Omega$.

b. Suppose $\Omega$ is a region with compact closure $\bar \Omega$.
If $u$ is harmonic in $\Omega$ and continuous in $\bar \Omega$, then \[ \sup _{z \in \Omega}|u(z)| \leq \sup _{z \in \bar \Omega -\Omega}|u(z)| .\]

> Hint: to prove (a), assume $u$ attains a local maximum at $z_0$.
> Let $f$ be holomorphic near $z_0$ with $\Re(f) = u$, and show that $f$ is not an open map.
> Then (a) implies (b).
:::

::: solution
For (a), suppose $u$ attains a local maximum at $z_0\in\Omega$. On a small
disk $D\Subset\Omega$ centered at $z_0$, choose a harmonic conjugate $v$, so
$F=u+iv$ is holomorphic on $D$. If $u(z)\le u(z_0)$ on $D$, then
\[
F(D)\subset\{w:\operatorname{Re}w\le u(z_0)\},
\]
while $F(z_0)$ lies on the boundary line of that half-plane. Thus $F(D)$ is
not open at $F(z_0)$. By the open mapping theorem, $F$ must be constant on
$D$, so $u$ is constant on $D$. Since $u_x-i u_y$ is holomorphic on
$\Omega$, vanishing on the open set $D$ forces it to vanish on the connected
region $\Omega$. Hence $u$ is constant on $\Omega$, contrary to the
hypothesis. Therefore a nonconstant harmonic function has no interior local
maximum. Applying the same argument to $-u$ excludes an interior local
minimum.

For (b), continuity on the compact set $\overline\Omega$ implies that $u$
attains its maximum and minimum there. By (a), unless $u$ is constant, both
extrema occur on $\partial\Omega=\overline\Omega\setminus\Omega$. Thus
\[
\sup_{z\in\Omega}|u(z)|
\le
\sup_{z\in\partial\Omega}|u(z)|.
\]
The same inequality is immediate when $u$ is constant. Hence
\[
\boxed{
\sup_{z\in\Omega}|u(z)|
\le
\sup_{z\in\overline\Omega-\Omega}|u(z)|.}
\]
:::
