---
schema: qual/card@1
id: FE-DERHAMNONLIN
kind: example
title: The de Rham differential is not $\OO_X$-linear
classification:
  areas:
  - algebraic-geometry
  topics:
  - Differentials
  - De Rham Complex
relations:
- kind: uses
  target: D-4GCH6
review: draft
prompts:
- Show that the differential in the de Rham complex is not $\OO_X$-linear.
---

::: {.example}
The de Rham differential $d \colon \OO_X \to \Omega^1_{X/k}$ satisfies the Leibniz rule $d(fg) = f\, dg + g\, df$, which differs from the $\OO_X$-linearity condition $d(fg) = f\, dg$ by the term $g\, df$.
On $X = \AA^1_k = \Spec k[x]$, take $f = x$ and $g = 1$: $d(x \cdot 1) = dx$, while $x\, d(1) = 0$, and $dx \neq 0$ since $\Omega^1_{k[x]/k}$ is free on $dx$.
So $d$ is $k$-linear but not $\OO_X$-linear, and the de Rham complex $\Omega^\bullet_{X/k}$ is a complex of sheaves of $k$-vector spaces whose terms are $\OO_X$-modules, not a complex of $\OO_X$-modules.
:::

::: {.remark}
This is why algebraic de Rham cohomology is the hypercohomology $\mathbb{H}^\bullet(X, \Omega^\bullet_{X/k})$ of a complex of $k$-sheaves, and why its Hodge-to-de Rham spectral sequence starts from the $\OO_X$-module cohomology groups $H^q(X, \Omega^p_{X/k})$ of the individual terms.
:::
