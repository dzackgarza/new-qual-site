---
schema: qual/card@1
id: P-VN3M2
kind: problem
title: "Compute the homology and cohomology of a closed, connected, oriented 3\u2026"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
Compute the homology and cohomology of a closed, connected, oriented 3-manifold $M$ with $\pi_1(M) = \ZZ^{\ast 2}$.

:::{.solution}
Facts used:

- $M$ closed, connected, oriented $\implies H_i(M)\cong H^{n-i}(M)$
- $H_1(X) = \Ab(\pi_1(X))$.
- For orientable manifolds $H_n(M^n) = \ZZ$

**Homology**

- Since $M$ is connected, $H_0 = \ZZ$
- Since $\pi_1(M) = \ZZ^{\ast 2}$, $H_1$ is the abelianization and $H_1(X) = \ZZ^2$
- Since $M$ is closed/connected/oriented, Poincaré Duality holds and $H_2 = H^{3-2} = H^1 = \mathbf{F} H_1 + \mathbf{T}H_0$ by UCT. Since $H_0=\ZZ$ is torsion-free, we have $H_2(M) = H_1(M) =  \ZZ^2$.
- Since $M$ is an orientable manifold, $H_3(M) = \ZZ$
- So $H_*(M) = [\ZZ, \ZZ^2, \ZZ^2, \ZZ, 0\rightarrow]$

**Cohomology**

- By Poincaré Duality, $H^*(M) = \widehat{H_*(M)} = [\ZZ, \ZZ^2, \ZZ^2, \ZZ, 0, \cdots]$. (Where the hat denotes reversing the list.)


:::
