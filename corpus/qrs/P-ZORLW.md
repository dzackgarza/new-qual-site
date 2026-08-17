---
schema: qual/card@1
id: P-ZORLW
kind: problem
title: Holomorphic functions vanishing on the boundary are constant or have an interior
  zero
classification:
  areas:
  - complex-analysis
  topics:
  - maximum-modulus-principle
  - zeros
relations: []
review: draft
solved: true
---

::: problem
- Show that if $\abs{f} = 0$ on $\bd \Omega$ then either $f$ is constant or $f$ has a zero in $\Omega$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** If $f$ is holomorphic on a bounded region $\Omega$, continuous on $\bar\Omega$, and $\abs f = 0$ (i.e. $f = 0$) on $\bd\Omega$, show that either $f$ is constant or $f$ has a zero in $\Omega$.

<1>1. If $f$ has no zeros in $\Omega$, then $\abs{f}$ attains its maximum on $\bd\Omega$.
Proof: $\abs{f}$ is continuous on the compact set $\bar\Omega$, so it attains its maximum somewhere in $\bar\Omega$; by the maximum modulus principle (or its version for $1/f$, valid because $f$ has no zeros), the maximum is attained on the boundary $\bd\Omega$.

<1>2. If $f$ has no zeros in $\Omega$, then $f \equiv 0$ on $\bar\Omega$.
Proof: By <1>1 and the hypothesis $\abs f = 0$ on $\bd\Omega$, $\max_{\bar\Omega}\abs f = 0$, so $f \equiv 0$ on $\bar\Omega$.

<1>3. If $f$ is not constant, then $f$ has a zero in $\Omega$.
Proof: Contrapositive of <1>2: if $f$ has no zero in $\Omega$, then by <1>2 $f \equiv 0$ on $\bar\Omega$, so $f$ is constant (the zero function).

<1>4. Q.E.D. Proof: <1>3 shows that a nonconstant $f$ must vanish somewhere in $\Omega$, which together with the trivial constant case proves the claim.
:::
