---
schema: qual/card@1
id: E-UDPOY
kind: exercise
title: "Suppose $f$ is holomorphic on $\\Delta^*$ and $\\Re(f) \\geq 0$."
classification:
  areas:
  - complex-analysis
  topics:
  - removable-singularities
  - conformal-maps
  - fractional-linear-transformations
  - singularities
relations: []
review: draft
---
:::{.problem title="?"}
Suppose $f$ is holomorphic on $\Delta^*$ and $\Re(f) \geq 0$.
Show that $f$ has a removable singularity at $z=0$.
:::

:::{.solution}
We have $f: \Delta^* \to \ts{\Re(z) > 0}$, so let $T: \ts{\Re(z) > 0}\to \Delta$ be the rotated Cayley map $T(z) = {z-1\over z+1}$.
Then $G\da T\inv \circ f: \Delta^* \to \Delta$, and since $\abs{T} < 1$, $z=0$ is a removable singularity for $F$ and $F$ extends holomorphically to $G:\Delta\to \CC$, since a priori $G(0)$ may not be bounded by 1.
Supposing $G$ is not constant, $G(\Delta) \subseteq \overline{\Delta}$ by continuity and $G(\Delta)$ is open by the open mapping theorem, and $\Delta = f(\Delta) \subseteq G(\Delta)$, so $G:\Delta\to \Delta$ is a map of the disc.
Then $F \da T\circ G: \Delta\to \ts{\Re(z) > 0}$ is an extension of $F$ which is bounded in neighborhoods of $z=0$, making zero a removable singularity for $f$.
:::

