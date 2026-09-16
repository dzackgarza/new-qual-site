---
schema: qual/card@1
id: P-AGH277VERONESESURF
kind: problem
title: The Veronese surface and rational surfaces from linear systems
classification:
  areas:
  - algebraic-geometry
  topics:
  - Linear Systems
  - Veronese Embedding
  - Ruled Surfaces
relations: []
review: draft
---

::: {.problem}
Let $X = \PP^2_k$, and let $\abs{D}$ be the complete linear system of all divisors of degree $2$ on $X$, the conics.
Here $D$ corresponds to the invertible sheaf $\OO(2)$, whose space of global sections has basis $x^2, y^2, z^2, xy, xz, yz$, where $x, y, z$ are the homogeneous coordinates of $X$.

a. The complete linear system $\abs{D}$ gives an embedding of $\PP^2$ in $\PP^5$, whose image is the **Veronese surface** (I, Ex. 2.13).

b. Show that the subsystem defined by $x^2, y^2, z^2, y(x - z), (x - y)z$ gives a closed immersion of $X$ into $\PP^4$.
   The image is called the Veronese surface in $\PP^4$. Cf. (IV, Ex. 3.11).

c. Let $\nu \subseteq \abs{D}$ be the linear system of all conics passing through a fixed point $P$.
   Then $\nu$ gives an immersion of $U = X - P$ into $\PP^4$.
   Furthermore, if we blow up $P$ to get a surface $\tilde X$, then this map extends to a closed immersion of $\tilde X$ in $\PP^4$.

   Show that $\tilde X$ is a surface of degree $3$ in $\PP^4$, and that the lines in $X$ through $P$ are transformed into straight lines in $\tilde X$ which do not meet.
   Since $\tilde X$ is the union of all these lines, we say $\tilde X$ is a **ruled surface** (V, 2.19.1).
:::
