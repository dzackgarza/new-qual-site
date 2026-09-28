---
schema: qual/card@1
id: D-DEFINTCL
kind: definition
title: Integrally closed domains
classification:
  areas:
  - algebraic-geometry
  topics:
  - Commutative Algebra
  - Integral Extensions
  - Normality
relations: []
review: draft
prompts:
- What does it mean for a domain to be integrally closed?
- Give a domain that is not integrally closed, and identify its integral closure.
- How do UFDs, integrally closed domains, and regular rings compare?
---

::: {.definition title="integrally closed"}
Let $A$ be an integral domain with fraction field $K(A)$.
$A$ is \dfn{integrally closed} if for every monic $f(x) \in A[x]$, any root $\alpha \in K(A)$ of $f$ already lies in $A$.
Equivalently, $A$ equals its integral closure in $K(A)$.
:::

::: {.remark}
Every UFD is integrally closed, by the rational root argument.
A domain $A$ is integrally closed if and only if $A_\mfp$ is integrally closed for every prime $\mfp$; so an integral scheme $\Spec A$ is normal, in the sense that its local rings are integrally closed, if and only if $A$ is integrally closed.

The coordinate ring of the cusp, $A = k[t^2,t^3] \subseteq k[t]$, is not integrally closed: the element $t = t^3/t^2$ lies in $K(A)$ and satisfies $x^2 - t^2 = 0$, so it is integral over $A$ but not in $A$, and $k[t]$ is the integral closure.
Geometrically the normalisation $\Spec k[t] \to \Spec A$ is the map resolving the cusp of $y^2 = x^3$.

For local rings, regular $\implies$ UFD $\implies$ integrally closed, with both implications strict; for a Noetherian local domain of dimension one, the three conditions coincide and characterize DVRs.
A regular ring that is not local need not be a UFD: the Dedekind domain $\ZZ[\sqrt{-5}]$ is regular and not a UFD.
:::
