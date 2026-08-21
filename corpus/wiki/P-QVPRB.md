---
schema: qual/card@1
id: P-QVPRB
kind: problem
title: Hungerford 7.5.2
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Determinants
  - Modules
relations: []
review: draft
solved: false
---

:::{.problem title="Hungerford 7.5.2"}
Show that if $\phi$ is an endomorphism of a free $k$-module $E$ of finite rank, then
$p_\phi(\phi) = 0$.

*Hint: If $A$ is the matrix of $\phi$ and $B = x I_n - A$ then*
\[
B^a B = |B| I_n = p_\phi I_n \in M_n(k[x])
.\]
*If $E$ is a $k[x]$-module with structure induced by $\phi$, and $\psi$ is the $k[x]$-module endomorphism $E\to E$ with matrix given by $B$, then*
\[ 
\psi(u) = x u -\phi(u) = \phi(u) - \phi(u) = 0 && \forall u\in E
.\]

:::

