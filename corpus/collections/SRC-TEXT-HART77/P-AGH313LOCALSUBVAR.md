---
schema: qual/card@1
id: P-AGH313LOCALSUBVAR
kind: problem
title: The local ring of a subvariety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Local Rings
  - Subvarieties
  - Function Fields
relations: []
review: draft
---

::: problem
Let $Y \subseteq X$ be a subvariety.
Let $\mco_{Y,X}$ be the set of equivalence classes $\gens{U, f}$ where $U \subseteq X$ is open, $U \intersect Y \neq \emptyset$, and $f$ is a regular function on $U$; two classes $\gens{U,f}$ and $\gens{V,g}$ are equivalent if $f = g$ on $U \intersect V$.

Show that $\mco_{Y,X}$ is a local ring with residue field $K(Y)$ and dimension $\dim X - \dim Y$.
It is called the **local ring of $Y$ on $X$**. When $Y = P$ is a point this recovers $\mco_P$, and when $Y = X$ it recovers $K(X)$.
Note also that if $Y$ is not a point then $K(Y)$ is not algebraically closed, so this construction produces local rings whose residue fields are not algebraically closed.
:::
