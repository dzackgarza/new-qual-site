---
schema: qual/card@1
id: P-AGH357AMPLENESS
kind: problem
title: Ampleness under restriction, reduction, and finite surjections
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ample Sheaves
  - Proper Schemes
  - Finite Morphisms
relations: []
review: draft
---

::: problem
Let $X$ (respectively, $Y$) be proper schemes over a noetherian ring $A$. We denote by $\mcl$ an invertible sheaf.

a. If $\mcl$ is ample on $X$, and $Y$ is any closed subscheme of $X$, then $i^* \mcl$ is ample on $Y$, where $i: Y \to X$ is the inclusion.

b. $\mcl$ is ample on $X$ if and only if $\mcl_{\mathrm{red}}=\mcl \tensor \mco_{X_{\mathrm{red}}}$ is ample on $X_{\mathrm{red}}$.

c. Suppose $X$ is reduced. Then $\mcl$ is ample on $X$ if and only if $\mcl \tensor \mco_{X_i}$ is ample on $X_i$, for each irreducible component $X_i$ of $X$.

d. Let $f: X \to Y$ be a finite surjective morphism, and let $\mcl$ be an invertible sheaf on $Y$. Then $\mcl$ is ample on $Y$ if and only if $f^* \mcl$ is ample on $X$.

Hints: Use (5.3) and compare (Ex. 3.1, Ex. 3.2, Ex. 4.1, Ex. 4.2).
:::
