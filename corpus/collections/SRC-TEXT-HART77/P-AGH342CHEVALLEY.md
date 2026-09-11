---
schema: qual/card@1
id: P-AGH342CHEVALLEY
kind: problem
title: Chevalley's theorem on finite surjective images of affine schemes
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Affine Schemes
  - Finite Morphisms
  - Noetherian Induction
relations: []
review: draft
---

::: problem
Prove Chevalley's theorem: Let $f: X \to Y$ be a finite surjective morphism of noetherian separated schemes, with $X$ affine. Then $Y$ is affine.

a. Let $f: X \to Y$ be a finite surjective morphism of integral noetherian schemes. Show that there is a coherent sheaf $\mcm$ on $X$, and a morphism of sheaves $\alpha: \mco_Y^r \to f_* \mcm$ for some $r>0$, such that $\alpha$ is an isomorphism at the generic point of $Y$.

b. For any coherent sheaf $\mcf$ on $Y$, show that there is a coherent sheaf $\mcg$ on $X$, and a morphism $\beta: f_* \mcg \to \mcf^r$ which is an isomorphism at the generic point of $Y$.

Hint: Apply $\sheafhom(\wait, \mcf)$ to $\alpha$ and use (II, Ex. 5.17e).

c. Now prove Chevalley's theorem. First use (Ex. 3.1) and (Ex. 3.2) to reduce to the case $X$ and $Y$ integral. Then use (3.7), (Ex. 4.1), consider $\operatorname{ker} \beta$ and $\coker \beta$, and use noetherian induction on $Y$.
:::
