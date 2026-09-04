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
Write the period lattice as $\Lambda=\omega_1\ZZ+\omega_2\ZZ$, and translate the fundamental parallelogram if necessary so that $f$ has no poles on $\bd P$.

If $f$ had no poles, periodicity would make it an entire bounded function: it is bounded on the compact closure of $P$, hence bounded on all of $\CC$ by translation through $\Lambda$.
Liouville's theorem would then force $f$ to be constant.
Thus $f$ has at least one pole.

Suppose, toward a contradiction, that $f$ has only one pole counted with multiplicity.
Then it is a single simple pole $z_0\in P$, so
\[
\Res_{z=z_0}f\neq0.
\]

Write $\bd P = \sum_{1\leq k \leq 4} \gamma_k$ where the $\gamma_k$ are the edges traversed counterclockwise.
By periodicity, opposite edges contribute equal integrals with opposite orientations, so
\[
\int_{\bd P}f(z)\,dz=0.
\]
But the residue theorem gives
\[
0=\int_{\bd P}f(z)\,dz
=2\pi i\Res_{z=z_0}f(z),
\]
contradicting the simplicity of the pole.

More generally, the same boundary cancellation always shows
\[
\sum_{z_k\in P}\Res_{z=z_k}f(z)=0
\]
for every elliptic function whose fundamental parallelogram has no poles on its boundary.
:::
