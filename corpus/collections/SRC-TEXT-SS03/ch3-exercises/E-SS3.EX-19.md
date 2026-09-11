---
schema: qual/card@1
id: E-SS3.EX-19
kind: problem
title: "SS 3.19: The maximum principle for harmonic functions"
classification:
  areas:
  - complex-analysis
  topics: ['Meromorphic Functions', 'Residue Theorem', 'Argument Principle']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
19. Prove the maximum principle for harmonic functions, that is:

(a) If u is a non-constant real-valued harmonic function in a region $\Omega ,$ , then u cannot attain a maximum (or a minimum) in Ω.

(b) Suppose that Ω is a region with compact closure $\overline { { \Omega } } .$ If u is harmonic in $\Omega$ and continuous in ${ \overline { { \Omega } } } ,$ then

$$
\sup _ {z \in \Omega} | u (z) | \leq \sup _ {z \in \overline {{\Omega}} - \Omega} | u (z) |.
$$

[Hint: To prove the first part, assume that u attains a local maximum at $z _ { \mathrm { 0 } }$ . Let f be holomorphic near $z _ { 0 }$ with $u = { \mathrm { R e } } ( f )$ , and show that $f$ is not open. The second part follows directly from the first.]
:::

::: solution
(a) Let $u$ be harmonic and suppose it has a local maximum at $z_0$. On a small disc $D$ about $z_0$, choose a harmonic conjugate $v$, so that
\[
F=u+iv
\]
is holomorphic on $D$. Then
\[
|e^{F(z)}|=e^{u(z)}\le e^{u(z_0)}=|e^{F(z_0)}|
\]
near $z_0$. Thus the holomorphic function $e^F$ attains a local maximum of its modulus, so by the maximum modulus principle it is constant. Hence $F$ is constant and therefore $u$ is constant on $D$. By unique continuation for harmonic functions (equivalently, by continuing local holomorphic primitives across overlapping discs), $u$ is constant on the connected region $\Omega$. Thus a nonconstant harmonic function cannot attain an interior maximum. Applying this to $-u$ gives the corresponding statement for minima.

(b) Since $\overline\Omega$ is compact and $u$ is continuous there, $|u|$ attains a maximum at some point of $\overline\Omega$. If the maximum were attained at an interior point and were strictly larger than the boundary maximum, then either $u$ or $-u$ would attain an interior maximum, forcing $u$ to be constant by part (a). In that constant case the same value occurs on the boundary. Therefore in all cases
\[
\sup_{z\in\Omega}|u(z)|\le
\sup_{z\in\overline\Omega\setminus\Omega}|u(z)|.
\]
:::
