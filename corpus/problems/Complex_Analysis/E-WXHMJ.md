---
schema: qual/card@1
id: E-WXHMJ
kind: problem
title: Poles of elliptic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Poles
  - Residues
  - Liouville's Theorem
relations: []
review: draft
---

::: {.exercise}
Let $f$ be an elliptic function and $P$ be its fundamental parallelogram.
Suppose that $f$ is nonconstant.
Show that $f$ has at least two poles in $P$, counted with multiplicity.
:::

::: {.solution}
Let $\Lambda=\omega_1\ZZ+\omega_2\ZZ$ be the period lattice.
Translating $P$ by a vector does not change the number of poles it contains modulo $\Lambda$, so assume $f$ has no poles on $\partial P$.

::: pf

::: {.pf-step #some-pole}
$f$ has at least one pole in $P$.

::: pf-proof
Otherwise $f$ is entire and bounded on the compact set $\overline P$, hence bounded on $\CC = \overline P + \Lambda$ by periodicity, and Liouville's theorem makes $f$ constant.
:::

:::

::: {.pf-step #residue-sum}
$\sum_{z_k\in P}\Res_{z=z_k}f = 0$.

::: pf-proof
By periodicity the integrals of $f$ over opposite edges of $\partial P$ cancel, since the edges are translates by $\omega_1$ or $\omega_2$ traversed in opposite directions.
So $\int_{\partial P}f\dz = 0$, and the residue theorem gives the claim.
:::

:::

::: pf-step
$f$ has at least two poles in $P$, counted with multiplicity.

::: pf-proof
If there were exactly one, it would be a simple pole $z_0$ with $\Res_{z=z_0}f\neq0$, contradicting step [](#residue-sum){.pf-ref}; step [](#some-pole){.pf-ref} excludes zero poles.
:::

:::

:::

:::
