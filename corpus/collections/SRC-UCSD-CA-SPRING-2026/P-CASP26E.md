---
schema: qual/card@1
id: P-CASP26E
kind: problem
title: 'A bounded harmonic function on $\abs z>1$ with $u\leq 0$ on $\abs z=1$ is nonpositive'
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Maximum Principle
  - Boundary Values
relations: []
review: draft
---

::: {.problem}
Let $G = \{z \in \CC : \abs{z} > 1\}$.
Let $u : G \to \RR$ be a continuous bounded function, such that $u$ is harmonic in $G$.
Assume $u(z) \leq 0$ for all $\abs{z} = 1$.
Show that $u(z) \leq 0$ for all $z \in G$.
:::

::: {.solution}
Define on the punctured unit disk
$$
v(w)=u(1/w),
\qquad 0<\abs{w}<1.
$$
Inversion is conformal away from $0$, so $v$ is harmonic on the punctured
disk. Since $u$ is bounded, $v$ is bounded near $0$. The removable
singularity theorem for harmonic functions therefore extends $v$ harmonically
across $0$.

On $\abs{w}=1$ we have
$$
v(w)=u(1/w)\le0.
$$
The maximum principle on the unit disk gives
$$
v(w)\le0
\qquad(\abs{w}<1).
$$
Substituting $w=1/z$ yields
$$
u(z)\le0
\qquad(\abs{z}>1).
$$
:::
