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
