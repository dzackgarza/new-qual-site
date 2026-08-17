---
schema: qual/card@1
id: E-WXHMJ
kind: exercise
title: "Poles of elliptic functions"
classification:
  areas:
  - complex-analysis
  topics:
  - meromorphic-functions
  - poles
  - residues
  - liouville-s-theorem
relations: []
review: draft
solved: true
---
:::{.exercise title="Poles of elliptic functions"}
Let $f$ be an elliptic function and $P$ be its fundamental parallelogram.
Supposing that $f$ is nonconstant, show that $f$ has at least two poles in $P$ (counted with multiplicity).

:::

:::{.solution}
Write the period lattice of $f$ as $\Lambda = \omega_1\ZZ + \omega_2 \ZZ$, and without loss of generality (by translating $P$ if necessary), assume that $f$ has no poles on $\bd P$.
Since $P$ is bounded and $f$ is periodic, if $f$ has no poles then its only singularities will be removable.
In this case $f$, extends to a holomorphic function on $P$, and thus an entire function, making $f$ constant by Liouville.
So $f$ has at least one pole.
Toward a contradiction, suppose $f$ has exactly one pole $z_0\in P$, in which case $\int_{\bd P} f \neq 0$ since the residue at $z_0$ will be nonzero.
We'll show that $\int_{\bd P} f$ is forced to be zero to derive the contradiction.

Write $\bd P = \sum_{1\leq k \leq 4} \gamma_k$ where the $\gamma_k$ are the edges traversed counterclockwise.
By periodicity, 

- $I_1 \da \int_{\gamma_1} f = - \int_{\gamma_3}f$
- $I_2 \da \int_{\gamma_2} f = - \int_{\gamma_4}f$

Thus
\[
\int_{\bd P} f = \sum_{1\leq k \leq 4} \int_{\gamma_k} f = I_1 + I_2 - I_1 - I_2 = 0
.\]
$\contradiction$

> Note that if there are at least two poles, the residues may cancel and $\int_{\bd P} f$ may be zero or nonzero.
This argument in fact shows that the residues *can not* cancel, i.e. $\sum_{k} \Res_{z=z_k} f(z)\neq 0$.

:::
